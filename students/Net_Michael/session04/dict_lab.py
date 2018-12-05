#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Dictionaries 1
# Create a dictionary containing “name”, “city”, and “cake” for “Chris” 
# from “Seattle” who likes “Chocolate” 

# literal dict

lab_info = {'name': 'Chris', 'city':'Seattle', 'cake':'Chocolate'}
lab_info


# In[61]:


# or key values or key arguements as keyword arguments

lab_info = dict(name= 'Chris', city='Seattle', cake='Chocolate')
lab_info.items()


# In[32]:


# or as sequence of pairs (key, values)
lab_info = dict([('name', 'Chris'), ('city', 'Seattle'), ('cake', 'Chocolate')])
lab_info


# In[39]:


lab_info = dict(zip(['name', 'city', 'cake'], ['Chris', 'Seattle', 'Chocolate']))


# In[40]:


# display dictionary

lab_info['name'] 
lab_info['city']


# In[43]:


# Delete the entry for “cake”.

del lab_info['cake']
lab_info


# In[44]:


#Add an entry for “fruit” with “Mango” and display the dictionary.

lab_info['fruit'] = 'Mango'


# In[46]:


#Display the dictionary keys
list(lab_info)


# In[59]:


#Display the dictionary values.
list(lab_info.values()) 


# In[60]:


#or 
lab_info.values()


# In[53]:



#Display whether or not “cake” is a key in the dictionary (i.e. False) (now).

'cake' in lab_info


# In[56]:


#Display whether or not “Mango” is a value in the dictionary (i.e. True).
'Mango' in lab_info.values()


# In[57]:


lab_info.items()

