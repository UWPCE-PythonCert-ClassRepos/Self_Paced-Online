#Series 1
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print (fruits)
add_fruit = input("What fruit do you want to add? ")
fruits.append(add_fruit)
print (fruits)
response = int(input("Type in a number "))
print(response," - ",fruits[response:response+1])
fruits = ['Mango'] + fruits
print (fruits)
fruits.insert(0,'Grapes')
print (fruits)
for i in fruits:
    if i[0][0] == 'P' or i[0][0] == 'p':
        print(i)

#Series 2
print(fruits)
del fruits[len(fruits)-1]
print(fruits)
flag =False
while flag == False:
    delete_response = input("What fruit you to delete? ")

    for i in fruits:
        if i == delete_response.capitalize():
            fruits.remove(delete_response.capitalize())
            print("Fruit deleted from list!")
            print(fruits)
            flag = True
    if flag == False:
        print("Fruit not found in list")

#Series 3

fruits_3 = fruits[:]
delete_list = []
for i in fruits_3:
    retain_fruits = input("Do you like {}?(yes/no) > ".format(i))
    if retain_fruits == 'no':
        delete_list += [i]
while retain_fruits not in ['yes','no']:
    retain_fruits = input("Do you like {}?(yes/no) > ".format(i))
    if retain_fruits == 'no':
        delete_list += [i]
for j in delete_list:
    fruits_3.remove(j)
print(fruits_3)

#Series 4

fruits_4 = []
for i in fruits_4:
    fruits_4 += [i[::-1]]

chop_last_fruit = fruits[:-1]
#print(fruits_4)
print(chop_last_fruit)