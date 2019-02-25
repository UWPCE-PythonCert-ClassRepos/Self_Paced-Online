#Lesson 4 Assignment 2
#Triagrams
#Jason Virtue 02/15/2019
#UW Self Paced Python Course

import random

source = "sherlock_holmes.txt"

def read_infile(source= source):
    with open(source, "r") as infile:
        book = infile.read()
    return book

def format_book(book):
    book = book.replace("\n", " ")
    book = book.replace("\\", " ")
    words = book.split(" ")
    while "" in words:
        words.remove("")
    for i in range(len(words)):
        while " " in words[i]:
            words[i] = words[i].replace(" ", "")
        while "\\" in words[i]:
            words[i] = words[i].replace("\\", "")
        while "\\\'" in words[i]:
            words[i] = words[i].replace("\\\'", "'")
    return words

def make_dictionary(lst):
    dic = {}
    for i in range(len(lst)- 2):
        two_words = lst[i] + " " + lst[i + 1]
        value = lst[i+2]
        if two_words not in dic:
            dic[two_words] = [value,]
        else:
            dic[two_words].append(value)
    return dic

def make_sentence(dic):
    sentence = []
    while True:
        if len(sentence) == 0:
            two_words = random.choice(list(dic.keys()))
            two_word_lst = two_words.split(" ")
            if "." in two_words:
                continue
            else:
                two_word_lst[0] = two_word_lst[0].capitalize()
            word = random.choice(dic[two_words])
            new_two_word = two_word_lst[1] + " " + word
            if new_two_word in dic:
                sentence.append(two_word_lst[0])
                sentence.append(two_word_lst[1])
                sentence.append(word)
        else:
            two_word_lst = sentence[-2:]
            two_words = " ".join(two_word_lst)
            word = random.choice(dic[two_words])
            new_two_word = two_word_lst[1] + " " + word
            if new_two_word in dic:
                sentence.append(word)
        if "." in sentence[-1]:
            break
    return " ".join(sentence)

def make_paragraph(dic):
    paragraph = []
    while len(paragraph) < 5:
        para = make_sentence(dic)
        paragraph.append(para)
    return " ".join(paragraph)

def create_literature(dic, paras = 4):
    entire_book = []
    while len(entire_book) < paras:
        para = make_paragraph(dic)
        entire_book.append(para)
    return "\n\n".join(entire_book)

if __name__ == "__main__":
    book = read_infile()
    words = format_book(book)
    dic = make_dictionary(words)
    paras = int(input("How many paragraphs would you like your 'book' to have?: "))
    new_book = create_literature(dic, paras)
    print("\nPresto here is your new book as follows: ")
    print()
    print(new_book)