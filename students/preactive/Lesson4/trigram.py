#!/usr/bin/env python3
import random


book_dict = {}
line_list, trigram, word_list = [], [], []
start_pair = set()

def read_book():
    with open('data.txt', 'r') as f:
        line = f.readline()[:-1]
        line_list.append(line)
        while line:
            line_list.append(f.readline()[:-1])
            line = f.readline()
        for line in line_list:
            words = line.split(' ')
            for word in words:
                word_list.append(word)

def populate_dict():
    for i in range(0, len(word_list)-2):
        first_word = word_list[i]
        second_word = word_list[i + 1]
        third_word = word_list[i + 2]
        word_key = first_word + " " + second_word
        if word_key not in book_dict:
            book_dict[str(word_key)] = [third_word]
        elif third_word not in book_dict.get(word_key):
            book_dict.get(word_key).append(third_word)

def write_trigram():
    global trigram
    while len(trigram) < 1:
        trigram.append(random.choice(list(book_dict)))
        trigram = trigram[0].split()
    last_two_words = trigram[-2] + " " + trigram[-1]
    while (len(trigram) < 200) and (last_two_words in book_dict):
        try:
            last_two_words = trigram[-2] + " " + trigram[-1]
            trigram.append(random.choice(book_dict[last_two_words]))
        except:
            continue
    tri_string = "{} " * len(trigram)
    print(tri_string.format(*trigram))

if __name__ == '__main__':
    read_book()
    populate_dict()
    write_trigram()
