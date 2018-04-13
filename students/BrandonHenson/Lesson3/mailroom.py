# Brandon Henson
# 4/8/18
# Lesson 03 mailroom.py

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
