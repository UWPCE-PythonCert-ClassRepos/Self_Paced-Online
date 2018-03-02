#!/usr/bin/env python3

infile = './sherlock_small.txt'

f = open(infile, 'r')

lines = f.readlines()
print('\n', type(lines), '\n')
print(lines)
print('\nnumber of elements:', len(lines), '\n')

wordlist = [] 

for i in lines:
    print('--- beginning ---')
    # wordlist = i.split()
    wordlist.append(i.split())
    print('--- end ---')

for w in wordlist:
    print(w)

    

# line = f.readline()
# print('\n', type(line), '\n')
# print(line)
# print('\nnumber of elements:', len(line), '\n')
# 
# wordlist = line.split()
# for i in wordlist:
#     print(i)
