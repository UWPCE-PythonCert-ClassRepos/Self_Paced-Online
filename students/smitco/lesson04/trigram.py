#Lesson 04 Kata Fourteen
#!/usr/bin/env python3
#using text file from The Project Gutenberg EBook of The Call of the Wild by Jack London
#creates trigrams from Chapter 1 only

def write_new_book(tri):
    import random
    new_text = ["..."]
    start = (random.choice(list(tri.keys())))
    new_text.append(start[0])
    new_text.append(start[1])
    for i in range(10000):
        nxt = tuple(new_text[-2:])
        if nxt not in tri:
            new_text.append("\n\n Word Count: {}".format(len(new_text)))
            break
        else:
            new_text.append(random.choice(list(tri.get(nxt))))
    with open("New Text by Courtney.txt.", "w", encoding = "utf8") as new_file:
        for word in new_text:
            new_file.write(word)
            new_file.write(" ")
    
def read_book():
    trigrams = {}
    words_in_book = []
    with open("The Call of the Wild.txt", "r", encoding = "utf8") as book:
        lines = book.readlines()
        lines = lines[54:421] #reads only chapter 1, use 3064 for whole book
    for line in lines:
        for word in line.split():
            words_in_book.append(word)
    for n in range(len(words_in_book)-2):
        pair = words_in_book[n], words_in_book[n+1]
        follower = words_in_book[n+2]
        if pair in trigrams and follower not in trigrams[pair]:
            trigrams[pair].append(follower)
        if pair in trigrams and follower in trigrams[pair]:
            pass
        else:
            trigrams[pair] = [follower]
    write_new_book(trigrams)


if __name__ == '__main__':
    read_book()