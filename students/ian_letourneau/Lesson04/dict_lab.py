#!/usr/bin/env python3
## Ian Letourneau
## 5/2/2018
## A script to utilize dictionarie, sets and their functions

myDict = {
    "name": "Chris",
    "city": "Seattle",
    "cake": "Chocolate"
    }

#Dictionaries 1
print (myDict)
del myDict["cake"]
print (myDict)
myDict["fruit"] = "Mango"
print (myDict)
print (myDict.keys())
print (myDict.values())
print ("cake" in myDict.keys())
print("Mango" in myDict.values())

#Dictionaries 2
newDict = {}
for key in myDict.keys():
    value = myDict[key]
    newValue = value.lower().count('t')
    newDict[key] = newValue
print (newDict)

#Sets 1
s2, s3, s4 = set(), set(), set()

for num in range(0,21):
    if num%2 == 0:
        s2.update([num])
    if num%3 == 0:
        s3.update([num])
    if num%4 == 0:
        s4.update([num])

print (s2, s3, s4)
print (s3.issubset(s2))
print (s4.issubset(s2))

#Sets 2
s = set(['P', 'y', 't', 'h', 'o', 'n'])
s.update(['i'])

fs = frozenset(('m', 'a', 'r', 'a', 't', 'h', 'o', 'n'))

print(s.union(fs))
print(s.intersection(fs))
