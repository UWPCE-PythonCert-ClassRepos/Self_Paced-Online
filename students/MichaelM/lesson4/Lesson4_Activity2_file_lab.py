# in filesystem copy Lesson4_Activity2_file_lab.py into new folder:
#        C:\Users\v-micmcd.Redmond\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson4
# wk: cd C:\Users\v-micmcd.Redmond\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson4
# mo: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson4
# hm: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson4
# git status
# git add Lesson4_Activity2_file_lab.py
# git commit Lesson4_Activity2_file_lab.py
# git push
# goto https://github.com/geekwriter2/Self_Paced-Online/tree/master/students/MichaelM/lesson4/
# click Pull request > new pull request
# go back to assignment webpage and fill in submission comments

import os
import sys
import pathlib
from pathlib import Path


def cleanup(directory, source_file, dest_file):
    """
    cleanup filesystem activities for next run

    {Extended description}

    Parameters:
    directory: string
    source_file: string
    dest_file: string

    Returns:
    {none}

    """
    try:
        os.remove(source_file)
    except:
        pass
    try:
        os.rmdir(directory)
    except:
        pass

    try:
        os.remove(dest_file)
    except:
        pass
    
    """"""



if __name__ == "__main__":
    pth = pathlib.Path('./')
    tmp_directory = "{}/tmp/".format(os.getcwd())
    tmp_source_file = "{}/MySourceFile.txt".format(tmp_directory)
    tmp_dest_file = "{}/MyDestinationFile.txt".format(pth)
    cleanup(tmp_directory, tmp_source_file, tmp_dest_file)
    print("Each file the current directory:")
    for file in pth.iterdir():
        print("{0}\\{1}".format(pth.absolute(),file))
    os.mkdir(tmp_directory)
    Path(tmp_source_file).touch()
    os.popen(f"copy {tmp_source_file} {tmp_dest_file}")
    print(f"New file created at: {tmp_dest_file}")

"""

Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command).
Advanced: make it work for any size file: i.e. don’t read the entire contents of the file into memory at once.
This should work for any kind of file, so you need to open the files in binary mode: open(filename, 'rb') 
(or 'wb' for writing). Note that for binary files, you can’t use readline() – lines don’t have any meaning for binary files.
Test it with both text and binary files (maybe jpeg or something of your choosing).



 

"""
