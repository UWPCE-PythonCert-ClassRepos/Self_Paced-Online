def series1():
    list1 = ["Apples", "Pears", "Oranges", "Peaches"]
    print(list1)
    added_fruit = input("What is your new fruit? >")
    list1.append(added_fruit)
    print(list1)
    number = input("Which number would you like to see? >")
    print(number+": "+list1[int(number)-1])
    added_fruit2 = input("Please name a fruit to add to the beginning of the list >")
    list1=[added_fruit2]+list1
    print(list1)
    added_fruit3 = input("Please name another fruit to add to the beginning of the list >")
    list1.insert(0,added_fruit3)
    print(list1)
    for a in list1:
        if a[0].lower() == "p":
            print(a)
    return list1

def series2(list2):
    print(list2)
    del list2[-1]
    print(list2)
    removed_fruit1 = input("Please name a fruit to be removed from the list >")
    list2.remove(removed_fruit1)
    print(list2)
    list2=list2*2
    while len(list2)>0:
        removed_fruit2 = input("Please name a fruit to be removed from the list >")
        while removed_fruit2 in list2:
            list2.remove(removed_fruit2)
        print(list2)

def series3(list3):
    print(list3)
    list4=[]
    for fruits in list3:
        answer1=""
        while answer1.lower() != "yes" or answer1.lower() != "no":
            answer1 = input("Do you like {}? >".format(fruits.lower()))
            if answer1.lower() == "yes":
                list4.append(fruits)
                break
            elif answer1.lower() == "no":
                break
            else:
                print("That's not a yes or no answer")
    print(list4)
    return list4

def series4(list5):
    