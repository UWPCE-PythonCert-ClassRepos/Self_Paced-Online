#!/usr/bin/env python3

DONOR_DB = {"Wassily Kandinsky": [43928.13, 131.34, 1928.0],
            "Jasper Johns": [3134.43, 153.34],
            "Mark Rothko": [135353.33],
            "Richard Serra": [153757.87, 28457.12, 1293451.0],
            "Yves Tanguy": [1534.23, 2542.19]}





def thank_you():
    thanks = True
    while thanks:
        user_in = input("Type List to view all donor names, type a current donor name, or type the name of a new donor: ")
        if user_in.lower() == "list": 
            for key in DONOR_DB:
                print(key)
        else:
            for key, value in DONOR_DB.items():
                if user_in.title() == key:
                    user_in = user_in.title()
                    donation = float(input(f"Add a donation amount for {key}: $"))
                    DONOR_DB[key].append(donation)
                    print(f"\nDear {key},\n\nThank you so much for your donation of ${value[-1]}.\n\nSincerely,\n\nThe Mailroom\n")
                    print(DONOR_DB)
                    thanks = False
                    break 
            else:
                user_in = user_in.title()
                donation = float(input(f"Add a donation amount for {user_in}: $"))
                DONOR_DB[user_in] = [donation]
                print(f"\nDear {user_in},\n\nThank you so much for your donation of ${donation}.\n\nSincerely,\n\nThe Mailroom\n")
                print(DONOR_DB)
                thanks = False


thank_you()