################################################################################
# Revision 1
# - Use dicts where appropriate
# - Use a dict to switch between user selections
# - Use a dict & format method to do the letter as one big template
#       .format(**dict) -> passes in dict as keyword args
################################################################################

################################################################################
# Revision 2
# - Adds a menu item to send a letter to all donors and writes a multi-line
# thank you letter to the disk as a text file -> fname_lname.tx
################################################################################

"""
Thomas Horn
mailroom.py
Tracks donor information and automates the sending of thank you notes.
"""

# Original Global that holds donor history and the amounts donated.
# donors = [
#     ['Tom Horn',        [599.23, 1000.00]],
#     ['Theo Hartwell',   [0.01, 0.01, 0.1]],
#     ['Bailey Kimmitt',  [8723.22, 27167.22, 91817.66]],
#     ['Paul Hubbell',    [90012.32, 2312.24]],
#     ['David Beckham',   [1817266.11, 123123.66, 111335.112]]
# ]

# Dict version of above var.
donors = {
    'Tom Horn':        [599.23, 1000.00],
    'Theo Hartwell':   [0.01, 0.01, 0.1],
    'Bailey Kimmitt':  [8723.22, 27167.22, 91817.66],
    'Paul Hubbell':    [90012.32, 2312.24],
    'David Beckham':   [1817266.11, 123123.66, 111335.112]
}

def send_thanks():
    """
    Prompts user for a full name and performs an action based on the input.
    - 'list' -> shows a list of donor names and re-prompts
    - Name not in list -> adds the name to the data structure and uses it
    - Name in list -> use it
    After name is used -> prompt for donation amount and turn into a number.
    - Add that amount to donation history of selected user
    - Print thank you note
    - Returns to original prompt or quit to prompt
    """
    name_request = input("Please enter a donor's full name, or 'list' for a full list of donors.  'Quit' or 'Return' valid commands. ")

    # Return or Quit.
    if name_request.lower() == "quit":
        quit()

    if name_request.lower() == "return":
        return

    # List request - only donors returned.
    if name_request.lower() == 'list':
        for donor in donors:
            print(donor)

    name_request = name_request.title()
    donation_amount = float(input(("Please enter a donation amount for {}: ".format(name_request))))

    # Add to existing donor or put new donor and amount in the list.
    if name_request in donors.keys():
        donations = list(donors.get(name_request))
        donations.append(donation_amount)
        donors[name_request] = donations
        print(f"Thank you {name_request.title()} for your donation of ${donation_amount:.2f}.\n")
        return

    donors[name_request] = [donation_amount]
    print(f"Thank you {name_request.title()} for your donation of ${donation_amount:.2f}.\n")


def create_report():
    """
    Prints a list of donors sorted by total historical donation amount.
    - Includes donor name, total donated, number of donations, average donation
      amount.
    - $ Total - 27 spaces in, right justified
    """
    print("Donor:                    | $    Total     |   Donations   | $   Average   |")
    print("-"*76)
    for item in donors:
        amt_total = float(sum(donors[item]))
        num_total = int(len(donors[item]))
        # Thousand separator as default. Careful with the space if we get some big donors.
        print("{:<26}| ${:>14,.2f}|{:>15}| ${:>13,.2f}".format(item, amt_total, num_total, amt_total/num_total))
    print('\n')


if __name__ == "__main__":
    # Select from options.  No checks to sanatize input.
    while True:
        choice = input(
        "Please select an option:\n\
        1 - Send Thanks\n\
        2 - Create Donor Report\n\
        3 - Quit\n")
        print()
        if choice == "1":
            send_thanks()
        elif choice == "2":
            create_report()
        elif choice == "3":
            print("Quitting.")
            break

