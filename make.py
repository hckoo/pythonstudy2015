from distutils.core import setup
import py2exe
from glob import glob

data_files = [("VC90", glob(r'C:\\Windows\\winsxs\\x86_microsoft.vc90.crt_1fc8b3b9a1e18e3b_9.0.21022.8_none_bcb86ed6ac711f91\\*.*')),
            ("VC90", glob(r'C:\\Windows\\winsxs\\Manifests\\x86_microsoft.vc90.crt_1fc8b3b9a1e18e3b_9.0.21022.8_none_bcb86ed6ac711f91.manifest'))
]

excludes = [
    "pywin",
    "pywin.debugger",
    "pywin.debugger.dbgcon",
    "pywin.dialogs",
    "pywin.dialogs.list",
    "win32com.server",
]

options = {
    "bundle_files": 1,                 # create singlefile exe
    "compressed"  : 1,                 # compress the library archive
    "excludes"    : excludes,
    "dll_excludes": ["w9xpopen.exe","POWRPROF.dll"]   # we don't need this
 }

setup(
    data_files=data_files,
    options = {"py2exe": options},
    zipfile = None,
    #console = ['TobeInterfaceV4.py'],
    console = ['PCDrv_V2.py'],

)