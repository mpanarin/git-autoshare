# -*- coding: utf-8 -*-
# Copyright © 2017 ACSONE SA/NV
# License GPLv3 (http://www.gnu.org/licenses/gpl-3.0-standalone.html)

from __future__ import print_function

import subprocess
import sys

from .core import git_bin, transform_cmd


def main():
    cmd = [git_bin(), 'clone'] + sys.argv[1:]
    skip = any(
        c in cmd for c in [
            '--reference',
            '--reference-if-able',
            '-s',
            '--share',
        ]
    )
    if not skip:
        quiet = '-q' in cmd or '--quiet' in cmd
        cmd = transform_cmd(cmd, quiet)
    r = subprocess.call(cmd)
    sys.exit(r)
