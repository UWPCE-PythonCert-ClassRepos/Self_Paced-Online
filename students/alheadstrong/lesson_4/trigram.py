import random
from tkinter import *


def generate_dictionary(input_text):
    """Return a dictionary with keys consisting of each two word combination in the text as a tuple. Values are lists
    of each one word string that follows the two word key.
    """
    d = {}
    delimiters = '\n', ' ', '\t', '\\r\\n', '\r', '\\xe2\\x80\\x9c', '\\xe2\\x80\\x9d'
    form_string = '|'.join(map(re.escape, delimiters))
    t_list = re.split(form_string, input_text)  # Using 're' module for multiple string delimiters.

    for word in t_list[:]:
        if word == '':
            t_list.remove(word)  # Remove empty string objects from list.

    for i in range(len(t_list)-2):
        key = tuple(t_list[i:i+2])
        if key in d.keys():
            d[key] = d[key]+[t_list[i+2]]
        else:
            d[key] = [t_list[i+2]]
    return d


def generate_start_key(d):
    """Return a two-word key that begins a sentence from a dictionary."""
    start_words = []
    for key in d.keys():
        if key[0][-1:] == ('.' or '?' or '!') and len(key[1:]) > 0:
            start_words += key[1:]  # Assign any word after sentence end punctuation(.,!,?) as sentence start word

    start_word = random.choice(start_words)

    start_keys = []
    for key in d.keys():
        if key[0] == start_word:
            start_keys.extend((key,))  # Create two word key from start word.

    return random.choice(start_keys)


def generate_sentence(d, max_sentence_length=30):
    """Return string pseudo-randomly generated from input dictionary 'd'.
    Keyword Arguments:

    max_sentence_length -- max number of 'words' from d(default 30)
    """
    key = generate_start_key(d)
    sentence_list = [key[0]]+[key[1]]  # Populates sentence list with starter 'words'.
    sentence_length = 2

    while 1:
        key = (sentence_list[-2], sentence_list[-1])
        v = [random.choice(d[key])]  # Select string from dictionary list at 'key' and hold in a one item list.
        sentence_list += v
        sentence_length += 1
        if sentence_length > max_sentence_length:
            sentence_list = sentence_list[:2]
            sentence_length = 3
        if v[0][-1:] == '.':
            return ' '.join(sentence_list)


def generate_paragraph(d, sentence_min=1, sentence_max=10):
    """ Take a text dictionary and return a paragraph of sentences from previously defined generate_sentences.
    Length of paragraph determined by optional args:

    Keyword arguments:
    sentence_min -- (default 1)
    sentence_max -- (default 10)
    """
    p = []
    for _ in range(random.randrange(sentence_min, sentence_max)):
        p += [generate_sentence(d)]
    return ' '.join(p)


def generate_short_story(t, min_paragraphs=5, max_paragraphs=10):
    """Return a pseudo-random short story string based on an input string, 't'.

    Keyword arguments:
    min_paragraphs -- (default 5)
    max_paragraphs -- (default 10)
    """
    e = []
    d = generate_dictionary(t)
    for i in range(random.randrange(min_paragraphs, max_paragraphs)):
        e += [generate_paragraph(d)]
    return '\n\n'.join(e)


if __name__ == '__main__':
    with open('heart_of_darkness.txt', 'rb') as f:
        text = str(f.read())
        print(text)
    with open('story_output.txt', 'w+') as f:
        f.write(generate_short_story(text))
