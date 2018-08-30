import random

trigram = {}

# Read in a file line by line and create a dictionary of trigrams.
string_words = ''

with open('sherlock.txt', 'r') as from_file:
    for line in from_file:
        word = ''
        for char in line:
            if char.isalpha():
                word += char.lower()
            else:
                word += ' '  # Add a space if character is not alphanumeric
        string_words += word

# Create a comma separated list of all the words in the book.
list_words = string_words.split()

# Create a dictionary with first two words as key, and third word as value.
for i in range(int(len(list_words)) - 2):
    dict_key = list_words[i] + ' ' + list_words[i + 1]
    if dict_key not in trigram:
        trigram[dict_key] = [list_words[i + 2]]
    else:
        trigram[dict_key].append(list_words[i + 2])
str_trigram = str(trigram)

# Printed to a file for verification of correct algorithm.
with open('trigram.txt', 'w') as to_file:
    to_file.write(str(trigram))

# Now that your dictionary of trigrams has been created, you can start
# writing a story. Start by choosing a random key to start the story.
random_key = random.choice(list(trigram.keys()))

# Start new story....
# Specify how may words you want in the story

story_length = 200
new_story = random_key.split() + trigram[random_key]

for i in range(story_length):
    pick_one = random.choice(trigram[new_story[-2] + ' ' + new_story[-1]])
    new_story = new_story + \
        [random.choice(trigram[new_story[-2] + ' ' + new_story[-1]])]

# Print the new story to a new text file.

with open('New_Story.txt', 'w') as to_file:
    to_file.write(" ".join(new_story))

print("Check you working directory for a text file named 'New Story.txt'"
      " to see the results of the kata.")
