# Brandon Henson
# 4/12/18
# Lesson 04 mailroom_2.py

donor_history = [
            ['Brandon Henson', 1005.49, 3116.72, 5200],
            ['Alicia Henson', 21.47, 1500],
            ['Michael Green', 2400.54],
            ['Brandon Henson Jr', 355.42, 579.31],
            ['Kaiya Henson', 636.9, 850.13, 125.23]
    ]
name_list = []
for i in donor_history:
    q = str(i[0])
    name_list.append(q)


def main_menu():
    menu_answer = input(" Enter '1' for Send a thank you\n Enter '2' for \
Create a report\n Enter '3' for\
 quit\n")
    if menu_answer == '1':
        menu_1()
    elif menu_answer == '2':
        menu_2()
    elif menu_answer == '3':
        exit()
    else:
        print("Enter 1, 2, or 3")
        main_menu()

# If the user (you) selects ‘Send a Thank You’, prompt for a Full Name
def menu_1():
    fullname = input("Enter a full name\n")
# If the user types ‘list’, show them a list of the donor names and re-prompt
    if fullname.lower() == 'list':
        print(name_list)
        menu_1()
    elif fullname in name_list:
        nameindex = (name_list.index(fullname))
        amount = float(input("Donation amount? \n"))
        donor_history[nameindex].append(amount)
        print("Thank you {} for your donation of ${}".format(fullname, amount))
    elif fullname not in name_list:
        new_profile = []
        new_profile.append(fullname)
        name_list.append(fullname)
        amount = float(input("Donation amount? \n"))
        new_profile.append(amount)
        donor_history.append(new_profile)
        nameindex = (name_list.index(fullname))
        print("Thank you {} for your donation of ${}".format(fullname, amount))
    print()
    print()
    main_menu()


def menu_2():
    print("\nDonor Name           |  Total Given | Num Gifts | Average Gift")
    print("---------------------------------------------------------------\n")
    list_names = []
    gifts_num = []
    totals = []
    avg_of_gifts = []
    for donor in donor_history:
        name = donor[0]
        list_names.append(name)
        gifts = len(donor) - 1
        gifts_num.append(gifts)
        total = sum(donor[1:])
        totals.append(total)
        avg_gift = total / gifts
        avg_of_gifts.append(avg_gift)
    for i in range(len(list_names)):
        print(f'{list_names[i]:20s}     ${totals[i]:8n} {gifts_num[i]:10n}\
        ${avg_of_gifts[i]:8n}')
    print()
    print()
    main_menu()

if __name__ == '__main__':
    main_menu()

'''
Use dicts where appropriate
See if you can use a dict to switch between the users selections. See Using a Dictionary to switch for what this means.
Try to use a dict and the .format() method to do the letter as one big template rather than building up a big string in parts.
Example:
In [3]: d
Out[3]: {'first_name': 'Chris', 'last_name': 'Barker'}
In [5]: "My name is {first_name} {last_name}".format(**d)
Out[5]: 'My name is Chris Barker'
Don’t worry too much about the “**” – we’ll get into the details later, but for now it means, more or less, pass this
whole dict in as a bunch of keyword arguments.
Update Mailroom with File Writing
Write a full set of letters to everyone to individual files on disk.
In the first version of mailroom, you generated a letter to someone who had just made a new donation, and printed it
to the screen.
In this version, add a function (and a menu item to invoke it), that goes through all the donors in your donor data
structure, generates a thank you letter, and writes it to disk as a text file.
Your main menu may look something like:
Choose an action:
1 - Send a Thank You
2 - Create a Report
3 - Send letters to everyone
4 - Quit
The letters should each get a unique file name – derived from the donor’s name, and maybe a date.
After running the “send letters to everyone” option, you should get a bunch of new files in the working dir –
one for each donor.
After choosing (3) above, I get these files in the dir I ran it from:
Jeff_Bezos.txt
Mark_Zuckerberg.txt
Paul_Allen.txt
William_Gates_III.txt
(If you want to get really fancy, ask the user for a directory name to write to!)
An example looks like this:
Dear Jeff Bezos,
Thank you for your very kind donation of $877.33.
It will be put to very good use.
Sincerely,
 -The Team
Feel free to enhance it with some more information about past generosity, etc….
The idea is to require you to structure your code so that you can write the same letter to the screen or to disk
 (and thus anywhere else) and also exercise a bit of file writing.
'''