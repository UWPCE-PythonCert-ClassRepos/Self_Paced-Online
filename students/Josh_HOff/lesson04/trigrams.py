import pathlib
import os
newdict = {}
words = ''
#main function
if __name__ == "__main__":
    with open('words.txt', "r") as word_list:
        words = word_list.read().split(' ')
        print(words)
        for x in range(len(words) - 2):
            key = f'{words[x]} {words[x+1]}'
            if key in newdict:
                newdict[key] += [words[x + 2]]
            else:
                newdict[key] = [words[x + 2]]
        print(newdict)