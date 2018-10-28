import random


def word_list(file_name):
    """Read file into a list of words"""
    with open(file_name, "r") as file:
        my_list = file.read().split()
        return my_list
        my_list = file.read().split()
        return my_list


def trigrams(my_list): 
    """break down words into dictionary of trigrams"""
    d ={}
    for index, word in enumerate(my_list[0:-2]):
        k = f"{my_list[index]} {my_list[index+1]}"
        v =  my_list[index +2]
        if k in d:
            d[k] = [d[k], v]
        else:
            d[f"{my_list[index]} {my_list[index+1]}"] = my_list[index + 2]
    return d


def random_pair(my_dict):
    """pick a random word pair from dictionary as a start point"""
    words = []
    random_key = random.choice(list(my_dict.keys()))
    if type(my_dict[random_key]) is str:
        random_value = my_dict[random_key]
    else:
        random_value = random.choice(my_dict[random_key])
    words.append(random_key)
    words.append(random_value)
    next_key = []
    next_key = words[0].split()[-1]
    next_v = words[1].split()[-1]
    return [next_key, next_v]


def make_kata(my_dict):
    """Loop over trigram (dict) and make a list of words that will be converter to text"""
    new_pair = " ".join(random_pair(my_dict))
    new_ls = [new_pair]
    for k, v in my_dict.items():
        if new_pair in k:
            new_key = k.split()[-1]
            if type(v) is list:
                new_val = v[0]
            else:
                new_val = v.split()[0]
            new_ls.append(new_val)
            new_pair = (f"{new_key} {new_val}")
            
    return new_ls


def kata_to_text(my_dict):
    """Convert our list of words from make_kata func into text"""
    text = " ".join(make_kata(my_dict)) + "."
    return text.capitalize() 


def write_to_disk(text, filename):
    """Write text to disk"""
    with open(filename, "w") as f:
        f.write(text)


if __name__ == "__main__":
    new_list = word_list("sherlock_small.txt")
    new_dict = trigrams(new_list)
    new_text = kata_to_text(new_dict)
    write_to_disk(new_text, "new_text.txt")

