# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 13:51:19 2019
@author: Florentin Popescu
"""

#===================LESSON_03====================
# String formatting lab exercise-----------------
#================================================
#================================================
# TASK 1
#================================================
string_file = (2, 123.4567, 10000, 12345.67)

#using magic methods
for idx, name in enumerate(string_file):
    if idx == 0 and type(name) == int:  paded_name = "".join(["file_", "%03d" % name, ":"])
    if idx == 1 and type(name) == float and str(name)[::-1].find('.') >2:
        rounded_float = "%.2f" % round(name, 2)
    if idx == 2: scintific_int =  '%.2e' % name
    if idx == 3: scintific_float =  '%.2e' % name

string_formated = ", ".join(["".join([paded_name, "  ", rounded_float]), scintific_int, scintific_float])
print("This is the formated string:\n '{}'".format(string_formated))

#================================================
# TASK 2
#================================================
#Option1 - using format()
for idx, name in enumerate(string_file):
    if idx == 0 and type(name) == int:  paded_name = ''.join(["file_", "{0:03d}".format(name), ":"])
    if idx == 1 and type(name) == float and str(name)[::-1].find('.') >2:
        rounded_float = "{0:.2f}".format(round(name, 2))
    if idx == 2: scintific_int = '{:.2e}'.format(name) #in Python 3
    if idx == 3: scintific_float = '{:.2e}'.format(name) #in Python 3

string_formated = ", ".join(["".join([paded_name, "  ", rounded_float]), scintific_int, scintific_float])
print("This is the formated string:\n '{}'".format(string_formated))

#Option2 - using f-strings
for idx, name in enumerate(string_file):
    if idx == 0 and type(name) == int:  paded_name = f"file_{0:02d}{name}:"
    if idx == 1 and type(name) == float and str(name)[::-1].find('.') >2:
        rounded_float = f"{round(name, 2):.2f}"
    if idx == 2: scintific_int = f"{name:.2e}"
    if idx == 3: scintific_float = f"{name:.2e}"

string_formated = ", ".join(["".join([paded_name, "  ", rounded_float]), scintific_int, scintific_float])
print("This is the formated string:\n '{}'".format(string_formated))

#================================================
# TASK 3
#================================================
def formatter(item):
    #gardian - all elements in the tuple are integers
    if type(item) == tuple and all(type(x) is int for x in item):
        print("Tuple of integers given: ".format(item))
        return " ".join(["the", str(len(item)), "numbers are:", 
                             '{:d}, '*len(item)])[:-2].format(*item)
    #gardian - all elements in the tuple are floats
    elif type(item) == tuple and all(type(x) is float for x in item):
        print("Tuple of floats given: ".format(item))
        return " ".join(["the", str(len(item)), "numbers are:", 
                             '{:.2f}, '*len(item)])[:-2].format(*item)
    #gardian - all elements in the tuple are strings        
    elif type(item) == tuple and all(type(x) is str for x in item):
        print("Tuple of strings given: ".format(item))
        return " ".join(["the", str(len(item)), "words are:", 
                             '{:s}, '*len(item)])[:-2].format(*item)
    #gardian - some elements in the tuple are numbers and some are strings
    elif type(item) == tuple:
        print("Tuple of numbers and strings given")
        return " ".join(["the", str(len(tuple([str(item) for item in item]))), "elements are:",'{:s}, '*len(tuple([str(item) for item in item]))])[:-2].format(*tuple([str(item) for item in item]))
    
#tests
#passing empty tuple    
formatter(((),))    
#Out:>>> 'the 1 elements are: ()'

#passing tuple of integers    
formatter((2, 3, 5))    
#Out:>>> 'the 3 numbers are: 2, 3, 5'

#passing a larger tuple of integers
formatter((2, 3, 5, 7, 9))    
#Out:>>> 'the 5 numbers are: 2, 3, 5, 7, 9'

#additional tests
#passing a tuple of floats
formatter((2.1, 3.2, 5.3, 7.4, 9.5))    
#Out:>>> 'the 5 numbers are: 2.100000, 3.200000, 5.300000, 7.400000, 9.500000'

#passing a tuple with int and floats
formatter((2.1, 3.2, 5.3, 7.4, 9))    
#Out:>>> 'the 5 elements are: 2.1, 3.2, 5.3, 7.4, 9'

#passing a tuple of strings
formatter(('this', 'is', 'a', 'string'))
#Out:>>> 'the 4 words are: this, is, a, string'
    
#passing a tuple of strings, floats and integers
formatter(('this', 'is', 'string', 1, 'and', 'this', 'is', 'string', 2.0))
#Out:>>> 'the 9 elements are: this, is, string, 1, and, this, is, string, 2.0'
    
#================================================
# TASK 4
#================================================
t = (4, 30, 2017, 2, 27) 
print(" ".join(['0{}'.format(*[t[3]]), 
                '{}'.format(*[t[4]]), 
                '{}'.format(*[t[2]]), 
                '0{}'.format(*[t[0]]),
                '{}'.format(*[t[1]])]))
#Out:>>> '02 27 2017 04 30'

#================================================
# TASK 5
#================================================
list_fruits = ['oranges', 1.3, 'lemons', 1.1]   

weights_fruits = f"The weight of an orange is {list_fruits[1]} and the weight of a lemon is {list_fruits[3]}"
print(weights_fruits)    
#Out:>>> 'The weight of an orange is 1.3 and the weight of a lemon is 1.1'   

weights_fruits_upper_20percent = f"The weight of an {list_fruits[0][:-1].upper()} is {list_fruits[1]} and the weight of a {list_fruits[2][:-1].upper()} is {1.2*list_fruits[3]}"
print(weights_fruits_upper_20percent)
#Out:>>> 'The weight of an ORANGE is 1.3 and the weight of a LEMON is 1.32'
  
#================================================
# TASK 6
#================================================
#Option1
#generate a formated table    
for i in range(15):
    max_len, dec_prec  = 10, 2
    print("Name_{:0{len_i}d} {:>{max_len}.{dec_prec}f} {:>{max_len}.{dec_prec}f}".format(i, 10.01*(i+1), 100.01*((i)), len_i = 2 if len(str(i)) == 1 else 1, max_len = max_len, dec_prec = dec_prec))
    
#Option2
table = [['Name_00', 10.01, 0.00],
         ['Name_01', 20.02, 100.01],
         ['Name_02', 30.03, 200.02],
         ['Name_03', 40.04, 300.03],
         ['Name_04', 50.05, 400.04],
         ['Name_05', 60.06, 500.05],
         ['Name_06', 70.07, 600.06],
         ['Name_07', 80.08, 700.07],
         ['Name_08', 90.09, 800.08],
         ['Name_09', 100.10, 900.90],
         ['Name_10', 110.11, 1000.10],
         ['Name_11', 120.12, 1100.11],
         ['Name_12', 130.13, 1200.12],
         ['Name_13', 140.14, 1300.13],
         ['Name_14', 150.15, 1400.14]]

max_len = max(len(table[-1][0]), len(str(table[-1][1])), len(str(table[-1][2])))
dec_prec = len(str(table[-1][1]).split(".")[1])
for item in table:
    org_table = "{:>{max_len}s} {:>{max_len}.{dec_prec}f} {:>{max_len}.{dec_prec}f}".format(item[0], item[1], item[2], max_len = max_len, dec_prec = dec_prec)
    print(org_table)
    
#Option3 - using Pandas's DataFrame() on table from Option2
import pandas as pd    
org_table = pd.DataFrame(table, columns = ['Name', 'Age', 'Cost'])    
print(org_table)

#================================================
# EXTRA TASK
#================================================
tuple_10 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

#Option1 - using format()
for i in range(len(tuple_10)): print("{0:05d}".format(tuple_10[i]))

#Option2 - using f-stings
for i in range(len(tuple_10)): print(f"{tuple_10[i]:05}")

#================================================
# END
#================================================
