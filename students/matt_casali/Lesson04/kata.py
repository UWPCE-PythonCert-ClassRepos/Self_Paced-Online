#!/usr/bin/env python3

import re, random, sys, os

# Create a list of words from the text. Clean up any non alpha numeric characters
def get_words(text):
    with open(text, "r") as book:
        cleaner = re.sub('[^0-9a-zA-Z \n]+', ' ', book.read())
        words = cleaner.split()
    book.close()
    return words


# Create dictionary of trigrams.
def create_tri_dic(words):
    trigrams = {}
    for counter, word in enumerate(words):
        # Check to stay in range of words list
        if counter != (len(words) - 2):
            # Create keys by adding word, counter plus 1
            tri_keys = word + ' ' + words[counter+1]
            # Add keys to dictionary or append if keys already exist, create values as counter plus 2
            if tri_keys not in trigrams:
                trigrams.update({tri_keys: [words[counter + 2]]})
            else:
                trigrams[tri_keys].append(words[counter + 2])
        else:
            break
    return trigrams


# Create the story
def create_story(trigrams):
    # Use random to pick which key from trigram dict to start story with
    start = random.choice(list(trigrams.keys())).split()

    # Create loop to iterate through trigram keys and append values to start list
    x = 0
    while True:
        key = start[x] + ' ' + start[x + 1]
        if key in trigrams.keys():
            start.append(random.choice(trigrams[key]))
            x += 1
        else:
            # Will break loop when key is no longer found in dict due to the last words being used
            break

    # Convert list of words to string
    story = ' '.join(x for x in start)
    return story


def main():
    # Use a try statement to make sure file exists.
    try:
        book = input("Please enter a text file to open: ")
        words = get_words(book)
        trigrams = create_tri_dic(words)

        # See if the user would like the trigram as a text file and ask for a place to save the file.
        print_or_text = input("Would you like this trigram saved as a text file? Choose Y/N: ")

        if print_or_text.lower() == "y":
            directory = input("Please choose a directory where the file can be saved: ")
            trigram_text = os.path.join(directory, "Trigram.txt")
            f = open(trigram_text, "w")
            f.write(create_story(trigrams))
            f.close()
        elif print_or_text.lower() == "n":
            print("The trigram will only appear in the console. ")
            print(create_story(trigrams))
        else:
            print("You did not choose Y or N. The trigram will only be printed in the console.")
            print(create_story(trigrams))

    except FileNotFoundError:
        print("The file you chose could not be found.")
        sys.exit()


if __name__ == "__main__":
    main()

