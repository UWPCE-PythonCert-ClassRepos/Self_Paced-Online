# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 18:08:14 2018

@author: Karl M. Snyder
"""
import random

from collections import defaultdict

text = """Are you all ready, Tom?"

"All ready, Mr. Sharp," replied a young man, who was stationed near
some complicated apparatus, while the questioner, a dark man, with a
nervous manner, leaned over a large tank.

"I'm going to turn on the gas now," went on the man. "Look out for
yourself. I'm not sure what may happen."

"Neither am I, but I'm ready for it. If it does explode it can't do
much damage."

"Oh, I hope it doesn't explode. We've had so much trouble with the
airship, I trust nothing goes wrong now."

"Well, turn on the gas, Mr. Sharp," advised Tom Swift. "I'll watch the
pressure gauge, and, if it goes too high, I'll warn you, and you can
shut it off."

The man nodded, and, with a small wrench in his hand, went to one end
of the tank. The youth, looking anxiously at him, turned his gaze now
and then toward a gauge, somewhat like those on steam boilers, which
gauge was attached to an aluminum, cigar-shaped affair, about five feet
long.

Presently there was a hissing sound in the small frame building where
the two were conducting an experiment which meant much to them. The
hissing grew louder.

"Be ready to jump," advised Mr. Sharp.

"I will," answered the lad. "But the pressure is going up very slowly.
Maybe you'd better turn on more gas."

"I will. Here she goes! Look out now. You can't tell what is going to
happen."

With a sudden hiss, as the powerful gas, under pressure, passed from
the tank, through the pipes, and into the aluminum container, the hand
on the gauge swept past figure after figure on the dial.

"Shut it off!" cried Tom quickly. "It's coming too fast! Shut her off!"

The man sprang to obey the command, and, with nervous fingers, sought
to fit the wrench over the nipple of the controlling valve. Then his
face seemed to turn white with fear.

"I can't move it!" Mr. Sharp yelled. "It's jammed! I can't shut off the
gas! Run! Look out! She'll explode!"

Tom Swift, the young inventor, whose acquaintance some of you have
previously made, gave one look at the gauge, and seeing that the
pressure was steadily mounting, endeavored to reach, and open, a
stop-cock, that he might relieve the strain. One trial showed him that
the valve there had jammed too, and catching up a roll of blue prints
the lad made a dash for the door of the shop. He was not a second
behind his companion, and hardly had they passed out of the structure
before there was a loud explosion which shook the building, and
shattered all the windows in it."""

text = text.replace('"', '')
text = text.replace('\n', ' ')
text = text.split(' ')
d = defaultdict(list, [])
for i, w in enumerate(text):
    if i < len(text)-2:
        d[(text[i] + ' ' + text[i+1])].append(text[i+2])
#print(d)
new_list = []
for i, (k, v) in enumerate(d.items()):
    if (i == 40): #40 chosen at random
        new_list.extend(k.split(' '))
        #print(new_list)
        
def build_list():
    for i, (k, v) in enumerate(d.items()):
        if i < len(d.keys()):
            init_key = new_list[-2] + ' ' + new_list[-1]
            #print(init_key)
            #print(random.choice(d[init_key]))
            new_list.append(random.choice(d[init_key]))
    
build_list()
#print(new_list)
new_story = ' '.join(new_list)
print(new_story)