from random import randint

# Global dictionary for trigram generation
tri_d = {}


def process_line(line_im1, line_i=''):
    
    # Assume there are no newline characters in the input strings
    # separate the input string line_im1 into words
    # (technically sequences of characters separated by white
    # spaces e.g. #this_couldbe!a-word)
    wordl_im1 = line_im1.split()
    # ?? Add logic to make punctuation it's own word? ??
    
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
    
    # Read input text file into global trigram dictionary
    with open(fname_in,'r') as infile:
        
        line_im1 = infile.readline()
        line_i = infile.readline()
        
        # Loop through two lines at a time so you can add the first word
        # from the next line
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
            
            line_im1 = line_i
            line_i = infile.readline()
            
        if len(line_im1) > 0:
            process_line(line_im1)
    
    
def generate_trigram(filename_out, word_limit):
    # Capitalization, and end with period
    with open(filename_out,'w') as outfile:
    
        # Generate output one line at a time, line wrap after 79 characters
        max_nchars = 79 # maximum number of characters per line
        
        tri_d_keys = list(tri_d.keys())
        start_ind = randint(0, len(tri_d_keys) - 1)
        # Get a random starting phrase
        seed_phrase = tri_d_keys[start_ind]
        
        # Keep words in a list and keep track of the number of characters in all of
        # the words. Write all the words in the list to the file when the number of
        # characters exceeds 79
        line_i = seed_phrase.capitalize().split()
        if seed_phrase in tri_d:
            newword_list = tri_d[seed_phrase]
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
                
        # print contents of line_i
        outfile.write(' '.join(line_i))
    

if __name__ == "__main__":
    
    fname_in = "sherlock_small.txt"
    fname_out = "trigram_out.txt"
    read_book(fname_in)
    generate_trigram(fname_out,100)
    
    
