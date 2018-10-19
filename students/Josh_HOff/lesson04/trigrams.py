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
#        print(words)
        for x in range(len(words) - 2):
            key = f'{words[x]} {words[x+1]}'
#            print(key)
            if key in newdict:
                newdict[key] += [words[x + 2]]
            else:
                newdict[key] = [words[x + 2]]
#        print(newdict)
#        while True:        
        a = random.choice(list(newdict.keys()))
#        print(a)
#            print(newdict[a])
#            print(len(newdict[a]))
        a += f' {newdict[a][0]}'
#        print(a)
#        print(a.split(' '))
        while True:
            b = a.split(' ')
#            print(b)
            #[random.choice(len(newdict[b - 1]))]
            b = f'{b[-2]} {b[-1]}'
#            print(a)
#            print(b)
            if b not in newdict:
                print('WOW')
                break
            elif len(newdict[b]) > 1:
                number = random.choice(range(len(newdict[b])))
            else:
                number = 0
    #        print(b)
    #        while True:
            if b not in newdict:
                print('WOW')
                break
            else:
#                print(number)
                a += f' {newdict[b][number]}'
#                print(a)
        print(a)
                