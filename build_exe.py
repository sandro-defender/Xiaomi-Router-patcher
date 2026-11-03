#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build a standalone XMiR-Patcher executable (.exe on Windows).

Usage:
    python build_exe.py                 # build onedir bundle into dist/XMiR-Patcher/
    python build_exe.py --onefile       # build a single dist/XMiR-Patcher.exe instead
    python build_exe.py --install-deps  # also pip-install requirements.txt first

The onedir build is recommended: the scripts read/write files relative to the
tool root (data/, kmod/, tmp/, config.txt, ...), which works out of the box
when the .exe sits next to those folders, exactly like run.bat.
"""

import argparse
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SPEC = os.path.join(ROOT, 'xmir_patcher.spec')
DIST = os.path.join(ROOT, 'dist')
BUILD = os.path.join(ROOT, 'build')


def run(cmd, **kwargs):
    print('+', ' '.join(cmd))
    subprocess.run(cmd, cwd=ROOT, check=True, **kwargs)


def ensure_pyinstaller():
    try:
        import PyInstaller  # noqa: F401
        return
    except ImportError:
        print('PyInstaller not found - installing...')
        run([sys.executable, '-m', 'pip', 'install', 'pyinstaller'])


def main():
    parser = argparse.ArgumentParser(description='Build the XMiR-Patcher standalone executable.')
    parser.add_argument('--onefile', action='store_true',
                        help='produce a single-file exe instead of an onedir bundle')
    parser.add_argument('--install-deps', action='store_true',
                        help='pip-install requirements.txt before building')
    parser.add_argument('--no-clean', action='store_true',
                        help='do not delete previous build/ and dist/ folders')
    args = parser.parse_args()

    if args.install_deps:
        run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

    ensure_pyinstaller()

    if not args.no_clean:
        for folder in (BUILD, DIST):
            shutil.rmtree(folder, ignore_errors=True)

    cmd = [sys.executable, '-m', 'PyInstaller', '--clean', '--noconfirm']
    if args.onefile:
        cmd.append('--onefile')
    cmd.append(SPEC)
    run(cmd)

    out = os.path.join(DIST, 'XMiR-Patcher.exe' if args.onefile else 'XMiR-Patcher')
    if not os.path.exists(out):
        print('ERROR: expected output not found:', out, file=sys.stderr)
        return 1

    # Convenience launcher mirroring !START.bat for the onedir bundle.
    if not args.onefile:
        bat = os.path.join(DIST, 'XMiR-Patcher', 'XMiR-Patcher.bat')
        with open(bat, 'w', newline='\r\n') as f:
            f.write('@echo off\r\n'
                    'chcp 65001 >NUL\r\n'
                    'cd /d "%~dp0"\r\n'
                    'start "" "%~dp0XMiR-Patcher.exe" %*\r\n')

    print('\nBuild finished: ' + out)
    return 0


if __name__ == '__main__':
    sys.exit(main())
