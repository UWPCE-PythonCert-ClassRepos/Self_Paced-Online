#!/usr/bin/env python3

book_dict = dict()
book_dict.setdefault((),[])
line_list = list() 

book = 'sherlock_small.txt'

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
            

        
def populate_dict():
    # split each line into lists of individual words
    for line in line_list:
        words = line.split(' ')
        # populate 'book_dict' with a key for each word
        # values are the preceeding two words
        for word in words:
            # If there aren't two words preceeding the key, skip it
            if words.index(word) < 2:
                pass
            #if book    
            book_dict[str(word)] = [words[words.index(word)-2], words[words.index(word)-1]]
        
read_book(book)
populate_dict()
print(book_dict)
