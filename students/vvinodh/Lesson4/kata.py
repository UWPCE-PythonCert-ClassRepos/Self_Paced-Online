import random
import math



def randomkey(i):

    return random.choice(list(i.keys()))

def randvalue(i, k):

    return random.choice(i[k])


if __name__ == "__main__":
    book = 'sherlock_small.txt'
    with open(book, 'r') as fp:
        input = fp.read()
        fp.close()

    input = input.replace('\n', ' ').replace('\r', ' ').lower()
    punctuation = set(['--', '.', ',', '!', '(', '('])
    for p in punctuation:
        input = input.replace(p, f'{p}')
    words = input.split()

    trigrams = {}
    for j in range(len(words) - 1):
        key = tuple(words[j:j + 1])
        value = words[j + 1]
        if key in trigrams.keys():
            trigrams[key].append(value)
        else:
            trigrams[key] = []
            trigrams[key].append(value)

    key_init = randomkey(trigrams)
    value_init = randvalue(trigrams, key_init)
    out_list = list(key_init)
    out_list.append(value_init)
    for i in range(1000):
        k = tuple(out_list[-2:])
        if k in trigrams:
            v = randvalue(trigrams, k)
        else:
            k = randomkey(trigrams)
            for i in list(k):
                out_list.append(i)
            v = randvalue(trigrams, k)
        out_list.append(v)
    paragraph = ' '.join(out_list)
    print(paragraph)