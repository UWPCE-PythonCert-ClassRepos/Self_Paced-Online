#!/usr/bin/env python3
import random
"""
Trigram analysis: Look at each set of three adjacent words in a document.
Use the first two words of the set as a *key*, and remember the fact that
the third word followed that key. Once you’ve finished, you know the *list*
of individual words that can follow each two word sequence in the document.
For example, given the input:

I wish I may I wish I might

You might generate:

"I wish" => ["I", "I"]
"wish I" => ["may", "might"]
"may I"  => ["wish"]
"I may"  => ["I"]

This says that the words “I wish” are twice followed by the word “I”,
the words “wish I” are followed once by “may” and once by “might” and so on.

To generate new text from this analysis, choose an arbitrary word pair
as a starting point. Use these to look up a random next word
(using the table above) and append this new word to the text so far.
This now gives you a new word pair at the end of the text, so look up
a potential next word based on these. Add this to the list, and so on.
"""

# Data
sample_st = 'I wish I may I wish I might'
read_data = []
s1 = ''
s2 = ''
st_key = ''
s3 = ''
st_dict = {}
count = 0
pron_set = set(['I', 'you', 'she', 'he', 'it', 'we', 'they'])
n = 0
new_st_lst= []
testfile_dict = {1: 'sherlock_small.txt', 2: 'sherlock.txt'}

# Processing
prompt = input('Choose "1" for small text file, or "2" for large text file: ')
# use 2 as param, if want to test with 'sherlock.txt'
with open(testfile_dict[int(prompt)], 'r') as f:
# header_size = 0
# with open('sherlock.txt') as f:
    read_data = f.read()
    # read_data = f.seek('To Sherlock Holmes she')
read_data = ''.join(read_data.split('\r'))
read_data = ''.join(read_data.split('"'))
read_data = ' '.join(read_data.split('\n'))
read_data = ' '.join(read_data.split('--'))
read_data = ' '.join(read_data.split('-'))
read_data = ' '.join(read_data.split(', '))
read_data = ' '.join(read_data.split('. '))
read_data = ''.join(read_data.split('('))
read_data = ''.join(read_data.split(')'))
read_data = ''.join(read_data.split('\'\''))
read_data = read_data.strip('.')
read_data = read_data.strip('  ')
read_data = read_data.split(' ')

print('type(read_data):', type(read_data), '\n')
# print('read_data:', read_data)
print(read_data)
# return read_data



# lines between this and next comment line can be encapsulated into a
# separate fxn
# possible name: def make_st_dict(lst):
for i, word in enumerate(read_data):
    if i + 2 < len(read_data):
        s1 = word
        s2 = read_data[i + 1]
        st_key = (s1, s2)
        s3 = read_data[i + 2]
        if st_key not in st_dict:
            st_dict[st_key] = [s3]
        else:
            st_dict[st_key] += [s3]
    # count += 1
# print(st_dict)
# see comment line above



print('\nst_dict:')
for k, v in st_dict.items():
    print(k, v, end='\n')
print('len(st_dict):', len(st_dict))



rand_k = random.choice(list(st_dict))
rand_v = random.choice(st_dict[rand_k])

new_st_lst.extend([rand_k[0], rand_k[1], rand_v])
# print('initial new_st_lst:', new_st_lst)
potential_k = (new_st_lst[-2], new_st_lst[-1])
print('potential_k:', potential_k)
while n < 10:
    if potential_k in st_dict:  # len(st_dict) * 2:
    
        new_st_lst.append(random.choice(st_dict[potential_k]))
        potential_k = (new_st_lst[-2], new_st_lst[-1])
        n += 1    
print('len(new_st_lst):', len(new_st_lst))
print(new_st_lst)


# clean_data()
# make_st_dict(read_data)
