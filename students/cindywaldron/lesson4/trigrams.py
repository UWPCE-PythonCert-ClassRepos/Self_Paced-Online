#!/usr/bin/env python3

import sys
import random

my_dict = {}

def read_file(filename):
    """
    read a file and store data in my_dict
    """
    # open file to read
    with open(filename, 'r') as infile:
        lines = infile.readlines()
    a_seq = []
    #replace \n
    for line in lines:
        # strip carriage return
        line = line.strip('\n')
        # create a list based on space
        alist = line.split(' ')
        a_seq.extend(alist)
    i = 0
    # create my_dict
    while ( i + 2 ) < len(a_seq):
        # generate a key using 1st word and 2nd word
        key = '{} {}'.format(a_seq[i], a_seq[i+1])
        # generate value using 3rd word
        value = a_seq[i+2]
        # if key exists, append the value to the value list
        if key in my_dict.keys():
             my_dict[key].append(value)
        else:
            # new key
            my_dict[key] = [value]
        i = i + 1

def write_file():
    """
    write data from my_dict to a file
    """
    #select a random key
    select_key = random.choice(list(my_dict.keys()))
    # create a list from select_key
    new_list = select_key.split()
    while True:
        # if select_key is in my_dict
        if select_key in my_dict.keys():
            # find the corresponding values
            list_values = my_dict[select_key]
            # if the values exist
            if list_values:
                # generate a random value from list of values
                random_value = random.choice(list_values)
                # add the random value to a new list
                new_list.append(random_value)
                # create a new selelct_key string using last two words on the lsit
                select_key = '{} {}'.format(new_list[-2], new_list[-1])
        else:
            break
    # open file to write
    with open('output.txt', 'w') as outfile:
        for item in new_list:
            outfile.write("{} ".format(item))


def main():
    # verify command line arguments
    if len(sys.argv) != 2:
        print('Error. Usage: ./trigrams.py <text file>')
    else:
        read_file(sys.argv[1])
        write_file()

if __name__ == '__main__':
    main()

