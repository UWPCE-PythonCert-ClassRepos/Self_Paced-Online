import random


def trigram_text(infile, out_len):
    """Generate trigram text of length out_len from text file infile."""
    punc = ['.', '!', '?', '"', ',', '$', '-']
    tri_dict = gen_trigram_dict(infile, punc)
    out_text = []
    word_count = 0
    while word_count < out_len:
            sent_len = random.randint(6, 25)
            if (word_count + sent_len) > out_len:
                sent_len = out_len - word_count
            out_text.extend(start_trigram(tri_dict))
            word_count += 2
            for _ in range((sent_len - 2)):
                if tuple(out_text[-2:]) in tri_dict:
                    out_text.append(get_trigram(out_text[-2:], tri_dict))
                    word_count += 1
                else:
                    out_text[-1] += '.'
                    break
            out_text[-1] += '.'
    format_text(out_text, punc)
    print(' '.join(out_text))


def gen_trigram_dict(infile, punc):
    """Return trigram generated text of set length from input txt file."""
    tri_word = dict()
    prev_word = ''
    cur_word = ''
    with open(infile, 'r') as f:
        for line in f:
            for word in line.split():
                if cur_word:
                    if prev_word:
                        word = word.translate({ord(i): None for i in punc})
                        tri_word.setdefault((prev_word, cur_word), []) \
                            .append(word)
                    prev_word = cur_word
                cur_word = word
    return tri_word


def get_trigram(prev_words, tri_dict):
    """Return word from trigram dict using prev two words."""
    return random.choice(tri_dict[tuple(prev_words)])


def start_trigram(tri_dict):
    """Return random starting word pair from trigram dict."""
    return random.choice(list(tri_dict))


def format_text(in_text, punc):
    """Formats text with capilization following puncuation"""
    in_text[0] = in_text[0].title()
    for i in range(len(in_text[1:])):
        if in_text[i - 1][-1] in punc:
            in_text[i] = in_text[i].title()
        elif in_text[i][0] == 'i' and (len(in_text[i]) == 0 or not
                                       in_text[i].isalpha()):
            in_text[i] = in_text[i].title()
