#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict
#Dictionaries 1
# Create a dictionary containing “name”, “city”, and “cake” for “Chris” 
# from “Seattle” who likes “Chocolate” 

# literal dict

lab_info = {'name': 'Chris', 'city':'Seattle', 'cake':'Chocolate'}
lab_info


# In[2]:


# or key values or key arguements as keyword arguments

lab_info = dict(name= 'Chris', city='Seattle', cake='Chocolate')
lab_info.items()


# In[4]:


# or as sequence of pairs (key, values)
lab_info = dict([('name', 'Chris'), ('city', 'Seattle'), ('cake', 'Chocolate')])
lab_info


# In[4]:


lab_info = dict(zip(['name', 'city', 'cake'], ['Chris', 'Seattle', 'Chocolate']))


# In[5]:


# display dictionary

lab_info['name'] 
lab_info['city']


# In[5]:


# Delete the entry for “cake”.

del lab_info['cake']
lab_info


# In[6]:


#Add an entry for “fruit” with “Mango” and display the dictionary.

lab_info['fruit'] = 'Mango'


# In[7]:


#Display the dictionary keys
list(lab_info)


# In[8]:


#Display the dictionary values.
list(lab_info.values()) 


# In[9]:


#or 
lab_info.values()


# In[10]:


#Display whether or not “cake” is a key in the dictionary (i.e. False) (now).

'cake' in lab_info


# In[11]:


#Display whether or not “Mango” is a value in the dictionary (i.e. True).
'Mango' in lab_info.values()


# In[12]:


lab_info.items()


# In[13]:


s2 = set(range(0,21,2))
s3 = set(range(0,21,3))
s4 = set(range(0,21,4))
s4


# In[15]:


def divis_by(a):
    output = {x for x in range(0, 21) if x % a == 0}
    return(output)


# In[16]:


s2 = divis_by(2)


# In[17]:


s3.issubset(s2)


# In[18]:


s4.issubset(s2)


# In[19]:


#Sets 2
#Create a set with the letters in ‘Python’ and add ‘i’ to the set.

s = set('python')
s.add('i')
s


# In[20]:


#Create a frozenset with the letters in ‘marathon’.


# In[21]:


m = frozenset("marathon")
m


# In[22]:


#union
print( s|m, s.union(m), m.union(s) )

# intersection

print(s&m, s.intersection(m), m.intersection(s))

outfile = open('trial.txt', 'w')
outfile

