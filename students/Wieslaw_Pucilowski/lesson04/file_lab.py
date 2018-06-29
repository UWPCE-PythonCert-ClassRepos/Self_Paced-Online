#!/usr/bin/env python3
import os
__author__="Wieslaw Pucilowski"


# Write a program which prints the full path for all files in the current directory, one per line
def list_file_path():
    w_dir=os.getcwd()
    for f in os.listdir():
        print('{}\{}'.format(w_dir, f))
print('Files with absolut path:\n')
list_file_path()

# Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command). 
# f.seek(offset)   - intially starting from the begining, then 
# f.tell() # for binary files, mostly

size = os.path.getsize('images.jpg') # size in bytes
print('File size: {} MB and {} bytes'.format(size//1024, size % 1024))

# entire contents (file open in binary mode)
def copy_files(src, dest_path):
    dest=dest_path+'/'+os.path.basename(src)
    with open(src, 'rb') as infile, open(dest, 'wb') as outfile:
        outfile.write(infile.read())

# copy in parts for binary
# read(buffer) reads buffer of bytes, f.tell() - returns position in read file, f.seek - set start position for next read()
def copy_files_parts(src, dest_path):
    buffer=1024
    dest=dest_path+'/'+os.path.basename(src)
    with open(src, 'rb') as source, open(dest, 'wb') as out:
        while out.write(source.read(buffer)):
            source.seek(source.tell())
    out.close()
    source.close()


