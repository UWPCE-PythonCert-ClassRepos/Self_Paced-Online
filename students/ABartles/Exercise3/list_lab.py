

#------------------------------------
#--------------Series 1--------------
print("--------------Series 1--------------")
lst_original = ["Apples", "Pears", "Oranges", "Peaches"]

lst_s1 = lst_original.copy()
print(lst_s1)

response = input("\nEnter a fruit: ")
response = response.title()
lst_s1.append(response)
print(lst_s1)
print()

response = 0

while len(lst_s1) < response or response <= 0:
    response = input("Enter a number from 1-{} to see the corresponding fruit: ".format(len(lst_s1)))
    try:
        response = int(response)
    except ValueError:
        print("That is not an integer!")
        response = 0
user_fruit = lst_s1[response-1]
print("Your selection {}: {}".format(response,user_fruit))

response = input("\nEnter a fruit: ")
response = response.title()
lst_s1 += [response]
print(lst_s1)

response = input("\nEnter a fruit: ")
response = response.title()
lst_s1.insert(0, response)
print(lst_s1)

print("\nFruits starting with 'p':")
for i in lst_s1:
    if i[0] == "P":
        print(i)
#------------------------------------
#--------------Series 2--------------
print("\n--------------Series 2--------------")
lst_s2 = lst_original.copy()
print(lst_s2)

lst_s2.pop()
print(lst_s2)

response = input("\nWhat fruit would you like to remove from the list? ")
response = response.title()

while response not in lst_s2:
    lst_s2 = lst_s2*2
    print(lst_s2)
    print("\nTry again, select from the list.")
    response = input("\nWhat fruit would you like to remove from the list? ")
    response = response.title()

while response in lst_s2:
    lst_s2.remove(response)
print(lst_s2)
#------------------------------------
#--------------Series 3--------------
print("\n--------------Series 3--------------")
lst_s3 = lst_original.copy()
response = "Not N or Y"
i = 0

while True:
    print(lst_s3)
    if i < len(lst_s3):
        fruit = lst_s3[i]
        response = input("Do you like {} (Y/N)?".format(fruit))
        response= response.upper()
        if response == "N":
            while fruit in lst_s3: # handles removing duplicates in list
                lst_s3.remove(fruit)
            response = "Not N or Y"
        elif response == "Y":
            i += 1
            response = "Not N or Y"
    if i == len(lst_s3):
        break
print(lst_s3)
#------------------------------------
#--------------Series 4--------------
print("\n--------------Series 4--------------")
lst_s4 = lst_original.copy()

tsl = []

for i in lst_s4:
    revfruit = i[::-1]
    tsl.append(revfruit)

lst_s4.pop()
print("Original list:")
print(lst_s4)
print("Original list w/ reversed strings:")
print(tsl)

t = input()
