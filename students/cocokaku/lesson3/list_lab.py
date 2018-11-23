#!/usr/bin/env python3

print('----- SERIES 1 -----')
a_list = ["Apples","Pears","Oranges","Peaches"]
print(a_list)
a_list.append(input("Add a fruit to end of list: ").title())
print(a_list)
while(True):
    n = input("Input a number between 1 and 5: ")
    if not n.isdigit():
        print("That is not a number, try again")
        continue
    n = int(n)
    if n>=1 and n<=5:break
    print("Invalid number, try again")
print("{} = {}".format(n,a_list[n-1]))
a_list = ["Kiwis"] + a_list
print(a_list)
a_list.insert(0,"Papayas")
print(a_list)
print('Fruits that start with P:',end=' ')
p_list = []
for fruit in a_list:
    if fruit[0].lower() == 'p': p_list.append(fruit)
print(p_list)

print('\n----- SERIES 2 -----')
b_list = list(a_list)
print(b_list)
b_list.pop()
print(b_list)
b_list *= 2
while(True):
    del_fruit = input("Delete a fruit from the list: ").title()
    if del_fruit in b_list: break
    print("Fruit not found, try again")
b_list = [fruit for fruit in b_list if fruit != del_fruit]
print(b_list)

print('\n----- SERIES 3 -----')
c_list = list(a_list)
for fruit in a_list:
    while(True):
        answer = input("Do you like {}?".format(fruit.lower())).lower()
        if answer in {"yes","no"}: break
        print("Please answer yes or no, try again")
    if answer == "no":
        c_list.remove(fruit)
print(c_list)

print('\n----- SERIES 4 -----')
d_list = list(a_list)
for i,fruit in enumerate(d_list):
    d_list[i]=fruit[::-1].title()
a_list.pop()
print(a_list)
print(d_list)