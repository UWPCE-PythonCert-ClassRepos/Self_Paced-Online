#!/usr/bin/env python3
import random
# trigram based on sherlock short text file
# trigram based on short string of words to begin with
#words = "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen Twenty".split()
#words = "One night--it was on the twentieth of March, 1888--I was returning from a journey to a patient (for I had now returned to civil practice), when my way led me through Baker Street. As I passed the well-remembered door, which must always be associated in my mind with my wooing, and with the dark incidents of the Study in Scarlet, I was seized with a keen desire to see Holmes again, and to know how he was employing his extraordinary powers. His rooms were brilliantly lit, and, even as I looked up, I saw his tall, spare figure pass twice in a dark silhouette against the blind. He was pacing the room swiftly, eagerly, with his head sunk upon his chest and his hands clasped behind him. To me, who knew his every mood and habit, his attitude and manner told their own story. He was at work again. He had risen out of his drug-created dreams and was hot upon the scent of some new problem. I rang the bell and was shown up to the chamber which had formerly been in part my own. ".split()
 
def build_trigrams(words):
    """ 
    build up the trigrams dict from the list of words
    
    returns a dict with:
        keys: word pairs
        values: lsit of followers
    """
    trigrams = {}
    # build up the dict here!
    for i in range(len(words)-2):
        pair = (words[i], words[i + 1])
        #print(type(pair))
        #print("pair is: ", pair)
        follower = [words[i + 2]]
        #print("follower is: ", follower)
        if pair not in trigrams:
            # add to dict
            trigrams[pair] = follower
        else:
            trigrams[pair].append(words[i + 2])

    return trigrams


# open file for reading
def read_file():
    with open("sherlock_small.txt", 'r') as f:
        text1 = f.read()
        f.close()
        text1 = text1.replace("\n", ' ')
        text1 = text1.replace("\r", ' ')
        text1 = text1.split()
    return text1

def generate_story(dict1):
    # randomize words to create new story
    random_words = []
    new_word = str()
    print("len of dict1 is: ", len(dict1))
    #print(dict1)
    counter1 = 0
    while counter1 < len(dict1):
        random_key = random.choice(list(dict1))
        new_word = dict1[random_key][0]
        #print("random key is: ", random_key)
        print("new word is: ", new_word)
        print("new word type is: ", type(new_word))
        counter1 += 1
        #random_words = random_words + new_word
        random_words.append(new_word)
    random_words = " ".join(random_words)
        
    return random_words

if __name__ == "__main__":
    words = read_file()
    trigrams = build_trigrams(words)
    #print(trigrams)
    new_story = generate_story(trigrams)
    #print(trigrams)
    print(new_story)


"""    
trigrams = {}

for i in range(len(words)-2):
    pair = (words[i], words[i + 1])
    print(type(pair))
    print("pair is: ", pair)
    follower = [words[i + 2]]
    print("follower is: ", follower)
    if pair not in trigrams:
        # add to dict
        trigrams[pair] = follower
    else:
        trigrams[pair].append(words[i + 2])
        #trigrams[pair] = []
        #trigrams(pair) = [follower]
        #trigrams.append(pair) = [follower]
        #trigrams.append(pair)
#print("")
#print("keys are: ", trigrams.keys())        
print("\n\n")
print("trigram dict is: ", trigrams)
"""





