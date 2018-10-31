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
# files, you can’t use readline() – lines don’t have any meaning for binary files.
# Test it with both text and binary files (maybe jpeg or something of your chosing).


def full_file_path():

    import os
    # directories in pwd:
    directories = os.listdir()
    # print("\n", directories, "\n")

    # print full path for each directory in the current directory:
    for directory in directories:
        print("\n", os.path.abspath(directory))

# full_file_path()

def copy_file_from(source, to_destination):
    """
    windows ==> path entered with prefix r, raw string, alt. duplicate all \
                works as long as the path doesn't end with \.
    source: abspath
    to_destination: abspath
    # file: name of file to be copied
    """
    # source_file = source + "\" + file

    # with open(source, 'rb') as infile, open(dest, 'wb') as outfile:
    #     outfile.write(infile.read())
    with open(source, 'rb') as infile, open(to_destination, 'wb') as outfile:
        for line in infile:
            # outfile.write(infile.read())
            outfile.write(line)
