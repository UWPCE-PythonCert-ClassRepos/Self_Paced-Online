'''
    Name: Muhammad Khan
    Date: 03/08/2019
    Assignment04

'''

import random
import re

def read_text(filename):
    '''
    The method reads the data from the text file.
    parm: text file
    return: text
    '''
    with open(filename, 'r') as f:
        text = f.read()
        f.close()
    return text

def write_text(filename, text_to_write):
    '''
    This method writes the data to an output file.
    parm: file
    parm: text data
    '''
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
        out.close()

def create_filtered_list(filename):
    text = read_text(filename)
    pattern = re.compile(r'[\r\n\t\--]')
    text = re.sub(pattern,' ',text)
    text_list = text.split()
    pattern = re.compile(r"[\W]")
    for index, text_item in enumerate(text_list):
        text_list[index] = re.sub(pattern,"",text_item)
    return text_list

def create_trigram(text_list):
    trigram= {}
    for i in range(0,len(text_list)-2):
        key1,key2, value = text_list[i], text_list[i+1], text_list[i+2]
        trigram.setdefault((key1,key2),[]).append(value)
    return trigram

def get_random_pair(trigram):
    '''
    This method returns a random key pair from the trigram dictionary
    return: tuple
    '''
    return random.choice(list(trigram.keys()))

def generate_new_text(trigram, number_of_words=500):
    """
    This method generates a trigram of words.
    parm: dict
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
    """ This method generates a trigram story
    parm: string
    parm: int
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


















