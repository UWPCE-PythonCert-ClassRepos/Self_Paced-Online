# NEIMA SCHAFI, LESSON 4 Assignment - Trigrams
import random
import re

# Open txt file
f = open('sherlock_small.txt')
text = f.read()
f.close()

# Split up imported txt and put in a list
d2 = re.sub('[^A-Za-z0-9]+', ' ', text)
d2 = d2.split()

# Create dict from imported txt
d = {}
for i in range(len(d2)-2):
    s2 = d2[i] + ' ' + d2[i+1]
    if s2 in d:
        d[s2].append(d2[i+2])
    else:
        d[s2] = [d2[i+2]]

# Start writing the trigram
start_key = random.choice(list(d))
trigram = start_key.split()
trigram.append(random.choice(d[start_key]))

# Add to the trigram
while (trigram[-2] + ' ' + trigram[-1]) in d:
    current_key = trigram[-2] + ' ' + trigram[-1]
    trigram.append(random.choice(d[current_key]))

# Print trigram story
print(' '.join(trigram))
