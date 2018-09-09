#!/usr/bin/env python3
"""
Created on Sun Sep  9 19:00:58 2018

@author: Laura.Fiorentino
"""
FruitList=['Apples', 'Pears', 'Oranges', 'Peaches']
for it in range(len(FruitList)):
    print(FruitList[it])
newfruit = input("Name another fruit > ")
FruitList=FruitList + [newfruit]
for it in range(len(FruitList)):
    print(FruitList[it])
fruitnumber=input("Pick a number between 1 and 5 > ")
print(FruitList[int(fruitnumber) - 1])
newfruit = input("Name another fruit > ")
FruitList.insert(0, newfruit)
for it in range(len(FruitList)):
    print(FruitList[it])
newfruit = input("Name another fruit > ")
FruitList=[newfruit] + FruitList
for it in range(len(FruitList)):
    print(FruitList[it])
print()
print('Fruits that start with P:')
for it in range(len(FruitList)):
    if FruitList[it][0] == 'P':
        print(FruitList[it])
        
        