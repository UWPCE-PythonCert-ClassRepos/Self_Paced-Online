#!/usr/bin/env python3



#series 1
list1 =  ["Apples", "Pears", "Oranges" , "Peaches"]
print(list1)
fruit1 = input("Tell me a fruit you like > ")
list1.append(fruit1)
print(list1)
num1 = int(input("Now, tell me a numer you like between 1 to {} > ".format(len(list1))))
while num1<0 or num1 > len(list1):
    num1 = int(input("Please pick up a number between 1 to {} ".format(len(list1))))
print("Okay, seems the number you choose are {}, and the fruit corresponding to that number is {}".format(num1, list1[num1-1]))
fruit1 = input("Tell me another fruit you like> ")
list1 = [fruit1] + list1
print("The list now is : ", list1)
fruit1 = input("Okay, now the last fruit you would like to choose> ")
list1.insert(0,fruit1)
print("The list now is : ", list1)
print("the fruit stating with letter 'P' is ")
for fruit in list1:
    if fruit[0] == 'P' or fruit[0] == 'p':
        print(fruit)

# series 2
# Multiply the list times two. Keep asking until a match is found.
# User can type both the names of the fruit of the corresponding number
# Once found, delete all occurrences
# series 2

list2 =  list1*2

print("the fruit list now is: ", list2)
list2.pop()
print("I'm gonna take away the last one in the list, and the fruit list now is: ", list2)

retry = True

while retry:
    print("please pickup a fruit you want to remove from the list,")
    num2 = input("You can type the name of the corresponding number > ")
    for fruitinlist in list2:
        if fruitinlist == num2:
            list2.remove(num2)
            retry = False
    if num2.isdigit():
        if int(num2)>=0 and int(num2)<=len(list2):
            rmfruit = list2[int(num2)-1]
            for fruitinlist in list2:
                if fruitinlist == rmfruit:
                    list2.remove(rmfruit)
                    retry = False
print("The fruit now in the list is: ",list2)




# series 3
nolikelist =[]
likelist=[]

for fruitinlist in list1:
    answer = input("Do you like {}, Please type 'Yes' or 'No' > ".format(fruitinlist.lower()))
    while answer.lower() != "yes" and answer.lower() != "no":
        answer = input("Please try again, type in 'Yes' or 'No' > ")
    if answer.lower() == 'yes':
        likelist.append(fruitinlist)
    else:
        nolikelist.append(fruitinlist)
print("According to your answer, the fruit you like are",likelist)


# series 4
list4=list1
reverselist=[]
for fruitinlist in list4:
    reverselist.append(fruitinlist[::-1])
list1.pop()
print(list1)
print(reverselist)
