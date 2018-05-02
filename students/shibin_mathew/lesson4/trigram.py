
def read_file(filename):
    # with open(path+'/'+filename, 'r+') as f:
    #     data = f.read()
    list_story = []
    f = open(filename, 'r')
    for line in f:
            list_story.append(line.split())
    return list_story


def word_library(list_story, dict_word):
    #  Adds new words to current list from the story
    list_punctutation = [',', '.', ';', "'", '"']
    print(list_story)
    for i in range(0, len(list_story)):
        if i + 1 <= len(list_story) and i + 2 <= len(list_story):
            for word in dict_word:
                # print(list_story[i] + ' ' + list_story[i+1])
                if list_story[i] + ' ' + list_story[i + 1] == word:
                    # if list_story[i + 2] not in list_punctutation:
                        dict_word[word].append(list_story[i + 2])
    return dict_word


if __name__ == '__main__':
    filename = 'sherlock_small.txt'
    dict_wordlist = {'I wish': ['I', 'I'], 'wish I': ['may', 'might'], 'may I': ['wish'], 'I may': ['I'],
                     'it was': ['at'], 'with the': ['cat']}
    list_story = read_file(filename)
    print('Original List')
    print(dict_wordlist)
    print('New List')
    print(word_library(list_story, dict_wordlist))
