#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""XMiR-Patcher entry point.

Works both as a plain Python script and as a PyInstaller-frozen executable:

* no arguments                              -> start the interactive menu (menu.py)
* first argument is a bundled script name   -> run that script (e.g. "connect.py")

This mirrors run.sh / run.bat behaviour, where menu.py re-launches sub-scripts
via ``subprocess.run([sys.executable, "<script>"])``: when frozen,
``sys.executable`` is this executable itself, so the dispatch below handles it.
"""

import os
import runpy
import sys


def base_dir():
    """Directory that holds the scripts and the data/ folders."""
    if getattr(sys, 'frozen', False):
        # PyInstaller onedir build: the .exe sits next to the bundled files.
        return os.path.dirname(os.path.abspath(sys.executable))
    return os.path.dirname(os.path.abspath(__file__))


def main():
    base = base_dir()
    # Scripts use paths relative to the tool root (data/, kmod/, bootloader/...).
    os.chdir(base)

    args = sys.argv[1:]
    script = None
    if args and args[0].endswith('.py') and os.path.isfile(os.path.join(base, args[0])):
        script = args.pop(0)

    if script is None:
        script = 'menu.py'

    path = os.path.join(base, script)
    sys.argv = [path] + args
    runpy.run_path(path, run_name='__main__')


if __name__ == '__main__':
    main()
