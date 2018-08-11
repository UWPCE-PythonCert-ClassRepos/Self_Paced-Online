# Trigrams.py Exercise by tfbanks

# !/usr/bin/env python3

import random

# Imports file, replace a handful of punctuation and returns, finds a place to start and end and then splits the words.
with open('sherlock.txt', 'r') as import_file:
    file = import_file.read().replace('\n', ' ').replace('""', ' ').replace('!', ' ').replace(';', ' ').replace('?', ' ').replace('"', ' ').replace(',', ' ').replace('.', ' ')
    Start_word_list = file.find('To Sherlock Holmes she is')
    Finish_word_list = file.find('End of the Project Gutenberg EBook')
    word_list = file[Start_word_list:Finish_word_list].split()
    import_file.close()
# print(word_list)

trigram_dict = {}

# This takes the list created from the sherlock.txt file into trigram dict
for v in range(len(word_list) - 2):
    key = (word_list[v], word_list[v + 1])
    value = word_list[v + 2]
    if key not in trigram_dict:
        trigram_dict[key] = [value]
    else:
        trigram_dict[key].append(value)
# print(trigram_dict)

# This creates the first three values of the new story
first_key = random.choice(list(trigram_dict.keys()))
first_value = trigram_dict[first_key][0]
string = list(first_key)
string.append(first_value)

# This takes the three values, take the last two and gets new value and appends for whatever comes first 500 iterations or break
# Other options were taking forever to run and so i capped it at 500 or break.
for v in range(500):
    s = tuple(string[-2:])
    if s not in list(trigram_dict):
        break
    elif s in list(trigram_dict):
        v = str(random.choice(list(trigram_dict[s])))
    string.append(v)

# Joins the individual list of words together
output = ' '.join(string)
print(output, '\n\n')


close_statement = input("Press Any key to exit")