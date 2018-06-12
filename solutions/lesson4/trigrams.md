# Trigrams Help

Problem can be broken down into 4 main parts:

1. read file text into a list of words
2. break down words into trigrams, end result is two word dict key with a list of associated words that follow the key words
3. new text from trigrams
4. write new text to file

#1 and #4 are simple enough and don't need explanation.

### Break down of #2:

Given a string: `I wish I may I wish I might`<br>
Grab the first two words and use that as a key, then associate third word with the key:<br>
"I wish": => I<br>
Move to next word (second word) and do the same:<br>
`"wish I": => may`<br>
next:<br>
`"I may": => I`<br>
next:<br>
`"may I": => wish`<br>
now because we already had "I wish" associated we will add to existing:<br>
`"I wish": => I, I`<br>
next, add to existing:<br>
`"wish I": => may, might`<br>
and here we stop, note that we stop at last 3 words. (first word of the key is end - 2)<br>


implementation hints:

* you should have a loop over the words
* your loop should stop at end - 2
* while you loop you should be creating a look up data structure with a key that contains current word + next word which maps to values that can follow that pair



### Break down for #3:

Next step is to pick a random word pair (key) from above as a starting point.<br>
Let's pick "wish I".<br>
the words that follow it are "may" and "might", pick random one -> may; so far new text is:<br>
`"wish I may"`<br>
now pick two last words from our new text -> "I may" and use that as a key for next look up:<br>
`"I may"` maps to I, so new text is:<br>
`"wish I may I"`<br>

and so worth..

implementation hints:
* you should have a loop where you continue grabbing a word pair based on the last two words in your new text (note that your first pair is a random selection
* your loop should stop when you can no longer find a matching pair based on the last two words of the new text
