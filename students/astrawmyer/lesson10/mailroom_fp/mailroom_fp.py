#!/usr/bin/env python3

import mailroom_oo_classes as mc


def thank_you():
    """Function to send a thank you letter."""
    while True:
        input_name = input("Enter full name: ")
        if input_name in donor_set.data.keys():
            while True:
                try:
                    donation = float(input("Enter donation amount:"))
                except ValueError:
                    print("Donation needs to be a number.")
                else:
                    break
            donor_set.add_donation(input_name,donation)
            #ddonors[input_name].append(donation)
            print(donor_set.write_letter(input_name,donation))
            break
        elif input_name == 'list':
            donor_set.display_list()
            
        else:
            print("Adding {} to donor database".format(input_name))
            while True:
                try:
                    donation = float(input("Enter donation amount:"))
                except ValueError:
                    print("Donation needs to be a number.")
                else:
                    break
            new_guy = mc.Donor(input_name,[donation])
            donor_set.new_donor(new_guy)
            print(donor_set.write_letter(input_name,donation))
            #print(ddonors)
            break

 
if __name__ == "__main__":
    # Adding this to import preset data.
    a = mc.Donor("James Hinchcliffe", [12.2,2.51,3.20])
    b = mc.Donor("Robert Wickens", [1024.14,22.21,323.45])
    c = mc.Donor("Sam Schmidt", [3.2,5.55,4.20])
    donor_set = mc.Donors()
    donor_set.new_donor(a)
    donor_set.new_donor(b)
    donor_set.new_donor(c)

    # Actual code.
    main_switch_function = {"1": thank_you, "2": donor_set.write_report, "3": donor_set.letter_files, "4": exit}
    while True:
        print("What do you want to do?")
        response = input("1. Send a Thank You, 2. Create a Report, 3. Send all letters, 4. Quit: ")
        try:
            main_switch_function.get(response)()
        except TypeError:
            print("Not a valid input.")