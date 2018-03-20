#!/usr/bin/env python3

donations = {}
donations['papa'] = [100, 5, 15]
donations['mama'] = [12, 200, 2, 66]
donations['bompa'] = [1000]
donations['bobonne'] = [500, 500]
donations['onbekende'] = [1000000]


def thankyou():
    """If the user types ‘list’, show them a list of the donor names and re-prompt
    If the user types a name not in the list, add that name to the data structure
    and use it.
    If the user types a name in the list, use it.
    Once a name has been selected, prompt for a donation amount.
    Turn the amount into a number – it is OK at this point for the program to
    crash if someone types a bogus amount.
    Once an amount has been given, add that amount to the donation history of
    the selected user.
    Finally, use string formatting to compose an email thanking the donor for their
    generous donation. Print the email to the terminal and return to the original
    prompt."""
    while True:
        name = input('Please enter a name or type "list" to see a list of names > ')
        if name == 'list':
            print(donations.keys())
        else:
            break
    if name not in donations.keys():
        donations[name] = []
    try:
        donation = input('Please enter a donation amount > ')
        donations[name].append(int(donation))
    except ValueError:
        while not donation.isdigit():
            print("You didn't enter a valid amount.")
            donation = input('Please enter a donation amount > ')
        donations[name].append(int(donation))
    d = {'name':name, 'donation':donation}
    print("Dear {name} , thank you very much for your generous donation of {donation}. Looking forward receiving even more money next time.".format(**d))
    print(donations.keys())
    print(donations.values())


def createfile(name):
    '''create .txt file containing thank you letter for each person who made a donation'''
    d = {'name':name, 'donation':donations[name][-1]}
    outfile = open(name+'.txt', 'w')
    outfile.write("Dear {name} , \n\n".format(**d))
    outfile.write("\t Thank you very much for your generous donation of ${donation}. \n\n".format(**d))
    outfile.write("\t It will be put to very good use. \n\n")
    outfile.write("\t\t Sincerely, \n")
    outfile.write("\t\t   -The Team \n")
    outfile.close()


def thankyoueveryone():
    [createfile(name) for name in donations.keys()]


def report():
    """ If the user (you) selected “Create a Report”, print a list of your donors,
     sorted by total historical donation amount.
     Include Donor Name, total donated, number of donations and average donation
     amount as values in each row. You do not need to print out all their
     donations, just the summary info.
     Using string formatting, format the output rows as nicely as possible.
     The end result should be tabular (values in each column should align with
     those above and below)
     After printing this report, return to the original prompt.
     At any point, the user should be able to quit their current task and return
     to the original prompt.
     From the original prompt, the user should be able to quit the script cleanly."""
    print(f'{"Donor Name":20s} {"|  Total Given":20s} {"|  Num Gifts  |":20s} {"Average Gift":20s}')
    print(f'{"-"*76}')
    [print(f'{name:20s} ${sum(donations[name]):20.2f} {len(donations[name]):13d}${sum(donations[name])/len(donations[name]):20.2f}') for name in donations.keys()]


if __name__ == '__main__':
    response = input('Please choose between the following 3 actions:\
    1. Send a Thank You; 2. Create a Report; 3. Send letters to everyone; 4. quit >  ')
    try:
        int(response)
    except:
        while not response.isdigit():
            print("You didn't enter a number.")
            print()
            response = input('Please choose between the following 3 actions:\
            1. Send a Thank You; 2. Create a Report; 3. Send letters to everyone; 4. quit >  ')
    arg_dict = {1:thankyou, 2:report, 3:thankyoueveryone}
    while int(response) != 4:
        try:
            arg_dict.get(int(response))()
        except (TypeError, ValueError):
            print('This is an invalid choice. Please enter a number between 1 and 4.')
            print()
            response = input('Please choose between the following 3 actions:\
            1. Send a Thank You; 2. Create a Report; 3. Send letters to everyone; 4. quit >  ')
        else:
            response = input('Please choose between the following 3 actions:\
                1. Send a Thank You; 2. Create a Report; 3. Send letters to everyone; 4. quit >   ')
        finally:
            if not response.isdigit():
                response = '99999'
