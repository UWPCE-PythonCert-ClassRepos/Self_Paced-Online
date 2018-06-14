# ----------------------------------------------------------------------------------------------------------------------
# NAME: MICAH BRAUN
# PROJECT: Markov_Analysis.py
# PURPOSE: Read in string data from text file and perform data manipulations on data.
# DATE: 06/11/2018
# DESCRIPTION: Uses text from large body of text (I used The Brothers Karamazov) and selects a designated number of
# text to accept as for analysis (300 in this case). Creates a dictionary of each word in the text and its associated
# words that could follow it (based on the text available) and stores the values in the trigram format. The text is
# then strung together "randomly" based on this predictive analysis and then printed out for the user to view.
# ----------------------------------------------------------------------------------------------------------------------
import re
import random
# --------------------------------------------------    DATA    --------------------------------------------------------
potential_words_map = {}                           # map from root_words to a list of potential_words
root_word = ()                                     # current tuple of words
big_list = []                                      # used for final data display

#   --------------------------------------------     FUNCTIONS     -----------------------------------------------------


def process_f(filename, order=3):
    """Reads-in file contents (from filename) with default value of 3 (trigram)"""

    fp = open(filename)                             # open file

    for line in fp:                                 # for each line of text in file: do something
        for word in line.rstrip().split():          # for each word in each line: strip \r and split into tuple
            process_word(word, order)               # for tuple, call process word()
    fp.close()                                      # close file


def process_word(word, order=3):
    """Processes each tuple/word (str, int)
    "During the first few iterations, all we do is store up the words;   <--- This quote is from Think Python's Example.
    after that we start adding entries to the dictionary."               <--- I liked their description better than
                                                                         <--- anything I could come up with.
    """
    global root_word                                       # access global tuple word collection
    if len(root_word) < order:                             # if the length of the tuple is less than order(3), add-
        root_word += (word,)                               # -word to root_word tuple. it needs to be at least 3 to work
        return

    try:
        potential_words_map[root_word].append(word)        # add value of root_word to dict potential_words_map{}
    except KeyError:
        potential_words_map[root_word] = [word]            # if key of root_word does not already exist in dict, create

    root_word = arrange_trigram(root_word, word)          # call arrange_trigram for root_word, word


def randomize(n=300):
    """Generates random words from the analyzed text -- n: number of words to generate"""
    global big_list                                                 # accesses global var big_list
    start = random.choice(list(potential_words_map.keys()))         # a random value (word) from dict

    for i in range(n):                                              # for items in range 0-300
        potential_words = potential_words_map.get(start, None)      # potential_words = random
        if potential_words == None:                                 # if == None, randomize(300 - 300)
            randomize(n-i)                                          # randomize all
            return                                              # Not None
        word = random.choice(potential_words)                       # word = random selection from potential_words
        big_list.append(word + " ")                                 # append word to big_list along with whitespace
        start = arrange_trigram(start, word)                       # start = call arrange_trigram() on start, word


def arrange_trigram(t, word):
    """Creates a new tuple with t (start) as the tuple and word as the end added on to the end (the
    beginning of the new tuple has been cut off ( see [1:] ) """
    return t[1:] + (word,)                                          # returns new tuple


def list_to_str_format():
    """Imports and uses regular expressions to break up long string of text and display
    in multiple lines for better viewing of trigrams"""

    global big_list                                                 # access global big_list
    whole = "".join(str(i) for i in big_list)   # whole = join each element in big_list (this is why I added whitespace)
    regex = re.compile('(.*?(\s))*')            # regex = re.compile((any character != \n\t\r) (repeat <-- 0:n times
                                                # (repeat 0-1 times for resulting -->)(any whitespace)(repeat 0:n)
    while whole != "":                                              # while whole isn't empty string:
        break_pos = regex.match(whole[:100]).end()                  # break_pos breaks after 100 words on whitespace
        print(whole[:break_pos])                                    # print whole up to break_pos
        whole = whole[break_pos:]                                   # whole = whole starting from previous break_pos


def main(filename, n=300, order=3):                                 # main function calls all other functions
    n = int(n)                                                      # n = default length of text to read-in from file
    order = int(order)                                              # order = default (trigram) values to store
    process_f(filename, order)                                      # open file
    randomize(n)                                                    # randomize
    list_to_str_format()                                            # format text to display
    print()                                                         # print empty line


#   ---------------------------------------------     DISPLAY     ------------------------------------------------------


main('C:\\Users\\Micah\\Desktop\\TheBrothersKaramazov.txt')          # file to use


