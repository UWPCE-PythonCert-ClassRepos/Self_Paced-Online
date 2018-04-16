def main_menu():
    choice = input(
        'Pick one:\n1) Send a thank you\n2) Create a Report\n3) Send letters to everyone\n4) Projections\n5) Quit\n'
        )
    return choice


def set_donor_name():
    donor_name = input(
                'Enter the donor\'s name: (type list if you want to get a list of donors)\n'
    )
    return donor_name
