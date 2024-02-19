from pathlib import Path
import os
import sys
import re
import tempfile
from ctypes import sizeof, c_uint16, c_byte, create_string_buffer, c_int32, c_uint32, byref, c_ushort, c_uint, c_uint64, \
    string_at, addressof, POINTER
from struct import unpack
import errno
import shutil
import logging
from typing import BinaryIO, Union

from startup_image import struct_startup_header, struct_image_header, struct_image_trailer, \
    STARTUP_HDR_FLAGS1_COMPRESS_MASK, \
    STARTUP_HDR_FLAGS1_COMPRESS_UCL, struct_image_attr, IMAGE_FLAGS_BIGENDIAN, STARTUP_HDR_FLAGS1_BIGENDIAN, \
    STARTUP_HDR_FLAGS1_COMPRESS_ZLIB, STARTUP_HDR_FLAGS1_COMPRESS_LZO, STARTUP_HDR_FLAGS1_COMPRESS_NONE, gzFile_s
from utils import run_v1, shutil_rm

logger = logging.getLogger(__name__)

S_IFMT = 0o0170000
S_IFDIR = 0o0040000  # Directory
S_IFCHR = 0o0020000  # Character device
S_IFBLK = 0o0060000  # Block device
S_IFREG = 0o0100000  # Regular file
S_IFIFO = 0o0010000  # FIFO
S_IFLNK = 0o0120000  # Symbolic link
S_IFSOCK = 0o0140000  # Socket
g_verbose = False


from forbiddenfruit import curse

def int_byteswap(this:int, bytelen:int)->int:
    return int.from_bytes(this.to_bytes(bytelen, 'little'), 'big', signed=False)

curse(int, 'byteswap', int_byteswap)


decompress_bin_path = Path(tempfile.mkstemp(prefix='ifs_decompressed', suffix='.bin')[1])
startup_header_pattern = b'\xEB\x7E\xFF\x00.{46}\x00{14}'
image_header_pattern = b'imagefs[\x00-\x07]'


def main() -> int:
    import argparse
    argparser = argparse.ArgumentParser()
    argparser.add_argument('ifs_filename')
    argparser.add_argument('-d', '--outputdir')
    argparser.add_argument('-v', '--verbose', action='store_true')
    args = argparser.parse_args()
    ifs_filepath = Path(args.ifs_filename).expanduser().resolve()
    outputdir = Path(args.outputdir).expanduser().resolve()
    global g_verbose
    g_verbose = args.verbose

    shutil.rmtree(outputdir, ignore_errors=True)
    outputdir.mkdir(parents=True, exist_ok=True)

    if not ifs_filepath.is_file():
        logger.error(f'{ifs_filepath=} is not a file')
        return errno.ENOENT
    try:
        res = process(ifs_filepath, outputdir)
        return res
    finally:
        global decompress_bin_path
        try:
            decompress_bin_path.unlink(missing_ok=True)
        except Exception as ex:
            logger.info(f'{ex=} while deleting {decompress_bin_path=}')
            pass



def process(ifs_file: Path, outputdir: Path) -> int:
    with ifs_file.open('rb') as fin:
        ipos = find(fin, image_header_pattern, 0)
        if ipos == 0:
            fin.seek(ipos)
            buf = fin.read(sizeof(struct_image_header))
            ihdr = struct_image_header.from_buffer_copy(buf)
            return process_uncompressed(ifs_file, outputdir, None, -1, ihdr, 0)
        spos = find(fin, startup_header_pattern, 0)
        if spos == -1:
            logger.warning(f'{fin=} unable to find startup_header_pattern or image_header_pattern')
            return errno.EINVAL
        fin.seek(spos)
        buf = fin.read(sizeof(struct_startup_header))
        shdr = struct_startup_header.from_buffer_copy(buf)
        if shdr.flags1 & STARTUP_HDR_FLAGS1_BIGENDIAN:
            shdr = shdr_byteswap(shdr)
        print(f'Image startup_size: 0x{shdr.startup_size:08x} ')
        print(f'Image stored_size: 0x{shdr.stored_size:08x} ')
        print(f'Compressed size: 0x{shdr.stored_size - shdr.startup_size - sizeof(struct_image_trailer)}')

        # if shdr.flags1 & STARTUP_HDR_FLAGS1_COMPRESS_MASK:
        res = decompress_ifs(fin, shdr, spos)
        if res != 0:
            return res
        res = process_uncompressed(decompress_bin_path, outputdir, shdr, spos, None, -1)
        if res != 0:
            return res
    return 0


def shdr_byteswap(shdr: struct_startup_header)->struct_startup_header:
    for i in range(4,17):
        fname = shdr._fields_[i][0]
        bytelen = getattr(struct_startup_header, fname).size
        setattr(shdr, fname,  getattr(shdr, fname).byteswap(bytelen))
    return shdr


