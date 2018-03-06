#!/usr/bin/env python3

import pathlib

def file_paths():
    pth = pathlib.Path('./')
    for f in pth.iterdir():
        if f.is_file():
            print(f.absolute())

def file_duplication(source_filename, dest_filename, binary = False):
    if binary:
        bnry = 'b'
    else:
        bnry = ''
    f = pathlib.Path(source_filename)
    if f.is_file():
        with open(source_filename, 'r' + bnry) as src, open(
                dest_filename, 'w' + bnry) as dst:
            if not binary:
                for line in src:
                    dst.write(line)


if __name__ == '__main__':
    file_paths()
