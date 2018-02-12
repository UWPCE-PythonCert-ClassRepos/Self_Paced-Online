#!/usr/bin/env python3

#Series 1
#Here's the initial list

fruit=['Apples','Pears','Oranges','Peaches']
print(fruit)

#This prompts the user to add a fruit, then makes a new list and prints the result

n=input('what fruit would you like to add?')
fruit2=[n]
fruit3=fruit+fruit2
print(fruit3)

#Now the user selects a number, and this function displays the associated fruit

x=int(input('what number fruit would you like to see?'))
if x<=len(fruit3) and x!=0:
    print(x, fruit3[x-1])
else:
    print("Invalid selection")

#This demonstrates adding a user defined fruit with +

y=input('what other fruit would you like to add?')
fruit4=[y]
fruit5=fruit4+fruit3
print(fruit5)

#Now we'll add a user defined fruit with the insert operation

z=input('Come on! Add one more fruit!')
fruit5.insert(0,z)

#Here we use startswith to print a list of fruits that start with P

for i in fruit5:
    if i.startswith('P'):
        print('Here are your P fruits:',i)

#Series 2

print('Now lets start series two')
print("Here's the same series again")
print(fruit)
print("And here it is with the last fruit removed")
fruit.remove("Peaches")
print(fruit)
x=input('What fruit would you like to remove?')
fruit.remove(x)
print(fruit)


#Series 3

print('Time for series 3!')
print("I'm going to ask you if you like the fruits in this list. Please answer yes or no")
print("If you don't like them, then they're gone!")
fruit=['apples','pears','oranges','peaches']
fruit2=('apples','pears','oranges','peaches')
print(fruit)

for i in fruit2:
    x=input(f"Do you like {i.lower()} yes or no?")

    while (x!="yes") and (x!="no"):
        x=input('Please enter "yes" or "no"')
    if x=="no":
        fruit.remove(i)
        
print(fruit)

#Series 4

fruit=['apples','peaches','oranges','pears']
fruit2=list(range(len(fruit)))

for i in range(len(fruit)):
    fruit2[i]=[fruit[i][::-1]]

del fruit[-1:]

print(fruit)
print(fruit2)
   
