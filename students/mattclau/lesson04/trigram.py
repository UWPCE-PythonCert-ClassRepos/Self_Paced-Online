#Program to create new text using trigrams on an existing text
import os.path
import re
import string
import random

def create_tridict(text):
    wordlist = []
    tridict = {}
    trikey =''
    trivalue = ''

    #convert to list of words
    wordlist = text.split()

    #split words into trigrams
    for x in range(len(wordlist)-2):
        trikey = wordlist[x]
        trikey += ' ' + wordlist[x+1]
        trivalue = wordlist[x+2]

        #add to dictionary if not already a key, else add values
        if trikey not in tridict:
            tridict[trikey.lower()] = [trivalue.lower()]
        else:
            tridict[trikey].append(trivalue.lower())

    return tridict

def clean_text(tempstring):
    cleaned_text = tempstring

    #create pattern to remove special characters except hyphens and apostrophes
    remove = string.punctuation
    remove = remove.replace('-', '').replace("'", '')
    pattern = r"[{}]".format(remove)
    cleaned_text = re.sub(pattern, ' ', cleaned_text)

    #remove double dashes as well as EOL and orphaned apostrophes
    cleaned_text = cleaned_text.replace('--',' ').replace('\n', ' ').replace(" '", ' ')

    #remove spaces greater than 1
    cleaned_text = re.sub(' +', ' ', cleaned_text)

    #remove all 1 letter words besides I, these are oddities where the author put spaces between abbreviations
    #this may remove some instances of a that started sentences, but in a large text, this is no great loss
    to_replace = string.ascii_uppercase
    to_replace = to_replace.replace('I', '')
    for letter in to_replace:
        letter = letter + ' '
        cleaned_text = cleaned_text.replace(letter, '')


    #set I to uppercase
    cleaned_text = cleaned_text.replace(' i ', ' I ')

    return cleaned_text

def get_next_key_value(last_2, trigramdict):
    """Gets the next key based on the last word pair of the passed in text and returns it
       If that word pair does not exist in the dictionary as key, choose a random key
       and return that key instead"""
    next_key = ''

    #set next key to last 2 words of text
    next_key = last_2

    if next_key not in trigramdict:
        next_key = random.choice(list(trigramdict.keys()))

    return random.choice(trigramdict[next_key])

def create_sentence(last_2, trigramdict):
    sentence = ''

    #remove punction from last 2 words passed in that serve as the next key
    sentence_key = last_2.replace('"', '').replace('.','')

    #generate random length for sentence between 3 and 20
    sentence_length = random.randint(3,20)

    #add words based on trigrams to sentence
    for i in range(sentence_length):
        sentence += ' ' + get_next_key_value(last_2, trigramdict)

    #capitalize sentence and add period
    sentence = ' ' + sentence.lstrip(' ').capitalize() + '.'

    #put I back to capital
    sentence = sentence.replace(' i ', ' I ')

    return sentence

def create_paragraph(sentences, last_2, trigramdict):
    """Returns a created paragraph with the number of requested words
       and sentences."""
    parapgraph = ''
    new_sentence = ''

    #create sentences, if no words are returned because random sentence length has used all
    #available words, then remaining sentences are skipped, sentences have a minimum length
    #of 3, so if fewer than 3 words remain to use, a full setence is still created.
    for x in range(sentences):
        new_sentence = create_sentence(last_2, trigramdict)

        parapgraph += new_sentence

    return parapgraph + '\n'


def create_quote():
    pass

def create_new_text(trigramdict, text_length):
    """Creates new text by using trigrams and random values for each key word pair
       quotes, paragraphs and sentence sizes are determined randomly"""

    list_index = []
    new_text = ''
    current_key = ''

    #put all keys into a list so they can be indexed numerically
    for k in trigramdict:
        list_index.append(k)

    #get random starting key and add to new text
    current_key = random.choice(list(trigramdict.keys()))
    new_text = current_key.capitalize() + ' '

    #get random value for key and add to text
    new_text += random.choice(trigramdict[current_key])

    #add rest of opening sentence
    new_text += create_sentence(new_text.split()[-2].lower(), trigramdict).lower()

    #fix the I's
    new_text = new_text.replace(' i ', ' I ')

    #add a random amount of sentences from 2 to 8 for the opening
    new_text += create_paragraph(random.randint(2,8), new_text.split()[-2].lower(), trigramdict)

    #build rest of text
    #get how many words are left from user's request
    words_left = text_length - len(new_text.split())

    print(words_left)

    #get a random number of paragraphs between length/100 and length
    paragraph_count = random.randint(words_left//100, words_left//10)

    print(words_left, paragraph_count)

    #create number of requested paragraphs with 2 to 20 setences until no more words are left
    for i in range(paragraph_count):
        new_text += create_paragraph(random.randint(2,20), new_text.split()[-2].lower(), trigramdict)

        #get how many words are left from user's request
        words_left = text_length - len(new_text.split())

        #if no words remain, exit
        if words_left <= 0:
            break


    return new_text


def main():
    """Main program flow for getting text to read and perform trigrams on"""
    #prompt user to enter filename
    filename = input("Please enter the name of a text file without the extension located in the same directory as this program: ") + '.txt'

    #string to hold contents of text file before converting into dictionary
    tempstring = ''

    #check if file exists and read it into the string
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            for line in f:
                tempstring += line

        #do text cleanup
        tempstring = clean_text(tempstring)

        #convert to trigram dictionary
        tridict = create_tridict(tempstring)

        #prompt user for length of new text
        userlength = int(input("Please enter how long the next book should be: "))

        #create new text
        print('\n',create_new_text(tridict, userlength))

    #print error and prompt for file again if file doesn't exist
    else:
        print('Error! File does not exist at the current location.\n')
        main()




#Main program
if __name__ == '__main__':
    main()