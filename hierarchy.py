#!/bin/env python3
## -*- coding: utf-8 -*-

#
# Copyright (c) 2023 Maksim Perov <coder@frtk.ru>
#

import os
from argparse import ArgumentParser

def eprint(message):
    print(message)
    exit(-1)

def walkLevel(some_dir, level=-1):
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        path = root.split(os.sep)
        print(root)
        num_sep_this = root.count(os.path.sep)
        if level > -1:
            if num_sep + level <= num_sep_this:
                del dirs[:]

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-d", "--dir", dest="dir",
                        help="path to directory. This argument is main!", metavar="/path/to/directory")
    parser.add_argument("-s", "--server", dest="server",
                        help="target remote server", metavar="ip address or hostname")
    parser.add_argument("-v", "--verbose", action='store_true',
                        help="this option enables debug mode")
    args = parser.parse_args()
    debug = args.verbose
    directory = args.dir
    level = 0
    if directory:
        if not os.path.isdir(directory):
            eprint(directory + " is not directory!")
        walkLevel(directory)
    else:
        parser.print_help()
