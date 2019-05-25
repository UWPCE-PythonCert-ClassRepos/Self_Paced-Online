#! /usr/bin/env python
import random
import string

example_text = "I wish I may I wish I might"

def load_file(file):
    # TODO: Strip not text, ie TOC, Intros, title lines, etc.
    with open(file, 'r') as f:
        text = f.read().replace('\n', ' ')
    return text


def remove_punctuation(text):
    #TODO: Look for contractions, code around to avoid ["can", "t", "won", "t"]
    # replace n't with unicode character, do translate, then sub back.
    return text.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation))).lower()


def random_start(trigram):
    return random.choice(list(trigram.keys()))


def next_word(choices):
    return random.choice(choices)


def build_trigram(text):
    
    words = text.split()
    word_dict = {}

    for i in range(len(words) - 2):
        key = (words[i],words[i+1])
        word_dict.setdefault(key,[]).append(words[i+2])
    return word_dict


def make_text(trigram):
    start = random_start(trigram)
    text = list(start)
    # while True:
    while len(text) < MAX_WORD_COUNT:
        seed = trigram[(text[-2], text[-1])]
        text.append(next_word(seed))
        # print(seed)
        if (text[-2], text[-1]) not in trigram.keys():
            break
    return text


def save_story(story):
    with open('story.txt', 'w') as f:
        f.write(story)


def make_sentences(text):
    sentence_threshold = 10
    forbidden_end_words = ['and', 'a', 'or', 'the' ]
    story = text[0].capitalize()
    i = 1

    #TODO: Add grammar rules, ie don't end sentence with preposition.
    #OPTION: Build dict for source words that end sentences rather than random.
    for word in text[1::]:
        if random.randint(1,100) < sentence_threshold and word not in forbidden_end_words:
            story += '. '
            i = 0
        if i == 0:
            word = word.capitalize()
        story += ' ' + word 
        i += 1
    story += '.'
    return story


if __name__ == "__main__":
    # file = 'sherlock_small.txt'
    file = 'sherlock.txt'

    MAX_WORD_COUNT = 100000
    trigram = build_trigram(remove_punctuation(load_file(file)))    
    text = make_text(trigram)
    story = make_sentences(text)

    print(story)
    save_story(story)