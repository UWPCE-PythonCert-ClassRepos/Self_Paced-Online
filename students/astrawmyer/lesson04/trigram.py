#!/usr/bin/env python3

# Trigram analysis.

# Change these for different initial pair and output length.
seed = 200
tri_length = 200

# Opens text file and makes it a list of words.
with open('sherlock.txt','r') as f:
    words = f.read()

# Format source text to remove capitilization and punctuation for more pairs.
words = words.lower()
words = words.replace(".","")
words = words.replace(",","")
words = words.replace("(","")
words = words.replace(")","")
words = words.replace("--"," ")
words = words.replace("\"","")
word_list = words.split()


# Create dictionary starting form word 1.
tri_dict = {}
for i, word in enumerate(word_list):
    if i+2 == len(word_list):
        break
    tri_key = "{} {}".format(word_list[i],word_list[i+1])
    if tri_key not in tri_dict:
        tri_dict[tri_key] = [word_list[i+2]]
    else:
        if word_list[i+2] not in tri_dict[tri_key]:
            tri_dict[tri_key].append(word_list[i+2])


# Initial random word pair seed.
out_text = [word_list[seed],word_list[seed+1]]

# Create and print 200 word trigram.
for i in range(tri_length):
    text_key = "{} {}".format(out_text[len(out_text)-2],out_text[len(out_text)-1])
    text_option_length = len(tri_dict[text_key])
    out_text.append(tri_dict[text_key][0])
    if text_option_length != 1:
        tri_dict[text_key].pop(0)

    
new_out = " ".join(out_text)
print(new_out)
