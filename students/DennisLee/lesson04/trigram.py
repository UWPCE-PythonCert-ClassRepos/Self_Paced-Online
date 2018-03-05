#!/usr/bin/env python3

def process_text(file):
    with open(file, 'r') as f:
        # Build the paragraph list
        pg, paragraphs = '', list()
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
    word_pairs = dict()
    for pg in paragraphs:
        words = pg.split(' ')
        for i in range(len(words[:-2])):
            key, value = f'{words[i]:s} {words[i+1]:s}', words[i+2]
            word_pairs.setdefault(key, set())
            word_pairs[key].add(value)
    
    # Isolate keys that can function as paragraph starters
    paragraph_starters = list()
    for k in word_pairs:
        if k[0] == '"' or k[0] == k[0].upper():
            paragraph_starters.append(k)

    with open('_word_pairs.txt', 'w') as f:
        for k, v in word_pairs.items():
            f.write(f'Key: {k:30s}  Value: {v}\n')

    with open('_paragraph_starters.txt', 'w') as f:
        for k in paragraph_starters:
            f.write(k + '\n')

if __name__ == '__main__':
    process_text('sherlock_Ch1_portion.txt')
