#!/usr/bin/env python3
donors_data = [["John", [200, 20]],
               ["Jeff", [500, 20]],
               ["Susan", [1000, 20, 70]],
               ["Rob", [250, 20]],
               ["Ross", [200]]]


def display_donors(donor_data):
    """Display donors if user enters list"""
    for _ in range(len(donor_data)):
        print('{:10}'.format(*donor_data[_]))


def add_donor_amount(donor_name,amount):
    """Function to add the new donor, if name is already present it will not add"""
    for donor_data in donors_data:
        if donor_data[0] == donor_name:
            donors_data[donors_data.index(donor_data)][1].append(amount)


def donor_find(donor_name):
    """Finding if a donor is already on the list"""
    for donor_data in donors_data:
        if donor_data[0] == donor_name:
            return 1


def thank_you_letter(donor_name,amount):
    """Send a thank you letter"""
    print(f"Thank you {donor_name} for donating {amount} dollars generously.")


def donor_details(*data):
    """Print the Donor table"""
    print(f'{"Donor Name":<20} |{"Total Given":>20} |{"Num Gifts":<20} |{"Average Gift":>20.4}\n')
    print('-'*90)
    for row in range(len(data)):
        print(f'{data[row][0]:<20} ${sum(data[row][1]):>20} {len(data[row][1]):>20} ${(sum(data[row][1]))/(len(data[row][1])):>10.4}\n')


while True:
    print("Select option 1, 2 or 3\n")
    print("1. Send a Thank you\n")
    print("2. Create a report\n")
    print("3. Quit\n")
    option = input("Choose the option:")
    if option == str(1):
        fullname = input("Enter the Full name:")
        if fullname == str("list"):
            display_donors(donors_data)
        elif donor_find(str(fullname)) != 1:
            donors_data.append([str(fullname), []])
            try:
                amount = input("Enter the donation amount:")
                donors_data[-1][1].append(int(amount))
                thank_you_letter(str(fullname), amount)
                print(donors_data)
            except ValueError:
                print("Amount should be an Integer")
        elif donor_find(str(fullname)) == 1:
            amount = input("Enter the donation amount:")
            add_donor_amount(str(fullname), amount)
    elif option == str(2):
        donor_details(*donors_data)
    elif option == str(3):
        break

