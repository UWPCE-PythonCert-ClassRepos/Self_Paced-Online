#!/usr/bin/env python3

# lesson 04, Trigrams Assignment

# import modules
import string
import random


def read_file(file_name):
    """
    This function reads the file and parses all the words, while dropping all the punctuation and setting the words to lower case
    :return words: A list of words
    """

    # read the file and pull out all the words for the trigrams
    with open(file_name, "r") as file:

        # read each line in the file
        lines = file.read()

        # use cool string module to remove the punctuation, including dealing
        # with hyphenated words
        words = lines.translate(str.maketrans(
            string.punctuation, " " * len(string.punctuation)))
        words = words.lower().split()

    # close the file
    file.close()

    # return the words
    return(words)


def trigrams(list_of_words):
    """
    This function creates the new trigrams
    :param list_of_words: The list of words created from the file
    :return new_trigrams: Returns the new trigrams
    """

    # rename the param
    words = list_of_words

    # create new trigrams
    new_trigrams = {}

    # loop through list of words to create keys/values for the dictionary of
    # trigrams
    for i in range(len(words) - 2):

        # create the trigram
        key = (words[i], words[i + 1])

        # if already in the dictionary
        if key in new_trigrams:
            new_trigrams[key].append(words[i + 2])

        # add it
        else:
            new_trigrams[key] = [words[i + 2]]

    return(new_trigrams)


def new_story(trig):
    """
    This function creates the story from the trigrams
    :param trig: The new Trigrams created
    :return story: Returns the new story
    """
    print(trig)
    story_line = list()

    # pick a random starting word
    key_words = random.choice(list(trig))

    # if you are at the starting point
    if len(trig[key_words]) > 1:
        random_value = random.choice(trig.get(key_words))
    # add it
    else:
        random_value = trig.get(key_words)[0]

    # start your first entry
    story_line.extend((key_words[0], key_words[1], random_value))

    # loop through the trigrams to create your new story!
    for i in range(100):
        key_words = (story_line[-2], story_line[-1])

        if key_words not in trig:
            break
        else:
            random_value = trig.get(key_words[-2:])
            story_line.append(random.choice(random_value))

    return(" ".join(story_line[:-1]))


def new_file(file, story_time):
    """
    This function writes the story to a file
    :param story_time: The new story created by trigrams
    :return file: Gets the file name to write the story to the file
    """

    # print message
    print("\nWriting your new story! ")
    # print(story_time)
    # open the file and write the story
    with open((file + "_new_trigrams.txt"), "w") as donor_file:
        donor_file.write(story_time)


def main():
    """
    This is the main function that calls the program, gives the user the menu selection (in a dictionary) and sets up the donor starting list
    """

    # The file name to read and convert
    file_nam = "sherlock_small"

    # read the file
    all_words = read_file(file_nam + ".txt")

    # create the new trigrams
    new_trigrams = trigrams(all_words)

    # knit it all together
    story = new_story(new_trigrams)

    # write to file
    new_file(file_nam, story)


# call the main function
if __name__ == '__main__':
    main()
