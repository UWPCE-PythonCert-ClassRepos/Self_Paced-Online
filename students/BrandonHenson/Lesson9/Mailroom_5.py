# Brandon Henson
# 5/16/18
# Lesson 09 mailroom_5.py
# Refactoring

class Donor:
    def __init__(self,name,donation = None):
        donation = []
        self.name = name
        self.donation = donation
        self.total_donation = sum(self.donation)




'''
donor_history = {'Brandon Henson': [1005.49, 3116.72, 5200],
                    'Alicia Henson': [21.47, 1500],
                    'Michael Green': [2400.54],
                    'Brandon Henson Jr': [355.42, 579.31],
                    'Kaiya Henson': [636.9, 850.13, 125.23]}

def names():
    name_list = [i for i in donor_history]
    return name_list
def email_all():
    for key, values in donor_history.items():
        filename = str(key)+'.txt'
        with open(filename, 'w') as fileobj:
            total = sum(values)
            numgifts = len(values)
            fileobj.write("Dear {}\nThank you for your {} generous donations \
totaling ${}\nThe money will be put to good use.\n\n\
        Sincerely, \n                -The Team".format(key, numgifts, total))
        fileobj.close()


def main_menu():
    arg_dict = {
        '1': menu_1,
        '2': menu_2,
        '3': email_all,
        '4': exit
    }

    prompt = '\nSelect an option:\n' \
             '[1] Send a Thank You\n' \
             '[2] Create a Report\n' \
             '[3] Send letters to everyone\n' \
             '[4] Exit\n' \

    menu_selection(prompt, arg_dict)


def menu_selection(prompt, arg_dict):
    try:
        while True:
            response = input(prompt)
            arg_dict[response]()
    except KeyError:
        print("Enter 1,2,3, or 4")



def menu_1():
    try:
        fullname = input("Enter a full name or 'list' to view all\n")
        if fullname.lower() == 'list':
            names()

        elif str(fullname) in donor_history:
            amount = int(input("Donation amount? \n"))
            newvalue = donor_history.get(fullname) + [amount]
            donor_history[fullname] = newvalue
            print("Dear {}\nThank you for your generous donation of ${}\nIt will \
     be put to good use.\n\n Sincerely,\n\
            -The Team".format(fullname, amount))
        elif str(fullname) not in donor_history:
            amount = int(input("Donation amount? \n"))
            donor_history[fullname] = amount
            print("Dear {}\nThank you for your generous donation\
     of ${}\nIt will be put to good use.\n\n Sincerely,\n\
            -The Team".format(fullname, amount))
    except ValueError:
        print("Please enter a number for the amount.")


def menu_2():
    try:
        print("\nDonor Name         |  Total Given | Num Gifts | Average Gift")
        print("------------------------------------------------------------\n")
        report = list()
        for donor, total in donor_history.items():
            report.append([donor, sum(total), len(total), sum(total)/len(total)])
        sorted_report = sorted(report, key=lambda x: -x[1])

        for i in sorted_report:
            print("{:<20}   ${:>8} {:>8}        ${:<1}".format(
                i[0], i[1], i[2], i[3]))
    except TypeError:
        print()

if __name__ == '__main__':
    main_menu()
'''

'''
As you design appropriate classes, keep in mind these three guidlines for good code structure:
Encapsulation: you have a data structure that holds your data, and you have functions that manipulate that data –
you want them “bundled up” in a neat package, so that the rest of the code doesn’t need to know about the data structure 
you are using.

Separation of Concerns: The user interaction code should be cleanly separated from the data handling code.
There should be no input function in the class that holds the data!

As always: DRY – Don’t repeat yourself – anywhere you see repeated code – refactor it!
SuggestionsOne of the hardest parts of OO design (particularly in Python) is to know how “low” to go with the classes
and data structures. In particular, you might have a bit of data collected together (say, a donor’s name and donation
history), This can be a simple tuple with a few items in it, it can be a dict with those same data available as key:value pairs,
 or it can be a class, with class attributes (and maybe methods).
There are no hard and fast rules, but I’ll try to provide guidelines:
For this assignment, it’s OK to go with simple tuples. However, in order for the code to be more flexible in the
future (for example if new “fields” were added to the donor object) it’s probably better to use a more structured
type, so you don’t have to worry about changing the order, etc of fields.
So now you have to think about whether to use dict or class, Again, for flexibility, I think a dict is a bit easier
– you can add fields to it very easily. However, with a class, you can build some functionality in there, too.
This is where encapsulation comes in – for instance, one thing you might want to do is get the total of all donations
a donor has made in the past. If you add a method to compute that (or a property!), then the rest of the code doesn’t
need to know how the donations are stored.
So: if you want my hints :-)…
You’ll want a Donor class – this will hold all the information about the donor, and have attributes and methods to
provide access to the donor specific information that is needed.
You’ll then want a class that handles the collection of donors. This will hold all the donor objects, but also methods
to add a new donor, search for a given donor, etc. If you want a way to save and re-load your data, this class would have that too.
Your class for the collection of donors will also hold the code that generates reports about multiple donors.
In general, you will have a method for each of the functions in your non-OO version. Which class they go in will
depend on whether the method only needs the information from one donor or from the whole collection.
'''