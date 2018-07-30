#!/usr/bin/env python3

import os

cwd = os.getcwd()

for dir in os.listdir():
    print(cwd + dir)

src = input("Enter file to copy: ")
dst = input("Enter copy location: ")

with open(src, 'rb') as in_file, open(dst, 'wb') as out_file:
    while(in_file):
        line = in_file.read(4096)
        if not line:
            break
        out_file.write(line)