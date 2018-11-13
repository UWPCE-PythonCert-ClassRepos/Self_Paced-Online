#########################################
#
#            SERIES 1
#
########################################
#Create a list
fruit=['Apples', 'Pears', 'Oranges','Peaches']

#Display list
print(fruit)

#Append new fruit and display
response = "Test" #input("Enter another fruit> ")
fruit.append(response)
print(fruit)

#Ask for a number
response =2 # input("Which fruit (order) would you like to see?> ")
print(fruit[int(response)-1])

#Add another fruit at the beginning
response ="Test" # input("Enter another fruit> ")
fruit=[response]+ fruit  # Add with plus
print(fruit)

fruit.insert(0,response)  #Insert
print(fruit)

#Display fruit starting with "P"
for item in fruit:
    if item[0]=='P':
        print(item)

########################################
#
#            SERIES 2
#
########################################
#Display the list
fruit=['Apples', 'Pears', 'Oranges','Peaches', 'Watermelon']
print(fruit)
#Remove the last fruit from the list & Display
fruit.pop()
print(fruit)
#Ask the user for a fruit to delete, find it and delete it
response='Pears' #input('Which fruit to delete=')
fruit.remove(str(response))
print(fruit)

########################################
#
#            SERIES 3
#
########################################
fruit=['Apples', 'Pears', 'Oranges','Peaches', 'Watermelon']
print(fruit)

for item in fruit:
    print(fruit)
    response=input("Do you like " + item.lower())
    print(response)

    if response.upper() == 'YES':
        #Keep
        print('Keeping ' + item)
    elif response.upper() == 'NO':
        #Remove
        print(item)
        fruit.remove(item)
        print(fruit)
    else:
        shouldLoop=True
        while shouldLoop:
            response = input("Please enter YES or NO!")
            print(response)
            if response.upper() == 'YES' or response.upper() == 'NO':
                shouldLoop = False

########################################
#
#            SERIES 4
#
########################################
fruit=['Apples', 'Pears', 'Oranges','Peaches', 'Watermelon']
#Make a copy of the list and reverse the letters in each fruit in the copy.
list_copy=list()

for item in fruit:
    list_copy.append(fruit [::-1])

print(list_copy)
#Delete the last item of the original list. Display the original list and the copy.
list_copy.pop(len(fruit)-1)
print(list_copy)