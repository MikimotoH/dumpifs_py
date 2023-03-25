r"""Wrapper for startup.h

Generated with:
/home/miki/miniconda3/bin/ctypesgen -lc startup.h image.h

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

import ctypes
import sys
from ctypes import *  # noqa: F401, F403

_int_types = (ctypes.c_int16, ctypes.c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have ctypes.c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if ctypes.sizeof(t) == ctypes.sizeof(ctypes.c_size_t):
        c_ptrdiff_t = t
del t
del _int_types


class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=False):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        super().__init__(string)
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1:]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1:]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, ctypes.Union):
    _fields_ = [("raw", ctypes.POINTER(ctypes.c_char)), ("data", ctypes.c_char_p)]

    def __init__(self, obj=b""):
        super().__init__(obj)
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, ctypes.c_char_p):
            return obj

        # Convert from POINTER(ctypes.c_char)
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))

        # Convert from ctypes.c_char array
        elif isinstance(obj, ctypes.c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to ctypes.c_void_p.
def UNCHECKED(type_):
    if hasattr(type_, "_type_") and isinstance(type_._type_, str) and type_._type_ != "P":
        return type_
    else:
        return ctypes.c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value


# End preamble

_libs = {}
_libdirs = []

# Begin loader

"""
Load libraries - appropriately for all our supported platforms
"""
# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import ctypes
import ctypes.util
import glob
import os.path
import platform
import re
import sys


def _environ_path(name):
    """Split an environment variable into a path-like list elements"""
    if name in os.environ:
        return os.environ[name].split(":")
    return []


class LibraryLoader:
    """
    A base class For loading of libraries ;-)
    Subclasses load libraries for specific platforms.
    """

    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup:
        """Looking up calling conventions for a platform"""

        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            """Return the given name according to the selected calling convention"""
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            """Return True if this given calling convention finds the given 'name'"""
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            # noinspection PyBroadException
            try:
                return self.Lookup(path)
            except Exception:  # pylint: disable=broad-except
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # check if this code is even stored in a physical file
            try:
                this_file = __file__
            except NameError:
                this_file = None

            # then we search the directory where the generated python interface is stored
            if this_file is not None:
                for fmt in self.name_formats:
                    yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, _libname):  # pylint: disable=no-self-use
        """Return all the library paths available in this platform"""
        return []


# # Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    """Library loader for MacOS"""

    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        """
        Looking up library files for this platform (Darwin aka MacOS)
        """

        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [fmt % libname for fmt in self.name_formats]

        for directory in self.getdirs(libname):
            for name in names:
                yield os.path.join(directory, name)

    @staticmethod
    def getdirs(libname):
        """Implements the dylib search as specified in Apple documentation:

        https://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [
                os.path.expanduser("~/lib"),
                "/usr/local/lib",
                "/usr/lib",
            ]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
            dirs.extend(_environ_path("LD_RUN_PATH"))

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    """Library loader for POSIX-like systems (including Linux)"""

    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    name_formats = ["lib%s.so", "%s.so", "%s"]

    class _Directories(dict):
        """Deal with directories"""

        def __init__(self):
            dict.__init__(self)
            self.order = 0

        def add(self, directory):
            """Add a directory to our current set of directories"""
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            order = self.setdefault(directory, self.order)
            if order == self.order:
                self.order += 1

        def extend(self, directories):
            """Add a list of directories to our set"""
            for a_dir in directories:
                self.add(a_dir)

        def ordered(self):
            """Sort the list of directories"""
            return (i[0] for i in sorted(self.items(), key=lambda d: d[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive function to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as fileobj:
                for dirname in fileobj:
                    dirname = dirname.strip()
                    if not dirname:
                        continue

                    match = self._include.match(dirname)
                    if not match:
                        dirs.add(dirname)
                    else:
                        for dir2 in glob.glob(match.group("pattern")):
                            self._get_ld_so_conf_dirs(dir2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
                "LD_LIBRARY_PATH",
                "SHLIB_PATH",  # HP-UX
                "LIBPATH",  # OS/2, AIX
                "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compatible
                unix_lib_dirs_list += [
                    "/lib/x86_64-linux-gnu",
                    "/usr/lib/x86_64-linux-gnu",
                ]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        # ext_re = re.compile(r"\.s[ol]$")
        for our_dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % our_dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# # Windows


class WindowsLibraryLoader(LibraryLoader):
    """Library loader for Microsoft Windows"""

    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        """Lookup class for Windows libraries..."""

        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

# load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()
load_library = PosixLibraryLoader()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for path in other_dirs:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        load_library.other_dirs.append(path)


del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries
_libs["c"] = load_library("c")


# 1 libraries
# End libraries

# No modules

# /home/miki/dumpifs/sys/startup.h: 44
class struct_startup_header(Structure):
    _fields_ = [
        ('signature', c_uint),
        ('version', c_ushort),
        ('flags1', c_ubyte),
        ('flags2', c_ubyte),
        ('header_size', c_ushort),
        ('machine', c_ushort),
        ('startup_vaddr', c_uint),
        ('paddr_bias', c_uint),
        ('image_paddr', c_uint),
        ('ram_paddr', c_uint),
        ('ram_size', c_uint),
        ('startup_size', c_uint),
        ('stored_size', c_uint),
        ('imagefs_paddr', c_uint),
        ('imagefs_size', c_uint),
        ('preboot_size', c_ushort),
        ('zero0', c_ushort),
        ('zero', c_uint * int(3)),
        ('info', c_uint * int(48)),
    ]


enum_startup_info_types = c_int  # /home/miki/dumpifs/sys/startup.h: 252

STARTUP_INFO_SKIP = 0  # /home/miki/dumpifs/sys/startup.h: 252

STARTUP_INFO_MEM = (STARTUP_INFO_SKIP + 1)  # /home/miki/dumpifs/sys/startup.h: 252

STARTUP_INFO_DISK = (STARTUP_INFO_MEM + 1)  # /home/miki/dumpifs/sys/startup.h: 252

STARTUP_INFO_TIME = (STARTUP_INFO_DISK + 1)  # /home/miki/dumpifs/sys/startup.h: 252

STARTUP_INFO_BOX = (STARTUP_INFO_TIME + 1)  # /home/miki/dumpifs/sys/startup.h: 252

STARTUP_INFO_USER = 0x8000  # /home/miki/dumpifs/sys/startup.h: 252


# /home/miki/dumpifs/sys/startup.h: 261
class struct_startup_info_hdr(Structure):
    __slots__ = [
        'type',
        'size',
    ]
    _fields_ = [
        ('type', c_ushort),
        ('size', c_ushort),
    ]


# /home/miki/dumpifs/sys/startup.h: 266
class struct_startup_info_skip(Structure):
    __slots__ = [
        'hdr',
    ]
    _fields_ = [
        ('hdr', struct_startup_info_hdr),
    ]


# /home/miki/dumpifs/sys/startup.h: 270
class struct_startup_info_mem(Structure):
    __slots__ = [
        'hdr',
        'addr',
        'size',
    ]
    _fields_ = [
        ('hdr', struct_startup_info_hdr),
        ('addr', c_ulong),
        ('size', c_ulong),
    ]


# /home/miki/dumpifs/sys/startup.h: 281
class struct_startup_info_mem_extended(Structure):
    __slots__ = [
        'mem',
        'addr_hi',
        'size_hi',
    ]
    _fields_ = [
        ('mem', struct_startup_info_mem),
        ('addr_hi', c_ulong),
        ('size_hi', c_ulong),
    ]


# /home/miki/dumpifs/sys/startup.h: 287
class struct_startup_info_disk(Structure):
    __slots__ = [
        'hdr',
        'drive',
        'zero',
        'heads',
        'cylinders',
        'sectors',
        'blocks',
    ]
    _fields_ = [
        ('hdr', struct_startup_info_hdr),
        ('drive', c_ubyte),
        ('zero', c_ubyte),
        ('heads', c_ushort),
        ('cylinders', c_ushort),
        ('sectors', c_ushort),
        ('blocks', c_ulong),
    ]


# /home/miki/dumpifs/sys/startup.h: 297
class struct_startup_info_time(Structure):
    __slots__ = [
        'hdr',
        'time',
    ]
    _fields_ = [
        ('hdr', struct_startup_info_hdr),
        ('time', c_ulong),
    ]


# /home/miki/dumpifs/sys/startup.h: 302
class struct_startup_info_box(Structure):
    __slots__ = [
        'hdr',
        'boxtype',
        'bustype',
        'spare',
    ]
    _fields_ = [
        ('hdr', struct_startup_info_hdr),
        ('boxtype', c_ubyte),
        ('bustype', c_ubyte),
        ('spare', c_ubyte * int(2)),
    ]


# /home/miki/dumpifs/sys/startup.h: 309
class struct_bootargs_entry(Structure):
    __slots__ = [
        'size_lo',
        'size_hi',
        'argc',
        'envc',
        'shdr_addr',
        'args',
    ]
    _fields_ = [
        ('size_lo', c_ubyte),
        ('size_hi', c_ubyte),
        ('argc', c_char),
        ('envc', c_char),
        ('shdr_addr', c_ulong),
        ('args', c_char * int(1)),
    ]

_Uint64t = c_ulong  # /home/miki/dumpifs/sys/startup.h: 318


# /home/miki/dumpifs/sys/startup.h: 329
class struct_startup_trailer(Structure):
    __slots__ = [
        'cksum',
    ]
    _fields_ = [
        ('cksum', c_ulong),
    ]

enum_anon_1 = c_int  # /home/miki/dumpifs/sys/image.h: 23

IMAGE_FLAGS_BIGENDIAN = 0x01  # /home/miki/dumpifs/sys/image.h: 23

IMAGE_FLAGS_READONLY = 0x02  # /home/miki/dumpifs/sys/image.h: 23

IMAGE_FLAGS_INO_BITS = 0x04  # /home/miki/dumpifs/sys/image.h: 23


# /home/miki/dumpifs/sys/image.h: 32
class struct_image_header(Structure):
    _fields_ = [
        ('signature', c_char * int(7)),
        ('flags', c_ubyte),
        ('image_size', c_uint),
        ('hdr_dir_size', c_uint),
        ('dir_offset', c_uint),
        ('boot_ino', c_uint * int(4)),
        ('script_ino', c_uint),
        ('chain_paddr', c_uint),
        ('spare', c_uint * int(10)),
        ('mountflags', c_uint),
        ('mountpoint', c_char * int(1)),
    ]


# /home/miki/dumpifs/sys/image.h: 47
class struct_ifs_bootstrap_head(Structure):
    __slots__ = [
        'signature',
        'bootstrap',
    ]
    _fields_ = [
        ('signature', c_uint),
        ('bootstrap', POINTER(None)),
    ]


# /home/miki/dumpifs/sys/image.h: 52
class struct_ifs_bootstrap_data(Structure):
    __slots__ = [
        'size',
        'next_entry',
        'args',
        'spare',
    ]
    _fields_ = [
        ('size', c_uint),
        ('next_entry', POINTER(None)),
        ('args', POINTER(None)),
        ('spare', c_uint),
    ]


# /home/miki/dumpifs/sys/image.h: 64
class struct_image_attr(Structure):
    _fields_ = [
        ('size', c_ushort),
        ('extattr_offset', c_ushort),
        ('ino', c_uint),
        ('mode', c_uint),
        ('gid', c_uint),
        ('uid', c_uint),
        ('mtime', c_uint),
    ]


# /home/miki/dumpifs/sys/image.h: 73
class struct_image_file(Structure):
    __slots__ = [
        'attr',
        'offset',
        'size',
        'path',
    ]
    _fields_ = [
        ('attr', struct_image_attr),
        ('offset', c_uint),
        ('size', c_uint),
        ('path', c_char * int(1)),
    ]



# /home/miki/dumpifs/sys/image.h: 79
class struct_image_dir(Structure):
    __slots__ = [
        'attr',
        'path',
    ]
    _fields_ = [
        ('attr', struct_image_attr),
        ('path', c_char * int(1)),
    ]


# /home/miki/dumpifs/sys/image.h: 83
class struct_image_symlink(Structure):
    __slots__ = [
        'attr',
        'sym_offset',
        'sym_size',
        'path',
    ]
    _fields_ = [
        ('attr', struct_image_attr),
        ('sym_offset', c_ushort),
        ('sym_size', c_ushort),
        ('path', c_char * int(1)),
    ]


# /home/miki/dumpifs/sys/image.h: 90
class struct_image_device(Structure):
    __slots__ = [
        'attr',
        'dev',
        'rdev',
        'path',
    ]
    _fields_ = [
        ('attr', struct_image_attr),
        ('dev', c_uint),
        ('rdev', c_uint),
        ('path', c_char * int(1)),
    ]


# /home/miki/dumpifs/sys/image.h: 63
class union_image_dirent(Union):
    __slots__ = [
        'attr',
        'file',
        'dir',
        'symlink',
        'device',
    ]
    _fields_ = [
        ('attr', struct_image_attr),
        ('file', struct_image_file),
        ('dir', struct_image_dir),
        ('symlink', struct_image_symlink),
        ('device', struct_image_device),
    ]


# /home/miki/dumpifs/sys/image.h: 98
class struct_image_trailer(Structure):
    __slots__ = [
        'cksum',
    ]
    _fields_ = [
        ('cksum', c_uint),
    ]


# /home/miki/dumpifs/sys/image.h: 133
class struct_script_hdr(Structure):
    __slots__ = [
        'size_lo',
        'size_hi',
        'type',
        'spare',
    ]
    _fields_ = [
        ('size_lo', c_ubyte),
        ('size_hi', c_ubyte),
        ('type', c_ubyte),
        ('spare', c_ubyte),
    ]


# /home/miki/dumpifs/sys/image.h: 145
class struct_anon_2(Structure):
    __slots__ = [
        'id',
        'reserved',
    ]
    _fields_ = [
        ('id', c_ubyte),
        ('reserved', c_ubyte * int(1)),
    ]


# /home/miki/dumpifs/sys/image.h: 143
class union_script_external_extsched(Union):
    __slots__ = [
        'reserved',
        'aps',
    ]
    _fields_ = [
        ('reserved', c_ubyte * int(2)),
        ('aps', struct_anon_2),
    ]


# /home/miki/dumpifs/sys/image.h: 139
class struct_script_external(Structure):
    __slots__ = [
        'hdr',
        'cpu',
        'flags',
        'extsched',
        'policy',
        'priority',
        'argc',
        'envc',
        'args',
    ]
    _fields_ = [
        ('hdr', struct_script_hdr),
        ('cpu', c_ubyte),
        ('flags', c_ubyte),
        ('extsched', union_script_external_extsched),
        ('policy', c_ubyte),
        ('priority', c_ubyte),
        ('argc', c_ubyte),
        ('envc', c_ubyte),
        ('args', c_char * int(1)),
    ]


# /home/miki/dumpifs/sys/image.h: 156
class struct_script_waitfor_reopen(Structure):
    __slots__ = [
        'hdr',
        'checks_lo',
        'checks_hi',
        'fname',
    ]
    _fields_ = [
        ('hdr', struct_script_hdr),
        ('checks_lo', c_ubyte),
        ('checks_hi', c_ubyte),
        ('fname', c_char * int(1)),
    ]


# /home/miki/dumpifs/sys/image.h: 162
class struct_script_display_msg(Structure):
    __slots__ = [
        'hdr',
        'msg',
    ]
    _fields_ = [
        ('hdr', struct_script_hdr),
        ('msg', c_char * int(1)),
    ]


# /home/miki/dumpifs/sys/image.h: 166
class struct_script_procmgr_symlink(Structure):
    __slots__ = [
        'hdr',
        'src_dest',
    ]
    _fields_ = [
        ('hdr', struct_script_hdr),
        ('src_dest', c_char * int(1)),
    ]


# /home/miki/dumpifs/sys/image.h: 170
class struct_script_extsched_aps(Structure):
    __slots__ = [
        'hdr',
        'parent',
        'budget',
        'critical_lo',
        'critical_hi',
        'id',
        'pname',
    ]
    _fields_ = [
        ('hdr', struct_script_hdr),
        ('parent', c_ubyte),
        ('budget', c_ubyte),
        ('critical_lo', c_ubyte),
        ('critical_hi', c_ubyte),
        ('id', c_ubyte),
        ('pname', c_char * int(1)),
    ]


# /home/miki/dumpifs/sys/image.h: 132
class union_script_cmd(Union):
    __slots__ = [
        'hdr',
        'external',
        'waitfor_reopen',
        'display_msg',
        'procmgr_symlink',
        'extsched_aps',
    ]
    _fields_ = [
        ('hdr', struct_script_hdr),
        ('external', struct_script_external),
        ('waitfor_reopen', struct_script_waitfor_reopen),
        ('display_msg', struct_script_display_msg),
        ('procmgr_symlink', struct_script_procmgr_symlink),
        ('extsched_aps', struct_script_extsched_aps),
    ]

# /home/miki/dumpifs/sys/startup.h: 73
# noinspection PyBroadException
try:
    STARTUP_HDR_FLAGS1_VIRTUAL = 0x01
except:
    pass

# /home/miki/dumpifs/sys/startup.h: 74
try:
    STARTUP_HDR_FLAGS1_BIGENDIAN = 0x02
except:
    pass

# /home/miki/dumpifs/sys/startup.h: 75
try:
    STARTUP_HDR_FLAGS1_COMPRESS_MASK = 0x1c
except:
    pass

# /home/miki/dumpifs/sys/startup.h: 76
try:
    STARTUP_HDR_FLAGS1_COMPRESS_SHIFT = 0x02
except:
    pass

# /home/miki/dumpifs/sys/startup.h: 77
try:
    STARTUP_HDR_FLAGS1_COMPRESS_NONE = 0x00
except:
    pass

# /home/miki/dumpifs/sys/startup.h: 78
try:
    STARTUP_HDR_FLAGS1_COMPRESS_ZLIB = 0x04
except:
    pass

# /home/miki/dumpifs/sys/startup.h: 79
try:
    STARTUP_HDR_FLAGS1_COMPRESS_LZO = 0x08
except:
    pass

# /home/miki/dumpifs/sys/startup.h: 80
try:
    STARTUP_HDR_FLAGS1_COMPRESS_UCL = 0x0c
except:
    pass

# /home/miki/dumpifs/sys/startup.h: 83
try:
    STARTUP_HDR_SIGNATURE = 0x00ff7eeb
except:
    pass

# /home/miki/dumpifs/sys/startup.h: 84
try:
    STARTUP_HDR_VERSION = 1
except:
    pass


# /home/miki/dumpifs/sys/startup.h: 324
def __SC(ch, pos):
    return ((_Uint64t(ord_if_char(ch))).value << ((7 - pos) * 8))


# /home/miki/dumpifs/sys/startup.h: 326
try:
    __STACK_SIG = ((((((((__SC('d', 0)) + (__SC('d', 1))) + (__SC('p', 2))) + (__SC('v', 3))) + (__SC('b', 4))) + (
        __SC('s', 5))) + (__SC('k', 6))) + (__SC('r', 7)))
except:
    pass


# /home/miki/dumpifs/sys/image.h: 21
def __FLEXARY(__type, __name):
    return ((__type + __name)[1])


# /home/miki/dumpifs/sys/image.h: 30
try:
    IMAGE_SIGNATURE = 'imagefs'
except:
    pass

# /home/miki/dumpifs/sys/image.h: 31
try:
    IMAGE_SIGNATURE_REV = 'sfegami'
except:
    pass

# /home/miki/dumpifs/sys/image.h: 46
try:
    IFS_BOOTSTRAP_SIGNATURE = (((('B' << 24) | ('S' << 16)) | ('H' << 8)) | ('D' << 0))
except:
    pass

# /home/miki/dumpifs/sys/image.h: 59
try:
    IFS_INO_PROCESSED_ELF = 0x80000000
except:
    pass

# /home/miki/dumpifs/sys/image.h: 60
try:
    IFS_INO_RUNONCE_ELF = 0x40000000
except:
    pass

# /home/miki/dumpifs/sys/image.h: 61
try:
    IFS_INO_BOOTSTRAP_EXE = 0x20000000
except:
    pass

# /home/miki/dumpifs/sys/image.h: 103
try:
    SCRIPT_FLAGS_EXTSCHED = 0x01
except:
    pass

# /home/miki/dumpifs/sys/image.h: 104
try:
    SCRIPT_FLAGS_SESSION = 0x02
except:
    pass

# /home/miki/dumpifs/sys/image.h: 105
try:
    SCRIPT_FLAGS_SCHED_SET = 0x04
except:
    pass

# /home/miki/dumpifs/sys/image.h: 106
try:
    SCRIPT_FLAGS_CPU_SET = 0x08
except:
    pass

# /home/miki/dumpifs/sys/image.h: 107
try:
    SCRIPT_FLAGS_BACKGROUND = 0x20
except:
    pass

# /home/miki/dumpifs/sys/image.h: 108
try:
    SCRIPT_FLAGS_KDEBUG = 0x40
except:
    pass

# /home/miki/dumpifs/sys/image.h: 110
try:
    SCRIPT_POLICY_NOCHANGE = 0
except:
    pass

# /home/miki/dumpifs/sys/image.h: 111
try:
    SCRIPT_POLICY_FIFO = 1
except:
    pass

# /home/miki/dumpifs/sys/image.h: 112
try:
    SCRIPT_POLICY_RR = 2
except:
    pass

# /home/miki/dumpifs/sys/image.h: 113
try:
    SCRIPT_POLICY_OTHER = 3
except:
    pass

# /home/miki/dumpifs/sys/image.h: 115
try:
    SCRIPT_TYPE_EXTERNAL = 0
except:
    pass

# /home/miki/dumpifs/sys/image.h: 116
try:
    SCRIPT_TYPE_WAITFOR = 1
except:
    pass

# /home/miki/dumpifs/sys/image.h: 117
try:
    SCRIPT_TYPE_REOPEN = 2
except:
    pass

# /home/miki/dumpifs/sys/image.h: 118
try:
    SCRIPT_TYPE_DISPLAY_MSG = 3
except:
    pass

# /home/miki/dumpifs/sys/image.h: 119
try:
    SCRIPT_TYPE_PROCMGR_SYMLINK = 4
except:
    pass

# /home/miki/dumpifs/sys/image.h: 120
try:
    SCRIPT_TYPE_EXTSCHED_APS = 5
except:
    pass

# /home/miki/dumpifs/sys/image.h: 122
try:
    SCRIPT_CHECKS_MS = 100
except:
    pass

# /home/miki/dumpifs/sys/image.h: 124
try:
    SCRIPT_SCHED_EXT_NONE = 0
except:
    pass

# /home/miki/dumpifs/sys/image.h: 125
try:
    SCRIPT_SCHED_EXT_APS = 1
except:
    pass

# /home/miki/dumpifs/sys/image.h: 127
try:
    SCRIPT_APS_SYSTEM_PARTITION_ID = 0
except:
    pass

# /home/miki/dumpifs/sys/image.h: 128
try:
    SCRIPT_APS_SYSTEM_PARTITION_NAME = 'System'
except:
    pass

# /home/miki/dumpifs/sys/image.h: 129
try:
    SCRIPT_APS_PARTITION_NAME_LENGTH = 15
except:
    pass

# /home/miki/dumpifs/sys/image.h: 130
try:
    SCRIPT_APS_MAX_PARTITIONS = 8
except:
    pass


class gzFile_s(Structure):
    _fields_ = [
        ('have', ctypes.c_uint),
        ('next', ctypes.POINTER(ctypes.c_ubyte)),
        ('pos', ctypes.c_int64)
    ]

# No inserted files

# No prefix-stripping
