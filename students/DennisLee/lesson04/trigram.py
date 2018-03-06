#!/usr/bin/env python3

def build_text_databases(source_file):
    # Data structures, which will be compiled into a giant dict
    word_pairs = {}              # dict: key=2 consecutive words, value=following word
    paragraph_starters = list()  # list: 2 words that can begin a paragraph
    paragraph_enders = list()    # list: 2 words that can end a paragraph

    with open(source_file, 'r') as f:
        # Build the paragraph list
        pg, paragraphs = '', []
        for line in f:
            if line.strip() != '':
                pg += line.strip() + ' '
                continue
            paragraphs.append(pg)
            pg = ''
        
        # If final line contains text, add the last paragraph manually
        if pg != '':
            paragraphs.append(pg)

    with open('_paragraphs.txt', 'w') as f:
        for pg in paragraphs:
            f.write(pg + '\n')

    # Create dictionary with two-word keys and sets of following words
    for pg in paragraphs:
        words = pg.split(' ')
        for i in range(len(words[:-2])):
            w1, w2, w3 = words[i:i+3]
            key, value = pair_words(w1, w2), w3
            word_pairs.setdefault(key, set())
            word_pairs[key].add(value)

            singles.setdefault(w1, set())
            singles[w1].add(key)
                
    # Isolate keys that can function as paragraph starters or enders
    for k in singles:
        if k[0] == k[0].upper():
            paragraph_starters.append(k)
        if k[-1] in '!?."':
            paragraph_enders.append(k)

    with open('_word_pairs.txt', 'w') as f:
        for k, v in word_pairs.items():
            f.write(f'Key: {k:30s}  Value: {v}\n')

    with open('_paragraph_starters.txt', 'w') as f:
        for k in paragraph_starters:
            f.write(k + '\n')

    return {'wp': word_pairs,
            'ps': paragraph_starters,
            'pe': paragraph_enders}

def build_new_story(source_file, counter = 50):
    if type(counter) != int:
        counter = 50  # Randomizer - any number will do
    db = build_text_databases(source_file)
    words, quote_opened, begin_paragraph, text = 0, False, True, []
    pg_starters, pg_enders, word_pairs = db['ps'], db['pe'], db['wp']

    while True:
        counter += 1
        if begin_paragraph:  # Get first 2 words in paragraph
            two_words = pg_starters[counter % len(pg_starters)]
            text.extend(unpair_words(two_words))
            quote_opened = quote_state(quote_opened, two_words[0])
            quote_opened = quote_state(quote_opened, two_words[1])
            words += 2
            begin_paragraph = False
        else:  # Continue paragraph
            two_words = get_next_key(two_words, next_word)

        # Get a word to complete the trigram
        next_word = word_pairs[two_words][counter % len(word_pairs[two_words])]
        text.append(next_word)
        if quote_opened is None:  # Start over if quotation marks get screwy
            words, quote_opened, begin_paragraph, text = 0, False, True, []
            continue
        elif next_word != '':  # Word == empty string means paragraph ended
            words += 1
            quote_opened = quote_state(quote_opened, next_word)
        elif words >= 200 and quote_opened == False:
            break
        elif words < 200 and quote_opened == False:
            text.append('\n\n')
            begin_paragraph = True

    return ' '.join(text)

def pair_words(word1, word2):
    return f'{word1:s} {word2:s}'

def unpair_words(key):
    result = None
    words = key.split(' ')
    if len(words) == 2:
        result = words
    return result

def get_next_key(previous_key, next_word):
    result = None
    words = unpair_words(previous_key)
    if words is not None and len(next_word.split(' ')) == 1:
        result = pair_words(words[1], next_word)
    return result

def quote_state(previous_state, word):
    new_state = None
    if word[1:-1].count('"') > 0:  # Disqualify interior quotation marks
        pass
    elif previous_state == True:
        if start_quote(word):
            pass
        else:
            new_state = not end_quote(word)
    elif previous_state == False:
        if not start_quote(word) and end_quote(word):
            pass
        else:
            new_state = start_quote(word) and not end_quote(word)
    elif previous_state is None:
        pass
    return new_state

def start_quote(str):
    return str[0] == '"'

def end_quote(str):
    return str[-1] == '"'

if __name__ == '__main__':
    build_new_story('sherlock_Ch1_portion.txt')
