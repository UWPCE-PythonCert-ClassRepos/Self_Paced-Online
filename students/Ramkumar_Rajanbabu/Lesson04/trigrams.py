#Trigrams

import random
import string

def read_book():
    """Opens and reads text file."""
    
    with open("sherlock_small.txt", "r") as f:
        book = f.read().replace("\n", " ").lower() #Replace new line with space and all in lowercase
    return book

def build_trigrams(book, words):
    """Build up the trigrams dict from the list of words.

    Args:
    Returns:
       keys: word pairs
       values: list of followers
    """

    trigrams_dict = {}
    punc_dict = {punc: "" for punc in string.punctuation}
    words = book.translate(punc_dict).split() # split by spaces
    
    for i in range(len(words)-2): # why -2 ?
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        trigrams_dict.setdefault(pair, []).append(follower)
    return trigrams_dict

if __name__ == "__main__":
    trigrams_dict = build_trigrams(book, words)
    print(trigrams_dict)