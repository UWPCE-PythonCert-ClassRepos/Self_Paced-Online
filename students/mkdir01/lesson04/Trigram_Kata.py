#!/usr/bin/env python3

import random
storage = {}  # dict storing keys of tuples and values of lists
global_loop_key0 = ""
global_loop_key1 = ""


def seperate_words(temp_file):
    temp_chars = list(temp_file)
    # break apart at " ", do not break at "-", turn "--" into a comma, remove "\n", "at" != "at."
    for i, char in enumerate(temp_chars):
        if char == "-":  # turn "--" into ","
            if temp_chars[i + 1] == "-":
                temp_chars[i] = ", "
                temp_chars.pop(i + 1)  # and pop() second dash
        elif char == "\n":
            temp_chars[i] = " "
        elif char == '':
            temp_chars[i] = " "
        elif char == '\"':
            if temp_chars[i + 1] == "\\":
                temp_chars[i] = " "
                temp_chars.pop(i + 1)

    return "".join(temp_chars).split(" ")  # turn into a list of words


def add_to_storage(word_list):
    # create dict from list
    for i in range(len(word_list) - 2):
        tup = (word_list[i], word_list[i + 1])
        elem = word_list[i + 2]
        if elem:
            if tup in storage and elem not in storage[tup]:
                storage[tup].append(elem)
            else:
                storage[tup] = [elem]


def read_file(file_name):
    f = open(file_name)
    temp_file = f.read()
    f.close()
    # take words and make into a list
    add_to_storage(seperate_words(temp_file))


def write_file(file_name, new_story):
    f = open(file_name, 'w')
    f.write(new_story)
    f.close()
    return


def look_for_pattern(temp_list):
    for i in range(1, int(len(temp_list) / 2)):
        # compares -1 to -2, then -1:-2 to -3:-4, etc...
        if temp_list[-1:((-1 * i) - 1): -1] == temp_list[((-1 * i) - 1)::-1]:
            global_loop_key0 = temp_list[(-1 * i)]  # first elem of looping list
            global_loop_key1 = temp_list[(-1 * i) + 1]  # second elem of looping list
            # copy the loop, from start to end (we've been traversing end to start)
            return detect_infinite_loop((global_loop_key0, global_loop_key1))  # returns 0 if loop is found
            # this uses 2 global variables to keep checking the original keys even as we recurse
        else:
            return 1


def detect_infinite_loop(tup):
    # there is an infinite loop if all possible paths from first element through storage lead to last element
    # only test until we find a path that does not loop
    for i in range(len(storage[tup])):
        if tup[1] == global_loop_key0 and storage[tup][i] == global_loop_key1:
            return 0  # if the current tuple matches the initial tuple, main = 0
        elif (tup[1], storage[tup][i]) in storage:
            return detect_infinite_loop(tup[1], storage[tup][i])  # else keep searching the dict
        else:
            return 1  # we come to a point where we learn the loop is not infinite


def create_key():
    # choose a random key where the first word doesn't end in punctuation
    tup = random.choice(list(storage.keys()))
    while tup[0] == '' or tup[0][-1] == ('.' or ',' or '"' or '!' or '?' or ';' or ':' or "'" or ')'):
        tup = random.choice(list(storage.keys()))
    return tup


def create_text(file_name, min_length):
    if storage:
        tup = create_key()
    else:
        return("Dictionary is empty")

    # create new story
    temp_list = [tup[0], tup[1]]
    counter = 1
    main = 1
    while main:
        if tup in storage:
            temp_elem = storage[tup][random.randint(0, (len(storage[tup]) - 1))]
            temp_list.append(temp_elem)

            # look for infinite loops
            if (counter % 2) == 0:  # we know 1st half != 2nd half on odd-numbered lists
                main = look_for_pattern(temp_list)

            # turn list into string
            new_story = " ".join(temp_list)
            tup = (temp_list[-2], temp_list[-1])

        elif counter < int(min_length):
            tup = create_key()

        else:
            main = 0  # exit loop

        counter += 1

    write_file(file_name, new_story)


def main():
    read_file(input("input file name: "))
    create_text(input("output file name: "), input("Minimum character length: "))


if __name__ == '__main__':
    main()

