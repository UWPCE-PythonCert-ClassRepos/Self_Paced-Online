#Lesson 4 Activities
#Jason Virtue 02/06/2019
#UW Self Paced Python Course

import pathlib
pth = pathlib.Path('./')
for f in pth.iterdir():
    print(f)

#Write a program that copies files to another directory

def copy_file(old_file, new_file):
    with open(old_file, 'rb') as infile, open(new_file, 'wb') as outfile:
        while True:
            line = infile.read(1000)
            if not line:
                break
            outfile.write(line)

# testing this script
original_file = './lesson03/list_lab.py'
new_file = 'list_lab_copy2.py'
copy_file(old_file=original_file, new_file=new_file)