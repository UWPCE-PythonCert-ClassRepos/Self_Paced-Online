#!/usr/bin/env python3

import collections

infile = './sherlock_small.txt'
# infile = './sherlock.txt'
oneline = './oneline.txt'
struct = collections.defaultdict(list)


def create_oneline():
    with open(infile, 'r') as f:
        a = ' '.join(l.strip() for l in f)
        with open(oneline, 'w') as o:
            o.write(a)

def get_stuff(n, l):
    # if n > 8:
    if n > (len(l) - 3):
        # print('n over 8, exiting')
        print('n reached ', len(l) - 3, 'exiting')
        return
    else:
        # e = n + 3
        e = n + 2
        # part = l[n:e]
        k = l[n:e]
        v = l[e] 
        # print(part)
        # print(k, v)
        print(' '.join(k), v)
        get_stuff(n + 1, l)
)

def create_dict():
    with open(oneline, 'r') as ofile:
        wordlist = ofile.readline().split()
        # while wordlist: 
        # while wordlist[:]: 
        get_stuff(0, wordlist)
            # key = str(' '.join(wordlist[s:e]))
            # print(key)
            # struct[key].append(str(wordlist[n]))
            # # s += 1
            # wordlist.pop()
            # print('bla')
            # get_stuff(s + 1)
                
    print('ende create_dict')


def show_dict():
    for i, v in struct:
        print(i, v)
        print('ende show_dict') 

    # print(struct)

def main():
    create_oneline()
    create_dict()
    # show_dict()


if __name__ == '__main__':
    main()
