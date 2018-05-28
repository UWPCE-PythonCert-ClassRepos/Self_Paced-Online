import random


def read_file(filename):
    with open(filename, 'r+') as f:
        data = f.read().replace('\n', ' ').replace('.', '').replace('--', ' ')
        return data.split()


def word_library(list_story):
    #  Adds new words to current list from the story
    list_punctutation = [',', '.', ';', "'", '"', '--']
    my_word_dict = {}
    for i in range(len(list_story)-2):
        two_adj_words = list_story[i] + ' ' + list_story[i+1]
        if list_story[i+2] not in list_punctutation:
            third_word = list_story[i+2]
            my_word_dict.setdefault(two_adj_words, []).append(third_word)
    return my_word_dict


def generate_story(sample_story, word_dict):
    # Generate a story based on the trigram dictionary
    rand_start = int(random.random()*len(word_dict))  # random starting point
    story = ''
    for i in range(len(sample_story)-2):
        try:
            if sample_story[i] + ' ' + sample_story[i+1] in word_dict.keys():
                # print(sample_story[i] + ' ' + sample_story[i+1])
                if i == 0:
                    story += sample_story[i] + ' ' + sample_story[i+1] + ' ' + word_dict[sample_story[i] + ' ' +
                                                                                         sample_story[i+1]][0] + ' '
                    try:
                        word_dict[sample_story[i] + ' ' + sample_story[i+1]].remove(word_dict[sample_story[i] + ' ' +
                                                                                              sample_story[i+1]][0])
                    except KeyError:
                        print("{} is not in the list".format(word_dict[sample_story[i] + ' ' + sample_story[i+1]]))
                else:
                    story += word_dict[sample_story[i] + ' ' + sample_story[i+1]][0] + ' '
                    try:
                        word_dict[sample_story[i] + ' ' + sample_story[i+1]].remove(word_dict[sample_story[i] + ' ' +
                                                                                              sample_story[i+1]][0])
                    except KeyError:
                        print("{} is not in the list".format(word_dict[sample_story[i] + ' ' + sample_story[i + 1]]))
        except IndexError:
            pass
    return story


if __name__ == '__main__':
    filename = 'sherlock_small.txt'
    file_test = 'sherlock_small.txt'
    list_story = read_file(filename)
    list_story_test = read_file(file_test)
    word_lib = word_library(list_story)
    story = generate_story(list_story_test, word_lib)
    print(story)
