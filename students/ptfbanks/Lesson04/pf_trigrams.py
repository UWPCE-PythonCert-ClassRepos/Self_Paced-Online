#!/sr/bin/env python
#Lesson04 - pf_Trigrams
#---- set-up--------------------
import re
import random
import os

#---- Uer Instructions/ Selections--------------------
print('Thefolowing prepares a raw text essay on any given input text,'
'based entirely on the content of that text. From the out put the user is'
'required to add personal touch of formatting, punctuation and advisably '
'a grammer check. - Be advised, no guarantee of passing grade is offered.')

siz = int(input('Of how many words is the essay to be?___'))

u_opt =input('Enter file name (sherlock.txt) on which to base the generated essay:----\n'
            'or enter "none" if default (test) text is peferred.__')
if u_opt == 'none':
    s = ('One night--it was on the twentieth of March, 1888--I was '
    'eturning from a journey to a patient (for I had now returned to '
    'civil practice), when my way led me through Baker Street. As I '
    'passed the well-remembered door, which must always be associated '
    'in my mind with my wooing, and with the dark incidents of the '
    'Study in Scarlet, I was seized with a keen desire to see Holmes '
    'again, and to know how he was employing his extraordinary powers. '
    'His rooms were brilliantly lit, and, even as I looked up, I saw '
    'his tall, spare figure pass twice in a dark silhouette against '
    'the blind. He was pacing the room swiftly, eagerly, with his head '
    'sunk upon his chest and his hands clasped behind him. To me, who '
    'knew his every mood and habit, his attitude and manner told their '
    'own story. He was at work again. He had risen out of his '
    'drug-created dreams and was hot upon the scent of some new '
    'problem. I rang the bell and was shown up to the chamber which '
    'had formerly been in part my own.')
else:
    alt_file = u_opt
    with open(alt_file, 'r')as f:
        s= f.read()
        
#-------Functional objects----------------------

def gen_words(s):     #prepares input file
#    s = s.lower()    # Convert to lowercases ('reads better with this turned off)
    s = s.replace("\n", " ")
    s = re.sub(r'[^a-zA-Z0-9\s\n\n]', ' ', s)  # Replace characters with spaces 
    s = s.replace("\n", "")
    words = [token for token in s.split(" ") if token != ""] # create token, remove empty
#    print('check1:',s)   #Diagnostic Insert
    return(words)

def build_trigrams(words_in):     # builds trigrams
    trigram_list = {}             # initiate dictionary
    for i in range(len(words_in)-2):
        pair = (words_in[i], words_in[i+1])
        next = []
        if pair in trigram_list:   # if key exists, append value
            trigram_list[pair].append(words_in[i+2])
        else:
            next = [words_in[i+2]]# if new key add dictionary entry
            trigram_list[pair]= next
#            print('check 2:',trigram_list)    # -- Diagnostic Insert
    return (trigram_list)

def rand_sel(n_gram):      #randomly select new key
    return random.choice(list(n_gram))

def find_nw(n_gram, n_set):    #select next word based on new key
    if len(n_gram[n_set])!=1:  #should key relate to multiple values
        return random.choice(list(n_gram[n_set]))
    else:
        return (n_gram[n_set][0]) #for single valued key


def build_text(n_gram, esay_lng):  #builds list based on trigrams
    gen_set = rand_sel(n_gram)   #select starting key
    out_file= list(gen_set)      #assign to out_file
    out_file.append(n_gram[gen_set][0]) #append third word
    while len(out_file) <= esay_lng:    #Set output size limit
        n_set=tuple(out_file[-2:])  #last two words as new key
#        print('check 3:', n_set)               #--Diagnositc insert
        if n_set not in list(n_gram):
            n_set = (rand_sel(n_gram))  #Re-Select key if invalid
#            print('check 4 - new pick is:', n_set)  #--Diagnostic insert
            out_file.extend(n_set)  #append new set to outfile 
#            print('check 5:', out_file)     #--Diagnostic insert
            out_file.append(find_nw(n_gram, n_set))
        else:          #for valid key set
            out_file.append(find_nw(n_gram, n_set))
#            print('check 6:', out_file)     #--Diagnostic insert
    return(out_file)
#--------- Sub Tasks to build_text object---------
def rand_sel(n_gram):      #randomly select new key 
    return random.choice(list(n_gram))

def find_nw(n_gram, n_set):    #select next word based on new key
    if len(n_gram[n_set])!=1:  #should key relate to multiple values
        return random.choice(list(n_gram[n_set]))
    else:
        return (n_gram[n_set][0]) #for single valued key
#-------------------NAIN----------------------------------------------
if __name__ == "__main__":
    trigram_list = build_trigrams(gen_words(s))  #build Trigrams
    essay = str(build_text(trigram_list, siz))   #apply Trigrams
    with open('essay.txt', 'w') as f:            #Create essay.txt file
        for item in essay:
            f.write("%s" % item)
        print('\n Find output file "essay.txt" in current directory.')