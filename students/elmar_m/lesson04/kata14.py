#!/usr/bin/env python3

infile = './sherlock_small.txt'
# infile = './sherlock.txt'

wordlist = [] 

with open(infile, 'r') as f:
    # lines = f.readlines()
    # lines = (l.strip('\n') for l in f)
    # print('\n', type(lines), '\n')

    # for i in lines:
    #     print(i)

    # for i in lines:
    #     wordlist.append(i.split())
    
    # wordlist.append(i.split())

    # lines = f.readlines()
    # lines = f.readline()
    # for i in lines:
    #     i.strip('\n')
    #     print(i, end='')

    # for l in f:
    #    line = f.readline()
    #    # line.strip('\n')
    #    line.strip()
    #    print(line, end='')
    
    print(' '.join(l.strip() for l in f))
    # print(''.join(l.replace('\n', ' ') for l in f))
    

    

# for w in wordlist:
#     print(w)

#print('\n', type(lines), '\n')
#print(lines)
#print('\nnumber of elements:', len(lines), '\n')
#
#wordlist = [] 
#
#for i in lines:
#    print('--- beginning ---')
#    # wordlist = i.split()
#    wordlist.append(i.split())
#    print('--- end ---')
#
#for w in wordlist:
#    print(w)
#
    

# line = f.readline()
# print('\n', type(line), '\n')
# print(line)
# print('\nnumber of elements:', len(line), '\n')
# 
# wordlist = line.split()
# for i in wordlist:
#     print(i)
