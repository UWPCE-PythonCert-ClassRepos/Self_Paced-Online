#Lesson 3 Assignment 1
#Write functions that slice strings
#Jason Virtue 01/13/2019
#UW Self Paced Python Course

#Series 1 Create a fruit list
def length(list):
    return len(fruit_list)

#Generate list
fruit_list = ["Apples","Pears","Oranges","Peaches"]
new_fruit_list = ["Apples","Pears","Oranges","Peaches"]

#Print Fruit list
print(fruit_list)

#User input new fruit
response = input("What is another fruit you like?> ")
fruit_list.append(response)
print("Print list with new fruit")
print(fruit_list)

#User input number from 1 to x
num_response = int(input("Please input one number from 1 to {}> ".format(length(fruit_list))))-1
print("Select fruit based on user input")
print((num_response+1) , ": " ,fruit_list[num_response])

#Add fruit to beginning
response = input("What is another fruit you like?> ")
fruit_list = [response] + fruit_list
print("Print fruit at end of list")
print(fruit_list)

#Add fruit to beginning with insert
response = input("What is another fruit you like?> ")
fruit_list.insert(0,response)
print("Print fruit at beginning of list")
print(fruit_list)

#Search list for "P"
search_term = "P"
search_fruit_names = [search_name for search_name in fruit_list if (search_name[0] in search_term)]
print("Search for fruit that starts with P")
print(search_fruit_names)

#Series 2
#Print the list
print("Print fruit list")
print(fruit_list)

#Remove the last item from fruit list
print("Remove last item on fruit list")
fruit_list.pop(-1)
print(fruit_list)

#Find fruit from list and delete it
response = input("What fruit do you want to delete?> ")
fruit_list.remove(response)
print("Remove fruit from list based on user input")
print(fruit_list)

#Series 3
#Ask user if they like the fruit and if no remove it from list
for item in new_fruit_list:
    answer_response = input("Do you like {}? ".format(item))
    while answer_response.lower() != "yes" and answer_response.lower() != "no":
        answer_response = input("Please answer yes or no ")
    if answer_response.lower() == "no":
        new_fruit_list.remove(item)

print("The fruits you like are {}".format(new_fruit_list))

#Series 4
#Copy list
fruit_list_copy = []

#Reverse list
for item in fruit_list:
    fruit_list_copy.append(item[::-1])

#Remove last item
fruit_list_copy.pop(-1)

#Print list to compare
print(fruit_list)
print(fruit_list_copy)
