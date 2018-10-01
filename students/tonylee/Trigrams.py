import random

def get_word_list():
    word_list = []
    with open('sherlock_small.txt') as inputFile:
        for line in inputFile:
            line.rstrip()
            for char in line:
                char = char.replace('--', ' ')
            words = line.split()

            for word in words:
                word_list.append(word)
    return word_list

def create_word_dict():
    word_dict = {}
    words = get_word_list()
    for index in range(len(words) - 2):
        word_dict.setdefault((words[index], words[index + 1]), []).append(words[index + 2])
    return word_dict

word_dict = create_word_dict()
word_list = get_word_list()
word_list_index = list(range(len(word_list)))

start_point = random.choice(word_list_index)

new_text = [word_list[start_point], word_list[start_point + 1]]
word_pair = (word_list[start_point], word_list[start_point + 1])

def create_new_text(pair):
    if pair in word_dict:
        next_word = random.choice(word_dict[pair])
        new_text.append(next_word)
        create_new_text((pair[1], next_word))

create_new_text(word_pair)
print(' '.join(new_text))
