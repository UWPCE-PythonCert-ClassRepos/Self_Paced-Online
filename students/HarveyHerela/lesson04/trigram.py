import string
import random

# Trigram is dictionary where the keys are 2-word tuples and the
# values are a list of words
trigrams = {}

# For creating the trigrams
prev_words = []

# Name of the book to parse
book_filename = "jack_london_white_fang.txt"

def add_word_to_trigram(new_word):
    """Helper function for creating the trigrams"""
    # Trigrams require 2 previous words
    # If we don't have those yet, then set them
    if len(prev_words) < 2:
       prev_words.append(new_word)
       return

    # If it exists, add the word to the list
    # If it doesn't exist, create it
    word_tuple = (prev_words[0], prev_words[1])
    if word_tuple in trigrams:
        trigrams[word_tuple].append(new_word)
    else:
        trigrams[word_tuple] = [new_word]

    # Increment the prev words
    prev_words.pop(0)
    prev_words.append(new_word)

def break_it_down(line):
    """Separates 'line' by spaces, similar to the built-in 'split' function.
    However, it also treats punctuation as separate words.
    """
    # Make a copy for us to play with
    words = str(line)
    # Strategy: Leverage the built-in split, by adding spaces
    # around punctuation
    # Supported punctuation: ; : , ? ! . "
    for p in (':', ';', ',', '?', '!', '.', '"'):
        words = words.replace(p, ' {p} '.format(p=p))
    
    # Special case: ellipsis
    while '.   .' in words:
        words = words.replace('.   .', '..')
        
    # Remove this punctuation: ( )
    for p in ('(', ')'):
        words = words.replace(p, ' ')
    
    return words.split()

def read_in_book():
    """Reads in a book and creates the trigrams"""
    # Keep track of paragraphs
    new_lines = False
    with open(book_filename, 'r') as book:
        # Ignore the top of the file, it's all boilerplate
        # 'project gutenberg' stuff anyway
        line_it = iter(book)
        line = next(line_it)
        while line[:3] != "***":
            line = next(line_it)

        line = next(line_it)

        # Read the rest, creating trigrams, until
        # another series of *** are found
        while line[:3] != "***":
            words = break_it_down(line)
            if len(words) == 0:
                new_lines = True
            else:
                if new_lines:
                    add_word_to_trigram('\n\n')
                new_lines = False
                
            for w in words:
                add_word_to_trigram(w)

            line = next(line_it)
    
            
def add_word_to_sentence(sentence, word, dialog=False):
    """Add 'word' to the sentence. 'word' could be punctuation, treat
    it accordingly
    """
    # In general, add a space before adding this word
    # In some instances, do not add a space:
    # * word is: . , ; : ! ?
    # * word is an ellipsis
    # * If the previous word was: \n\n
    
    skip_space = ((word in ('.', ',', ':', ';', '!', '?'))
        or (word == '.' * len(word))
        or (len(sentence) > 0 and sentence[-1] in ('\n\n'))
        or (len(sentence) == 0)
        or (word == '"' and dialog)
        or (dialog and sentence[-1] == '"'))
    
    if skip_space:
        sentence.append(word)
    else:
        sentence.append(' ')
        sentence.append(word)
    

def sentence_from(word_tuple):
    """Return a generated sentence as a list, given the starting tuple"""
    sentence = list()

    sentence_endings = ('.', '?', '!')
    
    # Try to match quotes...
    dialog = False
    
    # Add the beginning of the sentence
    for w in word_tuple:
        add_word_to_sentence(sentence, w, dialog)
        if w == '"':
            dialog = not dialog
        
    # Special case: 1 word sentence (eg: No!)
    if word_tuple[1] in sentence_endings:
        return sentence
    
    value = random.choice(trigrams[word_tuple])
    
    # Now the fun part: keep getting more trigrams until
    # finding the end of the sentence
    while value not in sentence_endings:

        add_word_to_sentence(sentence, value, dialog)
        if value == '"':
            dialog = not dialog
        
        # Advance the tuple
        word_tuple = (word_tuple[1], value)
        
        # Get the next value.
        if dialog:
            #  If it's dialog, try to end it!
            if '"' in trigrams[word_tuple] and random.random() < 0.25:
                value = '"'
            else:
                value = random.choice(trigrams[word_tuple])
        else:
            value = random.choice(trigrams[word_tuple])
    
    # Add the punctuation
    sentence.append(value)
    
    # If this is dialog, then end it. Dialog can always be closed after
    # a sentence ending
    if dialog:
        sentence.append('"')
    
    return sentence

    
def write_sentences(num_sentences):
    """Generates num_sentences number of sentences."""
    sentence_count = 0
    sentences = list()
    
    # Get a starting point
    word_tuple = random.choice(list(trigrams.keys()))
    value = random.choice(trigrams[word_tuple])

    # Find a trigram that'll start a sentence by finding '\n\n'
    while word_tuple[0] != '\n\n':
        word_tuple = random.choice(list(trigrams.keys()))
        value = random.choice(trigrams[word_tuple])
    # Advance to the start of the sentence (i.e., eat the '\n\n')
    word_tuple = (word_tuple[1], value)
    value = random.choice(trigrams[word_tuple])
    
    # Add on to the sentences until we reach the desired number
    while sentence_count < num_sentences:

        cur_sentence = sentence_from(word_tuple)
        # Get the last 2 words for the next trigram
        word_tuple = (cur_sentence[-2], cur_sentence[-1])
        
        # Add the sentence, and then a space
        sentences.extend(cur_sentence)
        sentences.append(' ')
        
        # Find the start of the next sentence
        # Advance tuple to the next one
        value = random.choice(trigrams[word_tuple])
        word_tuple = (word_tuple[1], value)
        
        # Advance again. \n\n is not allowed here!
        value = random.choice(trigrams[word_tuple])
        while value == '\n\n':
            value = random.choice(trigrams[word_tuple])
        word_tuple = (word_tuple[1], value)
            
        sentence_count += 1

    print(''.join(sentences))

if __name__ == "__main__":
    read_in_book()
    write_sentences(15)

    