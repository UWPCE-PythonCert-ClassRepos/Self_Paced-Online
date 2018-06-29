import random

# Load the test story
with open('wish_test.txt', 'r') as infile:
    story = infile.read()

    
# Remove paragraphs
story = story.replace('\n', ' ')

print(story)


# Make story into a list of words
story = story.split(' ')


# Create trigrams
trigrams = {}

for word in range(2, len(story)):
    new_k = (story[word-2], story[word-1])
    new_v = [story[word]]
    
    if trigrams.get(new_k, 'create') == 'create':
        trigrams[new_k] = new_v
    else:
        trigrams[new_k] = trigrams[new_k] + new_v
        
for t in trigrams.items():
    print(t)
    

# Start new story using input from user
word_1 = input('Enter first word of new story: ')
word_2 = input('Enter second word of new story: ')

start = (word_1, word_2)
choices = []
new_story = [word_1, word_2]

while choices != 'No Match':
    find_words = (new_story[-2], new_story[-1])
    
    choices = trigrams.get(find_words, 'No Match')
    
    if choices != 'No Match':
        new_word = random.choice(choices)
        new_story.append(new_word)


new_story_string = ' '.join(new_story)
print(new_story_string)