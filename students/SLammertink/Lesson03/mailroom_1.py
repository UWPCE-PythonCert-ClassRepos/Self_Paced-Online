#! /usr/bin/env python3
# Author: SLammertink
# UW Self Paced Lesson 03
# Mailroom part 1


# Initiate the lists used
don_list= [75, 25346.25, 125, 25, 200.50] # list with the donations
name_list = ['Sukhmani Travers', 'Sebastien Mayo', 'Aryan Davila', 'Zayan Langley', 'Charlotte Bates'] #list with the donor names
count_list =  [1, 2, 1, 3, 2] # list with a count of the donations given
choices_list = ['Sending a Thank You', 'Creating a Report', 'quit'] # list from where user can chose

# The Functions used:

def name_in_list():
    #Checks whether is name is in the name list if not it adds it
    input_name = input("Please enter the donor's name: ")
    if input_name not in name_list:
        print('')
        print("That name is not in the donor list, will add it now.") # notify the user that the name will be added to the list
        print('')
        name_list.append(input_name)
        print('')
        print('The donor {} has been added to the list!'.format(input_name)) # Notifty the user that the donot has been added
        print('')
        # add zero to the new user in the count_list
        count_list.append(0)
        don_list.append(0)
    elif input_name in name_list:
        print('')
        input_don = float(input("How much is the donation: "))
        print('')
        print("Sending email ----->") # pretending to send the email
        print("Thank you {} for your generous donation!".format(input_name)) # format the email message
        print('')
        for i, name in enumerate(name_list):
            if name == input_name:
                don_list[i] = (don_list[i] + input_don)
                count_list[i] = (count_list[i] + 1)
                return(don_list, count_list)

# Creating a report function:

def report():
    print("{:^30}{:5}{:^20}{:5}{:^30}{:5}{:^20}{:5}".format('Name', '|', 'Donation','|', 'Number of gifts','|', 'Average gift', '|'))
    print("{:-<116}".format(''))
    print(' ')
    for i, j, k in zip(name_list, don_list, count_list):
        print("{:35}${:^25.2f}{:^35}${:^20.2f}".format(i, j,k, (j / k)))


# ask the user to choose from three options:


def choices():
    # Function that prints the choices as long as it is True
    while True:
        print('')
        print("Please make a choice: ")
        print('')
        for i, j in enumerate(choices_list):
            print(i + 1, j)
        choice = input("Please chose an option, to see the list of donors type 'list': ")
        if choice == 'list':
            print('')
            print('Here are the donors already in the list: ')
            print('')
            print(name_list)
            print('')
        elif choice == "1":
            print('')
            name_in_list()
        elif choice == "2":
                print('')
                report()
        elif choice == "3":
            break

# the program starts here

if __name__ == '__main__':
    choices()