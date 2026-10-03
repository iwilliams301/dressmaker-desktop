"""Dressmaker Desktop — A local helper for Dressmaker studio folders, pattern files, and runway photos."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='dressmaker_desktop',
        description='A local helper for Dressmaker studio folders, pattern files, and runway photos.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Dressmaker Desktop')
    print('Keep the atelier on disk before a style pack.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
