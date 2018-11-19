#!/usr/bin/env python3

from random import randint
# Global dictionary for trigram generation
tri_d = {}


def process_line(line_im1, line_i=''):
    """Append the words in line_im1 to the global dictionary tri_d.
    
    :param line_im1: A line of the trigram input file preceding line_i
    :param line_i: A line of the trigram input file
    """
    
    # Assume there are no newline characters in the input strings,
    # separate the input string line_im1 into words
    # (technically sequences of characters separated by white
    # spaces e.g. #this_couldbe!a-word)
    wordl_im1 = line_im1.split()
    
    # Ignore this line if line_im1 only contains one word
    if len(wordl_im1) == 1: return
    
    if len(wordl_im1) >= 3:
        for w1, w2, w3 in zip(wordl_im1[:-2], wordl_im1[1:-1], wordl_im1[2:]):
            
            key_i = "{} {}".format(w1,w2)
            if key_i not in tri_d:
                tri_d[key_i] = [w3]
            else:
                tri_d[key_i].append(w3)
    
    # If there is a line after line_im1, add the last two words of line_im1 
    # into the dictionary as keys
    if len(line_i) > 0:
        
        wordl_i = line_i.split()
        
        # There is at least one word on line_i
        key_i = "{} {}".format(*wordl_im1[-2:])
        if key_i not in tri_d:
            tri_d[key_i] = [wordl_i[0]]
        else:
            tri_d[key_i].append(wordl_i[0])
        
        # If there are at least two words on line_i
        if len(wordl_i) > 1:
            
            key_i = "{} {}".format(wordl_im1[-1],wordl_i[0])
            if key_i not in tri_d:
                tri_d[key_i] = [wordl_i[1]]
            else:
                tri_d[key_i].append(wordl_i[1])
        

def read_book(fname_in):
    """Read the contents of the text file with name fname_in into the global
    dictionary tri_d by calling the helper function process_line on each line.
    
    :param fname_in:
    """
    
    # Read input text file into global trigram dictionary
    with open(fname_in,'r') as infile:
        
        line_im1 = infile.readline()
        line_i = infile.readline()
        
        # Loop through two lines at a time so you can add the first word
        # from the next line to the dictionary
        while line_i:
            
            # if line_i is a blank line get the next line
            # that is not a new line
            if line_i.find('\n') == 0:
                line_i = infile.readline() 
                continue
            
            # remove new line character from current line
            line_im1 = line_im1.replace('\n','')
            line_i = line_i.replace('\n','')
            process_line(line_im1, line_i)
            
            # increment the lines
            line_im1 = line_i
            line_i = infile.readline()
            
        if len(line_im1) > 0:
            process_line(line_im1)
    
    
def generate_trigram(filename_out, word_limit):
    """Generate trigram text and write it to the file filename_out
    
    :param filename_out: name of trigram output file
    :param word_limit: maximum number of words. If the word_limit is reached
                        and the output doesn't end in a period, it will
                        continue to search for a period until 1.5 * word_limit
                        is reached.
    """
    
    absolute_wordlim = 1.5 * word_limit
    
    # Capitalization, and end with period
    with open(filename_out,'w') as outfile:
    
        # Generate output one line at a time, line wrap after 79 characters
        max_nchars = 79 # maximum number of characters per line
        
        # Get a random starting phrase from the dictionary to start generating
        # output
        tri_d_keys = list(tri_d.keys())
        start_ind = randint(0, len(tri_d_keys) - 1)
        seed_phrase = tri_d_keys[start_ind]
        
        # Keep words in a list and keep track of the number of characters in all of
        # the words. Write all the words in the list to the file when the number of
        # characters exceeds 79
        
        line_i = seed_phrase.capitalize().split()
        if seed_phrase in tri_d:
            # newword_list is a list of words that have "seed_phrase" as a key
            newword_list = tri_d[seed_phrase]
            # randomly select one of these words and add it to the line
            line_i.append(newword_list[randint(0,len(newword_list) - 1)])
        else:
            line_i.append('')
            
        # number of chars on the current line
        char_count = 0
        for words in line_i: char_count += len(words)
        # total number of words that have been written (should be 3):
        word_count = len(line_i)
        
        # The new is the two previous words
        new_key = ' '.join(line_i[-2:])
        
        while (new_key in tri_d) and (word_count < word_limit):
            
            # get list value for the given key
            newword_list = tri_d[new_key]
            # the new word is randomly selected from the words in the list
            # if multiple are present
            new_word = newword_list[randint(0, len(newword_list) - 1)]
            last_word = line_i[-1]
            word_count += 1
            
            if char_count + len(new_word) > max_nchars:
                outfile.write(' '.join(line_i))
                outfile.write('\n')
                # reset line_i and char_count
                line_i = [new_word]
                char_count = len(new_word)  
            else:
                line_i.append(new_word)
                char_count += len(new_word)
                
            new_key = ' '.join([last_word, new_word])
                
        # save the current results of line_i
        last_line = line_i.copy()
        
        # If the output doesn't end with a period, continue looking for 
        # more words until a word with a period is found. If the total number of 
        # words exceeds 120 percent of word_limit, just otput the results
        # ignoring this search for a period
        
        # list of word lists for the additional lines 
        lines_after_wordlim =[line_i]
        count = 0
        while (new_key in tri_d) and (line_i[-1][-1] != '.'):
            count += 1
            print(count)
            if word_count > absolute_wordlim: 
                print('broke out')
                break
            
            # get list value for the given key
            newword_list = tri_d[new_key]
            # the new word is randomly selected from the words in the list
            # if multiple are present
            new_word = newword_list[randint(0, len(newword_list) - 1)]
            last_word = lines_after_wordlim[-1][-1]
            word_count += 1
            
            if char_count + len(new_word) > max_nchars:
                lines_after_wordlim.append([new_word])
                char_count = len(new_word)  
            else:
                lines_after_wordlim[-1].append(new_word)
                char_count += len(new_word)
                
            new_key = ' '.join([last_word, new_word])
            
        # The search for a period was unsuccessful, ingore the additional lines and
        # output what the last line would have been before the search
        if line_i[-1][-1] != '.':
            outfile.write(' '.join(last_line))      
        # the search was successful, append the additional lines that end with
        # a period
        else:
            
            for line in lines_after_wordlim:
                outfile.write(' '.join(line))
            return

        
    
if __name__ == "__main__":
    
    fname_in = "sherlock.txt"
    fname_out = "trigram_out.txt"
    n_output_words = 400
    read_book(fname_in)
    generate_trigram(fname_out, n_output_words)
    
    
