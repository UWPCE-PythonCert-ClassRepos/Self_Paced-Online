import random

def main():
    while True:
        read_file()
        #build_dictionary()
        #create_new()

def read_file(file="sherlock.txt"):
    punctuation = [".",",",";","'","!","@","#","$","%","^","&","*","(",")","_","=","+"]
    raw_words = []
    with open(file,"r") as f:
        for symbols in punctuation:
            raw_words = f.read().replace(symbols,'')
        raw_words.lower().split()
    with open('test.txt','w') as f:
        f.write(raw_words)


#def build_dictionary():

#def create_new():








if __name__ == '__main__':
    main()