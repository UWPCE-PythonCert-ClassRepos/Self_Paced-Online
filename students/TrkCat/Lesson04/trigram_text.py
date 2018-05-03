import random

def trigram_text(infile, out_len):
    """Generate trigram text of length out_len from text file infile."""
    punc = ['.', '!', '?']
    tri_dict = gen_trigram_dict(infile)
    out_text = list(start_trigram(tri_dict))
    for count in range(out_len - 2):
            if tuple(out_text[-2:]) in tri_dict:
                out_text.append(get_trigram(out_text[-2:], tri_dict))
            else:
                out_text[-1] += '.'
                out_text.extend(start_trigram(tri_dict))
    out_text = format_text(out_text, punc)
    print(' '.join(out_text))

def gen_trigram_dict(infile):
    """Return trigram generated text of set length from input txt file."""
    tri_word = dict()
    prev_word = ''
    cur_word = ''
    with open(infile, 'r') as f:
        for line in f:
            for word in line.split():                  
                if cur_word:
                    if prev_word:
                        tri_word.setdefault((prev_word, cur_word),[]).append(word.lower())
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
    prev_word = in_text[0]
    for word in in_text[1:]:
        if prev_word[-1] in punc:
            word = word.title()
        prev_word = word
    return in_text