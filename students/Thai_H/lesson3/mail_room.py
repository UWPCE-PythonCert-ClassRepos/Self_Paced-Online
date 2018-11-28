#!/usr/bin/env python3
import sys

def send_thank_you_letter(donor_name, donation_amt):
    print(f'\nDear {donor_name}\n'
         'Thank you for a recent donation to our Foundation in the amount of $' + f'{donation_amt}\n'
         '\nSincerely'
         '\nBill & Melinda Gates')

def is_existing_donor(donor_name):
    tmp_donor_list = []
    for each_donor in list_of_donors:
        tmp_donor_list.append(each_donor[0])
    return donor_name in tmp_donor_list # returns True if existing donor, False if new donor


def send_thank_you_add_new_donation():
    donor_name =input('\n\nPlease enter name of donor:  ')
    donation_amt = input('\nEnter the amount > ')
    if is_existing_donor(donor_name):
        for each_donor in list_of_donors:
            if donor_name == each_donor[0]:  #[0] is existing donor name
                each_donor[1].append(float(donation_amt))

    # New donor
    else:
        new_donor_name_amt = [donor_name,[float(donation_amt)]]
        list_of_donors.append(new_donor_name_amt)
    # send thank you letter to the the donor name user just entered
    send_thank_you_letter(donor_name, donation_amt)

def thank_you_menu_selection():
    user_selection = input('\n\nTHANK-YOU MENU\nChoose from one of options below:\n\
        L) List current donors\n\
        T) Send Thank-you letter (or Add donor and Send one)\n\
        M) Back to MAIN MENU\n\
        Q) Quit the program\n\
        Please type L, N, or B: ')
    return user_selection
#-------------------------------------------------------------------------

def thank_you_letter():
    while True:
        thank_you_selection = thank_you_menu_selection()

        if thank_you_selection.upper() == 'L':
            create_report()
        elif thank_you_selection.upper() == 'T':
            send_thank_you_add_new_donation()
        elif thank_you_selection.upper() == 'M':
            main()
        elif thank_you_selection.upper() == 'Q':
            exit_program()
        else:
            print('\n\nNot a valid option!\n\n')
#--------------------------------------------------------------------------


def sort_donor_list(unsorted_list):
    sorted_donation_list = []
    for d in unsorted_list:
        total_donation =  float(sum(d[1]))
        number_of_donation = int(len(d[1]))
        average = total_donation / number_of_donation
        sorted_donation_list.append([d[0], total_donation, number_of_donation, average])
    #
    sorted_donation_list.sort(key = sort_by_total_donation, reverse = True)

    return sorted_donation_list

def sort_by_total_donation(sorted_donation_list):
    return sorted_donation_list[1]


#------------------------------------------------------------------------------
def create_report():
    sorted_list = sort_donor_list(list_of_donors)
    report_header = ['Donor Name', 'Total Donation Amt', 'Num of Donation',  'Avg Per Donation']
    print('\n\n{:<25}{:>20}{:>20}{:>20}'.format(*report_header))
    print('-'*90)
    for donor in sorted_list:
        print('{:<26}${:>15,.2f}{:>15}{:>25,.2f}'.format(donor[0], donor[1], donor[2], donor[1] / donor[2]))
    print('\n\n')
#------------------------------------------------------------------------------
def init_donor_list():
    # create initial list of donors and their donations
    global list_of_donors
    list_of_donors = [
                ['William Boeing', [12.86, 2.00, 3.00, 4.00, 5.00]],
                ['Steve Jobs', [6.00, 7.00, 8.00]],
                ['Paul Allen', [9.00, 10.00, 11.00]],
                ['Charles Flint', [12.00, 13.00, 14.00]],
                ['Thomas Edison', [15.00, 16.00, 17.00]]
            ]
#------------------------------------------------------------------------------
def menu_selection():
    response = input('\n\nMAIN MENU\nChoose from one of the options below:\n\
        T) THANK-YOU MENU\n\
        R) Create a Report\n\
        Q) Quit the program\n\
        Please type T, R, or Q: ')
    return response
#------------------------------------------------------------------------------
def exit_program():
    print('Bye!')
    sys.exit()
#------------------------------------------------------------------------------
def main():
    while True:
        init_donor_list()
        menu_action = menu_selection()
        if menu_action.upper() == 'T':
            thank_you_letter()
        elif menu_action.upper() == 'R':
            create_report()
        elif menu_action.upper() == 'Q':
            exit_program()
        else:
            print('\n\nNot a valid option!\n\n')
#------------------------------------------------------------------------------
if __name__ == "__main__":
    main()