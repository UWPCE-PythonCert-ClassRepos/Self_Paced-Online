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
print("All the fruits that begin with P or p are:")
for x in range(len(a_list)):
    if a_list[x][0] is 'P':
        print(a_list[x])
    elif a_list[x][0] is 'p':
        print(a_list[x])
#Series2
print(a_list)
a_list.pop()
print(a_list)
a_list = a_list * 2
response = input("Tell me a fruit to delete > ")
while response not in a_list:
    response = input("Tell me a fruit to delete (it must be in this list) > ")
while response in a_list:
    a_list.remove(response)
print(a_list)
#Series 3
a_list_b = a_list[:]
for x in range(len(a_list)):
    response = input("Do you like {name}? (yes/no) > ".format(name=a_list[x].lower()))
    while not(response == 'yes'or response == 'no'):
        response = input("Do you like {name}? (yes/no) > ".format(name=a_list[x].lower()))
    if response == 'no':
        while a_list[x] in a_list_b:
            a_list_b.remove(a_list[x])
a_list = a_list_b[:]
print(a_list)
#Series 4
a_list_c = a_list[:]
for x in range(len(a_list_c)):
    a_list_c[x] = a_list_c[x][::-1]
a_list.pop()
print(a_list)
print(a_list_c)
