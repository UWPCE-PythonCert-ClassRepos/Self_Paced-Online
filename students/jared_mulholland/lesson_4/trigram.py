"""
Trigram analysis is very simple. Look at each set of three adjacent words in a document. Use the first two words of the set as a key, and remember the fact that the third word followed that key. Once you’ve finished, you know the list of individual words that can follow each two word sequence in the document. For example, given the input:
I wish I may I wish I might
You might generate:
"I wish" => ["I", "I"]
"wish I" => ["may", "might"]
"may I"  => ["wish"]
"I may"  => ["I"]
This says that the words “I wish” are twice followed by the word “I”, the words “wish I” are followed once by “may” and once by “might” and so on.
To generate new text from this analysis, choose an arbitrary word pair as a starting point. Use these to look up a random next word (using the table above) and append this new word to the text so far. This now gives you a new word pair at the end of the text, so look up a potential next word based on these. Add this to the list, and so on. In the previous example, we could start with “I may”. The only possible next word is “I”, so now we have:
I may I
The last two words are “may I”, so the next word is “wish”. We then look up “I wish”, and find our choice is constrained to another “I”.:
I may I wish I
Now we look up “wish I”, and find we have a choice. Let’s choose “may”:
I may I wish I may
Now we’re back where we started from, with “I may.” Following the same sequence, but choosing “might” this time, we get:
I may I wish I may I wish I might
It this point we stop, as no sequence starts “I might.
"""
import random

tg_dict = {"I wish": ["I","I"],"wish I": ["may","might"],"may I": ["wish"], "I may": ["I"]}

#set up initial 
new_key = random.choice(list(tg_dict.keys()))
trigram = new_key

while new_key in tg_dict:    
    trigram = trigram + " " + tg_dict[new_key][random.randint(0,len(tg_dict[new_key])-1)]
    new_key = " ".join(trigram.split()[-2:])
    

