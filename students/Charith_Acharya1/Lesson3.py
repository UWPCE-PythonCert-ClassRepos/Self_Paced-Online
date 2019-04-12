# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 14:14:25 2019

@author: acharch
"""

        
###Lesson 3        
##Slicing Lab Excercise

#First and last items exchanged
def first_last_exchange(seq):
    first = seq[0]
    middle = seq[1:len(seq)-1]
    last = seq[-1]
    result  = (last,middle,first)
    print(result)

#Every other item removed
def first_last_only(seq):
    first = seq[0]
    middle = seq[1:len(seq)-1]
    last = seq[-1]
    result  = (first,last)
    print(result)

#First four and last four items removed and then every other item inbetween
def four(seq):
    f = seq[0:3]
    l = seq[-1:-4]
    newseq = seq[4:len(seq)-4]
    finalseq = ""
    for i in range(len(newseq)):
        if i%2==0:
            finalseq = finalseq+ newseq[i]
    print(finalseq)

#With the elements reversed
def reverse(seq):
    negseq = seq[::-1]
    print(negseq)


##List Lab Excercise
#Series 1
Fruits=['Apples','Pears','Oranges','Peaches']
print(Fruits)
Another_Fruit = input("Enter another fruit")
Fruits.append(Another_Fruit)
print(Fruits)
Serial_Number = input("Enter the serial number for the fruit")
print (Fruits[int(Serial_Number)])
Fruits = ["Banana"]+Fruits
print(Fruits)
Fruits.insert(0,"Kiwi")
print(Fruits)
for i in range(len(Fruits)):
    if Fruits[i][0] == 'P':
        print(Fruits[i])

#Series 2
print(Fruits)
Fruits.pop()
print(Fruits)
Deletefruit = input("Enter the name of the fruit you want to delete")
Fruits.remove(Deletefruit)
print(Fruits)



#Series 3
Fruits=['Apples','Pears','Oranges','Peaches']
Duplicate = Fruits.copy()
for i in range(len(Fruits[:])):
    answer = ""
    answer2  =""
    print( " ".join(["Do you like", Fruits[i]]))
    answer = input("Type your answer here")
    if answer == 'no':
        Duplicate.remove(Fruits[i])
        continue
    elif answer == 'yes':
        continue
    else:
        flag=True
        while flag:
            print("Enter yes or no only")
            answer2 = input("Try again")
            if answer2 == 'no':
                Duplicate.remove(Fruits[i])
                flag = False
                continue
            elif answer2 == 'yes':
                flag = False
                continue
if Fruits == Duplicate:
    print(Fruits)
else:
    print(Duplicate)
    

#Series4
#String Formating Lab Execise
#Task1
"file_{:0>3d}: {:.2f} {:.2e} {:.2e}".format(2, 123.4567, 10000, 12345.67)

#Task2

#Task3

#Task 4
Task4 = (4, 30, 2017, 2, 27)
"{3:0>2d} {4:d} {2:d} {0:0>2d} {1:d}".format(4, 30, 2017, 2, 27)


#Task5
Wght = ['Orange', 1.3, 'Lemon', 1.1]
f'The weight of an {Wght[0]} is {Wght[1]} and the weight of a {Wght[2]} is {Wght[3]}'


f'The weight of an {Wght[0].upper()} is {Wght[1]*1.20} and the weight of a {Wght[2].upper()} is {Wght[3]*1.20}'




