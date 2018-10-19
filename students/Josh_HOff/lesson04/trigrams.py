import pathlib
import os
import random
newdict = {}
words = ''
b = ''
#main function
if __name__ == "__main__":
    with open('words.txt', "r") as word_list:
        words = word_list.read().split(' ')
        print(words)
        for x in range(len(words) - 2):
            key = f'{words[x]} {words[x+1]}'
#            print(key)
            if key in newdict:
                newdict[key] += [words[x + 2]]
            else:
                newdict[key] = [words[x + 2]]
        print(newdict)
#        while True:        
        a = random.choice(list(newdict.keys()))
        while True:
#            b = 
#            if b not in newdict:
#                break
            print(a)
#            print(newdict[a])
#            print(len(newdict[a]))
            a += f' {newdict[a][0]}'
            print(a)
            print(a.split(' '))
            b = a.split(' ')
            key2 = f'{b[-2]} {b[-1]}'
            print(key2)
            if key2 not in newdict:
                print('WOW')
                break
            else:
                print(newdict[key2])
                a += f' {newdict[key2][0]}'
#                print(a)