#!/usr/bin/env python3

# Initial donor list and the amounts they have donated
donor_history = [
            ['Red Herring', 65820.5, 31126.37, 15000],
            ['Papa Smurf', 210.64, 1000],
            ['Pat Panda', 55324.4],
            ['Karl-Heinz Berthold', 3545.2, 10579.31],
            ['Mama Murphy', 156316.99, 8500.3, 12054.33],
            ['Daphne Dastardly', 82]
        ]

def manage_donors():
    """
    Display the menu of choices for donor management.

    :return:  None.
    """
    choices = ("Send a Thank You", "Create a Report", "Quit")
    while True:  # Infinite loop until user chooses to exit
        # Print the menu list (with numbered choices)
        print()
        for i, j in enumerate(choices):
            print(i + 1, j)

        # Get the selection number
        response = ''
        while not response.isdigit() or int(
                response) not in range(1, len(choices) + 1):
            response = input("Type your selection: ").strip()
        response = int(response)

        # Call helper functions or exit
        if response == 1:
            send_thank_you()
        elif response == 2:
            create_a_report()
        elif response == 3:
            print("\nGoodbye.\n")
            return
        
def send_thank_you():
    """
    Add new donations for new or existing donors, and send a thank-you
    letter.

    :return:  None.
    """
    donors = [x[0] for x in donor_history]  # Get list of donor names

    # Get the donor name, show all donors, or quit
    response = input(
      "\nType the full donor name (or 'list' to show all donors, or 'quit'): "
      ).strip()

    if response.lower() == 'quit':
        return

    elif response.lower() == 'list':
        print("\nLIST OF DONORS:", donors)
        send_thank_you()  # Try getting a donor name again

    else:
        if response not in donors:  # Add to donor list if it's a new name
            donors.append(response)
            donor_history.append([response])

        donation = '...'  # Seed donation variable to continue the while loop
        # Make sure the donation amount is a valid, positive number
        while donation.count('.') > 1 or donation.strip('0123456789.'
                ) != '' or float(donation) <= 0.0:
            donation = input(
                    f"Type amount donated by '{response}' (or type 'quit'): "
                    ).strip().lower()
            if donation == 'quit':
                return

        # Add the donation to the master donor history and print the letter
        donation = float(donation)
        donor_history[donors.index(response)].append(donation)
        print(create_form_letter(response, donation))

def create_a_report():
    """
    Print out statistics for the entire donor list.

    :return:  None.
    """
    print('\n')
    print('Donor name                |         Total given | '
            + 'Number of gifts |        Average gift')
    print('--------------------------|---------------------|-'
            + '----------------|--------------------')
    for individual_donor in donor_history:
        total_donation = sum(individual_donor[1:])
        number_of_gifts = len(individual_donor) - 1
        average_donation = 1.0 * total_donation / number_of_gifts
        print('{:<25s} | ${:>18,.2f} | {:>15d} | ${:>18,.2f}'.format(
                individual_donor[0], total_donation,
                number_of_gifts, average_donation))

def create_form_letter(donor_name, donor_amount):
    """
    Create the form letter using the donor name and amount.

    :donor_name:  The name of the donor.

    :donor_amount:  The amount given by the donor this time.

    :return:  A string containing the filled-in form letter.
    """
    str = """\n\n\n
            From:     Random Worthy Cause Foundation
            To:       {0:s}
            Subject:  Your generous donation

            Dear {0:s},

            We want to express our genuine gratitude for your donation of
            ${1:,.2f} to the Random Worthy Cause Foundation.  To show our
            appreciation, we have enclosed a set of address labels
            and a custom tote bag that lets people know that you are a
            generous supporter of our cause.
            
            Thank you again, and please think of us the next time you want
            to give to a worthy cause.

            Sincerely,



            Mister E. Partner
            Random Worthy Cause Foundation
            """
    
    return str.format(donor_name, donor_amount)

if __name__ == "__main__":
    manage_donors()
