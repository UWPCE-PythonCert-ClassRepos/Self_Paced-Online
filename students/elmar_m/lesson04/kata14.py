#!/usr/bin/env python3

import collections

# infile = './sherlock_small.txt'
# infile = './sherlock.txt'
infile = './pg1661.txt'
oneline = './oneline.txt'
the_dict = collections.defaultdict(list)


def create_oneline(f):
    with open(f, 'r') as myfile:
        a = ' '.join(l.strip() for l in myfile)
        with open(oneline, 'w') as o:
            o.write(a)


def create_biglist():
    with open(oneline, 'r') as ofile:
        biglist = ofile.readline().split()
        # get_stuff(0, biglist)
    # get_stuff(0, biglist)

    for i in get_stuff_generator(0, biglist):
        print(i)


# def get_stuff(n, l):
#     if n > (len(l) - 3):
#         print('n reached ', len(l) - 3, ', exiting')
#         return
#     else:
#         e = n + 2
#         k = l[n:e]
#         y = l[e] 
#         x = ' '.join(k)
#         print('|=', x, '=|', y)
#         create_dict(x, y)
#         # return(x, y)
#         get_stuff(n + 1, l)     # start recursion / do it again...

def get_stuff_generator(n, l):
    while n >= 0:
        e = n + 2
        k = l[n:e]
        y = l[e] 
        x = ' '.join(k)
        # print('|=', x, '=|', y)
        yield x
        n += 1

# for i in get_stuff_generator(0, biglist):
#     print(i)

def create_dict(k, v):
        # the_dict[k].append(str(the_dict[v]))    # put key and value in dictionary
        the_dict[k].append(str(v))    # put key and value in dictionary


def show_dict():
    for i in the_dict:
        print('key:', i, 'value:', the_dict[i])
    print('ende show_dict') 


def main():
    create_oneline(infile)
    create_biglist()
    # get_stuff()
    # create_dict()
    show_dict()

if __name__ == '__main__':
    main()
