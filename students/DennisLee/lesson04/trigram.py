#!/usr/bin/env python3

import os

def build_text_databases(source_file):
    """
    Create a database for processing using the original text within a
    file.

    :source_file:  The source file of prose text to process into the
                   database.

    :return:  A dictionary of word pairs and sentence starters.
    """
    print("\n\nCreating text databases...")

    # Data structures, which will be compiled into a giant dict
    word_pairs = {}  # dict: key=2 consecutive words, value=following word
    sentence_starters = list()  # list: 2 words that can begin a paragraph

    with open(source_file, 'r') as f:
        # Build the paragraph list
        pg, paragraphs = '', []
        for line in f:
            if line.strip() != '':
                pg += line.strip() + ' '
                continue
            paragraphs.append(pg.strip())
            pg = ''
        
        # If final line contains text, add the last paragraph manually
        if pg != '':
            paragraphs.append(pg.strip())

    # Creating a temp paragraph file for debugging - can comment out
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
                
    # Isolate keys that can function as sentence starters
    for k in word_pairs:
        if k[0] == k[0].upper():
            sentence_starters.append(k)

    # Creating a temp word pair file for debugging - can comment out
    with open('_word_pairs.txt', 'w') as f:
        for k, v in word_pairs.items():
            f.write(f'Key: {k:30s}  Value: {v}\n')

    # Creating a temp sentence starter file for debugging - can comment out
    with open('_sentence_starters.txt', 'w') as f:
        for k in sentence_starters:
            f.write(k + '\n')

    return {'wp': word_pairs,
            'ss': sentence_starters}

def build_new_story(source_file, counter = 50):
    """
    Create a random story based on two-word keys and the possible words
    that follow the keys. Although the process of adding sentences to
    the story may sometimes fail, eventually a full story will be built.

    :source_file:  The file containing the original story text.

    :counter:  A miscellaneous number for randomizing the output text.

    :return:  The output text string, containing at least 200 words.
    """
    print('\n\nBuilding the story...')
    if type(counter) != int:
        counter = 50  # Randomizer - any number will do
    db = build_text_databases(source_file)  # Build text processing db
    text = []  # The story text (one list entry for every word)

    # Add new sentences until the text length is at least 200 words
    while len(text) < 200:
        new_sentence = create_sentence(db, counter)
        counter += 1
        if new_sentence != None:
            text.extend(new_sentence)

    return ' '.join(text)

def create_sentence(db, counter):
    """
    Build a sentence to add to the story. Note that the sentence
    building may fail on occasion (even frequently).

    :db:  The database of word pair keys to subsequent word values, and
          two-word sentence starters.

    :counter:  A miscellaneous number for randomizing the output text.

    :return:  The output sentence text, as a list of words. If there is
              an error, **None** is returned.
    """
    result = None
    sentence_starters, word_pairs = db['ss'], db['wp']
    quote_opened, begin_sentence, err = False, True, False
    words, next_word, text = 0, '', []

    while True:
        if begin_sentence:  # Randomly get the first 2 words in the sentence
            begin_sentence = False
            two_words = sentence_starters[counter % len(sentence_starters)]
            text.extend(unpair_words(two_words))
            words += 2
            print(f"\n\nAdding new sentence: {two_words:s}")

            # Get the text quotation state after the initial two words
            quote_opened = quote_state(quote_opened, text[0])
            quote_opened = quote_state(quote_opened, text[1])
        else:  # Continue sentence by forming the next two-word key
            two_words = get_next_key(two_words, next_word)

        # Get a word to complete the trigram
        next_word = pick_from_choices(word_pairs[two_words], quote_opened)
        if next_word == None:
            err = True
        else:  # Add the next word to the list if there's no error
            text.append(next_word)
            words += 1
            print(f"Adding sentence word {words:d}: {next_word:s}")
            quote_opened = quote_state(quote_opened, next_word)

            # Consider a long quotation as a single sentence
            if quote_opened == True:  
                continue
            # Exit if there's a bad quotation state or a never-ending sentence
            elif quote_opened == None or words > 1000:
                err = True
            # Check punctuation for the sentence ending
            elif next_word[-1] in '!"\'?.:':
                result = text
                break
        
        if err:  # Discard sentence if there's a problem
            input("ERROR - BACKTRACKING - PRESS ENTER TO CONTINUE:")
            return
            
    return result
    
