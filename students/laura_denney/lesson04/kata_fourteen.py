#-------------------------------------------------#
# Title: Kata Fourteen
# Dev:   LDenney
# Date:  October 18, 2018
# ChangeLog: (Who, When, What)
#   Laura Denney, 10/18/18, Created File
#   Laura Denney, 10/22/18, Continued Work on File
#-------------------------------------------------#

import random

test = ["I", "wish", "I", "may", "I", "wish", "I", "might"]
source = "sherlock_holmes.txt"

def read_from_source(source= source):
    with open(source, "r") as infile:
        book = infile.read()
    return book


    #book = book.replace("\n", " ")
    #book = book.replace("\\", " ")
    #book = book.replace("\\'", "'")
    #book = book.replace("\\\'", "'")
    #book = book.replace('"\\\'', '"\'')
    #book = book.replace('\"\\\'', '"\'')
    #words = book.split(" ")
    #return words

def format_book(book):
    book = book.replace("\n", " ")
    book = book.replace("\\", " ")
    # book = book.replace("\'", "'")
    # book = book.replace("\'", "'")
    words = book.split(" ")
    while "" in words:
        words.remove("")
    for i in range(len(words)):
        while " " in words[i]:
            words[i] = words[i].replace(" ", "")
        while "\\" in words[i]:
            words[i] = words[i].replace("\\", "")
        while "\'" in words[i]:
            words[i] = words[i].replace("\\\'", "'")
    return words



def make_dictionary(lst):
    dict = {}
    for i in range(len(lst)- 2):
        two_words = lst[i] + " " + lst[i + 1]
        value = lst[i+2]
        if two_words not in dict:
            dict[two_words] = [value,]
        else:
            dict[two_words].append(value)
    return dict



def create_literature(dict):
    lst = []
    while len(lst) < 5:
        two_words = random.choice(list(dict.keys()))
        two_word_lst = two_words.split(" ")
        print(two_word_lst)
        word = random.choice(dict[two_words])
        print(word)
        new_two_word = two_word_lst[1] + " " + word
        print(new_two_word)
        if new_two_word in dict:
            lst.append(two_word_lst[0])
            lst.append(two_word_lst[1])
            lst.append(word)
        else: continue
    return lst

if __name__ == "__main__":
    book = read_from_source()
    words = format_book(book)
    print(words)