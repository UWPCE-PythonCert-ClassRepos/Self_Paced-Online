#!/usr/bin/env python3
#-------------------------------------------------#
# Title: List Lab
# Dev:   LDenney
# Date:  October 10, 2018
# ChangeLog: (Who, When, What)
#   Laura Denney, 10/10/18, Created File
#-------------------------------------------------#
original_fruit = ["Apples", "Pears", "Oranges", "Peaches"]


def series1(fruit):
##SERIES 1 ---------------------------------------------------
    print("SERIES 1------------------------------")
    print("Current fruit: ", fruit)
    response = input("Please choose a fruit to add > ")
    #add users fruit choice
    fruit.append(response.title())
    print("Current fruit: ", fruit)
    #print fruit order and fruit
    num = input("Please choose a number between 1 and {} > ".format(len(fruit)))
    if num.isdigit():
        if int(num) >= 1 and int(num) <= len(fruit):
            num = int(num)
            print("{} {}".format(num, fruit[num - 1]))
        else:
            print("Sorry, that was not in the valid range.")
    else:
        print("Sorry, that was not a number.")
    #addition to add fruit
    fruit = ["Bananas"] + fruit
    print("Added a fruit: ", fruit)
    #insert to add fruit
    fruit.insert(0, "Grapes")
    print("Added a fruit: ", fruit)
    #print all fruit with p
    print("Fruit with p in name: ")
    for item in fruit:
        if "p" in item.lower():
            print(item)
    print()

def series2(fruit):
##SERIES 2 ----------------------------------------------------
    print("SERIES 2------------------------------")
    print("Current fruit: ", fruit)
    #remove last fruit
    fruit = fruit[:-1]
    print("Removed one fruit: ", fruit)
    remov = input("Please pick a fruit to remove > ").title()
    if remov in fruit:
        fruit.remove(remov)
    else:
        print("Sorry, {} was not in the list, could not remove.".format(remov))
    print("Current fruit: ", fruit)
    print()

def series3(fruit):
##SERIES 3 ----------------------------------------------------
    print("SERIES 3------------------------------")
    for item in fruit[:]:
        yesno = ""
        while yesno != "yes" and yesno != "no":
            yesno= input("Do you like {}? ".format(item)).lower()
            if yesno == "no":
                print("{} are gross! Successfully removed.".format(item))
                fruit.remove(item)
            elif yesno == "yes":
                print("{} are delicious, I agree.".format(item))
            else:
                print("Please choose yes or no.")
    print("Only the delicious fruit: ", fruit)
    print()

def series4(fruit):
##SERIES 4 ----------------------------------------------------
    print("SERIES 4------------------------------")
    fruit2 = fruit[:]
    #reversing the fruit words
    for item in range(len(fruit2)):
        fruit2[item] = fruit2[item][::-1]
    fruit = fruit[:-1]
    print("Original list minus last item: ", fruit)
    print("Copy list: ", fruit2)


if __name__ == "__main__":
    series1(original_fruit[:])
    series2(original_fruit[:])
    series3(original_fruit[:])
    series4(original_fruit[:])