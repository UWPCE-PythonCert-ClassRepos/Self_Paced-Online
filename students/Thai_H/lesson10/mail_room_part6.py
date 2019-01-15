#!/usr/bin/env python3
import sys
import os
from operator import itemgetter
import copy

#--------------------------------------------------------------------------
def send_thank_you_letter(donor_name, donation_amt):
    #print(donor_name, donation_amt)
    print(f'\nDear {donor_name}\n'
         'Thank you for a recent donation to our Foundation in the amount of $' + f'{donation_amt}\n'
        '\nSincerely'
        '\nBill & Melinda Gates')

#--------------------------------------------------------------------------
def add_donation(donor, amt, membership):
    if membership == 'N':
        list_of_donors[donor] = []
    list_of_donors[donor].append(amt)



#---------------------------------------------------------------------------
def is_existing_donor(donor_name):
    return (donor_name in list_of_donors)


#-----------------------------------------------------------------------------
def send_thank_you_add_new_donation():
    donor_name =input('\n\nPlease enter name of donor:  ')

    try:
        donation_amt = float(input('\nEnter the amount > '))
        divide_by_zero = 1 / donation_amt
    except ZeroDivisionError:
        print ('Can\'t have zero donation amount')
        send_thank_you_add_new_donation()
    else:
        print ('Amount validated: ', float(donation_amt))
        #test_create_report()
        #print('\n')

    #if is_existing_donor(donor_name):
    if donor_name in list_of_donors:
        #print('existing donor is true. before add $$\n')
        #test_create_report()

        # Add amount to existing donor
        #list_of_donors[donor_name].append(donation_amt)
        add_donation(donor_name, donation_amt,'E')

        #--- instead of using this block ------------------------------------
        #for each_donor in list_of_donors:
        #    if donor_name == each_donor['name']:
        #        each_donor['donation'].append(float(donation_amt))
        #-----------------------------------------------------------------

        #we will use this python list comprehension
        #[each_donor['donation'].append(float(donation_amt)) for each_donor in list_of_donors if donor_name == each_donor['name']]
        #test_create_report()

    # New donor
    else:
        #list_of_donors[donor_name] = []
        #list_of_donors[donor_name].append(donation_amt)
        add_donation(donor_name, donation_amt,'N')
    #send thank you letter to the the donor name user just entered
    send_thank_you_letter(donor_name, donation_amt)


#----------------------------------------------------------------------------
def create_thank_you_files():
    for donor_name in list_of_donors.keys():
        total_donation = sum(list_of_donors[donor_name]) #sum(each_donor['donation'])
        thks_letter = open('{name}.txt'.format(name = donor_name), 'w')
        thks_letter.write('Dear {name}, \n'
                          'Thank you for your generosity to our Foundation in the total amount of ${amt}'.format(name = donor_name,
                                                                                                                 amt = total_donation))
        thks_letter.close()

#----------------------------------------------------------------------------
def thank_you_menu_selection():
    user_selection = input('\n\nTHANK-YOU MENU\nChoose from one of options below:\n\
        L) List current donors\n\
        T) Send Thank-you letter (or Add donor and Send one)\n\
        F) Create/Write Thank-you files\n\
        M) Back to MAIN MENU\n\
        Q) Quit the program\n\
        Please type L, T, F, M, or Q: ')
    return user_selection


#-------------------------------------------------------------------------
def thank_you_letter():
    while True:
        # use of dictionary where 'key' is the menu choice and 'value' is function to call
        thank_you_menu_function = {
        'L': create_report,
        'T': send_thank_you_add_new_donation,
        'F': create_thank_you_files,
        'M': main,
        'Q': quit_program
    }
        thank_you_selection = thank_you_menu_selection().upper()
        thank_you_menu_function.get(thank_you_selection, invalid_thank_you_menu)()
        #invalid_menu is to handle non-of-above choices
                                                                #

#----------------------------------------
def sum_donation(d_amt):
    return sum(d_amt)


#-------------------------------------------
def num_of_donation(n_donation):
    return len(n_donation)


#------------------------------------------
def avg_donation(total, nd):
    if nd == 0:
        raise ValueError('can not divide by zero')
    return total / nd


#--------------------------------------------------------------------------
def sort_donor_list(unsorted_list):
    sorted_donation_list = []
    for d in unsorted_list:
        total_donation =  sum_donation(unsorted_list[d])
        number_of_donation = num_of_donation(unsorted_list[d])
        average = avg_donation(total_donation,  number_of_donation)
        sorted_donation_list.append([d, total_donation, number_of_donation, average])

    sorted_donation_list = sorted(sorted_donation_list, key = itemgetter(1), reverse = True)
    return sorted_donation_list

