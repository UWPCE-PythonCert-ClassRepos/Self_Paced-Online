#!/usr/bin/env python3
import random

# txt file to be used
text_in = 'sherlock_full.txt'

with open(text_in) as f:
    msg = f.read()

# manipulate text file to be more trigram friendly
string = msg.lower()
string = string.replace("\n", " ")
string = string.replace("--", " ")
string = string.replace("-", " ")
spl_string = string.split(" ")

# init vals
i = 0
j = 0
str_dict = {}

for i in range(0, len(spl_string)-2):
    key = spl_string[i] + " " + spl_string[i+1]
    str_dict.setdefault(key, []).append(spl_string[i+2])


def rand_start():
    rand_key = random.choice(list(str_dict.keys()))
    return rand_key


def get_next(x, key):
    out = ""
    for i in range(x):
        if key in str_dict:
            next_word_list = str_dict[key]
            # select random index from next word list
            rand_index = random.randint(0, len(next_word_list)-1)
            next_word_rand = next_word_list[rand_index]
            split_key = key.split(" ")
            key = split_key[1] + " " + next_word_rand
            out = out + " " + next_word_rand
        else:
            key = rand_start()
    return out


def trigrams(x):
    start = rand_start()
    print(get_next(x, start))


if __name__ == "__main__":
    print("you are in trigram main")
    print("you are currently using text from {}".format(text_in))
    while_asking_for_size = 1
    while while_asking_for_size == 1:
        sel = int(input("what size trigram do you want? ('0' to quit) "))
        if sel == 0:
            while_asking_for_size = 0
        else:
            trigrams(sel)
