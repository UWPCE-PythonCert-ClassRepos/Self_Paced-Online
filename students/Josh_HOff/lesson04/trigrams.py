import pathlib
import os
import random
newdict = {}
words = ''
b = ''
count = 0
#main function
if __name__ == "__main__":
    with open('words.txt', "r") as word_list:
        words = word_list.read().split(' ')
        temp_list = words[:]
        #this 
        for i in temp_list:
            words[count] = i.replace('\n', ' ').replace('(', '').replace(')', '')
            if ' ' in words[count]:
                check = words[count].split(' ')
                words[count] = check[0]
                words.insert((count+1), check[1])
                count += 1
            count += 1

        #this loop checks for new lines and removes them, seems cleaner
        count = 0
        for i in words:
            if f'{i[:1]}' == '\n':
                words[count] = i[1:]
            count += 1
        #this loop creates the dictionary needed to complete the assignment
        for x in range(len(words) - 2):
            key = f'{words[x]} {words[x+1]}'
            if key in newdict:
                newdict[key] += [words[x + 2]]
            else:
                newdict[key] = [words[x + 2]]
        #this chooses a random key to start with
        a = random.choice(list(newdict.keys()))
        a += f' {newdict[a][0]}'
        #loops over dictionary until it cannot find words to continue the paragraph
        while True:
            b = a.split(' ')
            b = f'{b[-2]} {b[-1]}'
            if b not in newdict:
                break
            elif len(newdict[b]) > 1:
                number = random.choice(range(len(newdict[b])))
            else:
                number = 0
            if b not in newdict:
                break
            else:
                a += f' {newdict[b][number]}'
    count = 0
    #writes the new text into it's own file
    end_list = a.split(' ')
    with open('trigrams_file.txt', "w") as text_file:
        text_file.write('')
    with open('trigrams_file.txt', 'a') as text_file:
        #used this loop to format the text a bit instead of writing the text all to a single line
        for word in end_list:
            text_file.write(f'{word} ')
            count += 1
            if count % 15 == 0:
                text_file.write('\n')
    print(a)
                