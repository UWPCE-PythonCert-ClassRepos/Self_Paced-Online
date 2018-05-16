#!/usr/bin/env python3

"""
Activity 1: Dictionary and Set Lab
Goal:
Learn the basic ins and outs of Python dictionaries and sets.

Procedure
In your student dir in the class repo, create a lesson04 dir and put in a new dict_lab.py file.

The file should be an executable Python script. That is to say that one should be able to run the script directly like so:

$ ./dict_lab.py
(at least on OS-X and Linux).

– you do that with this command:

$ chmod +x dict_lab.py
(The +x means make this executable)

Add the file to your clone of the repository and commit changes frequently while working on the following tasks. When you are done, push your changes to GitHub and issue a pull request.

(if you are struggling with git – just write the code for now)

When the script is run, it should accomplish the following four series of actions:

Dictionaries 1
Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
Display the dictionary.
Delete the entry for “cake”.
Display the dictionary.
Add an entry for “fruit” with “Mango” and display the dictionary.
Display the dictionary keys.
Display the dictionary values.
Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
Display whether or not “Mango” is a value in the dictionary (i.e. True).
Dictionaries 2
Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value as the value (consider upper and lower case?).
Sets 1
Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.
Display the sets.
Display if s3 is a subset of s2 (False)
and if s4 is a subset of s2 (True).
Sets 2
Create a set with the letters in ‘Python’ and add ‘i’ to the set.
Create a frozenset with the letters in ‘marathon’.
display the union and intersection of the two sets.
Activity 2: File Lab
Goal:
Get a little bit of practice with handling files and parsing simple text.

Paths and File Processing
Write a program which prints the full path for all files in the current directory, one per line
Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command).
Advanced: make it work for any size file: i.e. don’t read the entire contents of the file into memory at once.
This should work for any kind of file, so you need to open the files in binary mode: open(filename, 'rb') (or 'wb' for writing). Note that for binary files, you can’t use readline() – lines don’t have any meaning for binary files.
Test it with both text and binary files (maybe jpeg or something of your chosing).

"""
