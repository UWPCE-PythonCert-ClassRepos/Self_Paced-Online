import string
import random

file = 'sherlock_short.txt'


def read_file():
    with open(file, 'r') as f:
        text = f.read()

    for i in string.punctuation:
        text = text.replace(i, " ")

        words = text.split()
    return (words)

def build_trigram(words):

    trigram_dic={}

    for i in range(len(words)-2):
        #works with 3 words at a time. one pair of words and a single after
        pair = words[i:i +2 ]
        follower = words[i + 2]
        
        #creates a string for dic key from the pair list
        string = pair[0] + " " + pair[1]

        if string in trigram_dic.keys():
            trigram_dic[string].append(follower)
        else:
            trigram_dic[string] = [follower]

    
    return(trigram_dic)
    



    if __name__ == '__main__':
    trigrams = build_trigrams(words)
    print(trigrams)
