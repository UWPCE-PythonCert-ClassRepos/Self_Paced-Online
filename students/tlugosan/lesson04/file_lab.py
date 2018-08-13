"""Handling files and parsing exercises"""
import pathlib
import os


def print_path_all_files():
    """Prints each files from the current directory"""
    for p in pathlib.Path.cwd().iterdir():
        print(p)


def copy_file():
    """Copies a file from the current directory to its parent"""
    source_file = r'C:\Users\tlugo\Desktop\PythonUW\Class210\Self_Paced-Online\students\tlugosan\lesson04\original_file.txt'
    target_directory = r'C:\Users\tlugo\Desktop\PythonUW\Class210\Self_Paced-Online\students\tlugosan'

    source_file_path = pathlib.Path(source_file)
    file_name = source_file_path.name

    target_file_path = os.path.join(target_directory, file_name)

    with open(source_file, 'r') as sf, open(str(target_file_path), 'w')as tf:
        tf.write(sf.read())


def copy_byte_file(file_name):
    """Copies any file in binary mode from the current directory to its parent directory"""
    source_file = r'C:\Users\tlugo\Desktop\PythonUW\Class210\Self_Paced-Online\students\tlugosan\lesson04'
    target_directory = r'C:\Users\tlugo\Desktop\PythonUW\Class210\Self_Paced-Online\students\tlugosan'

    source_file_path = os.path.join(source_file, file_name)

    target_file_path = os.path.join(target_directory, file_name)

    with open(str(source_file_path), 'rb') as sbf, open(str(target_file_path), 'wb')as tbf:
        while True:
            byte = sbf.read(1)
            if not byte:
                break
            tbf.write(byte)


if __name__ == '__main__':
    # print_path_all_files()
    print()
    # copy_file()
    # copy_byte_file('books_picture.jpg')
    # copy_byte_file('original_byte_file.txt')
