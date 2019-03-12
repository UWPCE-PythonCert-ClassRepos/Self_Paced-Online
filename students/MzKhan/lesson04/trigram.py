'''
    Name: Muhammad Khan
    Date: 03/08/2019
    Assignment04

'''

import random
import re

def read_text(filename):
    """
    The method reads the data from the text file.
    parm: file  a text file
    return: string     a string of text data.
    """
    with open(filename, 'r') as f:
        text = f.read()
    return text

def write_text(filename, text_to_write):
    """
    This method writes the text data to an output file.
    parm: file
    parm: text
    """
    filename = filename.replace('.txt','_trigram_story.txt')
    text = text_to_write.split()
    with open(filename,'w') as out:
        min = 0
        max = 15
        while max < len(text):
            out.write(' '.join(text[min:max]))
            out.write("\n")
            min = max
            max += 15
            if max > len(text):
                out.write(' '.join(text[max:]))

def create_filtered_list(filename):
    """
    This method filters the data in the text file from all non numeric characters.
    parm: file
    return: list
    """
    text = read_text(filename)
    pattern = re.compile(r'[\r\n\t\--]')
    text = re.sub(pattern,' ',text)
    text_list = text.split()
    pattern = re.compile(r"[\W]")
    for index, text_item in enumerate(text_list):
        text_list[index] = re.sub(pattern,"",text_item)
    return text_list

def create_trigram(text_list):
    """
    Convert the text in the list to a dictionary.
    parm: list
    return: dict
    """
    trigram= {}
    for i in range(0,len(text_list)-2):
        key1,key2, value = text_list[i], text_list[i+1], text_list[i+2]
        trigram.setdefault((key1,key2),[]).append(value)
    return trigram

def get_random_pair(trigram):
    """
    return a random key pair from the trigram dictionary
    parm: dict
    """
    return random.choice(list(trigram.keys()))

def generate_new_text(trigram, number_of_words=500):
    """
    This method generates a trigram of words.
    parm: dict
    parm: kwarg1
    return: string
    """
    new_text = list(get_random_pair(trigram))
    while len(new_text) < number_of_words:
        if (new_text[-2], new_text[-1]) in trigram.keys():
            new_words = trigram[(new_text[-2],new_text[-1])]
            new_text.append(new_words[
                            random.randint(0, len(new_words) - 1)])
        else:
            new_key = get_random_pair(trigram)
            new_text.append(new_key[0])
            new_text.append(new_key[1])
    new_text = new_text[:number_of_words]
    return ' '.join(new_text)

def trigram_story(filename,number_of_words=500):
    """
    This method generates a trigram story
    parm: string
    parm: int (kwarg)
    """
    text_list= create_filtered_list(filename)
    trigram_dict = create_trigram(text_list)
    trigram_text = generate_new_text(trigram_dict,number_of_words)
    write_text(filename,trigram_text)
    print("Please read the trigram text generated!")


if __name__=="__main__":

    filename = "sherlock.txt"
    #filename = "sherlock_small.txt"
    trigram_story(filename,1000)


















