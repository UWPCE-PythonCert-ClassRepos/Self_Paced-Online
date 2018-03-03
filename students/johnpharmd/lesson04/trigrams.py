#!/usr/bin/env python3

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
s1 = ''
s2 = ''
st_key = ''
s3 = ''
st_dict = {}
count = 0
pron_set = set(['I', 'you', 'she', 'he', 'it', 'we', 'they'])
new_data = []
final_data = []

# Processing
with open('sherlock_small.txt', 'r') as f:
    read_data = f.read()
# lines between this and next comment line can be encapsulated into a fxn
    # read_data = read_data.split(' ')
# copy_read_data = read_data[:]
# for i, st in enumerate(copy_read_data):
read_data = ' '.join(read_data.split('\n'))
read_data = ' '.join(read_data.split('--'))
read_data = ' '.join(read_data.split('-'))
read_data = ' '.join(read_data.split(', '))
read_data = ' '.join(read_data.split('. '))
read_data = ' '.join(read_data.split('('))
read_data = ' '.join(read_data.split(')'))
read_data = read_data.strip('.')
read_data = read_data.strip('  ')
read_data = read_data.split(' ')
# read_data = ' '.join(read_data.split(' '))
# read_data = read_data.split(' ') 
    # for st in read_data:
    #    new_data.append(st.strip(',.()'))

print('type(read_data):', type(read_data), '\n')
print('read_data:', read_data)
# for st in read_data:
#    print(st)
# for i, word in enumerate(st_split_lst):
#     if i + 2 < len(st_split_lst):
#         s1 = word
#         s2 = st_split_lst[i + 1]
#         st_key = (s1, s2)
#         s3 = st_split_lst[i + 2]
#         if st_key not in st_dict:
#                 st_dict[st_key] = [s3]
#         else:
#             st_dict[st_key] += [s3]
#         count += 1
# see comment line above
# print()
# print('st_dict:', st_dict)
# print('len(st_dict):', len(st_dict))

# rand_kv = st_dict.popitem()
# print('rand_kv:', rand_kv)
# print('st_dict:', st_dict)
