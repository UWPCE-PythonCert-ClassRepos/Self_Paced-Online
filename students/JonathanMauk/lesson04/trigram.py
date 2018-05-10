import random
import re
import textwrap


trigram_dict = {}


def read_text(filename):
    with open(filename) as f:
        text = f.read()
        f.close()
        return text

def make_list(source):
    formatted_text = replace(r"[\r\n]|[+---]", ' ')
    list = formatted_text.split(" ")
    for




print(read_text('sherlock_small.txt'))


# def mutate_text():


# if __name__ == '__main__':
#     get_filename = input("Enter the name of a text file to generate text from trigrams: ")
#
#     read = read_text(get_filename)



