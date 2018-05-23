# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 16:04:54 2018

@author: Karl M. Snyder
"""

#DICTIONARIES 1

my_dict = dict(name='Chris', city='Seattle', cake='Chocolate')
print(my_dict)
my_dict.pop('cake')
print(my_dict)
my_dict['fruit'] = 'Mango'
print(my_dict.keys())
print(my_dict.values())
print('cake' in my_dict)
print('Mango' in my_dict.values())

#DICTIONARIES 2

my_dict = dict(name='Chris', city='Seattle', cake='Chocolate')
my_new_dict = {}
for k,v in my_dict.items():
    my_new_dict[k] = v.count('t'.lower())
print(my_new_dict)

#SETS 1

num = range(21)
s2 = {i for i in num if i % 2 == 0}
print(s2)
s3 = {i for i in num if i % 3 == 0}
print(s3)
s4 = {i for i in num if i % 4 == 0}
print(s4)

#SETS 2

my_set = set('Python')
my_set.add('i')
my_frozenset = frozenset('marathon')
print(my_set.union(my_frozenset))
print(my_set.intersection(my_frozenset))

#FILE LAB 1

import os
cwd = os.getcwd() #shows current working dir
def long_file_name(cur_dir):
    for file_name in os.listdir(cur_dir): #get file names in dir
        full_path = os.path.join(cur_dir, file_name) #concatenate dir and file
        if os.path.isfile(full_path):
            print(full_path)
        else:
            long_file_name(full_path) #recursive to sub-dir?
long_file_name(cwd)

#FILE LAB 2

with open('\\\\goflex_home\\GoFlex Home Personal\\UofW\\repo\\Self_Paced-Online\\students\\kmsnyde\\lesson04\\data_in.txt', 'w') as f:
    f.write(("This is my first write test\n")*10)
with open('\\\\goflex_home\\GoFlex Home Personal\\UofW\\repo\\Self_Paced-Online\\students\\kmsnyde\\lesson04\\data_copy.txt', 'w') as g:
    for line in open('\\\\goflex_home\\GoFlex Home Personal\\UofW\\repo\\Self_Paced-Online\\students\\kmsnyde\\lesson04\\data_in.txt').read():
        g.write(line)
