a_list = ["Apples", "Pears", "Oranges", "Peaches"]
print (a_list)
response = input("Tell me another fruit to add to the end > ")
a_list.append(response)
print (a_list)
response = input("Tell me index number starting from 1 > ")
print("the number is ", response, " and the fruit is ", a_list[int(response)-1])
response = input("Tell me a fruit to add to the beginning > ")
a_list = [response] + a_list
print(a_list)
response = input("Tell me another fruit to add to the beginning > ")
a_list.insert(0,response)
print(a_list)
