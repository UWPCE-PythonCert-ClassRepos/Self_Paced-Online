
import sys
import random, os


def build_trigrams(words):
    '''
    build up the trigrams dict from the list of words
    returns a dict with:
       keys: word pairs
       values: list of followers
    '''
    
    trigrams = {}

    for i in range(len(words)-2): 
        pair = tuple(words[i:i + 2]) #make trigrams key as tuple
        follower = words[i + 2] #make value as list

        trigrams.setdefault(pair,[]).append(follower) #create key with value if key not already exist

    return trigrams

def make_words(words):
    
    return words.split(" ")

def build_text(word_pairs):

    '''
    build up a new story with the trigram dict
    '''

    story_words = list()
    #randomely select two staring words
    start_key = random.choice(list(word_pairs))
    [story_words.append(item) for item in start_key]
    
    i = 1

    while start_key is not None:
        if start_key in word_pairs: 
            next_words = random.choice(word_pairs[start_key]) #select random following word
            story_words.append(next_words)
            start_key = tuple(story_words[i:i + 2])
            i+=1
        else: #if no key found, break the loop
            break
    return story_words


def read_in_data(file_name):
    with open(file_name, 'r') as f:
        for line in f:
            if 'START OF THIS PROJECT GUTENBERG' in line:   #read the story after this line
                for line in f:
                    if 'END OF THIS PROJECT GUTENBERG' in line:   #stop at this line
                        break
                    else: 
                        read_data = f.read()
                        f.closed

    #some string cleaning
    firstString = "-&*"
    secondString = "   "
    translation = read_data.maketrans(firstString, secondString)

    # translate string
    return read_data.translate(translation)
    #read_data = read_data.replace('-',' ')

if __name__ == "__main__":
    # get the filename from the command line
    try:
        file_name = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    #path = os.getcwd()
    #file_name = path + '\lesson04\sherlock_small.txt'
    #words = "I wish I may I wish I might"

    in_data = read_in_data(file_name)
    
    words = make_words(in_data)
    
    word_pairs = build_trigrams(words)
    
    new_text = build_text(word_pairs)

    #capitalize first word of the new story
    new_text[0] = new_text[0].capitalize()

    print(" ".join(new_text), end='')
    #end new story with period
    print(".")