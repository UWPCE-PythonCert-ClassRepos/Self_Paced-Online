#!/usr/bin/env python3
import pathlib
import os
import random

triagram_dictionary = {}
total_string = []


def file_to_words():
    # read file
    source_file = r'C:\Users\tlugo\Desktop\PythonUW\Class210\Self_Paced-Online\students\tlugosan\lesson04\sherlock_small.txt'
    source_file_path = pathlib.Path(source_file)
    with open(str(source_file_path), 'r') as sf:
        one_line_no_carriage = sf.read().replace('\n', ' ')
        one_line = one_line_no_carriage.replace('--', ' ')
        words_list = []
        for sentence in one_line.split():
            words_list.append(sentence)
    return words_list


def build_triagram(words_list):
    words_list_length = len(words_list)
    for i in range(words_list_length - 2):
        dictionary_key = words_list[i] + ' ' + words_list[i + 1]
        if dictionary_key not in triagram_dictionary:
            triagram_dictionary[dictionary_key] = [words_list[i + 2]]
        else:
            triagram_dictionary[dictionary_key].append(words_list[i + 2])


def text_from_triagrams(random_key, triagram_dictionary):
    if random_key not in triagram_dictionary.keys():
        return
    else:
        sec = random.choice(triagram_dictionary[random_key])
        total_string.append(sec)
        if len(triagram_dictionary[random_key]) > 1:
            triagram_dictionary[random_key].remove(sec)
        else:
            del triagram_dictionary[random_key]
        first = str(random_key).split()[1].rstrip(' ')
        third = first + ' ' + sec
        text_from_triagrams(third, triagram_dictionary)


def rebuild_story(key_to_start):
    target_directory = r'C:\Users\tlugo\Desktop\PythonUW\Class210\Self_Paced-Online\students\tlugosan\lesson04'
    file_name = "kata_result.txt"
    target_file_path = os.path.join(target_directory, file_name)
    another_words_list = []
    another_words_list = file_to_words()
    build_triagram(another_words_list)
    print(triagram_dictionary)
    # key_to_start = ''
    text_from_triagrams(key_to_start, triagram_dictionary)
    with open(str(target_file_path), 'w') as tf:
        total_string.insert(0, key_to_start)
        final_string = ''
        for parts in total_string:
            final_string += ' ' + parts
        final_string += '\n'
        tf.write(final_string)
        print(final_string)


if __name__ == '__main__':
    rebuild_story("I was")
