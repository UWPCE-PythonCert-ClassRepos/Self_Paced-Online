#!/usr/bin/env python3
print("")
import pathlib


# lab1 - print file names in current folder with full path
pth = pathlib.Path('./')
path1 = pth.absolute()
for f in pth.iterdir():
    path1 / f
    zpath = str(path1)+"\\"+ str(f)
    print(zpath)

