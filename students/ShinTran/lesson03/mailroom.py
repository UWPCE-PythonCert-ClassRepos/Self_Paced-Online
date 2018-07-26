'''
Shin Tran
Python 210
Lesson 3 Assignment
'''

master_list = []
name_list = []


# Creates the master_list where it has 12 donations pre-populated
def initialize():
    global master_list
    master_list = [
        ["James Smith", 91561.25],
        ["Mary Johnson", 5811.05],
        ["John Williams", 41113.42],
        ["Patricia Brown", 19184.81],
        ["Robert Jones", 51227.53],
        ["Jennifer Miller", 53514.94],
        ["Michael David", 31051.46],
        ["Mary Johnson", 71646.16],
        ["William Rodriguez", 69244.21],
        ["Mary Johnson", 12689.07],
        ["Michael David", 57145.50],
        ["Patricia Brown", 81679.15],
    ]

# Prompts the user to enter an option
def main_prompt():
    response = input("Choose from one of 3 actions:\n\
        1) Send a Thank You\n\
        2) Create a Report\n\
        3) Quit\n\
        Please type 1, 2, or 3: ")
    return response

# Takes in a user input as a parameter, enters a donation, prints a report,
# prints list, exit, prompts again if the input is bad
# If the user types exit it'll go back to the main prompt
def action(user_input):
    temp_list = []
    createname_list()
    if user_input == 'list':
        for name in name_list:
            print(name)
        action(main_prompt())
    elif user_input == '1':
        donor_name = input("Enter a full name: ")
        if (donor_name != 'exit'):
            temp_list.append(donor_name)
            donation_amt = input("Enter a donation amount: ")
            if (donation_amt != 'exit'):
                temp_list.append(float(donation_amt))
                master_list.append(temp_list)
                printEmail(temp_list)
        action(main_prompt())
    elif user_input == '2':
        printReport()
        action(main_prompt())
    elif user_input == '3':
        quit()
    else:
        action(main_prompt())

# Creates a list of names of distinct donors
def createname_list():
    global master_list
    global name_list
    for name in master_list:
        name_list.append(name[0])
    name_list = list(set(name_list))

# Prints a thank you email to a donator
# Donor name and amount is passed in as a parameter
def printEmail(currentDonation):
    print("Dear {:s},\n\
        Thank you for the generous donation of {:.2f}.\n\
        Sincerely,\n\
        Your Local Charity".format(*currentDonation))

# Prints a report of all the previous donators
# Report includes name, total donated, count of donations, average gift
# Report is also formatted with a certain spacing
def printReport():
    global master_list
    global name_list
    donation_total = []
    for name in name_list:
        donation_sum = 0
        counter = 0
        for name2 in master_list:
            if name2[0] == name:
                donation_sum += name2[1]
                counter += 1
        donation_total.append([name, round(donation_sum,2), counter, round(donation_sum/counter,2)])
    donation_total.sort(key=lambda l: l[1], reverse = True)
    print("Donor Name          |   Total Given  |  Num Gifts |  Average Gift")
    print("-----------------------------------------------------------------")
    for z in range(0, len(donation_total)):
        print('{:20} ${:13.2f}{:14}  ${:13.2f}'.format(*donation_total[z]))

# Python program to use main for function call
if __name__ == "__main__":
    initialize()
    the_input = main_prompt()
    action(the_input)