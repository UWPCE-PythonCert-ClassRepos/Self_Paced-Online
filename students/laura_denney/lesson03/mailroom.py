#-------------------------------------------------#
# Title: Mail Room Part 1
# Dev:   LDenney
# Date:  October 11, 2018
# ChangeLog: (Who, When, What)
#   Laura Denney, 10/11/18, Created File
#   Laura Denney, 10/12/18, Modified File
#-------------------------------------------------#

tabl = [["john doe", 100, 200], ["laura denney", 5],
        ["bill gates", 4000], ["samuel jackson", 1, 2, 3],
        ["mr. bean", 500, 100]]

#Main menu to prompt user
def prompt_user():
    response = ""
    while response != "3":
        response = input('''
What would you like to do today?
1) Send a Thank You
2) Create a Report
3) Quit
Please choose the number of your choice >> ''')
        if response == "1":
            send_thank_you()
        elif response == "2":
            create_report()
        elif response == "3":
            continue
        else:
            print("\nThat is not a valid selection. Please choose 1, 2 or 3.")
    else:
        print("\nYou have chosen to quit. Have a good day!")

def send_thank_you():
    print("\nYou have chosen to Send a Thank You.")
    name = "list"
    while name.lower() == 'list':
        print("Please enter the full name of the donor you would like to thank")
        name = input("OR type 'list' to see current donors. >> ")
        if name.lower() == "list":
            print_list()
        else:
            donor, amount = check_list(name.lower())
            send_email(donor, amount)
    print("You have successfully sent a Thank You.")

def print_list():
    names = []
    for item in tabl:
        names += [item[0].title()]
    strformat = "\nWe have {} current donors: " + ", ".join(["{}"] * len(names))
    print(strformat.format(len(names), *names))

def check_list(name):
    for x in tabl:
        if name in x:
            print("\n{} is a current donor.".format(name.title()))
            num = input("How much money did they donate? (type 100 for $100) >> ")
            try: #validate donation amount entered is a number
                num = float(num)
                x.append(num)
                return name.title(), num
            except:
                print("Invalid amount entered, marking donation as $0.")
                x.append(0)
                return name.title(), 0
    else: #not a current donor
        print("\n{} is not a current donor, we will add them to our list.".format(name.title()))
        num = input("How much did they donate? (type 100 for $100) >> ")
        try: #validate donation is number
            num = float(num)
            tabl.append([name, num])
            return name.title(), num
        except:
            print("\nInvalid amount entered, marking donation as $0.")
            tabl.append([name, 0])
            return name.title(), 0

def send_email(donor, amount):
    print("\nThe email you are sending is as follows:")
    fstring =f'''
    Dear {donor},

    We would like to thank you for your generous donation
    of ${amount}. Thank you!

    Cheers,
    The MailRoom
    '''
    print(fstring)

def create_report():
    print("\nYou have chosen to Create a Report.")
    header = '''
Donor Name                | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------'''
    print(header)
    strformat = '{:<26}${:>13}{:^12}${:>13}'
    for row in tabl:
        sumamount = sum(row[1:])
        numberdonations = len(row[1:])
        average = sumamount/numberdonations
        print(strformat.format(row[0].title(),round(sumamount,2), numberdonations, round(average,2 )))

if __name__ == "__main__":
    prompt_user()
