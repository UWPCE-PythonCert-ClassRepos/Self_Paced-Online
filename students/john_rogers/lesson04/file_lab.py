#!/usr/bin/env python3
"""
ungraded lab work for working with files
Author: JohnR
Version: .5
Date: 12/28/2018
Notes: Having trouble copying the text file - no such file or directory
"""

import pathlib as path


def main():
    """
    1) print the full path for all files in the current directory, 1/line.
    2) copy a file from a source to destination (no shutil or os copy)
    3) make it work for any file size (don't read all into memory)
    4) make it wor for any file type; use binary mode and a jpg file
        NOTE: readline() has no meaning for binary files
    5) test with both text files and binary files
    :return:
    """
    print()
    dir_contents()
    print()

    print('Use the format c:/foo/somefile.txt')

    file_a = input('File to copy: ')
    file_b = input('New location and name: ')

    file_copy(file_a, file_b)


def dir_contents():
    """
    print out contents of current directory, one per line (full path)
    :return: none
    """
    # set the working directory
    pth = path.Path('./')

    # this prints the file only, one per line
    for i in pth.iterdir():
        print(i)

    # print out the sub-directories using a list generator(?)
    print([x for x in pth.iterdir() if x.is_dir()])

    # print files with full path
    for i in pth.iterdir():
        print(i.absolute())


def file_copy(source, destination):
    """
    copy a file from source to destination
    test with any size or file type
    :return:
    """
    # this work for a binary file, but is fragile
    with open(source, 'rb') as infile, open(destination, 'wb') as outfile:
        outfile.write(infile.read())

    # this doesn't see the source file
    # with open(source, 'r') as infile, open(destination, 'w') as outfile:
    #    outfile.write(infile.read())


if __name__ == '__main__':
    main()
