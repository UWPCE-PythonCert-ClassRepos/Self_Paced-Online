'''
Shin Tran
Python 210
Lesson 5 Assignment
'''

master_dict = {"Jennifer Miller": [145076.19,2],
    "Mary Johnson": [90146.28,3],
    "William Rodriguez": [161585.16,3],
    "Patricia Brown": [100863.96,2],
    "Michael David": [88196.96,2]
} # For all donations made

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
    switch_dict = {
        'list': list_func,
        '1': send_thanks,
        '2': print_report,
        '3': send_letters,
        '4': quit
    }
    try:
        switch_dict.get(user_input)()
    except (TypeError, ValueError):
        print("Invalid input, {} please try again.".format(user_input))
        action(main_prompt())
    else:
        action(main_prompt())

# Creates a list of all the distinct donors
def list_func():
    for name in master_dict:
        print(name)

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
            #master_dict.append(temp_list)
            if donor_name in master_dict:
                temp_list2 = master_dict.pop(donor_name)
                master_dict[donor_name] = [temp_list[1]+temp_list2[0],temp_list2[1]+1]
            else:
                master_dict[donor_name] = [temp_list[1],1]
            print_email(temp_list)

# Prints a thank you email to a donator
# Donor name and amount is passed in as a parameter
def print_email(currentDonation):
    print("Dear {:s},\n\
        Thank you for the generous donation of ${:,.2f}.\n\
        Sincerely,\n\
        Your Local Charity".format(*currentDonation))

# Goes through all the previous donators, gets their total donated,
# sends a thank you letter that is output on a .txt file
def send_letters():
    message = "Dear {:s},\n\
    Thank you for the your generous total donation of ${:,.2f}.\n\
    Sincerely,\n\
    Your Local Charity"
    for name, vals in master_dict.items():
        with open(name + ".txt",'w') as output:
            output.write(message.format(name, vals[0]))

# Prints a report of all the previous donators
# Report includes name, total donated, count of donations, average gift
# Report is also formatted with a certain spacing
def print_report():
    donation_total = []
    for name, vals in master_dict.items():
        donation_total.append([name, round(vals[0],2), vals[1], round(vals[0]/vals[1],2)])
    donation_total.sort(key=lambda l: l[1], reverse = True)
    print("Donor Name          |   Total Given  |  Num Gifts |  Average Gift")
    print("-----------------------------------------------------------------")
    for z in range(0, len(donation_total)):
        print('{:20} ${:13,.2f}{:14}  ${:13,.2f}'.format(*donation_total[z]))

# Python program to use main for function call
if __name__ == "__main__":
    action(main_prompt())