#!/usr/bin/env python3.7
# katafourteen.py
# Coded by LouReis

# Take a text file as input and for each set of 3 words, make the first two words keys.

print('This program takes a file and creates a dictionary.\n')
print('Here are the files you have to choose from in this directory:\n\n')
import pathlib
pth = pathlib.Path('./')
# pth.is_dir()
pth.absolute()
# The above command should return: PosixPath('/home/america/gitrepo/Self_Paced-Online/students/LouReis/Lesson04')
for f in pth.iterdir():
    print(f)

# Prompt the user to specify a text file to process.
filename = input("\n\nPlease enter a filename: \n\n")
print("You chose: ", filename)
print("\n\nHere's the dictionary:\n")
# The following lines open the text file & process it creating keys, values for a dictionary.
kata = {}
count = 1
key = ''
value = []
with open(filename,'r') as f:
    for line in f:
        for word in line.split():
            if count == 1:
                key = word
                count = count + 1
            elif count == 2:
                key = key + ' ' + word
                count = count + 1
            elif count == 3:
                if key in kata:
                    value = [word]
                    kata[key] = kata[key] + [word]
                    value = []
                    count = 1
                    key = ''
                else:
                    kata.update({key:[word]})
                    count = 1
                    key = ''
for k, v in kata.items():
    print(k, "=>", v)

"""
The output from the following line of text should be as follows:

I wish I may I wish I might

You might generate:

"I wish" => ["I", "I"]
"wish I" => ["may", "might"]
"may I"  => ["wish"]
"I may"  => ["I"]

"""

new_text = input("\n\nWould you like to generate a random story of 300 words? (Enter Y or N):\n\n")
import random
from random import randint
if new_text == 'Y':
    for x in range(100):
        random_key = random.sample(list(kata), 1)[0]
        temp_list = kata[random_key]
        index = randint(0, len(temp_list))
        #random_value = kata.get(random_key[index])
        random_value = temp_list[index-1]
        print (random_key, random_value, end = " ")
else:
    print("Goodbye!")
print("\n\nThe End\n\n")
