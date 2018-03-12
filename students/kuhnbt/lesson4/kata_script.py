# My book is Dante's inferno (technically a poem)
import requests
import string
import random
url = 'https://www.gutenberg.org/files/1001/1001-h/1001-h.htm'

full_text = requests.get(url).text

start = 'Inferno: Canto I'
end = 'End of the Project Gutenberg EBook'

# Remove start and end material, newlines and punctuation

full_text = full_text[full_text.find(start):full_text.find(end)]

full_text = full_text.replace('\n', ' ').replace('\r', ' ')
for s in string.punctuation:
    full_text = full_text.replace(s, '')

full_text = full_text.split()


def generate_dict(txt):
    """Create triplets dictionary in format (wd_one, wd_two):wd_three"""
    d = {}
    for idx in range(len(txt)-2):
        wd_one, wd_two, wd_three = txt[idx], txt[idx+1], txt[idx+2]
        d.setdefault((wd_one, wd_two), []).append(wd_three)
    return d


def generate_text(trigrams_dict, length):
    """Generate text from trigrams dict with given number of words"""
    start_loc = random.randint(0, len(trigrams_dict))
    start_key = list(trigrams_dict.keys())[start_loc]
    results = [start_key[0], start_key[1]]
    for _ in range(length-2):
        next_word_choices = trigrams_dict[start_key]
        next_word = next_word_choices[random.randint(0,
                                      len(next_word_choices)-1)]
        start_key = (start_key[1], next_word)
        results.append(next_word)
        # Lines tend to be about 7 words long
        reshaped_results = []
        for i, j in enumerate(results):
            if i>0 and i % 7 == 0:
                reshaped_results.append('\n')
                reshaped_results.append(j.title())
            else:
                reshaped_results.append(j.lower())
    return ' '.join(reshaped_results)


def print_chapter(length):
    """Print chapter of inferno-like text with given length"""
    trigrams_dict = generate_dict(full_text)
    print(generate_text(trigrams_dict, length))


if __name__ == '__main__':
    print_chapter(100)
