#File Lab
import os


# Write a program which prints the full path for all files in the current directory, one per line
cwd = os.getcwd()
file_list = os.listdir(cwd)
print(file_list)
for f in file_list:
    print(os.path.abspath(f))


# Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command).
def copy_file(source_file, dest_file):
    with open(source_file) as file:
        text = file.read()
    with open(dest_file, "w") as copy:
        copy.write(text)

# copy_file('text.txt', 'dest.txt')




# Advanced: make it work for any size file: i.e. don’t read the entire contents of the file into memory at once.

# This should work for any kind of file, so you need to open the files in binary mode: open(filename, 'rb') (or 'wb' for writing). Note that for binary files, you can’t use readline() – lines don’t have any meaning for binary files.
def copy_file_advanced(source_file, dest_file):
    with open(source_file, "rb") as file, open(dest_file, "ab") as copy:
        for line in file:
            copy.write(line)


# Test it with both text and binary files (maybe jpeg or something of your chosing).
copy_file_advanced('text_long.txt', 'text_long_copy.txt')
copy_file_advanced('binary.jpg', 'dest.txt')