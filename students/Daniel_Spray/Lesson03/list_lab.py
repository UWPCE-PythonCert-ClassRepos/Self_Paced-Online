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
