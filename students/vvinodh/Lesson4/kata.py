import random
tridict = {}
list1 = []


def process_file():
    with open('sherlock_small.txt', 'r') as fileobj:
        read_data = fileobj.read()
        words = read_data.replace('\n', ' ').replace('!', ' ').replace("'", ' ')\
            .replace(',', ' ').replace('.', ' ').replace('  ', ' ').split(' ')
        for word in words:
            if not word == '':
                list1.append(word)
    for x, y in enumerate(list1):
        if x < len(list1) - 3:
            one = y
            two = list1[x + 1]
            key = (one, two)
            if key not in tridict:
                tridict[key] = [list1[x + 2]]
            else:
                tridict[key].append(list1[x + 2])
    print(tridict)

if __name__ == '__main__':
    process_file()
