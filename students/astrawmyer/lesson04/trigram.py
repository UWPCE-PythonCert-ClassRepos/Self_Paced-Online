#!/usr/bin/env python3

#Trigram analysis.


# Opens text file and makes it a list of words.
with open('sherlock_small.txt','r') as f:
    words = f.read()
word_list = words.split()
#print(word_list)

# Create dictionary starting form word 1.
tri_dict = {}
for i, word in enumerate(word_list):
    if i+2 == len(word_list):
        break
    #print(i, word)
    print("{} {}".format(word_list[i],word_list[i+1]))
    tri_dict["{} {}".format(word_list[i],word_list[i+1])] = word_list[i+2]
print(tri_dict)