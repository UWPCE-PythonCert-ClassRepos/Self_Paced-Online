
print("Series 1")
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print("This is list of fruit: ")
print(fruit_list)


response = input("please add another fruit > ")
fruit_list.append(response)
print(fruit_list)


response = int(input("please give a number > "))
print("This is your number {}".format(response))
print("This is your fruit {}".format(fruit_list[response-1]))

fruit_list += ['Durian']
print(fruit_list)

fruit_list.insert(0, 'Grapes')
print(fruit_list)

for f in fruit_list:
    if f.startswith("P"):
        print(f)

print("Series 2")
print(fruit_list)
fruit_list.pop()

print(fruit_list)
response = input("please insert fruit to be deleted > ")
if response in fruit_list:
    fruit_list.remove(response)
    print(fruit_list)
else:
    print("That fruit is not in the list")


print("Series 3")

fruit_list_2 = fruit_list
for fruit in fruit_list[:]:
    while (True):
        response = input("Do you like {} ? ".format(fruit))
        if 'no' in response:
            fruit_list.remove(fruit)
            break
        elif 'yes' in response:
            break
        else:
            pass

print(fruit_list)


print("Series 4")
fruit_list_2 = fruit_list
print(fruit_list_2)

fruit_list_3 = []

for fruit in fruit_list_2:
    fruit_list_3.append(fruit[::-1])

fruit_list_2.pop()
print(fruit_list_2)
print(fruit_list_3)

