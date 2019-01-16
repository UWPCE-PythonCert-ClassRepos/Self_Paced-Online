#Lesson 3 Assignment 1
#Write functions that slice strings
#Jason Virtue 01/13/2019
#UW Self Paced Python Course

#Series 1 Create a fruit list
def length(list):
    return len(fruit_list)

fruit_list = ["Apples","Pears","Oranges","Peaches"]
print(fruit_list)
response = input("What is another fruit you like?> ")
fruit_list.append(response)
print(fruit_list)
num_response = int(input("Please input one number from 1 to {}> ".format(length(fruit_list))))-1
print((num_response+1) , ": " ,fruit_list[num_response])
response = input("What is another fruit you like?> ")
fruit_list = [response] + fruit_list
print(fruit_list)
response = input("What is another fruit you like?> ")
fruit_list.insert(0,response)
print(fruit_list)
search_term = "P"
search_fruit_names = [search_name for search_name in fruit_list if (search_name[0] in search_term)]
print(search_fruit_names)
