#!/usr/bin/env python3

# Joshua Bone - UW Python 210 - Lesson 4
# 01/06/2019
# Assignment: Kata Fourteen: Tom Swift Under Milk Wood

import random
import re
from enum import Enum


with open("alice_in_wonderland.txt", "r") as f:
    # Read all lines from file, stripping out carriage returns (\r) and
    # newlines (\n). Filters out any lines that are chapter headers.
    lines = list(filter(lambda line: "CHAPTER" not in line,
                        list([line.rstrip() for line in f.readlines()])))

# Books from Project Gutenberg have filler material (licensing information,
# etc) before and after the main book text. This line extracts only the text
# from the book, combined into a single string.
book_text = re.split(r"\*\*\*[^a-z]+\*\*\*", " ".join(lines))[1]
# Replace single and double dashes ("-", "--") with spaces.
book_text = book_text.replace("--", " ")
book_text = book_text.replace("-", " ")
# Create a list containing the individual words from the text. Strip out the
# header and footer of this particular book.
words = book_text.split()[11:-13]

trigrams = {}


def is_sentence_stop(word):
    return any((c in word for c in ".!?"))


# Strip punctuation and lower the case.
NORMALIZE_PATTERN = re.compile(r'[\W_]+')


def normalize(word):
    return NORMALIZE_PATTERN.sub('', word).lower().strip()


def do_trigram(word1, word2, word3):
    n1, n2, n3, = [normalize(w) for w in (word1, word2, word3)]
    if (n1, n2) not in trigrams:
        trigrams[(n1, n2)] = []
    trigrams[(n1, n2)].append(n3)


# Populate the trigram dictionary
for i in range(len(words) - 2):
    word1, word2, word3 = words[i:i+3]
    if not is_sentence_stop(word1) and not is_sentence_stop(word2):
        do_trigram(word1, word2, word3)


def do_sentence(max_words=50):
    sentence = list(random.choice(list(trigrams.keys())))
    while (len(sentence) < max_words):
        last_two = (sentence[-2], sentence[-1])
        if last_two in trigrams:
            sentence.append(random.choice(trigrams[last_two]))
        else:
            break
    return " ".join(sentence).capitalize() + "."


def format_paragraph(paragraph, width=80):
    lines = []
    while (len(paragraph) > width):
        i = width
        while paragraph[i] != ' ':
            i -= 1
        lines.append(paragraph[0:i])
        paragraph = paragraph[i+1:]
    lines.append(paragraph)
    return "\n".join(lines)


def do_paragraph(min_sentences=3, max_sentences=12):
    num_sentences = random.randint(min_sentences, max_sentences)
    paragraph = " ".join([do_sentence() for i in range(num_sentences)])
    return format_paragraph(paragraph)


def do_chapter(number=1, min_paragraphs=5, max_paragraphs=20):
    num_paragraphs = random.randint(min_paragraphs, max_paragraphs)
    chapter = "\n\n".join([do_paragraph() for i in range(num_paragraphs)])
    return f"CHAPTER {number}\n\n" + chapter


def do_title(min_words=4, max_words=8):
    num_words = random.randint(min_words, max_words)
    return do_sentence(num_words).upper()[:-1]


def do_book(num_chapters=10, author="Hal 9000"):
    chapters = "\n\n".join(do_chapter(i) for i in range(1, num_chapters + 1))
    return f"{do_title()}\nby {author}\n\n" + chapters + "\nTHE END"


if __name__ == "__main__":
    print(do_book())
