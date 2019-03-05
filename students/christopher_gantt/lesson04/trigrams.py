#!/usr/bin/env python3
import random

wish_i_may = "I wish I may I wish I might"

f = open('sherlock.txt')
book = f.read()


def create_dict(a_string):
    words = a_string.split()

    #Creating the Trigram Dictionary
    tri_dict = {}
    for i in range(len(words)-2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2] 
        if pair in tri_dict:
            tri_dict[pair].append(follower)
        else:
            tri_dict[pair] = [follower]
    return tri_dict


def random_start(a_dict):
    #Random Starting Point
    key_list = []
    for key in a_dict:
        key_list.append(key)
    my_key = random.choice(key_list)
    return my_key


def create_list(my_key, tri_dict):
    new_list = [my_key[0], my_key[1]]
    random_num = random.randint(0,len(tri_dict[my_key])-1)
    random_follower = tri_dict[my_key][random_num]
    new_list.append(random_follower)

    try:
        while True:
            my_key = (my_key[1], tri_dict[my_key][random_num])
            random_num = random.randint(0,len(tri_dict[my_key])-1)
            random_follower = tri_dict[my_key][random_num]
            new_list.append(random_follower)
    except KeyError:
        pass   
    return new_list
    

def write_file(a_list):
    with open(f'{a_list[0]}.txt', 'w') as t:
        t.write(' '.join(a_list))



if __name__ == '__main__':
    #creating a simple trigram
    my_dict = create_dict(wish_i_may)
    rand_tuple = random_start(my_dict)
    my_list = create_list(rand_tuple, my_dict)
    write_file(my_list)

    #creating a trigram with a .txt file
    my_dict = create_dict(book)
    rand_tuple = random_start(my_dict)
    my_list = create_list(rand_tuple, my_dict)
    write_file(my_list)
    f.close()



