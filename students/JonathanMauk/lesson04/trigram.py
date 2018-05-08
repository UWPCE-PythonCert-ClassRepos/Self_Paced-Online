import random
import string


trigram_dict = {}


def create_trigram_dict(filename):
    word_list = []

    with open(filename) as f:
        for line in f:
            split = line.split()
            word_list += split
    return word_list

print(create_trigram_dict('sherlock_small.txt'))


# def mutate_text():


# if __name__ == '__main__':
#     try:
#         get_user_input = input("Enter the name of a file to generate 300 words of text from trigrams: ")
#         create_trigram_dict(get_user_input)
#     except:
#         print("Error. Please restart the program to try again.")