import sys, random, re

trigram_dict={}

def read_book(book_file):
    """read the book and make trigram dict"""
    with open(book_file, 'r') as book:
        digram = ''
        for line in book:
            #need to remove punctuation from words
            punc = "\W"
            line = re.sub(punc, ' ', line.strip())
            words = line.split()

            for i in range(len(words)):
                if i > 1:
                    digram = f"{words[i-1]} {words[i]}"
                if i < len(words)-1:
                    if digram in trigram_dict:
                        trigram_dict[digram].append(words[i+1])
                    else:
                        trigram_dict[digram] = [words[i+1]]

def write_book():
    """write book in trigram syntax"""
    trigram_usage_dict = {}
    for digram in trigram_dict:
        trigram_usage_dict[digram] = 0
    
    out = open('my_book.txt','w')
    max_length = 200
    cur_length = 0
    while cur_length < max_length:
        digram = random.choice(list(trigram_dict.keys()))
        print('outer loop: ' + digram)
        cur_length += 2

        while digram in trigram_dict and cur_length < max_length:
            out.write(digram + ' ')
            print('writing digram\ninner loop: ' + digram)
            num_words_used = trigram_usage_dict[digram]
            word_list = trigram_dict[digram]
            
            print("{} {}".format(num_words_used,len(word_list)))
            if num_words_used < len(word_list):
                third_word = word_list[num_words_used]
                trigram_usage_dict[digram] = num_words_used + 1
                out.write(third_word + ' ')
                print('writing third word: ' + third_word)
                cur_length += 1
            else:
                break

            if len(digram.split()) > 0:
                digram = digram.split()[1] + ' ' + third_word
                print('end of loop ' + digram)
            

        out.write('.')   


if __name__ == '__main__':
   
    book_file = sys.argv[1]
    read_book(book_file)   
    #print(trigram_dict)
    write_book() 
