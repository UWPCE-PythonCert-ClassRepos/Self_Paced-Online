#!/usr/bin/env python3
import os


def print_local_dir():
    """Print the full path of all files in the current directory."""
    for path in os.listdir():
        print(os.path.abspath(path))


def file_copy(src_path, dst_path):
    """Copy file from src_path to dst_path

    Args:
        src_path (str): path to source file
        dst_path (str): path to copy destination
    """
    chunk_size = 100
    dst_path = os.path.join(dst_path, os.path.basename(src_path))

    with open(src_path, 'rb') as src_f:
        with open(dst_path, 'wb') as dst_f:
            while True:
                src = src_f.read(chunk_size)
                if not src:
                    break
                dst_f.write(src)


if __name__ == '__main__':
    print_local_dir()
    file_copy('../lesson03/list_lab.py', '/Users/dustinlane/Desktop')
