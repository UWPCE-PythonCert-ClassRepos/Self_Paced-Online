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
    :param trigram: dictionary representing trigram
    :return: sequence of words randomized
    """
    random_key = random.choice(list(trigram)).split()

    for index in range(len(trigram)):
        new_key = random_key[index] + ' ' + random_key[index + 1]
        if new_key in trigram:
            new_value = random.choice(trigram[new_key])
            random_key.append(new_value)
        else:
            break

    return ' '.join(random_key)
