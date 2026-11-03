# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller spec for the XMiR-Patcher standalone executable.

Builds an onedir bundle named "XMiR-Patcher": the .exe sits in dist/XMiR-Patcher/
together with all helper scripts and the data/, firmware/, bootloader/, kmod/,
image/ and xmir_base/ folders, so the relative paths used by the scripts keep
working exactly like when running run.bat from the repository root.

Run via build_exe.py (recommended) or directly:
    pyinstaller --clean xmir_patcher.spec
"""

import glob
import os

from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

# Bundle every top-level script so the frozen exe can re-launch them through
# subprocess.run([sys.executable, "<script>"]) exactly like run.bat does.
datas = [(f, '.') for f in glob.glob('*.py')]

# Resource folders used by the scripts (relative paths from the tool root).
for folder in ['data', 'firmware', 'bootloader', 'kmod', 'image', 'xmir_base']:
    if os.path.isdir(folder):
        datas.append((folder, folder))

for extra in ['README.md', 'LICENSE', 'requirements.txt']:
    if os.path.isfile(extra):
        datas.append((extra, '.'))

# Packages whose submodules are imported dynamically (ssh2, xmir_base vendored
# fdt/ubireader/telnetlib, pyftpdlib, requests stack) must be forced in.
hiddenimports = []
for pkg in ['requests', 'urllib3', 'certifi', 'charset_normalizer', 'idna',
            'ssh2', 'pyftpdlib', 'xmir_base']:
    hiddenimports += collect_submodules(pkg)

a = Analysis(
    ['xmir_patcher.py'],
    pathex=[os.getcwd()],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['tkinter', 'matplotlib', 'numpy', 'PIL'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='XMiR-Patcher',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='XMiR-Patcher',
)
