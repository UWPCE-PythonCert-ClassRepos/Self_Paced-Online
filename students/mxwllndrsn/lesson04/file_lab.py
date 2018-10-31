#!/usr/bin/env python3

#uw python 210
#lesson04
#max anderson

#file lab

if __name__ == "__main__":

    import pathlib
    import os
    import io

    #pth = pathlib.Path('./')

   # print(pth.absolute())

    lst = os.listdir()
    pth = os.getcwd()

    for file in lst:
        print(f'{pth}\\{file}')

    with open('secrets.txt', 'r') as instream:
        with open('secrets2.txt', 'w+') as outstream:
            line = instream.read()
            outstream.write(line)

    instream = open()