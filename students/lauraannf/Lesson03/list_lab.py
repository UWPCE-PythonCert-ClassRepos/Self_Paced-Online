#!/usr/bin/env python3
"""
Created on Sun Sep  9 19:00:58 2018

@author: Laura.Fiorentino
"""
#Series 1
# =============================================================================
# print('------Series 1------')
# FruitList=['Apples', 'Pears', 'Oranges', 'Peaches']
# for it in range(len(FruitList)):
#     print(FruitList[it])
# newfruit = input("Name another fruit > ")
# FruitList=FruitList + [newfruit]
# for it in range(len(FruitList)):
#     print(FruitList[it])
# fruitnumber=input("Pick a number between 1 and 5 > ")
# print(FruitList[int(fruitnumber) - 1])
# newfruit = input("Name another fruit > ")
# FruitList.insert(0, newfruit)
# for it in range(len(FruitList)):
#     print(FruitList[it])
# newfruit = input("Name another fruit > ")
# FruitList=[newfruit] + FruitList
# for it in range(len(FruitList)):
#     print(FruitList[it])
# print()
# print('Fruits that start with P:')
# for it in range(len(FruitList)):
#     if FruitList[it][0] == 'P':
#         print(FruitList[it])
# for it in range(3):
#     print()
#     
# #Series 2    
# print('------Series 2------')
# FruitList=['Apples', 'Pears', 'Oranges', 'Peaches']
# for it in range(len(FruitList)):
#     print(FruitList[it])
# print()
# print('Remove last fruit')
# del FruitList[-1]
# for it in range(len(FruitList)):
#     print(FruitList[it])
# badfruit = input("Name fruit to get rid of > ")
# FruitList.remove(badfruit)
# for it in range(len(FruitList)):
#     print(FruitList[it])
# FruitList=FruitList*2
# print()
# print('Double the fruit')
# for it in range(len(FruitList)):
#     print(FruitList[it])
# badfruit = input("Name another fruit to get rid of > ")
# while badfruit in FruitList:
#     FruitList.remove(badfruit)
# for it in range(len(FruitList)):
#     print(FruitList[it])
# for it in range(3):
#     print()
# 
# =============================================================================
# Series 3
# =============================================================================
# print('------Series 3------')
# FruitList=['Apples', 'Pears', 'Oranges', 'Peaches']
# NewFruits=FruitList[:]
# for fruit in FruitList:
#     yesorno = input("Do you like {} ?>".format(fruit.lower()))
#     while yesorno !='yes' and yesorno!='no':
#         yesorno = input('Please answer yes or no>')
#     if yesorno == 'yes':
#         print('Ok, keeping {}'.format(fruit.lower()))
#     elif yesorno == 'no':
#         print('Ok, removing {}'.format(fruit.lower()))
#         NewFruits.remove(fruit)
# print()
# print('Ok, here''s your fruit')
# for it in range(len(NewFruits)):
#     print(NewFruits[it])
# =============================================================================
    

# Series 4
print('------Series 4------')
FruitList=['Apples', 'Pears', 'Oranges', 'Peaches']
