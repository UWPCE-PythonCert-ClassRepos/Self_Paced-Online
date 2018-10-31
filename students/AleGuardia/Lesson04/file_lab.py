#!/usr/bin/env python3

import os, io

# Write a program which prints the full path for all files in the current directory, one per line

for file in os.listdir():
    print(os.path.abspath(file))


def read_chunk(file_copy, chunk_size=1024):
    while True:
        chunk = file_copy.read(chunk_size)
        if not chunk:
            break
        yield chunk


def move_file(source, destination):
    with open(source, 'rb') as infile, open(destination, 'wb') as outfile:
        for piece in read_chunk(infile):
            outfile.write(piece)


