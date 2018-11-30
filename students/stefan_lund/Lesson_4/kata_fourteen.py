# python 3
# Stefan Lund
# Lesson_4

# import os
import urllib.request
import random

def scrub(s):

    b = []
    i = 0
    # print("\ns: ", s)
    while i < len(s):
        word = s[i]
        # print("i: ", i, "   word: ", word)
        if word == "mr" and len(s) - i >2:
            word = "mr."
            print("i: ", i, "   word: ", word, "s[i + 2]: ", s[i + 2], "\ns: ", s)
            c = word, s[i + 2]
            c = " ".join(c)
            c = c.title()
            # print("i: ", i, "   c: ", c)
            b.append(c)
            i += 3
        elif (word == "tom" or word == "tom's") and len(s) - i >1:
            if s[i + 1] == "swift":
                c = word, s[i + 1]
                c = " ".join(c)
                i += 1
            else:
                c = word
            c = c.title()
            b.append(c)
            i += 1
        elif word == "chapter" and len(s) - i >1:
            if s[i + 1].count("i") == len(s[i + 1]):
                i += 2
            else:
                c = word
                b.append(c)
                i += 1
        elif word == "i":
            b.append("I")
            i += 1
        elif word == "ned":
            b.append("Ned")
            i += 1
        elif "." in word:
            word1 = word.split(".")[0]
            word2 = "."
            b.append(word1)
            b.append(word2)
            i += 1
        elif word.count("-") > 1:
            words = word.split("-")
            word1, word2 = words[0], words[-1]
            b.append(word1)
            b.append(word2)
            i += 1
        else:
            b.append(word)
            i += 1
    return b


def splitstrip(s):
    a = s.lower().split()
    b = []
    i = 0
    # print("\ns: ", s)
    while i < len(a):
        word = a[i]
        word = word.strip(";:?!-\"'")
        # print("word: ", word)
        if "," in word:
            x, y = word.split(",")
            if x and y:
                b.append(x)
                b.append(y)
                i += 1
            else:
                b.append(word.strip(","))
                i += 1
        else:
            b.append(word)
            i += 1
    # print("b: ", b)
    return b

def markov(s, dic):
    for i in range(len(s) - 3):
        # print("i: ", i, "  i+2: ", i+2, len(s), end="")
        combo = s[i] + " " + s[i + 1]
        next_word = s[i + 2]
        # print("    combo: ", combo, end="")
        # print("    next_word: ", next_word, end="")
        if combo in dic:
            if next_word in dic[combo]:
                # print("   A")
                dic[combo][next_word] += 1
            else:
                # print("   B")
                dic[combo][next_word] = 1
        else:
            # print("   C")
            dic[combo] = {}
            dic[combo][next_word] = 1
    return dic

def read_from(url_srce):

    # try:
        # with open(to_destination, 'ab') as outfile:

    r = urllib.request.urlopen(url_srce)
    text = r.readline
    line = text()
    start = False
    s = "CHAPTER I\r".encode("utf-8")
    e = "End of the Project Gutenberg EBook".encode("utf-8")
    old_line = []
    old_trigram_dict = {}
    while line != b"":
        # skip the header part
        while not start:
            if line.startswith(s):
                start = True
            else:
                line = text()
        # stop reading when book ends, before the footer
        if line.startswith(e):
            line = "".encode("utf-8")
        else:
            if line != "\r\n".encode("utf-8"):
                line = line.decode("utf-8")
                s_line = splitstrip(line)
                old_line.extend(s_line)
                if len(old_line) > 3:
                    old_line = scrub(old_line)
                    new_trigram_dict = markov(old_line, old_trigram_dict)
                    # print("old_line: ", old_line, len(new_trigram_dict))
                    old_line = old_line[-3:]
                    # print("old_line: ", old_line, len(new_trigram_dict))
                    old_trigram_dict = new_trigram_dict
            line = text()
    return old_trigram_dict

def dict_frequency_keys(word_frequency_dict):
    # returns a dictionary with a number as key (frequency) and corresponing
    # word as value
    # print("dict_frequency_keys, word_frequency_dict: {}".format( word_frequency_dict))
    current_sum = 0
    frequency_word_dict = {}
    for word in word_frequency_dict:
        value = word_frequency_dict[word]
        # print("frequency_keys, word: {:>15},  trigram_dict[word]: {}".format( word, trigram_dict[word]))
        current_sum += value
        frequency_word_dict[current_sum] = word

    return frequency_word_dict


