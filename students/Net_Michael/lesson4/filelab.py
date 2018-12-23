#!/usr/bin/env python
# coding: utf-8

# In[1]:

import os
import io
import pathlib
import shutil

#Write a program which prints the full path for all files in the current 
#directory, one per line

[os.path.join(os.getcwd(),file) for file in os.listdir()]

# copy file 
source = os.getcwd()
destn = os.path.split(os.getcwd())[0]
srcname = os.path.join( source, 'testfile.txt')
dstname = os.path.join( destn, 'session04\\testfile1.txt')
shutil.copyfile(srcname, dstname)


src_students = os.path.join(destn,'session04\\students.txt')
students = open(src_students)
prgr_lang = set()
nick_names = set()

for line in students:
    line_a = "".join(line.split()).split(":")
    names_langs = dict(zip( ['Name', 'Language'], line_a))
    nickname_lang = list(names_langs.values())[1].split(",")
    prgr_lang = prgr_lang.union(nickname_lang[1:])
    nick_names = nick_names.union(nickname_lang[:1])   

print(prgr_lang)

nicknames = (nick_names.difference(prgr_lang))
print(nicknames)
