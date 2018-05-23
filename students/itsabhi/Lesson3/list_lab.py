#! /usr/bin/env Python3


def series1():
    my_list = ["Apples", "Pears", "Oranges", "Peaches"]
    print(my_list)
    add_fruit = input("Add another fruit: ")
    my_list.append(add_fruit)
    print(my_list)
    (number) = input("Enter a number: ")
    print(my_list[int(number)-1])
    my_list = ["Mangos"] + my_list
    print(my_list)
    my_list.insert(0, "Berries")
    print(my_list)
    for fruit in my_list:
        if fruit.startswith("P"):
            print(fruit)
    return my_list


def series2():
    my_list = ["Apples", "Pears", "Oranges", "Peaches", "Mangos", "Berries"]
    print(my_list)
    my_list.pop()
    print(my_list)
    delete_fruit = input("Enter a fruit to delete: ")
    new_list = []
    for item in my_list:
        if item != delete_fruit:
            new_list.append(item)
    print(new_list)
    double_list = my_list * 2
    delete_more_fruits = ""
    while delete_more_fruits not in double_list:
        delete_more_fruits = input("Enter another fruit to delete: ")
    new_list = []
    for item in double_list:
        if item != delete_more_fruits:
            new_list.append(item)
    print(new_list)


def series3():
    my_list = ["Apples", "Pears", "Oranges", "Peaches"]
    i = 0
    like_apples = input("Do you like apples: ")
    like_pears = input("Do you like pears: ")
    like_oranges = input("Do you like oranges: ")
    like_peaches = input("Do you lile peaches: ")
    while not (like_apples == "yes" or like_apples == "no"):
        like_apples = input("Do you like apples, yes or no: ")
    while not (like_pears == "yes" or like_pears == "no"):
        like_pears = input("Do you like pears, yes or no: ")
    while not (like_oranges == "yes" or like_oranges == "no"):
        like_oranges = input("Do you like oranges, yes or no: ")
    while not (like_peaches == "yes" or like_peaches == "no"):
        like_peaches = input("Do you like peaches, yes or no: ")
    like_list = [like_apples, like_pears, like_oranges, like_peaches]
    my_list_copy = my_list[:]
    for item in like_list:
        if item == "no":
            my_list.remove(my_list_copy[i])
        i += 1
    print(my_list)


def series4():
    my_list = ["Apples", "Pears", "Oranges", "Peaches"]
    my_list_copy = my_list[:] #Shallow copy
    reverse_my_list = []
    for item in my_list_copy:
        reverse_my_list.append(item[::-1])
    print(reverse_my_list)
    my_list.pop()
    print(my_list)
    print(my_list_copy)


def main():
    series1()
    series2()
    series3()
    series4()


if __name__ == '__main__':
    main()