#!/usr/bin/env python3

#Trigram analysis.


# Opens text file and makes it a list of words.
with open('sherlock_small.txt','r') as f:
    words = f.read()
words = words.lower()
words = words.replace(".","")
words = words.replace(",","")
words = words.replace("(","")
words = words.replace(")","")
words = words.replace("--"," ")
word_list = words.split()
#print(word_list)

# Create dictionary starting form word 1.
tri_dict = {}
for i, word in enumerate(word_list):
    if i+2 == len(word_list):
        break
    #print(i, word)
    #print("{} {}".format(word_list[i],word_list[i+1]))
    if "{} {}".format(word_list[i],word_list[i+1]) not in tri_dict:
        tri_dict["{} {}".format(word_list[i],word_list[i+1])] = [word_list[i+2]]
    else:
        tri_dict["{} {}".format(word_list[i],word_list[i+1])].append(word_list[i+2])
print(tri_dict)

#Initial word pair seed.
seed = 8
out_text = "{} {} ".format(word_list[seed],word_list[seed+1])
out_text = out_text + tri_dict["{} {}".format(word_list[seed],word_list[seed+1])][0]
print(out_text)