from collections import defaultdict
from random import randint
import random
import io

def create_trigram(txt_location):
    mem_file = io.StringIO()
    mem_file.write('I wish I may I wish I might I wish upon a star tonight a star I wish a star I might')
    my_file = mem_file.getvalue()


    #my_file = open(txt_location)
    #txt = my_file.read()

    txt_list = my_file.split()
    trigrams = []
    i = 0
    while i < len(txt_list) - 2:
        trigrams.append(list((txt_list[i], txt_list[i + 1], txt_list[i + 2])))
        i += 1
    bigram_list = []
    for item in trigrams:
        bigram_list.append(["{} {}".format(item[0], item[1]), item[2]])
    d = defaultdict(list)
    for k, v in bigram_list:
        d[k].append(v)
    starting_pt = random.choice(list(d.keys()))
    #print("original starting_pt: " + starting_pt)
    my_story = starting_pt + " "
    for i in range(10):
        for k, v in d.items():
            if k == starting_pt:
                rand_value = randint(0, len(v) - 1)
                #print("keys and values: {}, {}".format(k, v))
                my_story += v[rand_value] + " "
                new_key = k.split(' ', 1)[1]
                #print("new_key: ")
                #print(new_key)  # the list rearranges
                starting_pt = "{} {}".format(new_key, v[rand_value])
                #print("new starting point: " + starting_pt)
        i += 1
    print()
    print()
    print(my_story)

