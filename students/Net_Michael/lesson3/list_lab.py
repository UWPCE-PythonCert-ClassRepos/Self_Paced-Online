#!/usr/bin/env python
# coding: utf-8

# In[1]:


# series 1
# Create and display the given list 

fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)


# In[2]:


# series 1
# Ask the user for another fruit add it to the end of the list
# display the list

new_fruit = input("Please add new fruit to the list ")
output = fruit.append(new_fruit)
print(fruit)


# In[3]:


# series 1
# Ask the user for a number  display the number back to the user 

def sel_fruit(f, fruit = fruit):
    m = len(fruit) + 1
    while f <= m:
        for i in range(1,m):
            if f == i : 
                sel_fr = fruit[i-1]
                return(sel_fr)

index = input("Fruits indexed by ")
print("are " + sel_fruit(int(index)) + ".")


# In[4]:


# series 1
# add another fruit to the list using +

new_fruit = input("Add new fruit to the list ")
output = [new_fruit] + fruit
print( output)


# In[5]:


# series 1
# add new fruit at the begining of the list using insert()

add_fruit = input("Add new fruit at the begining of the list ")
output = fruit.insert(0, add_fruit)
print(fruit) 


# In[6]:


# series 1
# display all the fruits that begin with "P" 
            
def first_letter(fruit, word_a):
    m = len(fruit)
    for i in range(m):
        if word_a in fruit[i]:
            print(fruit[i])


# In[7]:


first_letter(fruit, "P")


# In[8]:


# series 1
# not part of the homework 
# to answer display all the fruits that contain "P" or "p"

def find_letter(fruit, word_a):
    m = len(fruit)
    fruits = [item.lower() for item in fruit]
    for i in range(m):
        if word_a in fruits[i]:
            print(fruit[i])


# In[9]:


find_letter(fruit, "p")


# In[10]:


# series 2
# Display the list.

print(fruit)


# In[11]:


# series 2
# Remove the last fruit from the list.
# display the list

fruitsel = fruit[:-1]
print(fruitsel)


# In[4]:


# series 2
# Ask the user for a fruit to delete, find it and delete it.

fruit = [item.lower() for item in fruit]
print(fruit)
fruit_sel = input("Do you want to delet a fruit? (Yes/No)")
if fruit_sel.lower() in "yes":
    fruit_del = input("Please remove the fruit from the list.")
    fruit_del = fruit_del.lower()
    if fruit_del not in fruit:
        print("The fruit is not in the list.")
    else:
        fruit.remove(fruit_del)
print(fruit)


# In[15]:


# series 3
#  Ask the user for input displaying a line 

fruit = ('Apples', 'Pears', 'Oranges', 'Peaches', 'Mangos')
m = len(fruit) 
fruits = [item.lower() for item in fruit]
print(fruits)

for i in range( m):    
    sel_fruit = fruits[i]
    quest = input("Do you like like {}?" .format(sel_fruit))


# In[4]:


# series 3
# For each “no”, delete that fruit from the list.
# For any answer that is not “yes” or “no”, 
#prompt the user to answer with one of those
# two values (a while loop is good here)


fruits = [item.lower() for item in fruit]
print(fruits)

for sel_fruit in fruits:
    quest = input("Do you like {}? (yes/no)" .format(sel_fruit))
    quest.lower()
    if quest == "no":
        fruits.remove(sel_fruit)
    if quest == "yes":
        fruits = fruits[:]
    print(fruits)


# In[7]:


# series 4
#  Make a copy of the list and reverse the letters in each fruit in the copy.
def reverse_fruit(fruit):
    fruits = [item.lower() for item in fruit]
    m = len(fruits)
    fruit_rev = [0] * m
    for j in range(m):
        fruit_rev[j] = str(fruits[j])[::-1]
    return(fruit_rev)

# Delete the last item of the original list. 
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches', 'Mango']
rev_fruit = reverse_fruit(fruit=fruit)
rev_fruit


# In[9]:


#Display the original list
fruit[:-1]


# In[10]:


#Display the copy
rev_fruit[:-1]

