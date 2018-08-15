'''
Shin Tran
Python 210
Lesson 5 Assignment
'''

master_dict = {"Jennifer Miller": [145076.19,2],
    "William Rodriguez": [161585.16,3],
    "Patricia Brown": [100863.96,2]
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
    name_list = [k for k, v in master_dict.items()]
    for name in name_list:
        print(name)
    return name_list

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
            if donor_name in master_dict:
                temp_list2 = master_dict.pop(donor_name)
                master_dict[donor_name] = [temp_list[1]+temp_list2[0],temp_list2[1]+1]
            else:
                master_dict[donor_name] = [temp_list[1],1]
            print(print_email(temp_list))

# Prints a thank you email to a donator
# Donor name and amount is passed in as a parameter
def print_email(currentDonation):
    return "Dear {:s},\n\
        Thank you for the generous donation of ${:,.2f}.\n\
        Sincerely,\n\
        Your Local Charity".format(*currentDonation)

# Goes through all the previous donators, gets their total donated,
# sends a thank you letter that is output on a .txt file
def send_letters():
    letter_list = []
    message = "Dear {:s},\n\
    Thank you for donating ${:,.2f}.\n\
    Sincerely,\n\
    Your Local Charity"
    for name, vals in master_dict.items():
        with open(name + ".txt",'w') as output:
            output.write(message.format(name, vals[0]))
            letter_list.append(message.format(name, vals[0]))
    return letter_list

# Prints a report of all the previous donators
# Report includes name, total donated, count of donations, average gift
# Report is also formatted with a certain spacing
def print_report():
    donation_total = [[key, round(val[0],2), val[1], round(val[0]/val[1],2)] for key, val in master_dict.items()]
    donation_total.sort(key=lambda l: l[1], reverse = True)
    s1 = "Donor Name          |   Total Given  |  Num Gifts |  Average Gift\n"
    s2 = "-----------------------------------------------------------------\n"
    final_string = s1 + s2
    for z in range(0, len(donation_total)):
        s3 = '{:20} ${:13,.2f}{:14}  ${:13,.2f}\n'.format(*donation_total[z])
        final_string += s3
    print(final_string)
    return final_string

# Python program to use main for function call
if __name__ == "__main__":
    action(main_prompt())