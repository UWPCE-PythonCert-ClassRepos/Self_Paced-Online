
trigram_dict={}

def read_book(book_file):

    book = open(book_file, 'r'):
    digram = ''
    for line in book:
        line.strip()
        words = line.split()
        for i in range(len(words)):
            if i > 1:
                digram = f"{words[i-1]} {words[i]}"
            if i < len(words)-1:
                if digram in triagram_dict:
                    word_list = trigram_dict[digram]
                    word_list.append(words[i+1])
                    trigram_dict[digram] = wordlist
                else:
                    trigram_dict[digram] = []

def write_book():
    trigram_usage_dict = {}
    for digram in trigram_dict:
        trigram_usage_dict[digram] = 0
    
    out = open('my_book.txt','w')
    max_length = 200
    while cur_length < max_length:
        digram = random.choice(trigram_dict.keys())

        while digram in trigram_dict:
            num_words_used = trigram_usage_dict[digram]
            word_list = trigram_dict[digram]
            third_word = word_list[num_words_used]
            trigram_usage_dict[diagram] = num_words_used + 1
            out.write(digram + ' ' + trigram)

        out.write('.')   


if __name__ == '__main__':
   
    book_file = sys.argv[1]
    read_book(book_file)    
