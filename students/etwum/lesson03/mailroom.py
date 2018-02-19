#!/usr/bin/env python3

if __name__ == "__main__":
    print()


def send_thank_you():

    return print("works")


def create_report():

    return print("works")

print("Welcome to the Mail Room")
print("------------------------------------------------------------------------")
# ****Input/Output****
while True:
    print("""
    Menu of Options
    1) Send Thank You Note
    2) Create Report
    3) Exit Program
    """)
    strChoice = None
    try:
        strChoice = int(input("Which option would you like to perform? Input a number [1 to 3] "))
        if strChoice == 1 or strChoice == 2 or strChoice == 3:
            print()
        else:
            raise Exception
    except Exception:
        print("Please input a valid option: 1, 2, or 3")

    if (strChoice == 1):
        send_thank_you()
        continue

    elif (strChoice == 2):
        create_report()
        continue
    elif (strChoice == 3):
        break 