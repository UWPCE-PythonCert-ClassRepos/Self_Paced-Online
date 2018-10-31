print ("Today we are going to be playing with fruits.  It's a healthy exercise.  Don't take it personally")
print ("We start with a list of:")
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print (fruits, "\n")
add_entry = input("Enter your additional favorite fruit: ")
fruits.append(add_entry)
print ("Thank you.  The fruit sequence is now:")
print(fruits,"\n")

i = int(input("Now, in that list, which is your favoite?, Select by number, 1, 2,... :  "))
print("Ahh, Good Choice, number", (i), " ", fruits[i-1], "\n")

add_entry = input("Another fruit to lead the list? ")
fruits = [add_entry] + fruits
print (fruits,"\n")

add_entry = input("Please add another fruit to lead the list?")

fruits.insert(0,add_entry)
print (fruits, "\n")

print ("interesting.....  All fruits beginning with 'P' include:")
p_fruits = []
for element in fruits:
    if element[0]== "p":
        p_fruits.append(element)
print (p_fruits, "\n")
print ("end series 1--------------------------------------------------\n")

print ("Now recall, list of fruits is:")
print (fruits, "\n")

print ("scaling back from the last fruit added, the list returns to:")
del fruits [0]
print (fruits)
del_entry = input("Please select a fruit to delete:")
fruits.remove(del_entry)
print (fruits)
print ("end series 2--------------------------------------------------\n")

x_fruit = []
like_fruits = fruits
print (like_fruits)
for fruit in (like_fruits):
    a = input(f"Do you like the fruit {fruit} (y/n):")
    while a != "n" and a != 'y':
        a = input(f"'Sorry, {a} will not work. Please enter 'y' or 'n' :")
    if a == 'n':
        x_fruit.append(fruit)
print ("fruits you do not care for: ", x_fruit)
for fruit in (x_fruit):
    like_fruits.remove(fruit)
print("That leaves accepable fruits as: ", like_fruits)
print("End series 3---------------------------\n")
      
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
rev_fruits = []
for fruit in (fruits):
    fruit=fruit[::-1]
    rev_fruits.append(fruit)
print ("Original fruits were: ", fruits)
print ("Fruits with names inverted are: ", rev_fruits)
print ("fruits, less the last include : ", fruits[:-1])
print("End series 4---------------------------\n")