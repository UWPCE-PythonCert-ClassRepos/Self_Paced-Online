#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import io
import pathlib
import shutil


# In[3]:


#Write a program which prints the full path for all files in the current 
#directory, one per line


# In[2]:


[os.path.join(os.getcwd(),file) for file in os.listdir()]


# In[3]:


# copy file 
source = os.getcwd()
destn = os.path.split(os.getcwd())[0]
srcname = os.path.join( source, 'testfile.txt')
dstname = os.path.join( destn, 'session04\\testfile1.txt')
shutil.copyfile(srcname, dstname)


# In[4]:



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


# In[7]:


(prgr_lang)


# In[6]:


nicknames = (nick_names.difference(prgr_lang))

