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
    tri_key = "{} {}".format(word_list[i],word_list[i+1])
    if tri_key not in tri_dict:
        tri_dict[tri_key] = [word_list[i+2]]
    else:
        if word_list[i+2] not in tri_dict[tri_key]:
            tri_dict[tri_key].append(word_list[i+2])
#print(tri_dict)

#Initial word pair seed.
seed = 2
out_text = [word_list[seed],word_list[seed+1]]
#print(out_text)

text_key = "{} {}".format(out_text[len(out_text)-2],out_text[len(out_text)-1])
while text_key in tri_dict:
    text_option_length = len(tri_dict[text_key])
    #print(text_option_length)
    if text_option_length == 1:
        out_text.append(tri_dict[text_key][0])
    else:
        #print(tri_dict[text_key])
        out_text.append(tri_dict[text_key][0])
        tri_dict[text_key].pop(0)
    text_key = "{} {}".format(out_text[len(out_text)-2],out_text[len(out_text)-1])
        
    #print(out_text)


new_out = " ".join(out_text)
print(new_out)
