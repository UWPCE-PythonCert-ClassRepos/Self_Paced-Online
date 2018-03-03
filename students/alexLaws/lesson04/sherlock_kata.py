import random

# Read in the file

with open('sherlock_small.txt', 'r') as f:
    sherlock_small = f.read()

# Remove line breaks, separate words, eliminate blank words

words = [x for x in
         sherlock_small.replace("\n", " ").replace("--", " ").split(" ")
         if x != ""]

# Build a dictionary of next words

next_word = {}

for i in range(len(words) - 2):
    word_pair = (words[i], words[i + 1])
    third_word = []
    if word_pair in next_word:
        next_word[word_pair].append(words[i + 2])
    else:
        third_word = [words[i + 2]]
        next_word[word_pair] = third_word

starting_point = int(input("Where should we start? "
                           "(Max of {}): ".format(len(words))))

output = [words[starting_point], words[starting_point + 1]]
first_pair = (words[starting_point], words[starting_point + 1])


def trigram(search_pair):
    if search_pair in next_word:
        word_to_add = random.choice(next_word[search_pair])
        output.append(word_to_add)
        trigram((search_pair[1], word_to_add))

trigram(first_pair)

print(" ".join(output))
