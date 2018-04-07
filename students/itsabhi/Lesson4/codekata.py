#! /usr/bin/env python3


def wordmap(fh):
    # This function creates a dictionary of trigram sequence
    oneline = ""
    while True:
        line = fh.readline()
        oneline += line.rstrip('\r')
        if not line:
            break

    print(oneline)
    word_list = oneline.split()
    n = 0
    word_dict = {}
    while(n+2 < len(word_list)):
        f_word = word_list[n]
        s_word = word_list[n+1]
        t_word = word_list[n+2]

        if (f_word + " " + s_word) not in word_dict:  # If key exists in dict
            #Handling period, bang or question mark
            if s_word.endswith("." or "!" or "?"):
                punctuation = s_word[-1]
            else:
                punctuation = ""
            word_dict[f_word + " " + s_word] = [t_word + punctuation]
        else:                                         #If key does not exist dict
            #Handling period, bang or question mark
            if s_word.endswith("." or "!" or "?"):
                punctuation = s_word[-1]
            else:
                punctuation = ""
# Append value to existing value list
            word_dict[f_word + " " + s_word] = word_dict[f_word + " " + s_word] + [t_word + punctuation]

        n += 1

    print(word_dict)
    return word_dict


def generate(word_dict):
    #This function generates the trigram output based on the dictionary input
    pointer_key = "He was"
    space_count = 1
    print(pointer_key)

    while space_count < 200:
        try:
            pointer_value = word_dict[pointer_key][0]
            print(pointer_value)
            pointer_key = pointer_key.split()[1] + " " + pointer_value
        except KeyError:
            print("Encountered a KeyError: " + pointer_key)
            pointer_value = word_dict[pointer_key[0:len(pointer_key)-1]][0]
            print(pointer_value)
            pointer_key = pointer_key[0:len(pointer_key)-1].split()[1] + " " + pointer_value
        space_count += 1


def main():
    fh = open("testinput.txt", 'r')
    word_dict = wordmap(fh)
    generate(word_dict)


if __name__ == '__main__':
    main()