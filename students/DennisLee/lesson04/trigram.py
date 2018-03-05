#!/usr/bin/env python3

def process_text(file):
    with open(file, 'r') as f:
        # Build paragraph list
        pg, paragraphs = '', list()
        for line in f:
            if line.strip() != '':
                pg += line.strip() + ' '
                continue
            paragraphs.append(pg)
            pg = ''

        word_pairs = dict()
        for pg in paragraphs:
            words = pg.split(' ')
            for i in range(len(words[:-3])):
                key = f'{words[i]:s} {words[i+1]:s}'
                word_pairs.setdefault(key, set())
                word_pairs[key].add(words[i+2])
        for k, v in word_pairs.items():
            print(f'Key: {k:30s}  Value: {v}')

if __name__ == '__main__':
    process_text('sherlock_small.txt')
