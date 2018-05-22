#!/usr/bin/env python3
## Ian Letourneau
## 5/2/2018
## A script to read through a text file and parse the necessary information

f = open('students.txt')
languages = set()
langTrack = []
lineCount = 1
for line in f:
    line = line.replace('\n','')
    line = line.replace(' ', '')
    if lineCount == 1:
        lineCount += 1
    else:
        halved = line.split(':')
        name = halved[0]
        second = halved[1].split(',')
        for item in second:
            if not item.istitle() and item:
                languages.update([item])
                langTrack.append(item)
langCount = {x:langTrack.count(x) for x in langTrack}
print (languages)
print("")
print (langCount)
