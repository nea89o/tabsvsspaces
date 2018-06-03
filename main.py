#!/usr/bin/env python3.6

import argparse
from pathlib import Path

from lib.argparse.pathtype import PathType
from lib.find_stats import find_stats
from lib.print_stats import print_stats
from lib.stats import Statistics


def main():
    parser = argparse.ArgumentParser(
        prog='tabsvsspaces',
        description='Shows statistics about the usage of tabs and spaces in a given folder'
    )
    parser.add_argument('folder',
                        type=PathType(type='dir', exists=True))
    parser.add_argument('--by-extension', '-e',
                        dest='extension',
                        action='store_true',
                        help='show distribution by file extension'
                        )
    parser.add_argument('--verbose', '-v',
                        dest='verbose',
                        action='store_true',
                        help='show debug information')
    ns = parser.parse_args()
    folder: str = ns.folder
    extension: bool = ns.extension
    verbose: bool = ns.verbose
    stats: Statistics = find_stats(Path(folder), verbose=verbose)
    print_stats(stats, extension)


if __name__ == '__main__':
    main()
