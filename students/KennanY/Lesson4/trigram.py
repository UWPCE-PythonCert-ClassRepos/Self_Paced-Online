import string

trigramdata={}

def readfile():
    '''Open a file and reads text'''
    with open("sherlock.txt", 'r') as file:
        return (file.read().replace("\n", " ").lower())

def print_trigram():
    '''Prints the trigram on the screen'''
    print('\nSherlock Trigram\n')
    print('[Key] ---------> [Value]\n')
    for key, value in trigramdata.items():
        print('[' + key + '] ---->' + '[' + value +']' )

def create_trigram(wordlist):
    '''Creates a trigram from a list'''
    #First two words become the key, next becomes value
    counter=0
    key=' '
    for each in wordlist:
        counter=counter+1
        if counter%3 ==0:
            trigramdata[key] = each
            key=''
        else:
            key=key.strip() + ' ' + each

def trigram():
    """Creates triagram from text"""

    text=readfile() #Read the text from the file

    #Clean text. Remove punctuation.
    tr = str.maketrans("", "", string.punctuation)
    cleaned_text=text.translate(tr)

    words=cleaned_text.split() #Split into words
    create_trigram(words)  # Create the trigram
    print_trigram()  #Print the structure

if __name__ == "__main__":
    trigram()