#--------------------------------------------------------------------------
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
def test_create_report():
    for key, item in list_of_donors.items():
        print("{:<20}: {}".format(key, item))





def projection_calculation(threshold, multiplier):
    donation_above_threshold = dict(list((key, list(filter(lambda x : x >= threshold, value))) for key, value in list_of_donors.items()))
    filtered_donations = dict(list((key, list(filter(lambda x : x < threshold, value))) for key, value in list_of_donors.items()))
    adjusted_donation_calc = dict(list((key, list(map(lambda y : y * multiplier, value))) for key, value in filtered_donations.items()))

    for key in donation_above_threshold:
        donation_above_threshold[key].extend(adjusted_donation_calc[key])
    return donation_above_threshold


def donation_projection():
    multiplier = int(input("Enter a multiplier: "))
    min_donation = float(input("Enter minimum donation amt: "))

    projected_donation = projection_calculation(min_donation, multiplier)
    filtered_donation = dict(list((key, list(filter(lambda x: x < min_donation, value))) for key, value in list_of_donors.items()))

    print('\n\n')
    for key in projected_donation:
        if sum(list_of_donors[key]) == sum(projected_donation[key]):
            print('\n{} has no donation less than ${:,.2f}.\nDonor\'s total donation still at: '
                  '${:,.2f}\n'.format(key, min_donation, sum(projected_donation[key])))
        else:
            print('\n{} has {} donations less than ${:,.2f}.\nIf each donation is multiplied by a factor of {},\nthen total donation goes '
                  'from ${:,.2f} to ${:,.2f}\n'.format(    key, len(filtered_donation[key]),
                                                            min_donation, multiplier,
                                                            sum(list_of_donors[key]),
                                                            sum(projected_donation[key])))

#------------------------------------------------------------------------------
def donation_challenge():

    multiplier = int(input('Enter a multiplier: '))
    min_donation = float(input('Enter minimum donation amt: '))
    max_donation = float(input('Enter maximum donation amt: '))

    filtered_donor = dict(list((key, list(filter(lambda x: x >= min_donation and x <= max_donation, value))) for key, value in list_of_donors.items()))

    challenged_donation = dict(list((key, list(map(lambda y: y * multiplier, value))) for key, value in filtered_donor.items()))

    print('\nKeeping only donations between ${:,.2f} and ${:,.2f} and multiplied each by the factor of {}, '
          '\nthe new challenged donations look like this: \n'.format(min_donation, max_donation, multiplier ))
    for key, value in challenged_donation.items():
        print(key, value, ' = ', sum(value))


#------------------------------------------------------------------------------
def init_donor_list():
    # create initial list of donors and their donations
    global list_of_donors
    list_of_donors = {'William Boeing': [100, 200.00, 300.00, 400.00, 500.00],
                      'Steve Jobs':     [600.00, 700.00, 800.00],
                      'Paul Allen':     [900.00, 1000.00, 1100.00],
                      'Charles Flint':  [1200.00, 1300.00, 1400.00],
                      'Thomas Edison':  [1500.00, 1600.00, 1700.00]  }


#------------------------------------------------------------------------------
def main_menu_selection():
    response = input('\n\nMAIN MENU\nChoose from one of the options below:\n\
        T) THANK-YOU MENU\n\
        R) Create a Report\n\
        P) Donation Projection\n\
        C) Donation Challenge\n\
        Q) Quit the program\n\
        Please type T, R, or Q: ')
    return response


#------------------------------------------------------------------------------
def quit_program():
    print('Bye!')
    sys.exit()


#-----------------------------------------------------------------------------
def invalid_menu():
    print('\nNot a valid option!\n\n')
    main()


#-----------------------------------------------------------------------------
def invalid_thank_you_menu():
    print('\nNot a valid option!\n\n')
    thank_you_menu_selection()


#------------------------------------------------------------------------------




#------------------------------------------------------------------------------
def main():
    # use of dictionary where 'key' is the menu choice and 'value' is function to call
    main_menu_options = {
        'T': thank_you_letter,
        'R': create_report,
        'P': donation_projection,
        'C': donation_challenge,
        'Q': quit_program
    }
    while True:
        main_menu_action = main_menu_selection().upper()
        main_menu_options.get(main_menu_action, invalid_menu)() #invalid_menu is to handle
                                                                # non-of-above choices


#------------------------------------------------------------------------------
if __name__ == "__main__":
    init_donor_list()
    main()