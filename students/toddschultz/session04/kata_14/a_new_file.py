import re

def ngrams(s, n=2, i=0):
    while len(s[i:i+n]) == n:
        yield s[i:i+n]
        i += 1

def qwerty(n):
    for i in n:
        print(i)

def read_txt(t):
    with open(t, 'r') as f:
        while True:
            lines = f.read()
            if len(lines) == 0:
                break
            unigram = ngrams(lines.split(), n=1)
            bigram = ngrams(lines.split(), n=2)
            trigram = ngrams(lines.split(), n=3)
            qwerty(unigram)
            qwerty(bigram)
            qwerty(trigram)
    
read_txt('/Users/toddschultz/Projects/UW/Self_Paced-Online/Students/toddschultz/session04/kata_14/sherlock_small.txt')


















































'''def format_text(line):
    print("wer")
    line = line.lower()
    line = re.sub(r'[^a-zA-Z0-9\s]', ' ', line)
    line = line.replace('\n', '')
    line = line.replace("'", "")
    line = line.replace("  ", " ")
    return line'''
