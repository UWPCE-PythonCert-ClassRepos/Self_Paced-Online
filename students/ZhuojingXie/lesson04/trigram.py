#!/usr/bin/env python3
import os
import random

def read_file():
     with open("sherlock_small.txt", "r") as rf:
        rf_chunk = rf.read().replace('\n', ' ').replace('.','').replace('(',' ').replace(')', ' ').replace(',','').replace('--',' ')
        return rf_chunk.lower().split()

def my_key(rf_list):
    default_dict = {}
    for i in range(len(rf_list)-2):
        two_words_key=rf_list[i] +' ' + rf_list[i+1]
        third_word = rf_list[i+2]
        default_dict.setdefault(two_words_key,[]).append(third_word)
    return default_dict

def new_text(a_dict):
    new_text_list=[]
    starting = random.choice(list(a_dict))

    #starting from a random key

    new_text_list.extend(starting.split())

    while True:

        try:
            last_two_words = ' '.join(new_text_list[-2:])
            #trying to extract last two words from the sentence
            next_word_list= a_dict[last_two_words]
            #in case there are mutile choice for that key, i use 'if' and 'pop'
            #to pop out the first one, and always keep last one.
            if len(next_word_list) > 1:
                next_word = next_word_list.pop(0)
            else:
                next_word = next_word_list[0]
            new_text_list.append(next_word)

        except:
            #keep trying and adding word in my sentence unless there is an error that there is no more
            #word i can add in.
            break

    print( ' '.join(new_text_list))


def main():
    a = read_file()
    b = my_key(a)
    new_text(b)

if __name__ == "__main__":
    main()
