# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 11:50:46 2019

@author: acharch
"""

#Grid Printer Excercise
#Part 1
print('+'+'-'*5+'+'+'-'*5+'+')
print('|'+' '*5+'|'+' '*5+'|')
print('|'+' '*5+'|'+' '*5+'|')
print('|'+' '*5+'|'+' '*5+'|')
print('|'+' '*5+'|'+' '*5+'|')
print('|'+' '*5+'|'+' '*5+'|')
print('+'+'-'*5+'+'+'-'*5+'+')
print('|'+' '*5+'|'+' '*5+'|')
print('|'+' '*5+'|'+' '*5+'|')
print('|'+' '*5+'|'+' '*5+'|')
print('|'+' '*5+'|'+' '*5+'|')
print('|'+' '*5+'|'+' '*5+'|')
print('+'+'-'*5+'+'+'-'*5+'+')

#Part 2
def fun(p):
    q = round(p/2)
    if p == 0:
        print()
    else:
        print('+' + '-'*q + '+' + '-'*q + '+')
        for i in range(q):
            print('|' + ' '*q + '|' + ' '*q + '|')
        print('+' + '-'*q + '+' + '-'*q + '+')
        for i in range(q):
            print('|' + ' '*q + '|' + ' '*q + '|')                    
        print('+' + '-'*q + '+' + '-'*q + '+')
        
#Part 3
def fun(p,q):
    if p == 0 or q==0:
        print()
    else:
        for i in range(p):
            print(('+' + '-'*q)*p + "+")
            for i in range(q):
                print(('|' + ' '*q)*p + '|') 
        print(('+' + '-'*q)*p + "+")
        
#Fizzbuzz
def buzz(n):
    for i in range(n):
        if i ==0:
            continue
        elif i%3 == 0 and i%5 == 0:
            print ("FizzBuzz") 
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print ("Buzz")
        else:
            print (i)
            
#Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
    
    
    
#Lucas
def luc(n):
    if n==0:
        return 2
    if n==1:
        return 1
    else:
        return (luc(n-1) + luc(n-2))
    

#Generalizing Fibonacci and Lucas
def luc(n,f,s):
    if f==0 and s==1:
        if n==0:
            return 0
        if n==1:
            return 1
        else:
            return (luc(n-1,f,s) + luc(n-2,f,s))
    elif f==2 and s==1:
        if n==0:
            return 2
        if n==1:
            return 1
        else:
            return (luc(n-1,f,s) + luc(n-2,f,s))
    else:
         return (luc(n-1,f,s) + luc(n-2,f,s))
