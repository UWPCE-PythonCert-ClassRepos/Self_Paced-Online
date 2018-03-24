import os
import random
#get path of current work directory
os.chdir(os.path.dirname(__file__))
cwd = os.getcwd()

#open the text file and read it into a list of words

f = open(cwd + '\sherlock.txt','r')
text = f.read()
words = text.split()
words = [str(i) for i in words]
f.close()

#create a dictionary of all 2 word combinations as the key and the following word as value
words_dict = {}
for i in range(len(words)-3):
    try:
        words_dict[words[i] + '_' + words[i+1]].append(words[i+2])
    except:
        words_dict[words[i] + '_' + words[i+1]] = [words[i+2]]

#chose arbitrary word pair as a starting point
start_i = random.randint(0,len(words)-3)
word1 = words[start_i]
word2 = words[start_i+1]
start_key = word1 + '_' + word2
kata = word1 + ' ' + word2
new_word = random.choice(words_dict[start_key])
kata = kata + ' ' + new_word

#continue chain for 100 steps
for _ in range(100):
    word1 = word2
    word2 = new_word
    new_key = word1 + '_' + word2
    new_word = random.choice(words_dict[new_key])
    kata = kata + ' ' + new_word

#print computer generated text
print(kata)
