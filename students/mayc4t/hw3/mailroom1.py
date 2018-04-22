#!/usr/bin/env python3
# #############################################################################
# Written By: Mayc4t
# March 21, 2018
# Self-paced Python

# #############################################################################

dn0 = ['Lily Maycat', [200]]
dn1 = ['Lulu Lemon', [10000, 100000, 1000000]]
dn2 = ['Marc Jacobs', [20000, 2000000]]
dn3 = ['Kate Spade', [30000, 30000, 30000]]
dn4 = ['Luis Vuiton', [44000, 40000]]
dn5 = ['Bobbi Brown', [10000000]]
dn_table = [dn0, dn1, dn2, dn3, dn4]


# #############################################################################
def update_donation_list(name):
    """ Update the raw list of donation

        if the name is already in the list, update their donation history
        else add the new donor, and update their donation history

        Argv: 
            Name: string, case-sensitive
    """
    # check to see if name availale --> update gift list
    if any(name in donor for donor in dn_table):
        # list comprehension
        dn = [dn for dn in dn_table if name in dn][0]
        index = dn_table.index(dn)
        ans = int(input("\tEnter gift amount '{}' donate : ".format(dn[0])))
        dn[1].append(ans)
        dn_table[index] = dn
    else:
        ans = int(input("\tEnter gift amoutn '{}' donate : ".format(name)))
        # note to myself
        dn = list()  # creat a nother pointer to a new list()
        dn = [name, [ans, ]]  # remember ans has to be  and comma [,]
        dn_table.append(dn)

    # print the thank you note
    print ('\t' + '='*80)
    print ("\t\tDear {},\n\n\t\tThank you so much for you generous donation of ${}.\n\n\t\tThanks,".format(name, ans))
    print ('\t' + '='*80 + "\n\n\n")

# #############################################################################


def send_thank_you_note():
    """ Get donor name or option of action (list, quit)

        if "donor name" is quit --> come back to orignial menu
        if "donor name" is list --> list all the donors in the data
        if "donor name" is not anything above, update the donation list

    """
    print("\n\n\t" + "* * " * 20)
    print ("\tSEND THANK YOU NOTE")
    ans = input("\tEnter Full Name(CaSeSeNsItIvE), List, or quit(to quit) : ")
    # simplify the name: no space, and all lower case to compare
    #ans = ans.split()
    #ans = ''.join(ans)
    #ans = ans.lower()

    while(ans.lower() != 'quit'):
        if ans.lower() == "list":
            print ("\n\n\tList of Donor")
            print ("\t" + "===" * 10)
            for idx, donor in enumerate(dn_table):
                print("\t {}:  {}".format(idx, donor[0]))
            print ("\t" + "===" * 10)
        else:
            update_donation_list(ans)

        print("\n\n\t" + "* * " * 20)
        print ("\tSEND THANK YOU NOTE")
        ans = input(
            "\tEnter Full Name(CaSeSeNsItIvE), List, or quit(to quit) : ")

    #for dn in dn_table:print("{:30} {}" .format(*dn))

# #############################################################################


def create_report():
    """ Creat the summary report of all donation.

        DonorName  | Total Gift | Num Gift | Average Git
        Table is sorted with Total Gift Value
    """
    #for dn in dn_table:print("{:30} {}" .format(*dn))
    print("\n\n\t" + "* * " * 20)
    print("\tCREAT THE REPORT")
    rpt_tb = list()
    # create the summary list or table
    for donor in dn_table:
        # note to myself
        # this donor actually point to the same donor in dn_table
        # change donot will chang dn_table
        this_dn = list(donor)
        gnum = len(this_dn[1])
        gval = 0
        for val in this_dn[1]:
            gval += val
        gavg = gval / gnum
        this_dn.append(gval)
        this_dn.append(gnum)
        this_dn.append(gavg)
        this_dn.pop(1)
        rpt_tb.append(this_dn)

    # sort the total gift column
    rpt_tb = sorted(rpt_tb, key=lambda x: -x[1])

    # print the report
    print("\t{:<40}|{:>14} | {:>12} | {:>14}".format(
        "Donor Name", "Total Give", "Num Gifts", "Average Gift"))
    print("\t" + "_"*40 + " " + "_"*14 + "   " + "_"*12 + "   " + "_"*14)
    for donor in rpt_tb:
        print("\t{:<40}   ${:>14} {:>12}   ${:>14}".format(
            donor[0], donor[1], donor[2], donor[3]))

    #for dn in dn_table:print("{:30} {}" .format(*dn))
    # Note to myself
    # In [44]: dnlist
    # Out[44]:
    # [['one', [1, 11, 1111, 200]],
    #  ['two', [2, 22, 22345]],
    #  ['three', [5000]],

    # In [45]: dn1[0]
    # Out[45]: 'one'
    #
    # In [46]: dnlist[0]
    # Out[46]: ['one', [1, 11, 1111, 200]]
    #
    # In [47]: dnlist[0][0]
    # Out[47]: 'one'
    #
    # In [48]: dnlist[0][1]
    # Out[48]: [1, 11, 1111, 200]

    #rpt_tb = sorted(rpt_tb, key=lambda x: x[1], reverse=True)


# ##############################################################################
if __name__ == "__main__":

    print ("RAW DATA")
    for dn in dn_table:
        print("{:30} {}" .format(*dn))

    ans = 0
    while (ans != 3):
        print("\n\n\n" + "= = " * 20)
        print("SELECT WHAT TO DO")
        print("----------------------*")
        print("* 1: Send a Thank you *")
        print("* 2: Create a Report  *")
        print("* 3: quit             *")
        print("----------------------*")
        ans = int(input("\nEnter your number : "))

        if ans == 1:
            send_thank_you_note()
        if ans == 2:
            create_report()

# the end