def frequency_keys(trigram_dict):
    # returns a dictionary with a number as key (frequency) and corresponing
    # word as value
    current_sum = 0
    frequency_word_dict = {}
    for word in trigram_dict:
        temp = trigram_dict[word].values()
        # print("frequency_keys, word: {:>15},  trigram_dict[word]: {}".format( word, trigram_dict[word]))
        current_sum += sum(temp)
        frequency_word_dict[current_sum] = word

    return frequency_word_dict

def max_frequency(frequency_dict):
    """
        frequency_dict: {word1: count of appearance + cumulative count of appearance for word2,
                         word2: count of appearance + cumulative count of appearance for word3,
                         word3: count of appearance}
    """
    # print("frequency_dict: ", frequency_dict)
    d = {}
    for key in frequency_dict:
        # print("max_frequency\nfrequency_dict[key]: ", frequency_dict[key], "  key: ", key)
        d[frequency_dict[key]] = key
    # print(d)
    # list of keys
    ks = list(d.keys())
    # highest number represents 100% of the counted words
    mx = max(ks)
    print("max_frequency,    mx: ", mx)
    return mx

def choose_word(word_frequency):
    """
    word_frequency: dictionary{cumulative-frequency:word, etc}
    """
    # get total of all the possible frequencies
    # total_frequency = max_frequency(word_frequency)
    total_frequency = max(word_frequency.keys())
    # print("choose_word,  total_frequency: ", total_frequency)
    assert(total_frequency > 0), "choose_word total_frequency is not a number"
    # print("word_frequency: ", word_frequency)
    # print("total_frequency: ", total_frequency)
    # choose start from all the possibilities
    r = random.randint(1, total_frequency)
    # print("choose_word, r: ", r, type(r))
    # find key corresponding key in word_frequency dictionary
    key_random = min(k for k in word_frequency if k >= r)
    # word randomly selected
    word = word_frequency[key_random]
    return word


def next_word(combo, tri_dict):
    # using the combo word as key, get dict with all words following this combo

    if combo in tri_dict:
        next_word_dict = tri_dict[combo]
    else:
        # if combo was never used in the book, return False
        return False
    # create a revers dictionary with cumulative frequency for each word as key
    word_frequency = dict_frequency_keys(next_word_dict)
    # get the word
    word = choose_word(word_frequency)
    return word

def make_word_count(total_count, from_source):
    # create a combo word frequency dictionary from book at url_source
    # combo_dict = {combo word: {word1:word-count, word2:word-count, etc}}
    # combo-word count is the sum of word-count for word1, word2 etc
    tri_dict = read_from(from_source)

    frequency_combo = frequency_keys(tri_dict)
    # frequency_combo-dict = {cumulative frequency:combo-word, etc}

    word_list = []
    while len(word_list) < 2 and "." not in word_list:
        start_combo = choose_word(frequency_combo)
        word_list = start_combo.split()

    count = 2
    while count <= total_count:
        previous = word_list[-2], word_list[-1]
        previous_combo = " ".join(previous)
        # print("make_word_count,  tri_dict[previous_combo]: ", tri_dict[previous_combo])
        new_word = next_word(previous_combo, tri_dict)
        if new_word:
            word_list.append(new_word)
            count += 1
        else:
            # if previous_combo was never use in book,
            # create a new combo word and add them to
            # the word_list
            new_start_combo = choose_word(frequency_combo)
            new_word_list = []
            while len(new_word_list) < 2:
                new_start_combo = choose_word(frequency_combo)
                new_word_list = new_start_combo.split()
                word_list.extend(new_word_list)
                count += 2
                # print("\n  make_word_count,  new_word_list: ", new_word_list)
    return word_list

def run_trigram():

    url_source = "http://www.gutenberg.org/cache/epub/499/pg499.txt"
    word_count = 200
    new_writings = make_word_count(word_count, url_source)

    i = 0
    nw_lst = []
    while i < len(new_writings):
        word = new_writings[i]
        if i == 0:
            if word == ".":
                word = new_writings[1]
                i = 1
            nw_lst.append(word.title())

        elif word == ".":
            sentence_end = nw_lst.pop() + "."
            nw_lst.append(sentence_end)
            if i + 1 < len(new_writings):
                nw_lst.append(new_writings[i + 1].title())
                i += 1
        else:
            nw_lst.append(word)
        i += 1
    #     # print(i, "    ", word)
    nw_lst = " ".join(nw_lst)
    print(nw_lst)


if __name__ == '__main__':
    run_trigram()
