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
    response_two_txt = "Pick a integer from 1 to %s:\n>" % str(len(fruits))
    response_two = input(response_two_txt)
    print(response_two + ":" + fruits[int(response_two) - 1])

    if response_two not in range(1,5):
        print("Not in range. Try again mouth breather.")
        series_one()
    else:
        print(response_two + ":" + fruits[response_two-1])



if __name__== "__main__":
    series_one()
