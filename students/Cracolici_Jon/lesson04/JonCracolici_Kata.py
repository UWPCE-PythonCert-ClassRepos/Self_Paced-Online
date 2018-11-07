#Jon Cracolici
#UW-Python Cert
#Lesson 4 Kata Exercise

#This lesson focuses on building a new text document in the style of a 
#provided text document using the dictionary data structure.

#I will need 4 basic functions: a way to import text, a way to parse it,
#a way to build the Kata dict, and a way to use the Kata dict to create 
#and write a new file. Lets go!

import random as rand
def import_parse_text(file):
    """This function takes a text file, opens it and parses it into a list of lower case words."""
    #File import portion
    localfile = open(file, 'r')
    opentext = localfile.read()
    localfile.close()
    #Setting to lowercase, and elimating \n splitlines
    opentext = opentext.lower()
    opentext = opentext.splitlines()
    #Scrubbing punctuation from text
    translationtable = dict.fromkeys(map(ord, '-,.!@#?:;%&$)(""'), ' ')
    fstring = ''
    for item in opentext:
        fstring += ' ' + item.translate(translationtable)
    #Whitespace handling
    translation_table2 = dict.fromkeys(map(ord, '   '), ' ')
    opentext = fstring.translate(translationtable2)
    opentext = opentext.replace('  ', ' ' )
    #print(opentext)
    #spliting the string into list of words
    wordlist = opentext.split(' ')
    #print(wordlist)
    #clearing empty strings from the list
    wordlist = list(filter(None, wordlist))
    return wordlist
def build_dict(wordlist):
    """Builds a dictionary of word pairs and the words that follow, based on a text."""
    katadict={}
    for i in range(len(wordlist[:-2])):
        wordpair = '{} {}'.format(wordlist[i],wordlist[i+1])
        if wordpair in katadict:
            katadict[wordpair].append(wordlist[i+2])
        else:
            katadict.update({wordpair: [wordlist[i+2]]})
    return katadict
def new_book(katadict):
    '''This function takes a kata dictionary and returns a text written in the style of the seed text.'''
    #select a random key from the dict as the first wordpair
    wordpair = rand.choice(list(katadict.keys()))
    #wordpair = 'dark incidents'
    wcounter = 2
    mybook = ''
    mybook+= ' '+wordpair
    while (wcounter < 310):
           #string comes in with wordpair
           #lookup wordpair in dict
        if wordpair in katadict:
            nextword = rand.choice(katadict[wordpair])
            mybook += ' '+nextword
            wordpair = '{} {}'.format(*mybook.split(' ')[-2:])
            wcounter +=1
        else:
            return mybook
    return mybook        
def export_book(book):
    """This function takes a string and makes a document with it."""
    bookname = input('What do you want to name the file?')
    bookname+='.txt'
    outfile = open(bookname, 'w')
    outfile.write(book)
    outfile.close()

#The following line executes all the above for the Adventures of Sherlock Holmes
export_book(new_book(build_dict(import_parse_text('sherlock.txt'))))