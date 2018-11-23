import random
d = {}
with open('sherlock.txt', 'r') as f:
    for line in f:
        wordlist = line.split()
        for i in range(len(wordlist) - 2):
            grab = ' '.join(wordlist[i:(i + 2)])
            if grab in d.keys():
                d[grab].append(wordlist[(i + 2)])
            else:
                d[grab] = [wordlist[(i + 2)]]
for x in range(5):
    starting_point = random.choice(list(d))
    my_string = starting_point + ' ' + d[starting_point][0]
    next_key = ' '.join(my_string.split()[-2:])
    while next_key in d.keys():
        my_string = my_string + ' ' + random.choice(d[next_key])
        next_key = ' '.join(my_string.split()[-2:])
    print(my_string)
    with open('output.txt', 'a') as f2:
        f2.write('\n' + my_string)
f.closed
f2.closed
