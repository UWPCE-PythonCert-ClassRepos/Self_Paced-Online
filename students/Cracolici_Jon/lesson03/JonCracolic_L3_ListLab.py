#!/usr/bin/env python 3
#Jon Cracolici
#Lesson 03 List Lab
#UW Python Cert
import copy
#
#series 1
fruitlist1 = ['Apples','Pears','Oranges','Peaches']
print("Series 1")
print(fruitlist1)
fruitlist1.append(input("Please input a new fruit!"))
print(fruitlist1)
number = input("Please input a number")
if int(number) <= len(fruitlist1):
    print('The {}th fruit in the list is {}'.format(number,fruitlist1[int(number)-1]))
else:
    print("Please input a number less than or equal to {}".format(len(fruitlist1)))
nextfruit1 = input('Please input a new fruit')
fruitlist1 = [nextfruit1] + fruitlist1
print(fruitlist1)
nextfruit2 = input('Please input a new fruit')
fruitlist1.insert(0,nextfruit2)
print(fruitlist1)
for item in fruitlist1:
    if item[0]=='P':
        print(item)
#
#Series 2
print("Series 2")
print(fruitlist1)
fruitlist2 = copy.deepcopy(fruitlist1)
#print(fruitlist2)
fruitlist2.pop(len(fruitlist2)-1)
print(fruitlist2)
badfruit = input('Please select a fruit to remove.')
fruitlist2.remove(badfruit)
print(fruitlist2)
print("Series 2- Bonus Points Part")
#Bonus Points Sections
#so this code does as you asked, but also uses a couple indicators to see if you are removing something,
#or if the loop is running too long. Pick a fruit darn it!
bfruitlist2 = fruitlist2 *2
n=int((len(bfruitlist2)-1)/2)+1
#print(list)
mark = 0
mark2=0
while mark ==0 and mark2<11:
    badfruit2 = input('Please select a fruit to remove.')
    if badfruit2 in bfruitlist2:
        while badfruit2 in bfruitlist2:
            bfruitlist2.remove(badfruit2)
        print(bfruitlist2)
        mark = 1
    else:
        print('Please select a fruit from the following choices {}'.format(bfruitlist2[:n]))
    mark2+=1
#
#series 3
#I approach this problem using sets to test whether or not the user
#has given a valid answer for each type of fruit, rather than instance.
print("Series 3")
fruitlist3 = copy.deepcopy(fruitlist1)
fruitlist3original = set(fruitlist3)
validanswers = set([])
#while fruitlist3original <= validanswers:
while validanswers < fruitlist3original:
    for item in fruitlist3original:
        fruit = item
        fruitl = fruit.lower()
        #print(fruitl)
        preference = input('Do you like {}?'.format(fruitl))
        if preference == 'no':
            validanswers.add(item)
            while fruit in fruitlist3:
                fruitlist3.remove(fruit)
            #print(validanswers)
            #print(fruitlist3)
            #print(fruitlist3original)
            #print(fruitlist1)
        elif preference != "yes":
            print('Please answer the question with "yes" or "no".')
        else:
            validanswers.add(item)
            #print(validanswers)
            #print(fruitlist3)
            #print(fruitlist3original)
            #print(fruitlist1)
print(fruitlist3)
#
#Series 4
#
print("Series 4")
fruitlist4 = [item[::-1] for item in fruitlist1]
fruitlist1.pop(len(fruitlist1)-1)
print(fruitlist4)
print(fruitlist1)
        
        
            