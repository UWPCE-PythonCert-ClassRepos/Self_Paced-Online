# python 3

# file_lab.py


# https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Files.html#files

# Get a little bit of practice with handling files and parsing simple text.
# Paths and File Processing
# Write a program which prints the full path for all files in the current
# directory, one per line
# Write a program which copies a file from a source, to a destination
# (without using shutil, or the OS copy command).
# Advanced: make it work for any size file: i.e. don’t read the entire
# contents of the file into memory at once.
# This should work for any kind of file, so you need to open the files in
# binary mode: open(filename, 'rb') (or 'wb' for writing). Note that for binary
# binary files, you can’t use readline() – lines don’t have any meaning.
# Test with both text and binary files, maybe jpeg, something of your chosing.


import os


def full_file_path():

    # directories in pwd:
    directories = os.listdir()
    # print("\n", directories, "\n")

    # print full path for each directory in the current directory:
    for directory in directories:
        absp = os.path.abspath(directory)
        print("\n", absp)
        # basen = os.path.basename(absp)
        # print("basen: ", basen)
        # dirn = os.path.dirname(absp)
        # print("dirn: ", dirn)
        folder_path, file = os.path.split(absp)
        print("folder_path: {},   file: {}".format(folder_path, file))
    cwdir = os.getcwd()
    print("cwdir: ", cwdir)


def copy_file_from(source, to_destination=None):
    """
    windows ==> path entered with prefix r, raw string, alt. duplicate all \
                works as long as the path doesn't end with \.
    source: abspath
    to_destination: abspath
    # file: name of file to be copied
    """
    if to_destination is None:
        to_destination = os.path.join(os.getcwd(), "bin_text_2.bin")

    with open(source, 'rb') as infile, open(to_destination, 'wb') as outfile:
        outfile.write(infile.read())

    print("bin_data stored at: ", to_destination)


def copy_txt_file_from(source):
    """
    copies .txt file from source, can be in any directory, reads it as 'r'
        encodes to binary, writes it as 'wb' to 'bin_text.bin' in cwd

    windows ==> path entered with prefix r, raw string, alt. duplicate all \
                works as long as the path doesn't end with \.
    source:         abspath, any directory
    to_destination: abspath in cwd
    """

    to_destination = os.path.join(os.getcwd(), "bin_text.bin")
    with open(source, 'r') as infile, open(to_destination, 'wb') as outfile:
        # outfile.write(infile.read())  # open(source, 'rb')
        for line in infile:
            # print(line, '\n in line: ', '\n' in line)
            line = line.replace("\n", "/")
            bin_line = line.encode('utf-8')
            # bin_line = bytearray()
            # bin_line.extend(map(ord, line))
            outfile.write(bin_line)
    print("data stored at: ", to_destination)
    return to_destination


if __name__ == '__main__':

    # if text_file.txt not in cwd, set fpath to the abspath
    # where text_file.txt is located
    fpath = os.getcwd()
    # text_file.txt file in cwd, with name, total amount and number of times
    # donating, '/' delimited, not binary
    infile = "text_file.txt"
    source = fpath + "\\" + infile

    full_file_path()
    print("\n"*3)

    # creates new file in cwd, 'bin_text.bin', stores text in binary format
    new_source = copy_txt_file_from(source)

    # copy new binary file from source to_destination in cwd
    copy_file_from(new_source)
