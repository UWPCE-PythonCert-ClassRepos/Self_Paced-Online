#List Lab

#Series 1
list1 = ["Apples", "Pears", "Oranges", "Peaches"] #Create a list
print(list1) #Display list

fruit = str(input("Enter the fruit to add to the list: ")) #Ask user to add fruit to list
list1.append(fruit) #Add fruit to end of list
print(list1) #Display list 

num = int(input("Enter the number to choose the fruit from the list: ")) #Ask user to choose number for fruit
num -= 1 #Using -1 since items in list is chosen from index of 0
if num < 0 : 
    print("Please enter a number of 1 or above.") #User can't choose 0 as an option
else:
    print(list1[num]) #Display list
    
list2 = ["Pineapple"] #Creating a new list to add item to existing list
list1 = list2 + list1 #Adding item to the beginning of the list
print(list1) #Display list

list1.insert(0, "Watermelon") #Using insert to add item to beginning of list
list1 #Display list

for fruit in list1: #For every fruit in the list
    if fruit.startswith("P"): #If statement looks for fruits that start with P
        print(fruit) #Prints the fruit from the list
        
#Series 2
list1 = ["Apples", "Pears", "Oranges", "Peaches"] #Create a list
print(list1) #Display list

list1.pop() #removes last item in list
print(list1)

answer = str(input("Enter the name of the fruit to delete: "))
if answer == "Apples":
    list1.remove("Apples")
elif answer == "Pears":
    list1.remove("Pears")
elif answer == "Oranges":
    list1.remove("Oranges")
elif answer == "Peaches":
    list1.remove("Peaches")
else:
    print("Please choose a fruit to delete that is within the list.")
print(list1)

#Series 3
list1 = ["Apples", "Pears", "Oranges", "Peaches"] #Create a list
print(list1) #Display list

while True:
    answer = str(input("Do you like apples? "))
    if answer == "no":
        list1.remove("Apples")
        print(list1)

    answer = str(input("Do you like pears? "))
    if answer == "no":
        list1.remove("Pears")
        print(list1)

    answer = str(input("Do you like oranges? "))
    if answer == "no":
        list1.remove("Oranges")
        print(list1)

    answer = str(input("Do you like peaches? "))
    if answer == "no":
        list1.remove("Peaches")
        print(list1)
    else:
        print("Please answer between yes or no.")
        
#Series 4
list1 = ["Apples", "Pears", "Oranges", "Peaches"] #Create a list
print(list1) #Display list

reverse = (list1[0][::-1], list1[1][::-1], list1[2][::-1], list1[3][::-1])
print(reverse)

