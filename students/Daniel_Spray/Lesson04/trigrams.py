import random

def main():
    while True:
        raw_words = read_file()
        dictionary = build_dictionary(raw_words)
        create_new_trigram(dictionary)
        break

def read_file(file='sherlock.txt'):
    punctuation = [".",",",";",'"',"!","@","#","$","%","^","&","*","(",")","_","=","+","-","`","~","<",">","?",":","{","}","[","]","\\","|","/"]
    with open(file,"r") as f:
        raw_text = f.read().lower()
        for symbol in punctuation:
            raw_text = raw_text.replace(symbol,'')
    raw_words=raw_text.split()
    for word in raw_words:
        if word == 'i':
            raw_words[raw_words.index("i")]="I"
    return raw_words

def build_dictionary(raw_words):
    dictionary = {}
    for index in range (len(raw_words)-2):
        dictionary.setdefault(raw_words[index]+' '+raw_words[index+1],[]).append(raw_words[index+2])
    return dictionary

def create_new_trigram(dictionary):
    trigram_list = []
    for trigram_length in range(random.randint(1,7)):
        trigram_list.append(paragraph(dictionary))
    trigram_string = """
	
""".join(trigram_list)
    with open("Trigram.txt",'w') as f:
        f.write(trigram_string)
    print(trigram_string)

def sentence(dictionary):
    first_word=random.choice(list(dictionary))
    sentence_list = []
    sentence_list.append(first_word)
    for index in range(random.randint(3,10)):
        key = sentence_list[index-1]+' '+sentence_list[index]
        try:
            len(dictionary[key])<2
        except KeyError:
            next_word = random.choice(list(dictionary))
        else:
            next_word = random.choice(dictionary[key])
        sentence_list.append(next_word)
    sentence_string=" ".join(sentence_list)
    final_string = sentence_string[0].upper()+sentence_string[1:]+"."
    return final_string

def paragraph(dictionary):
    paragraph_list = []
    for quantity in range(random.randint(3,5)):
        paragraph_list.append(sentence(dictionary))
    paragraph_string=" ".join(paragraph_list)
    return paragraph_string

if __name__ == '__main__':
    main()