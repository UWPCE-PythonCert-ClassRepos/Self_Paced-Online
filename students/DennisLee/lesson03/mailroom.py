#!/usr/bin/env python3

# List of donors and amounts they have donated
donor_history = [
            ['Red Herring', 65820.5, 31126.37, 15000],
            ['Papa Smurf', 210.64, 1000],
            ['Pat Panda', 55324.4],
            ['Karl-Heinz Berthold', 3545.2, 10579.31],
            ['Mama Murphy', 156316.99, 8500.3, 12054.33],
            ['Daphne Dastardly', 82]
        ]

def manage_donors():
    choices = ("Send a Thank You", "Create a Report", "Quit")
    while True:
        print()
        for i, j in enumerate(choices):
            print(i + 1, j)
        response = ''
        while not response.isdigit() or int(response) not in range(
                1, len(choices) + 1):
            response = input("Type your selection: ").strip()
        response = int(response)
        if response == 1:
            send_thank_you()
        elif response == 2:
            create_a_report()
        elif response == 3:
            print("\nGoodbye.\n")
            return
        
def send_thank_you():
    options = ('quit', 'list')
    donors = [x[0] for x in donor_history]
    response = input(
      "\nType the full donor name (or 'list' to show all donors, or 'quit'): "
      ).strip()
    if response.lower() == 'quit':
        return
    elif response.lower() == 'list':
        print("\nLIST OF DONORS:", donors)
        send_thank_you()
    else:
        if response not in donors:
            donors.append(response)
            donor_history.append([response])
        donation = ''
        while not donation.isnumeric() or float(donation) <= 0.0:
            donation = input(f"Enter a new donation amount for '{response}': ")
        donor_history[donors.index(response)].append(float(donation))
        pass # Implement email thank you letter here

def create_a_report():
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

if __name__ == "__main__":
    manage_donors()