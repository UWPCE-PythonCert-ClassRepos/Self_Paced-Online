import random
import re
import textwrap


def get_file_text(filename):
    with open(filename, 'r') as f:
        text = f.read()
        f.close()
        return text


def text_to_list(text):
    formatted_text = re.sub(r"[\r\n]", ' ', text)
    string_list = formatted_text.split(" ")
    for index, word in enumerate(string_list):
        string_list[index] = re.sub(r"[^\w,\-!.?']|[+--]", "", word)
    string_list = [x for x in string_list if x]
    return string_list


def list_to_trigram(input_list):
    trigram = {}
    while len(input_list) >= 3:
        key1 = input_list[-3]
        key2 = input_list[-2]
        value = input_list.pop(-1)
        trigram.setdefault((key1, key2), []).append(value)
    return trigram


def get_random(trigram):
    return random.choice(list(trigram.keys()))


def generate_text(trigram, num_words):
    word_list = list(get_random(trigram))
    while len(word_list) < num_words:
        if (word_list[-2], word_list[-1]) in trigram:
            potential_words = trigram[(word_list[-2], word_list[-1])]
            word_list.append(potential_words[
                random.randint(0, len(potential_words) - 1)])
        else:
            rand_key = get_random(trigram)
            word_list.append(rand_key[0])
            word_list.append(rand_key[1])
    word_list = word_list[:num_words]
    return ' '.join(word_list)


if __name__ == "__main__":
    get_filename = input("Enter the name of a text file to generate text from trigrams: ")
    get_number = input("Enter the number of words to generate: ")
    file_text = get_file_text(get_filename)
    str_list = text_to_list(file_text)
    trigram = list_to_trigram(str_list)
    cleanup = generate_text(trigram, int(get_number))
    print(write_text('sherlock.txt', cleanup))