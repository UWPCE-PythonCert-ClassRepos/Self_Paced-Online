import random  # used further down to select seed values

# making database

def depunc(str):  # purging punctuation from a string
    punct = "?!().;:,"
    for x in str:
        if x in punct:
            str = str.replace(x, "")
    return str


# load data and put words into a list
def texttolist(filename):
    file = open(filename, "r")
    words = []
    for line in file:
        phrase = line.rstrip().replace("--", " ").split()  # splits line of file into a list of strings. carriage return removed
        for x in phrase:
            y = depunc(x)  # removes punctuation
            words.append(y)  # adds string y to list words
    return words


# check if two words are (already) a key in dictionary
def indict(dictin, words):
    tester = False
    for x in dictin:
        if x == words:
            tester = True
    return tester


# main function for creating database
def datamaker(filename):
    record = texttolist(filename)
    wordlot = {}
    for idx, wordone in enumerate(record):
        if idx >= (len(record) - 2):
            break
        keyname = record[idx] + " " + record[idx+1]  # creates key of first 2 words of three word set
        if indict(wordlot, keyname):  # checks if key already in dictiornary
            wordlot[keyname].append(record[idx+2])
        else:
            wordlot[keyname] = [record[idx+2]]
    return wordlot


# making text
# pick a random word pair from dictionary
def pickpair(dictin):
    str = random.choice(list(dictin))  # gets a random keyword out of dictionary by converting dictionary keywords to list first
    return str


# pick random word from keyword's list
def pickword(dictin, keyword):
    str = random.choice(dictin[keyword])  # gets random word from the list that is the value of dictin[keyword]
    return str


def storymaker(dictin):  # main function for generating a new story
    story = []
    while len(story) <= 200:
        keyword = pickpair(dictin)  # randomsly chooses pair of seed words
        hold = keyword.split()  # makes them into a list
        for x in hold:  # adds seed words to story list
            story.append(x)
        hold2 = story[-2] + " " + story [-1]  # makes a string hold2 which will act as a dictionary keyword in the following loop
        while indict(dictin, hold2):
            story.append(pickword(dictin, hold2))  # uses pickword to select a word from dictin[hold2]'s list and add it to story list
            hold2 = story[-2] + " " + story[-1]  # redefines hold2 to be the new last two words
        end = [".", "!", "?"]
        story.append(random.choice(end))  # When the program hits a keyword deadend, it adds punctuation and picks new keywords to start a new sentence
    pretty = " ".join(story)
    return pretty


def kata(filename):  # puts everything together into one function
    record = datamaker(filename)
    story = storymaker(record)
    return story


print(kata("sherlock_small.txt"))