def decompress_ifs(fin: BinaryIO, shdr: struct_startup_header, spos: int) -> int:
    from struct import unpack
    from ctypes.util import find_library
    from ctypes import cdll, POINTER
    nullptr = POINTER(c_int32)()
    out_buf = create_string_buffer(b'\x00', 0x10000)
    in_buf = create_string_buffer(b'\x00', 0x10000)
    til, tol = 0, 0

    with open(decompress_bin_path, 'wb') as fout:
        fin.seek(0)
        fout.write(fin.read(spos + shdr.startup_size))
        fout.flush()
        cmpr_algo = shdr.flags1 & STARTUP_HDR_FLAGS1_COMPRESS_MASK
        if cmpr_algo == STARTUP_HDR_FLAGS1_COMPRESS_ZLIB:
            lib = cdll.LoadLibrary(find_library('z'))
            fd = fin.fileno()
            os.lseek(fd, fin.tell(), os.SEEK_SET)
            ptr = lib.gzdopen(fd, "rb")
            if ptr == 0:
                logger.error(f'lib.gzdopen() failed, {fin.tell()=}')
                return errno.EIO
            zin = POINTER(gzFile_s)(ptr)
            while True:
                n = lib.gzread(zin, in_buf, sizeof(in_buf))
                if n<= 0:
                    break
                fout.write(in_buf.raw[:n])

        elif cmpr_algo == STARTUP_HDR_FLAGS1_COMPRESS_LZO:
            lib = cdll.LoadLibrary(find_library('lzo2'))
            res = lib.lzo_init()
            if res != 0:
                logger.error(f'lzo_init() failed, {res=}')
                return res
            while True:
                nowPtr = fin.tell()
                buf = fin.read(2)
                in_len, *_ = unpack('>H', buf)
                if in_len == 0:
                    break
                in_buf.raw = fin.read(in_len)
                out_len = c_uint64()
                status = lib.lzo1x_decompress(byref(in_buf), in_len,
                                              byref(out_buf), byref(out_len))
                if status != 0:
                    logger.error(f'lzo1x_decompress() failed, {status=}, out_len={out_len.value}, {nowPtr=:x}')
                    return status
                til += in_len; tol += out_len.value
                fout.write(out_buf.raw[:out_len])
                print(f'LZO Decompress rd={in_len}, wr={out_len} @ 0x{nowPtr:x}')
            print(f'Decompressed {til} bytes -> {tol} bytes')

        elif cmpr_algo == STARTUP_HDR_FLAGS1_COMPRESS_UCL:
            lib = cdll.LoadLibrary(find_library('ucl'))

            print(f'UCL Decompress @0x{fin.tell():016x}')
            while True:
                nowPtr = fin.tell()
                buf = fin.read(2)
                # noinspection PyShadowingBuiltins
                in_len, *_ = unpack('>H', buf)
                if in_len == 0:
                    break
                in_buf.raw = fin.read(in_len)
                out_len = c_uint32(0x10000)
                status = lib.ucl_nrv2b_decompress_8(byref(in_buf), in_len,
                                                    byref(out_buf), byref(out_len), nullptr)
                if status != 0:
                    logger.warning(f'ucl_nrv2b_decompress_8() failed, {nowPtr:08x=}')
                    return errno.EINVAL
                til += in_len; tol += out_len.value
                if g_verbose:
                    print(f'UCL Decompressed rd={in_len} (0x{in_len:x}) wr={out_len.value}, 0x{nowPtr:x}')
                fout.write(out_buf.raw[0:out_len.value])
            if g_verbose:
                print(f'Decompressed {til} bytes -> {tol} bytes')
        elif cmpr_algo == STARTUP_HDR_FLAGS1_COMPRESS_NONE:
            while True:
                data = fin.read(sizeof(in_buf))
                if len(data)==0:
                    break
                fout.write(data)    
        else:
            sys.stderr.write(f"{cmpr_algo=:#04x} unknown compression")
            sys.exit(errno.EINVAL)
    return 0


def ihdr_byteswap(ihdr:struct_image_header)->struct_image_header:
    # buf = string_at(addressof(ihdr), sizeof(ihdr))
    # pInt = POINTER(c_uint)(buf)
    struct_image_header.image_size.offset

    ihdr.image_size = ihdr.image_size.byteswap(4)
    ihdr.hdr_dir_size = ihdr.hdr_dir_size.byteswap(4)
    ihdr.dir_offset = ihdr.dir_offset.byteswap(4)
    for i in range(4):
        ihdr.boot_ino[i] = ihdr.boot_ino[i].byteswap(4)
    ihdr.script_ino = ihdr.script_ino.byteswap(4)
    ihdr.chain_paddr = ihdr.chain_paddr.byteswap(4)
    return ihdr


