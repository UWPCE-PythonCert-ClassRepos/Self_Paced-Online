#!/usr/bin/env python
# coding: utf-8

# In[1]:


# input 

strs = ( 2, 123.4567, 10000, 12345.67)


# In[2]:


# task one & two

strs_new = ("file_00{:^1}   :" .format(strs[0]),
            "{:.2f}".format(strs[1]),
            "{:.2e}".format(strs[2]), 
            "{:.2e}".format(strs[3])    )

task_12 = ", ".join(strs_new)
task_12


# In[3]:


# Task three
task3 = ("file_00{:^1}, :   {:.2f}, {:.2e}, {:.2e}" .format(*strs[:]))
task3


# In[5]:


# task 4

task4 = (4, 30, 2017, 2, 27)
mm = len(task4)
task4out = [0]*mm


for j in range(mm):
    task4out[j] = ('%(number)02d' %{"number": task4[j]})

task4out.sort()
task4out = " ".join(task4out)
task4out


# In[6]:


# task5
fruit = ("oranges", 'lemons')
weight = (1.3, 1.1)
 
f"The weight of {fruit[0]} is {weight[0]} and the weight of {fruit[1]} is {weight[1]}"


# In[7]:


# task5
# names of the fruit in upper case,
# and the weight 20% higher 

fruits = [item.upper() for item in fruit]

f"The weight of {fruits[0]} is {weight[0]*1.2} and the weight of {fruits[1]} is {weight[1]*1.2}"


# In[22]:


# task 6
# Write some Python code to print a table of several rows, each with a name,
# an age and a cost. Make sure some of the costs are in the hundreds
# and thousands to test your alignment specifiers.

Name = ( "chips", "candy", "olive", "oven")
Age = ( 10, 8, 2, 5 )
Cost = ( 100, 200, 500, 3000)

m = len(Name)
print("Name\t\tAge\t\tCost")

for j in range(m):
    Names = Name[j][0].upper() + Name[j][1:]
    print('{:8}'.format(Names), '{:^20}'.format(Age[j]), 
          '${:.2f}'.format(Cost[j]))


# In[9]:


# task 6
#And for an extra task, given a tuple with 10 consecutive numbers, 
#can you work how to quickly print the tuple in columns 
#that are 5 charaters wide? It can be done on one short line!

tuple(range(1, 11))

