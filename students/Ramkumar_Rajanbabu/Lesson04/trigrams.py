#Trigrams

import random
import string

def main():
    """Runs main functions."""
    
    raw_words = read_book()
    trigrams_dict = build_dictionary(raw_words)
    show_trigrams(trigrams_dict)

def read_book():
    """Opens and reads text file."""
    
    with open("sherlock_small.txt", "r") as f:
        raw_book = f.read().replace("\n", " ").lower() #Replace new line with space and all in lowercase
        punc_dict = {punc: "" for punc in string.punctuation}
        punc_swap = str.maketrans(punc_dict)
        raw_book = raw_book.translate(punc_swap) # split by spaces
        raw_words = raw_book.split()
    return raw_words

def build_dictionary(raw_words):
    """Build trigrams dictionary"""
    
    trigrams_dict = {}
    for i in range(len(raw_words)-2):
        trigrams_dict.setdefault(raw_words[i] + " " + raw_words[i+1], []).append(raw_words[i+2])
    return trigrams_dict

def show_trigrams(trigrams_dict):
    """Show trigrams output."""
    
    text = list()
    trigram_key = random.choice(list(trigrams_dict))
    trigram_val = trigrams_dict.get(trigram_key)[0]
    trigram_key_split = trigram_key.split() #Splits items within key into 2 items

    for each_text in trigram_key_split:
        text.append(each_text) #Append 1st and 2nd item
    text.append(trigram_val) #Append 3rd item

    trigram_key = text[1] + " " + text[-1]
    trigram_val = trigrams_dict.get(trigram_key)[0]

    for index in range(random.randint(0,100)):
        trigram_key = text[-2] + " " + text[-1]
        if trigram_key in trigrams_dict:
            trigram_val = trigrams_dict.get(trigram_key)[0]
            text.append(trigram_val)
        else:
            break
    paragraph = " ".join(text)
    print(paragraph)

if __name__ == "__main__":
    main()