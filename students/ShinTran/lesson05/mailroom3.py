'''
Shin Tran
Python 210
Lesson 5 Assignment
'''

master_list = [] # For all donations made
name_list = [] # For list of unique names


# Creates the master_list where it has 12 donations pre-populated
def initialize():
    global master_list
    master_list = [
        ["Jennifer Miller", 91561.25],
        ["Mary Johnson", 5811.05],
        ["William Rodriguez", 41113.42],
        ["Patricia Brown", 19184.81],
        ["William Rodriguez", 51227.53],
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
    response = input("Choose from one of 4 actions:\n\
        1) Send a Thank You\n\
        2) Create a Report\n\
        3) Send letters to everyone\n\
        4) Quit\n\
        Please type 1, 2, 3, or 4: ")
    return response

# Takes in a user input as a parameter, enters a donation, prints a report,
# prints list, exit, prompts again if the input is bad
# If the user types exit it'll go back to the main prompt
def action(user_input):
    create_name_list()
    switch_dict = {
        'list': list_func,
        '1': send_thanks,
        '2': print_report,
        '3': send_letters,
        '4': exit_quit
    }
    try:
        switch_dict.get(user_input)()
    except (TypeError, ValueError):
        print("Invalid input, {} please try again.".format(user_input))
        action(main_prompt())
    else:
        action(main_prompt())

# Prints a list of all the distinct donors
def list_func():
    for name in name_list:
        print(name)

# Creates a list of names of distinct donors
def create_name_list():
    global master_list
    global name_list
    for name in master_list:
        name_list.append(name[0])
    name_list = list(set(name_list))

# Prompts the user to type a name of a donor, enter a donation amount,
# prints an email thanking the donor
# If the user types exit, it would return to the main prompt
def send_thanks():
    temp_list = []
    donor_name = input("Enter a full name: ")
    if (donor_name != 'exit'):
        temp_list.append(donor_name)
        donation_amt = input("Enter a donation amount: ")
        if (donation_amt != 'exit'):
            temp_list.append(float(donation_amt))
            master_list.append(temp_list)
            print_email(temp_list)

# Prints a thank you email to a donator
# Donor name and amount is passed in as a parameter
def print_email(currentDonation):
    print("Dear {:s},\n\
        Thank you for the generous donation of ${:,.2f}.\n\
        Sincerely,\n\
        Your Local Charity".format(*currentDonation))

# Prints a report of all the previous donators
# Report includes name, total donated, count of donations, average gift
# Report is also formatted with a certain spacing
def print_report():
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
        print('{:20} ${:13,.2f}{:14}  ${:13,.2f}'.format(*donation_total[z]))

# Goes through all the previous donators, gets their total donated,
# sends a thank you letter that is output on a .txt file
def send_letters():
    global master_list
    global name_list
    donation_sum = 0
    message = "Dear {:s},\n\
    Thank you for the your generous total donation of ${:,.2f}.\n\
    Sincerely,\n\
    Your Local Charity"
    for name in name_list:
        output = open(name + ".txt",'w')
        for name2 in master_list:
            if name2[0] == name:
                donation_sum += name2[1]
        output.write(message.format(name, donation_sum))
        donation_sum = 0
    output.close()

# Closes out of the prompt and ends the program
def exit_quit():
    quit()

# Python program to use main for function call
if __name__ == "__main__":
    initialize()
    action(main_prompt())