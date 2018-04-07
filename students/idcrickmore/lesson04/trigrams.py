#!/usr/bin/env python3

book_dict = dict()
book_dict.setdefault((),[]) 
line_list = list() 
word_list = list()

book = 'sherlock.txt'

def read_book(b):
    with open(str(b), 'r') as f:
        # 'line' var get the value of the first line of the book
        # minus the '\n' of every line ([:-1])
        line = f.readline()[:-1]
        # 'line_list' var starts with 'line'
        line_list.append(line)
        
        # as long as 'line' is True
        # append 'line_list' by reading new lines
        while line:
            line_list.append(f.readline()[:-1])
            # as soon as f.readline() doesn't have a line to read
            # 'line' will be null, and the while loop stops
            line = f.readline()
        
        # populate word list one line at a time
        for line in line_list:
            words = line.split(' ')
            for word in words:
                word_list.append(word)
        
def populate_dict():

    for word in word_list[:-2]:
        # define 'first_word', 'second_word' and 'third_word'
        # using the .index() function
        first_word = word_list[word_list.index(word)]
        second_word = word_list[word_list.index(word) + 1]
        third_word = word_list[word_list.index(word) + 2]
        
        # combine 'first_word' and 'second_word' to make 'word_key'
        word_key = first_word + " " + second_word
        
        book_dict[str(word_key)] = [third_word]

        
        if word_key not in book_dict:
            book_dict[str(word_key)] = third_word
            
        #this isn't working, no examples of multiple values
        elif third_word not in book_dict.get(word_key):
            book_dict[str(word_key)].append(third_word)
            

def test():
    for x in book_dict:
        #if len(book_dict.get(x))>1:
         #   print(x)
        print(len(book_dict.get(x)), end="")

read_book(book)
populate_dict()         
test()

