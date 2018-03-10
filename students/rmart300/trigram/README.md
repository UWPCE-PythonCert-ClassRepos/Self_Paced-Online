Trigram creator made by Ross Martin
2/18/2018
python 210

Reads book and looks at each set of three adjacent words in a document. Uses the first two words of the set as a key, and remember the fact that the third word followed that key. Record the list of individual words that can follow each two word sequence in the book.

Then writes new book by choosing an arbitrary word pair as a starting point. Uses these to look up a random next word and appends this new word to the text so far. This gives a new word pair at the end of the text, and looks up a potential next word based on these. Adds this to the list, and so on

def read_book(book_file):
    """read the book and make trigram dict"""

def write_book():
    """write book in trigram syntax"""

