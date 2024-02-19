import logging
import subprocess
from pathlib import Path
import shutil

logger = logging.getLogger(__name__)
class RunCmdFailed(Exception):
    def __init__(self, cmd: str, stderr: str):
        self.cmd = cmd
        self.stderr = stderr

def run_v1(cmd: str, shell: bool = True, check_result: bool = False, suppress_warning=False,
           cwd=None) -> subprocess.CompletedProcess:
    """
    it is suitable to stdout length less than 4kb
    :param cmd:
    :param shell:
    :param check_result: if True and returncode != 0 then RunCmdFailed() will be raised
    :param suppress_warning: logger don't warning when returncode not zero when this param is true
    :param cwd: Sets the current directory before the child is executed.
    :return:
    """
    from shlex import split, quote
    resp = subprocess.run(cmd if shell else [quote(_) for _ in split(cmd)], shell=shell, capture_output=True,
                          encoding='utf8', errors='backslashreplace', cwd=cwd)
    if resp.returncode != 0:
        if check_result:
            raise RunCmdFailed(cmd, resp.stderr)
        elif not suppress_warning:
            logger.warning(f"cmd=`{cmd}`; {resp.returncode=} ; {resp.stderr=!s}")
    return resp


def shutil_rm(path: Path, ignore_errors=True):
    if path.is_symlink() or path.is_file():
        path.unlink(missing_ok=ignore_errors)
    elif path.is_dir():
        shutil.rmtree(path, ignore_errors=ignore_errors)
