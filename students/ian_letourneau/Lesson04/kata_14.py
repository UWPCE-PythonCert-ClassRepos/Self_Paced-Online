#!/usr/bin/env python3
# Ian Letourneau
# 5/2/2018
# A script to generate a few hundred words using trigrams from the
# book Sherlock Holmes
import random


def setupTrigram(text):
    """A function that reads through the given text file and parses lines into 
    individual words to be added to a trigram dictionary that is returned to 
    the main script. The function replaces most punctuation and newline calls 
    so that only the words get into the dictionary.

    param text: a text file containing multiple lines of text. 
    In this case, a book."""
    f = open(text)
    file = ''
    trigramDict = dict()
    trigramTemp = []
    # Replace all puncuation and combine lines into one long string
    for line in f:
        line = line.replace("\"", "").replace("\'", "").replace(
            '\n', ' ').replace('--', ' ').replace('(', '').replace(
            ')', '').replace(',', '').replace('.', '').replace(
            '!', '').replace('?', '').replace(':', '').replace(';', '')
        file += line

    # Split the long string into a list of words. Sift through
    # the list and combine the trigram combinations into a trigram
    # dictionary formatted as per kata_14 recomendations.
    splitFile = file.split(' ')
    trigramTemp = splitFile[0:2]
    splitFile = splitFile[2:]
    for word in splitFile:
        if word:
            trigramTemp.append(word.lower())
            key = "{} {}".format(trigramTemp[0], trigramTemp[1])
            val = trigramTemp[2]
            if key in trigramDict:
                trigramDict[key].append(val)
            else:
                trigramDict[key] = [val]
            del trigramTemp[0]
    # Return the final trigram dictionary
    return trigramDict


def writeParagraph(dictionary):
    """A function that takes in a dictionary of trigrams and composes
    a literary paragraph based on defined rules. The function starts
    the text at a random key in the trigram dictionary using the random()
    function. It also chooses random points to insert commas and periods.
    If a period is added, the next word is always capitalized. Perioeds
    and commas cannot be inserted next to each other. When the paragrapgh
    limit of 100 words is reached, or the function cannot find a key for
    the trigram, the pragraph will end. and return theword count."""

    # Set all paragraph traits, both predefined and random values.
    capitalize = False
    wordCount = 3
    paragraphLimit = 100
    randomStart = random.randint(1, len(dictionary))
    randomComma = random.randint(5, 15)
    randomPeriod = random.randint(10, 30)
    while randomComma == randomPeriod:
        randomComma = random.randint(5, 15)

    # Begin list with first trigram from random key
    triList = list(dictionary.keys())
    first = triList[randomStart]
    # If dictionary key has more than one value, use first value to print.
    # Shift all values one index lower and place the used value at the
    # end of the list.
    if len(dictionary[first]) > 1:
        second = dictionary[first][0]
        for value in range(0, len(dictionary[first])):
            if value < (len(dictionary[first])-1):
                dictionary[first][value] = dictionary[first][value+1]
            else:
                dictionary[first][value] = second
    else:
        second = dictionary[first]
    second = "".join(second)
    # Split the dictionary key into a first and second word for
    # formatting and word replacement purposes.
    firstSplt = first.split(" ")
    print("\t{} {} {}".format(
        firstSplt[0].title(), firstSplt[1], second), end="")

    # While paragraph limit has not been reached, continue printing
    # trigram words
    while wordCount < paragraphLimit:
        wordCount += 1
        firstSplt[0] = firstSplt[1]
        firstSplt[1] = second
        first = " ".join(firstSplt)
        # If trigram cannot be found in dictionary keys, end the
        # paragraph and return word count
        try:
            # If dictionary key has more than one value, use
            # first value to print. Shift all values one index
            # lower and place the used value at the end
            # of the list.
            if len(dictionary[first]) > 1:
                second = dictionary[first][0]
                for value in range(0, len(dictionary[first])):
                    if value < (len(dictionary[first])-1):
                        dictionary[first][value] = dictionary[first][value+1]
                    else:
                        dictionary[first][value] = second
            else:
                second = dictionary[first]
            second = "".join(second)
        except:
            print(".\n\t")
            return wordCount
        # If period was used prior, capitalize word, else print as normal
        if capitalize:
            print(" {}".format(second.title()), end="")
        else:
            print(" {}".format(second), end="")
        # Print commas and periods at randomly generated word counts
        if wordCount == randomComma:
            print(",", end="")
        if wordCount == randomPeriod:
            print(".", end="")
            capitalize = True
        else:
            capitalize = False
    # Paragraph limit reached, end paragrapgh and return word count
    print(".\n\t")
    return wordCount


# Executable portion of the function. Sets the text file, calls functions,
# and passes relevant values as parameters. Continues until word count
# has been rached.
if __name__ == '__main__':
    defText = 'sherlock_small.txt'
    bookDict = setupTrigram(defText)
    count = writeParagraph(bookDict)
    while count < 300:
        count += writeParagraph(bookDict)
