import string, random

file = open('sherlock_small.txt', 'r')
file_text = file.read().lower()
file.close()

translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))

new_file_text = file_text.translate(translator).split()


def trigrams(list):
    trigram_list = []
    for i in range(len(list)-2):
        trigram_list.append(('{} {}'.format(list[i], list[i+1]), list[i+2]))
    return trigram_list


def convert_to_dict(list):
    trigram_dict = dict()
    for i in list:
        if i[0] in trigram_dict:
            trigram_dict[i[0]].append(i[1])
        else:
            trigram_dict[i[0]] = [i[1]]

    return trigram_dict


new_dict = convert_to_dict(trigrams(new_file_text))
new_book = list()
random_key = random.choice(list(new_dict))
random_key_split = random_key.split()
new_book.append(random_key_split[0])
new_book.append(random_key_split[1])

count = 0
while random_key in new_dict and count < 100:
    random_key_split = random_key.split()
    random_value = random.choice(new_dict[random_key])
    new_book.append(random_value)

    random_key = random_key_split[1] + " " + random_value

    count += 1

print(' '.join(new_book[0:]))

