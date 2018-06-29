#! /usr/bin/env python3
# Author: SLammertink
# UW Self Paced Lesson 03
# mailroom exercise


# Initiate lists
don_list= [100, 100, 100, 100, 100]
name_list = ['Sukhmani Travers', 'Sebastien Mayo', 'Aryan Davila', 'Zayan Langley', 'Charlotte Bates']
count_list =  [1, 1, 1, 1, 1]
choices_list = ['Sending a Thank You', 'Creating a Report', 'quit']


# Send a thank you functions:

def choices():
    while True:
        for i, j in enumerate(choices_list):
        print(i + 1, j)

def show_list():
    return(name_list)

def donor_not_in_list():
# if donor not in the list add him/her:
    while True:

        if input_name not in name_list:
            name_list.append(input_name)
            # add zero to the new user in the count_list
            count_list.append(0)
            break


def donor_in_list():
        # Check if the name is in the list adn prompt for a donation:
    if input_name in name_list:
        input_don = int(input("Donation: "))
        for i, name in enumerate(name_list):
            don_list[i] = int(don_list[i] + input_don)
            count_list[i] = int(count_list[i] + 1)
            avg_gift = int(don_list[i] / count_list[i])
            return(don_list, count_list, avg_gift)

def send_email():
    # Use string formatting to send a thank you email, print it to the screen and re prompt
    while True:
        print(" Thank you, {} for donating {}.".format(input_name), input_don)
        break


# Creating a report functions:

def report():
    print("{:^30}{:5}{:^20}{:5}{:^30}{:5}{:^20}{:5}".format('Name', '|', 'Donation','|', 'Number of gifts','|', 'Average gift', '|'))
    print("{:-<116}".format(''))
    print(' ')
    for i, j, k in zip(name_list, don_list, count_list):
        print("{:35}{:^25}{:^35}{:^20}".format(i, j,k, (j / k)))


# the program starts here

if __name__ == '__main__'

# ask the user to choose from three options:


