#!/usr/bin/env python3
import pathlib

# Print full path for all files in cwd
pth = pathlib.Path.cwd()
for index, f in enumerate(pth.iterdir()):
    print(f'File {index + 1}: ', f)

# Copy files from a source to a destination
source_file = 'file_to_move.txt'
destination = pathlib.Path.home()
outfile = open(destination / 'output.txt', 'w')

for line in open(source_file):
    outfile.write(line)
outfile.close()
