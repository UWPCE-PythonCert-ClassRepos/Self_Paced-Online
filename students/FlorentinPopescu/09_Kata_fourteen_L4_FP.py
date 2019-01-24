# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 00:04:07 2019
@author: Florentin Popescu
"""

#===================LESSON_04====================
# Kata fourteen - Tom Swift under milk wood------
#================================================

#================================================
# Trigrams
#================================================

#------------------------------------------------
# Option 1 - construct a trigram
#------------------------------------------------
import re
import random
import string

#------------------------------------------------
def trigram(words):
    trigram = [(words[i], words[i+1], words[i+2]) for i in range(len(words) - 2)]
    return trigram

#------------------------------------------------
def generate_text(trigram, number_sentences = 10, sentence_lenght= 5):
    trigram_dict = {trigram[i][0:2]:[trigram[i][2]] for i in range(1, len(trigram))}
    
    """ generate text """
    text = ''
    for i in range(number_sentences):  
        # start with a random pair of neighbors
        chain = random.choice(list(trigram_dict.keys()))
        sentence = list(chain) 
    
        for j in range(sentence_lenght):
            #generate new key from old key and new word
            try: 
                chain = (chain[1], trigram_dict.get(chain)[0])
                sentence.append(chain[1])
            except:
                break

        sentence[0] = sentence[0].capitalize()
        sentence[-1] += ". "
        sentence = " ".join(sentence)
        text += sentence
    
    return text

#------------------------------------------------
def main():
    #Open the file for reading 
    try:
        with open("sherlock_small.txt", 'r') as f:
            small_text = f.read()
    except: FileNotFoundError("File indicated not found.")
    
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    small_text = regex.sub(' ', small_text)
    
    # lower case & split
    words = small_text.lower().split()
    word_trigram = trigram(words)
  
    print("Please enter an integer as the number of sentences you want to generate, preferably between {} and {}:>>".format(len(word_trigram)//10, 2*(len(word_trigram)//10)))
    number_sentences = input()
    print("Please enter an integer as the lenght of the sentence in the generated text, preferably bigger than 2 and smaller than {}:>>".format(len(word_trigram)//10))
    sentence_lenght = input()
    
    print("Text generated from trigram:>>\n")
    text_new = generate_text(word_trigram, int(number_sentences), int(sentence_lenght)-2)
    print(text_new)

#------------------------------------------------
if __name__=='__main__':
  main()
#================================================

#------------------------------------------------
# Option 2 - using NLTK for trigram generation
#------------------------------------------------
from nltk import word_tokenize, trigrams
from nltk.probability import FreqDist
#from nltk.corpus import stopwords
    
#open text file
try:
    with open("sherlock_small.txt", 'r') as f:
        small_text = f.read()
except: FileNotFoundError("File indicated not found.")
    
#tokenize words
tokens = word_tokenize(small_text)
    
#eliminate non-alpha chacracters
words_nltk = [token.lower() for token in tokens if token.isalpha()]
    
#compute word frequency in text
fdist = FreqDist(words_nltk)
# get the most two common words in the text
fdist.most_common(2)
    
"""
stop_words = set(stopwords.words("english"))

filtered_words=[]
for w in words_nltk:
    if w not in stop_words:
        filtered_words.append(w)
"""
    
#generate trigram
trigram_nltk = [t for t in trigrams(words_nltk)]
#trigram_nltk = [t for t in trigrams(filtered_words)]

print("Note: We are running now NLTK Option 2! For text generation we'll use text generating function from Option 1 in the program.")

print("Please enter an integer as the number of sentences you want to generate, preferably between {} and {}:>>".format(len(trigram_nltk)//10, 2*(len(trigram_nltk)//10)))
number_sentences = input()
print("Please enter an integer as the lenght of the sentence in the generated text, preferably bigger than 2 and smaller than {}:>>".format(len(trigram_nltk)//10))
sentence_lenght = input()

#use text generating function from Option 1
text_new_nltk = generate_text(trigram_nltk, int(number_sentences), int(sentence_lenght)-2)
print("Text generated from trigram:>>\n")
print(text_new_nltk)

#===============================================
#---------------- END --------------------------
#===============================================     
