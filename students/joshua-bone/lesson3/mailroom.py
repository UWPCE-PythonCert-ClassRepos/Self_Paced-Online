#!/usr/bin/env python3

# Joshua Bone - UW Python 210 - Lesson 3
# 12/25/2018
# Assignment: Mailroom, Part 1

menu = ("Welcome to the Mailroom!\n\n\n" +
        "Please select from the following options:\n" +
        "(S)end a Thank You\n" +
        "(C)reate a Report\n" +
        "(Q)uit\n\n\n")
donors = {}
NUM_WIDTH = 13
TY = ("\n\nDear {:s},\n\nThank you for your generous donation of ${:.2f}.\n\n")


def add(name, amt):
    assert isinstance(amt, (int, float))
    assert amt > 0
    assert isinstance(name, str)
    if name not in donors:
        donors[name] = []
    donors[name].append(amt)


add("William Gates, III", 456456.22)
add("William Gates, III", 197328.27)
add("Mark Zuckerberg", 4567.97)
add("Mark Zuckerberg", 7521.42)
add("Mark Zuckerberg", 4306.71)
add("Jeff Bezos", 877.33)
add("Paul Allen", 150.00)
add("Paul Allen", 450.00)
add("Paul Allen", 108.42)


def printHorizontal():
    print('-' * 80)


def doMenu():
    printHorizontal()
    print(menu)
    return input("Your selection: ")


def createReport():
    max_len = 5 + max((len(d) for d in donors))
    # print header and horizontal lines
    print("-" * (max_len + 2 + 3 * (1 + NUM_WIDTH)))
    print((f"{'Donor Name': <{max_len}}|" +
           f"{'Total Given': >{NUM_WIDTH}} |" +
           f"{'Num Gifts': >{NUM_WIDTH}} |" +
           f"{'Average Gift': >{NUM_WIDTH}}"))
    print("-" * (max_len + 2 + 3 * (1 + NUM_WIDTH)))
    for name in donors:
        amt = sum(donors[name])
        num = len(donors[name])
        avg = amt / num
        print((f"{name: <{max_len}}" +
               f"${amt:{NUM_WIDTH}.2f}  " +
               f"{num:>{NUM_WIDTH}d} " +
               f"${avg:{NUM_WIDTH}.2f}"))
    print("-" * (max_len + 2 + 3 * (1 + NUM_WIDTH)) + "\n\n")


def sendThankYou():
    while True:
        printHorizontal()
        print("Enter a name, or type 'list' for existing donors.")
        print("Type 'q' or 'quit' to go back to main menu.\n")
        i = input("Your input: ")
        if i.lower() == 'list':
            print ("Existing donors:")
            for d in donors:
                print(d)
            continue
        elif i.lower() in ("q", "quit"):
            break
        elif i not in donors:
            donors[i] = []
        amt = float(input("Enter amount: "))
        donors[i].append(amt)
        printHorizontal()
        print(TY.format(*(i, amt)))
        break


if __name__ == "__main__":
    while(True):
        i = doMenu().lower()
        if (i == 's'):
            sendThankYou()
        elif (i == 'c'):
            createReport()
        elif (i == 'q'):
            print("Exiting...")
            break
        else:
            print("Input not understood. Try again.\n")