def process_uncompressed(ifs_filepath: Path, outputdir: Path, shdr: Union[struct_startup_header, None], spos: int,
                         ihdr: Union[struct_image_header, None], ipos: int) -> int:
    """

    :param ifs_filepath: not compressed or decompressed IFS file
    :param outputdir:
    :param shdr:
    :param spos: pos of struct_startup_header
    :param ihdr:
    :param ipos: pos of struct_image_header
    :return:
    """
    file_size = ifs_filepath.lstat().st_size
    with ifs_filepath.open('rb') as fin2:
        if spos != -1:
            fin2.seek(spos + shdr.startup_size)
            ihdr = struct_image_header.from_buffer_copy(fin2.read(sizeof(struct_image_header)))

            ipos = find(fin2, image_header_pattern, spos + shdr.startup_size)
            if ipos == -1:
                logger.warning(f'Failed to find image header in {ifs_filepath}')
                return errno.EINVAL
            fin2.seek(ipos)
        assert ipos != -1
        if ihdr.flags & IMAGE_FLAGS_BIGENDIAN:
            ihdr = ihdr_byteswap(ihdr)
        dpos = ipos + ihdr.dir_offset
        print("   Offset     Size  Name")
        if spos != -1:
            if spos != 0:
                print(f' {0:x} {spos:x}  "*.boot"')
            display_shdr(spos, shdr)
            print(f' {spos + sizeof(shdr):x} {shdr.startup_size - sizeof(shdr):x}  startup.*')
        display_ihdr(ipos, ihdr)
        print(f' {dpos:x} {ihdr.hdr_dir_size - ihdr.dir_offset:x} Image-directory')

        processing_done = False
        while not processing_done:
            fin2.seek(dpos)
            attr = struct_image_attr.from_buffer_copy(fin2.read(sizeof(struct_image_attr)))
            if ihdr.flags & IMAGE_FLAGS_BIGENDIAN :
                attr = attr_byteswap(attr)
            if attr.size < sizeof(attr):
                logger.warning(f'Invalid dir entry')
                return errno.EINVAL
            elif attr.size > sizeof(attr):
                buf_to_read = attr.size - sizeof(attr)
                buf = fin2.read(buf_to_read)
                if buf.__len__() != buf_to_read:
                    logger.warning(f'Error reading dir_ent')
                    return errno.EINVAL

            dpos += attr.size

            endian = '<' if not (ihdr.flags & IMAGE_FLAGS_BIGENDIAN) else '>'
            attrmode = attr.mode & S_IFMT
            if attrmode == S_IFREG:
                path_strlen = buf.__len__() - sizeof(c_uint32) * 2
                offset, size, path, *_ = unpack(f'{endian}2I{path_strlen}s', buf)
                file_path = path[:path.index(b'\x00')].decode('ascii')
                process_file(fin2, outputdir, ipos, attr, offset, size, file_path)
                display_file(ipos, offset, size, file_path)
                if (file_size - (ipos + offset + size)) < 8:
                    processing_done = True

            elif attrmode == S_IFDIR:
                path_strlen = buf.__len__()
                path, *_ = unpack(f'{endian}{path_strlen}s', buf)
                dir_path = path[:path.index(b'\x00')].decode('ascii')
                process_dir(outputdir, attr, dir_path)
                display_dir(dir_path)

            elif attrmode == S_IFLNK:
                path_strlen = buf.__len__() - sizeof(c_uint16) * 2
                sym_offset, sym_size, path, *_ = unpack(f'{endian}2H{path_strlen}s', buf)
                sym_path = path[:path.index(b'\x00')].decode('ascii')
                target = path[sym_offset:path.index(b'\00', sym_offset + 1)].decode('ascii')
                process_symlink(outputdir, attr, sym_path, target)
                display_symlink(sym_size, sym_path, target)
            else:
                path_strlen = buf.__len__() - sizeof(c_uint32) * 2
                dev, rdev, path, *_ = unpack(f'{endian}2I{path_strlen}s', buf)
                dev_path = path[:path.index(b'\x00')].decode('ascii')
                if attrmode == S_IFCHR:
                    attr_str = 'S_IFCHR'
                elif attrmode == S_IFBLK:
                    attr_str = 'S_IFBLK'
                elif attrmode == S_IFIFO:
                    attr_str = 'S_IFIFO'
                display_device(dev_path, dev, rdev, attr_str)

    return 0


