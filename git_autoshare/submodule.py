# -*- coding: utf-8 -*-
# Copyright 2018 Camptocamp SA
# License GPLv3 (http://www.gnu.org/licenses/gpl-3.0-standalone.html)

from __future__ import print_function

import subprocess
import sys

from .core import get_submodules_paths, git_bin, transform_cmd


def add():
    cmd = [git_bin(), 'submodule', 'add'] + sys.argv[1:]
    skip = '--reference' in cmd
    if not skip:
        quiet = '-q' in cmd or '--quiet' in cmd
        cmd = transform_cmd(cmd, quiet)
    r = subprocess.call(cmd)
    sys.exit(r)


def update():
    args = sys.argv[1:]
    # no repositories passed -> operating on all
    multi_repo = not [x for x in args if not x.startswith('-')]
    skip = '--reference' in args
    cmd = [git_bin(), 'submodule', 'update'] + args
    if not skip:
        quiet = '-q' in cmd or '--quiet' in cmd
        if multi_repo:
            modules = get_submodules_paths()
            for module in modules:
                mod_cmd = cmd.copy()
                mod_cmd.append(module)
                mod_cmd = transform_cmd(mod_cmd, quiet, submodule_path=True)
                r = subprocess.call(mod_cmd)
                if r:
                    sys.exit(r)
            sys.exit(0)
        else:
            cmd = transform_cmd(cmd, quiet, submodule_path=True)
    r = subprocess.call(cmd)
    sys.exit(r)
