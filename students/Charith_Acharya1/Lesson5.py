# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 16:39:28 2019

@author: acharch
"""

import os
path = 'C:/U of W/Session 5'
os.chdir(path)
from except_test import fun, more_fun, last_fun
first_try = ['spam', 'cheese', 'mr death']
try:
    joke = fun(first_try[0])
except NameError:
    joke = fun(first_try[1])
    print()
try:
    not_joke = fun(first_try[2])
except SyntaxError:
    print('Run Away!')
else:
    print(not_joke)
langs = ['java', 'c', 'python']
try:
    more_joke = more_fun(langs[0])
except IndexError:
    more_joke = more_fun(langs[1])
    last_fun()
    
    
#MailRoom Part 3

import os
os.chdir("C:/U of W")
os.getcwd()

import sys

Master_List = {"Bill Gates":[1000,2000,3000,4000,5000],
               "Marc Zuckerberg":[1005,2005,3005,4005,5005],
               "Jeff Bezos": [9000,12000],
               "Warren Buffet": [1100,2200,3300,4000,5000],
               "Tim Cook": [100000,300000,400000,500000],
               "Sundar Pichai":[1000],
               "Satya Nadella":[1900,45672,983564,7646,5000,1,2,3],
               "Charith Acharya":[10,80,24,621]}

prompt = "\n".join(('Welcome',
        'Please select from the following options',
        '1.Send A Thank You!',
        '2.Create a report',
        '3.Send a letter to all participants',
        '4. Quit'))


def main():
    while True:
        try:
            response = int(input(prompt))
            if response not in (1,2,3,4):
                raise ValueError
                break
        except ValueError:
            print("Response has to be 1,2,3,or 4. Try again!")
            continue
        SwitchFuncDict = {1:Thanks,2:Report,3:Letter_to_all,4:Quit}
        SwitchFuncDict.get(response)()


def Thanks():
    Full_Name = input("Please enter the full name".title())
    while True:
        try:
            New_Amount = int(input("Please enter new amount"))
            break
        except ValueError:
            print("Amount has to be a number")
            continue
    if Full_Name in Master_List.keys():
        Master_List[Full_Name].append(New_Amount)
        print(" ".join(["Hello",Full_Name,"Thank you for the donation of",str(New_Amount)]))
    if Full_Name not in Master_List.keys():
        Master_List[Full_Name] = [New_Amount]
        print(" ".join(["Hello",Full_Name,"Thank you for the donation of",str(New_Amount)])) 
        

def Report():
    Sum_List = []
    Len_List = []
    Avg_List = []
    for i in Master_List.keys():
        Sum = sum(Master_List[i])
        Len = len(Master_List[i])
        Average = Sum/Len
        Sum_List.append(Sum)
        Len_List.append(Len)
        Avg_List.append(Average)            
    print(Sum_List)
    print(Len_List)
    print(Avg_List)  
    for i in range(len(list(Master_List.keys()))):
        print(list(Master_List.keys())[i] + "-"*5 + str(Sum_List[i]) + "-"*5 + str(Len_List[i]) +"-"*5 + str(Avg_List[i]))


def Reportcomprehension():
    Sum_List = [sum(Master_List[i]) for i in Master_List.keys()]
    Len_List = [len(Master_List[i]) for i in Master_List.keys()]
    Avg_List = [sum(Master_List[i]) / len(Master_List[i]) for i in Master_List.keys()]         
    for i in range(len(list(Master_List.keys()))):
        print(list(Master_List.keys())[i] + "-"*5 + str(Sum_List[i]) + "-"*5 + str(Len_List[i]) +"-"*5 + str(Avg_List[i]))
    

def Letter_to_all():
    for i in range(len(Master_List)):
        with open('Letter{}.txt'.format(list(Master_List.keys())[i]),'w') as f:
            f.write("Hello")
            f.write(list(Master_List.keys())[i])
            f.write("Thank you for your donation of")
            f.write(str(sum(list(Master_List.values())[i])))
    
def Quit():
    print("Bye!")
    sys.exit()

        
if __name__ == "__main__":
    main()
   