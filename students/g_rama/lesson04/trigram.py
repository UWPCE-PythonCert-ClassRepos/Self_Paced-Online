#!/usr/bin/env python3
import random


def cleanse(s):
    """Clean the words if it ends with some specific characters. This function needs more enhancements to remove
     the more patterns and as well cleaning the words that start with some characters."""
    s = s[:-1] if s.endswith('.') or s.endswith('?') or s.endswith(',') or s.endswith(')') or s.endswith('!') else s
    return s


with open("sherlock.txt", 'r') as outfile:
    """Open the file that is needed. At present assuming that file is present on same location as script"""
    count = 0
    words = []
    for line in outfile:
        count += 1
        line_words = line.split()
        words = words + line_words

    len(words)
    my_book_dict = {}
    for i in range(len(words)-2):
        if cleanse(words[i]) + " " + cleanse(words[i + 1]) in my_book_dict:
            # print("yes I am here\n")
            my_book_dict[cleanse(words[i]) + " " + cleanse(words[i + 1])].append(cleanse(words[i + 2]))
            # print(cleanse(words[i]) + " " + cleanse(words[i + 1]))
            # print(my_book_dict[cleanse(words[i]) + " " + cleanse(words[i + 1])])
        else:
            my_book_dict.update({cleanse(words[i]) + " " + cleanse(words[i + 1]): [cleanse(words[i + 2])]})
    # print(list(my_book_dict))
    random_key = random.choice(list(my_book_dict))
    # print(random_key)
    random_value = random.choice(my_book_dict[random_key])
    # print(random_value)
    gen_trigram = random_key.split()
    gen_trigram.append(random_value)
    # print(gen_trigram)
    # print(my_book_dict.keys())
    while True:
        if gen_trigram[-2] + " " + gen_trigram[-1] in my_book_dict.keys():
            random_value2 = random.choice(my_book_dict[gen_trigram[-2] + " " + gen_trigram[-1]])
            gen_trigram.append(random_value2)
            # print(gen_trigram)
            if len(gen_trigram) > 200:
                """ If the length is not specified, with random choice option for values 
                it could go on for a long time"""
                break
        else:
            print("The trigram ended as there are no words after this pattern")
            break
    print(" ".join(gen_trigram))