def pick_from_choices(word_choices, quote_opened):
    """
    Choose an appropriate word to add to the story, based on a specified
    set of choices and the quotation state of the existing text. The
    function prioritizes the choice in hopes of having a closed
    quotation state after the word is chosen.

    :word_choices:  The set of word choices for a given two-word key.

    :quote_opened:  Whether the existing text is currently inside an
                    open quotation (**True**), outside of an open
                    quotation (**False**), or has an invalid quotation
                    state (**None**).

    :return:  The chosen word. If no appropriate word can be selected,
              **None** is returned.
    """
    filtered_choices, result = [], None

    # Word categories based on if a quotation mark precedes and/or succeeds it
    # The first value in the tuple key indicates whether there's a quotation
    # mark before the word. The second value indicates whether a quotation mark
    # follows the word.
    d = { 
            (False, False): 'none',
            (True, False): 'open',
            (False, True): 'close',
            (True, True): 'both'
    }

    # Create dict of available words based on those categories
    categorized = {val: set() for val in d.values()}

    # Fill in the word choices dict
    if word_choices is not None:
        word_choices = list(word_choices)  # Change set into an iterable list
        for word in word_choices:
            word_quotes = (start_quote(word), end_quote(word))
            if word_quotes in d:
                categorized[d[word_quotes]].add(word)

    # Define the groups of words that can be chosen based on the previous
    # text's quotation state (from most preferred to least preferred)
    q = {True: ['close', 'none'], False: ['none', 'both', 'open']}

    if quote_opened != None:
        # Add the words to the filtered choice list
        for i in q[quote_opened]:  
            filtered_choices.extend(categorized[i])

        # Pick the first item in the list. (If we ever need to do a more
        # sophisticated selection, the filtered list is still available here)    
        if len(filtered_choices) > 0:
            result = filtered_choices[0]

    return result

def pair_words(word1, word2):
    """
    Create a string containing the specified two consecutive words.

    :word1:  The first word.
    
    :word2:  The second word.

    :return:  The combined words, as a single string.
    """
    return f'{word1:s} {word2:s}'

def unpair_words(key):
    """
    Split a string of two words into a sequence of two strings (each
    containing one word).

    :key:  The two-word single string.

    :return:  A list of two words.
    """
    result = None
    words = key.split(' ')
    if len(words) == 2:
        result = words
    return result

def get_next_key(previous_key, next_word):
    """
    Get the next two-word key based off the previous two-word key and
    its follow-up word.

    :previous_key:  The previous two-word key string.

    :next_word:  The word that follows the two-word key in the original
                 text.

    :return:  A two-word key string beginning with the second word of
              the previous string and the following word. If there is
              a problem, **None** is returned.
    """
    result = None
    words = unpair_words(previous_key)
    if words != None and len(next_word.split(' ')) == 1:
        result = pair_words(words[1], next_word)
    return result

def quote_state(previous_state, word):
    """
    Show whether the text currently is in the middle of a quotation that
    needs to be ended.

    :previous_state:  The state of the quotation text (**True** if it
                      needs a closing quotation mark, **False**
                      otherwise) before adding the next word.

    :word:  The next word to be added.

    :return:  The state of the quotation text (**True**/**False**) after
              adding the next word.  It returns **None** if the state is
              not valid (if an open quotation mark follows
              an unended quotation mark, or if a closed quotation mark
              is the first quotation mark or follows another closed
              quotation mark).
    """
    # Code is verbose here because of confusing multi-case boolean logic
    new_state = None
    if word[1:-1].count('"') > 0:  
        pass  # Disqualify interior quotation marks
    elif previous_state == True:
        if start_quote(word):  
            pass  # Quotation mark can't precede next word if prev state==True
        else:
            new_state = not end_quote(word)
    elif previous_state == False:
        if not start_quote(word) and end_quote(word):
            pass  # If prev state==False, quot marks can't only follow word
        else:
            new_state = start_quote(word) and not end_quote(word)
    elif previous_state == None:
        pass  # If prev state was already invalid, reflect that
    return new_state

def start_quote(str):
    """
    Show whether the current string begins with an opening quotation
    mark.

    :str:  The specified string.

    :return:  **True** if the current string starts with a `"`;
              **False** otherwise.
    """
    return str[0] == '"'

def end_quote(str):
    """
    Show whether the current string ends with a closing quotation mark.

    :str:  The specified string.

    :return:  **True** if the current string ends with a `"`; **False**
              otherwise.
    """
    return str[-1] == '"'


if __name__ == '__main__':
    options = {
            '1': 'Quit', 
            '2': 'Enter source text filename', 
            '3': 'Enter number for random text seeding'
    }
    counter = 50  # Initial random number

    while True:
        # Print menu
        print('\n\n')
        for k, v in options.items():  
            print(k, v)
        
        ui = input("\nType a menu number: ")
        if ui == '1':  # Quit
            print("\n\nGoodbye!")
            break
        elif ui == '2':  # Run the mutator with the specified filename
            print(f'\n\nCurrent directory is {os.getcwd():s}')
            file_name = input(
                    '\n\nType the name of the file to mutate using trigrams: '
                    ).strip()
            print('\n\n', build_new_story(file_name, counter))
        elif ui == '3':  # Change the seed number without running the mutator
            num = input('Type a random number to seed mutated text: ').strip()
            if num.isdigit():
                counter = int(num)
                print(f'\n\nSeed number is now {counter:d}')

            else:
                print(f'\n\nInvalid entry - seed number remains {counter:d}')
        
