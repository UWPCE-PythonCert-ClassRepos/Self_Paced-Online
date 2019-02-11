import string
import random


def trigram(words_list):
    """
    :param words_list:
    :return:
    """
    trigram = {}
    for index, word in enumerate(words_list):
        if index + 2 < len(words_list):
            key = word + ' ' + words_list[index + 1]
            if key not in trigram.keys():
                trigram[key] = [words_list[index + 2]]
            else:
                trigram[key].append(words_list[index + 2])
    return trigram


def read_file(file_name):
    """
    :param file_name: file name

    :return: list of words
    """
    with open(file_name, 'r') as file:
        read = file.read()
    for punctuation in string.punctuation:
        read = read.replace(punctuation, ' ')
    words_list = read.split()
    file.closed
    return words_list


def create_file(trigram):
    """
    :param words_list:
    :return:
    """
    output_text = ''
    rand_key = random.choice(list(trigram.keys()))
    print(output_text)
    output_text += rand_key
    print(output_text)
    output_text += ' '+random.choice(trigram[rand_key])
    print(output_text)
    new_key = output_text.split()[-2:]
    print(output_text)
    output_text += ' ' + random.choice(trigram[new_key])
    print(output_text)
    return output_text
