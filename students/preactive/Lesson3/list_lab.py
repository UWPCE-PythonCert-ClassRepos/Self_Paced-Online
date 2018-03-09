#!/usr/bin/env python3


def series_one():
    # Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
    # Display the list (plain old print() is fine…).
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    print(fruits)

    # Ask the user for another fruit and add it to the end of the list.
    # Display the list.
    response_one = input("Add a fruit:\n>")
    fruits.append(response_one)
    print(fruits)

    # Ask the user for a number and display the number back to the user and
    # the fruit corresponding to that number (on a 1-is-first basis).
    # Remember that Python uses zero-based indexing,
    # so you will need to correct.
    num_fruits = len(fruits)
    response_two_txt = "Pick a integer from 1 to %s:\n>" % str(num_fruits)
    response_two = input(response_two_txt)
    try:
        response_two_int = int(response_two)
        if response_two_int not in range(1, num_fruits + 1):
            print("Not in range. Try again, mouth breather.")
            series_one()
        else:
            print(response_two + ": " + str(fruits[response_two_int - 1]))
    except:
        print("Not in ranges. Try again, mouth breather.")
        series_one()

    # Add another fruit to the beginning of the
    # list using “+” and display the list.
    fruits = ["tomato"] + fruits
    print(fruits)

    # Add another fruit to the beginning of the list
    # using insert() and display the list.
    fruits.insert(len(fruits), "banana")
    print(fruits)

    # Display all the fruits that begin with “P”, using a for loop.
    for fruit in fruits:
        try:
            if fruit[0:1].lower() == "p":
                print(fruit)
        except:
            print("Something went wrong with lower method. "
                  "But did you know you could save 15% or more "
                  "on your car insurance by switching to Geiko?")
    return fruits


def series_two():
    series_one_stub = series_one()

    # Display the list.
    print(series_one_stub)

    # Remove the last fruit from the list.
    series_one_stub.pop()

    # Display the list.
    print(series_one_stub)

    # Ask the user for a fruit to delete, find it and delete it.
    delete_fruit = input("enter a fruit to remove. CaSe SeNsItIvE:\n>")
    if delete_fruit in series_one_stub:
        series_one_stub.remove(delete_fruit)
        print(series_one_stub)
    else:
        print("Try again, El Jefe!")
        series_two()

    # (Bonus: Multiply the list times two. Keep asking until
    # a match is found. Once found, delete all occurrences.)
    doubled_list = []
    for fruit in series_one_stub:
        doubled_list.append(fruit * 2)
    processable = True
    while processable:
        delete_fruit = input("enter a times two fruit item to remove."
                             " CaSe SeNsItIvE:\n>")
        if delete_fruit in doubled_list:
            doubled_list = list(filter(lambda a: a != delete_fruit, doubled_list))
            processable = False
        else:
            print("Bro Do you even, try again?!")
    print(doubled_list)


def series_three():
    # Ask the user for input displaying a line like “Do you like apples?”
    # for each fruit in the list (making the fruit all lowercase).
    series_one_stub = series_one()
    processed_fruits = []
    for fruit in series_one_stub:
        processable = True
        if fruit in processed_fruits:
            continue
        while processable:
            like_fruit = input("(yes|no) Do you like %s\n>" % fruit.lower())

            # For each “no”, delete that fruit from the list.
            # For any answer that is not “yes” or “no”, prompt the user to
            # answer with one of those two values (a while loop is good here)
            if "no" == like_fruit:
                series_one_stub = list(
                    filter(lambda a: a != fruit, series_one_stub))
                processable = False
                processed_fruits.append(fruit)

            if "yes" == like_fruit:
                processable = False
                processed_fruits.append(fruit)

    # Display the list.
    print(series_one_stub)


def series_four():
    # Make a copy of the list and reverse the letters in each fruit in the copy.
    series_one_stub = series_one()

    fruits_reversed = []
    for fruit in series_one_stub:
        fruits_reversed.append(fruit[::-1])
    # Delete the last item of the original list.
    # Display the original list and the copy.
    series_one_stub.pop()

    print(series_one_stub)
    print(fruits_reversed)


if __name__ == "__main__":
    # series_one()
    # series_two()
    # series_three()
    series_four()
