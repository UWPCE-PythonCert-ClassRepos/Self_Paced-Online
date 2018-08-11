import string
import textwrap
from random import randint

aList = []
aDict = {}
aGram = []
n = 3


def read(filename):
    instream = open(filename, 'r', encoding = 'utf-8-sig')
    for line in instream:
        ln = line.split(' ')
        aList.extend(ln)
    instream.close()


def sanitize():
    dirt = ('"', ')', '(', '_', '\r', '\n')
    for word in aList:
        aList[aList.index(word)] = word.translate({ord(x):'' for x in dirt})
        # that was a fun expression that took me an hour to figure out


def ngrammer():
    for i in range(len(aList) - (n + 1)):
        k = (i + n - 1) #index clarity
        aDict.setdefault(' '.join(aList[i:k]), []).append(aList[k])
        # dictionary is searched for key (slice length 2 of aList)
        # if not found an empty list is returned and immediately appended
        # with following value (aList index k)
        # if key is found, following value is appended to the existing value
        # length of key value pair can be controlled with global variable 'n'


def generate():
    rand = randint(0, len(aList))
    aGram = aList[rand:rand + n - 1]

    while True:
        key = ' '.join(aGram[-(n - 1):])
        val = aDict.setdefault(key, 0)
        if val == 0: break
        aGram.append(val[(len(val)//2)-1])
        if len(val) > 1: val.append(val.pop(0))

    nstr = ''
    for word in aGram:
        nstr = ' '.join([nstr, word])
    # string formatting
    return nstr


def write(filename):
    nstr = generate()
    print(nstr)
    filename = filename.replace('.txt', '_ngram.txt')
    outstream = open(filename, 'w+')
    outstream.write(textwrap.fill(nstr, 80))
    outstream.close()
    print("File: ", filename, " generated.")


if __name__ == "__main__":

    filename = input('Please enter filename: ')

    read(filename)
    sanitize()
    ngrammer()
    write(filename)