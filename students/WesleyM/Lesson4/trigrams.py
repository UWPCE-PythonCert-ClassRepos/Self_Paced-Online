import re
import random

def open_file(string):
    '''Opens, reads and closes a .txt file'''
    f = open(string)
    secret_data = f.read()
    f.close()
    return secret_data

def ngrams(input, n):
    '''Takes text and makes n-grams'''
    input = input.split(' ')
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output[:-1]

def main():
    dict = {}
    text = (re.sub('[^A-Za-z]+', ' ', "{}".format(open_file('sherlock_small.txt')))).lower()
    trigram = ngrams(text,3)

    for i in range(len(trigram)):
        if dict.get(trigram[i][0] + ' ' + trigram[i][1], False) == False:
            dict[trigram[i][0] + ' ' + trigram[i][1]] = [trigram[i][2]]
        else:
            dict[trigram[i][0] + ' ' + trigram[i][1]].append(trigram[i][2])

    r = random.randint(0, len(trigram))
    text_trigram = trigram[r]
    word_new = trigram[r][-1]

    while word_new:
        word_new = dict.get(" ".join(text_trigram[-2:]), False)
        if word_new:
            text_trigram.append(random.choice(word_new))
    print(' '.join(text_trigram))
            
if __name__ == "__main__":
    main()
        
