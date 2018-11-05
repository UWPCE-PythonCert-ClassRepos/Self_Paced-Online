#!/usr/bin/env python3

# Activity 2 File Lab

# import
import pathlib


def main():

    # print the full path for all files in a directory
    pth = pathlib.Path('./')
    for files in pth.iterdir():
        print(files.absolute())

    # copy a file
    with open('C:/Users/thood/Documents/Python/Python210-TESTING AREA/lesson04_test/Test.txt', 'rb') as sr:
        with open('C:/Users/thood/Documents/Python/Python210-TESTING AREA/lesson04_test/Test_copy.txt', 'wb') as dt:
            for stuff in sr:
                dt.write(stuff)


if __name__ == '__main__':
    main()
