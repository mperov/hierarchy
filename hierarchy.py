#!/bin/env python3
## -*- coding: utf-8 -*-

#
# Copyright (c) 2023 Maksim Perov <coder@frtk.ru>
#

from argparse import ArgumentParser

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
    parser.print_help()
