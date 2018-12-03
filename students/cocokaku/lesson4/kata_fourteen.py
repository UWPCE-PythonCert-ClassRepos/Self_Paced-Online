import random

def main():
    # set file names and initialize sequences
    input_file = "sherlock.txt"
    output_file = input_file[:-4]+"_out.txt"
    words = []
    trigrams = {}
    story_string = ""

    # open input file and read words into words list
    with open(input_file, 'r') as f:
        for line in f:
            for word in line.strip().split():
                words.append(word)

    # process trigrams and save to trigrams dict
    # key = words[i] + ' ' + words[i+1]
    # value = list of existing words[i+1] for a given key
    for i in range(len(words)-2):
        tri = words[i]+' '+words[i+1]
        if tri not in trigrams.keys():
            trigrams[tri] = []
        trigrams[tri].append(words[i+2])

    # start story as random choice of a trigram from trigrams dict
    story = random.choice(list(trigrams.keys())).split()
    i = 0

    # create story based on trigram processing
    # key = story[i] + ' ' + story[i+1]
    # value = random choice from list of possible values => story[i+2]
    while True:
        key = story[i]+' '+story[i+1]
        if key in trigrams.keys():
            story.append(random.choice(trigrams[key]))
            i += 1
        else:
            break

    # convert story list to string
    for word in story:
        story_string += ' '+word
    story_string = story_string.lstrip()

    # save story to output file
    with open(output_file, 'w') as f:
        f.write(story_string)

if __name__ == "__main__":
    main()
