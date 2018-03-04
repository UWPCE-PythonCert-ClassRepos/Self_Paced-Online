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


def create_dict():
    with open(oneline, 'r') as ofile:
        wordlist = ofile.readline().split()
        wordlist.reverse() 
        # while wordlist: 
        while wordlist[:]: 
            
            s = 0
            e = s + 2
            n = s + 2
            # key = str(' '.join(wordlist[0:2]))
            key = str(' '.join(wordlist[s:e]))
            print(key)
            # struct[key] = str(wordlist[n])
            struct[key].append(str(wordlist[n]))
            s += 1
            wordlist.pop()


def show_dict():
    for i, v in struct:
        print(i, v)
        

    # print(struct)

def main():
    create_oneline()
    create_dict()
    show_dict()


if __name__ == '__main__':
    main()
