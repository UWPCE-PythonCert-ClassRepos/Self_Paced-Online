import random

def file_to_string(file):
    # Open the file passed and read it to a string
    try:
        with open(file, "r") as f:
            s = f.read()
        f.close()
        return s
    except Exception as e:
        print("open_book: {}".format(e))

def create_lst(string):
    # Convert the string to a list split on spaces
    # Puctuation can be read as part of a word...
    try:
        lst = string.split(" ")
        return lst
    except Exception as e:
        print("create_lst: {}".format(e))


def create_dict(lst):
    # Iterates through the length of the list
    # Creates Keys (first two words) and values (third word)
    # If the key is a duplicate, than the word is added to a sting of values
    try:
        length = len(lst)
        dictionary = {}
        i = 0
        while i < (length - 2):
            key = "{} {}".format(lst[i], lst[i + 1])
            value = lst[i + 2]
            if key in dictionary:
                dictionary[key].append(value)
            else:
                dictionary[key] = [value]
            i = i + 1
        return dictionary
    except Exception as e:
        print("create_dict: {}".format(e))

def dct_key_lst(dct):
    # Creates a list of the dictionary keys
    try:
        keylst = list(dct)
        return keylst
    except Exception as e:
        print("dct_key_lst: {}".format(e))


def random_lst_item(lst):
    # pulls a random item from a list unless the list is one item long
    try:
        length = len(lst)
        if length > 1:
            random_num = random.randint(0, length - 1)
            random_item = lst[random_num]
        else:
            random_item = lst[0]
        return random_item
    except Exception as e:
        print("random_lst_item: {}".format(e))

def back_to_string(lst):
    length = len(lst)
    i = 0
    space = " "
    string = ""
    while i < length:
        string = string + lst[i]
        i = i + 1
        if i <  length:
            string = string + space
    return string

def char_prep(string):
    char = [ ",", ".", "?", "!"]
    for i in char:
        s = string.replace(i, " {} ".format(i))
    return s


def getrdone(in_file, out_file):
    # Tie it all together, allowing a more simple name is main
    try:
        s = file_to_string(in_file)
        #s2 = char_prep(s)
        original_lst = create_lst(s)
        dictionary = create_dict(original_lst)
        print("Original file loaded in...")
        keylst = dct_key_lst(dictionary)
        start_key = random_lst_item(keylst)
        start_values = dictionary[start_key]
        start_value = random_lst_item(start_values)
        print("Building new story...")
        new_lst = create_lst(start_key)
        new_lst.append(start_value)

        while True:
            next_key = "{} {}".format(new_lst[len(new_lst) - 2], new_lst[len(new_lst) - 1])
            if next_key in keylst:
                next_value = dictionary[next_key]
                next_value = random_lst_item(next_value)
                new_lst.append(next_value)
            else:
                break
        string = back_to_string(new_lst)
        print("Creating file...")
        with open(out_file, "w+") as f:
            f.write(string)
        f.close
    except Exception as e:
        print("getrdone: {}".format(e))

#++++++++++++++++++++++++
#++++++++++++++++++++++++
if __name__=='__main__':
    try:
        in_file = "AdventuresOfTomSawyer.txt"
        out_file = "AdventuresOfTomSawyerRemix.txt"
        getrdone(in_file, out_file) # Change this to pass a file
        hold = input("Complete (any key to exit)")
    except Exception as e:
        print("__main__: {}".format(e))
