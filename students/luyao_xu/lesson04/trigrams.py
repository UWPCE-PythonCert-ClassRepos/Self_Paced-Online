import random


def read_file(filename):
    """
    Read file into a new list of words
    :param f: filename
    :returns: read file
    """
    with open(filename, 'r') as f:
        text = f.read()
        return text


def trigram_dict(s):
    """
    set up a trigram dictionary
    :param s:the split word
    :param result: final dictionary
    :param bigram: key
    :returns: a trigram dictionary with first two words use as key,and then associate third word with the key
    """
    # split words
    s = s.split()
    # Grab the first two words and use that as a key, then associate third word with the key
    result = {}
    for i in range(0, len(s) - 2):
        bigram = '{} {}'.format(s[i], s[i + 1])
        v = result.get(bigram, False)
        if not v:
            result[bigram] = [s[i + 2]]
        else:
            # move the next word and do the same
            result[bigram].append(s[i + 2])
    return result


def formulate(trigrams):
    """
    create a new text
    :param trigrams: the dictionary
    :param k:  random key in the dic
    :param words: split the random key
    :param third: a split word chose from the random key
    :param new_word: continue grabbing a word pair based on the last two words in your new text
    :param words: the new text
    :returns: a new text form from trigrams
    """

    k = random.choice(list(trigrams.keys()))
    words = k.split()
    third = random.choice(trigrams.get(k))
    words.append(third)
    while True:
        new = " ".join(words[-2:])
        next_word = trigrams.get(new)
        if next_word is None:
            break
        words.append(random.choice(next_word))
    return " ".join(words)


# Write new text to file
def write_file(filename, content):
    """
    Write file
    :param f: filename
    :param content: the new text
    :returns: write file into a new text form
    """

    with open(filename, 'w') as f:
        f.write(content)


if __name__ == '__main__':
    s = read_file('sherlock_short.txt')
    d = trigram_dict(s)
    result = formulate(d)
    write_file('output.txt', result)
