trigram={}
import string
# Read in a file line by line and create a dictionary of trigrams)
string_words=''

with open('sherlock_small.txt', 'r') as from_file:
    for line in from_file:git
        word = ''
        for char in line:
            if char.isalpha():
                word+=char.lower()
            else:
                word+=' ' #Add a space if character is not alphanumeric
        string_words+=word

# This is the list of all the words as read in from the input text
# file, with all the non-alphanumeric characters removed.
list_words = string_words.split()
print(list_words)