def attr_byteswap(attr:struct_image_attr)->struct_image_attr:
    for fn, _ in attr._fields_:
        bytelen = getattr(struct_image_attr, fn).size
        v = getattr(attr, fn).byteswap(bytelen)
        setattr(attr, fn, v)
    return attr


def display_file(ipos: int, offset: int, size: int, path: str) -> None:
    print(f' {ipos + offset:8x} {size:8x}  {path}')


def process_file(fin2: BinaryIO, outputdir: Path, ipos: int, attr: struct_image_attr, offset: int, size: int,
                 path: str):
    filePath = outputdir / Path(path)
    filePath.parent.mkdir(parents=True, exist_ok=True)
    with open(filePath, 'wb') as fout:
        oldpos = fin2.tell()
        fin2.seek(ipos + offset)
        fout.write(fin2.read(size))
        fin2.seek(oldpos)
    os.utime(filePath, (attr.mtime, attr.mtime))
    # res = run_v1(f'sudo chmod {attr.mode & 0o7777:03o} {filePath}')
    # if res.returncode!=0:
    #     logger.debug(f'res.stderr=\n{res.stderr}')


def process_dir(outputdir: Path, attr: struct_image_attr, path: str):
    if not path:
        return
    filePath = outputdir / Path(path)
    filePath.mkdir(parents=True, exist_ok=True)
    os.utime(filePath, (attr.mtime, attr.mtime), follow_symlinks=False)
    # res = run_v1(f'sudo chmod {attr.mode & 0o7777:03o} {filePath}')
    # if res.returncode != 0:
    #     logger.debug(f'res.stderr=\n{res.stderr}')


def display_dir(path: str):
    filename = 'Root-dirent' if not path else path
    print(f'     ----     ----  {filename}')


def process_symlink(outputdir: Path, attr: struct_image_attr, path: str, target: str):
    filePath = outputdir / path
    filePath.parent.mkdir(parents=True, exist_ok=True)
    if target[0] == '/':
        target_is_abs = True
        sym_target = (outputdir / target[1:]).resolve()
    else:
        target_is_abs = False
        sym_target = (outputdir / filePath / target).resolve()

    if not sym_target.is_absolute():
        target_abspath = (filePath.parent / sym_target).resolve()
        if not target_abspath.exists():
            logger.debug(f'{target_abspath=} not exist')
    else:
        if not sym_target.exists():
            logger.debug(f'{sym_target} not exists')
    if filePath.exists():
        shutil_rm(filePath)
    try:
        filePath.symlink_to(target)
    except Exception as ex:
        logger.warning('ex=%s, type(ex)=%s, filePath=%s, target=%s', ex, type(ex), filePath, target)
    try:
        os.utime(filePath, (attr.mtime, attr.mtime), follow_symlinks=False)
    except FileNotFoundError:
        pass
    except PermissionError:
        pass
    # res = run_v1(f'sudo chmod {attr.mode & 0o7777:03o} {filePath}')
    # if res.returncode != 0:
    #    logger.debug(f'res.stderr=\n{res.stderr}')


def display_symlink(sym_size: int, path: str, target: str):
    print(f'     ---- {sym_size:8x}  {path} -> {target}')


def display_device(dev_path: str, dev: int, rdev: int, attr_str: str):
    print(f'     ----     ----  {dev_path} dev={dev} rdev={rdev} {attr_str}')


def find(fin: BinaryIO, pattern: bytes, start_pos: int = 0) -> int:
    import math
    from itertools import count
    chunk_size: int = 4 * 1024 * 1024
    # start_chunk: int = start_pos // chunk_size
    oldpos = fin.tell()
    file_len = os.lstat(fin.name).st_size
    # total_chunks = math.ceil(file_len/chunk_size)
    # fin.seek(start_chunk * chunk_size)
    fin.seek(start_pos)
    try:
        for chunk_pos in count():
            chunk = fin.read(chunk_size)
            if not chunk:
                return -1
            matches = list(re.finditer(pattern, chunk))
            if matches:
                return matches[0].start() + chunk_pos * chunk_size + start_pos
            chunk_pos += 1
        return -1
    finally:
        fin.seek(oldpos)


def display_shdr(spos: int, hdr: struct_startup_header):
    print(
        f' {spos:8x} {hdr.header_size:8x}  Startup-header flags1=0x{hdr.flags1:x} flags2=0x{hdr.flags2:x} paddr_bias=0x{hdr.paddr_bias:x}')


def display_ihdr(ipos: int, hdr: struct_image_header):
    print(f' {ipos:8x} {sizeof(hdr):8x}  Image-header')


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s %(name)s [%(filename)s:%(lineno)s - %(funcName)s] %(levelname)s %(message)s",
        stream=sys.stdout, level=logging.INFO)
    ret = main()
    sys.exit(ret)
