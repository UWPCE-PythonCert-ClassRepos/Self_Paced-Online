#!/usr/bin/env python3

data = [['John Doe', 120.00, 353.33, 400.00], ['Jane Doe', 3500.04, 2624.44], ['John Smith', 33.33, 400.00, 29.20], ['Jane Smith', 2.00], ['Billy Jo Jones', 100.00, 100.00, 100.00]]


# mode 1 - "send a thank you"
def thank_you():
    sub = 1
    while sub:
        new_row = []  # reset to make sure we don't copy data twice in case new_row isn't overwritten
        name = input("Please enter a full name (or type \'list\', or hit \'return\' to go back)> ")
        if name == "list":
            for row in data:
                print(row[0])  # name is always the 1st entry in each data row
                sub = 0  # runs the subroutine again
        elif name == "":
            sub = 0
            continue
        else:
            for i, row in enumerate(data):  # search for a name match
                if row[0] == name:
                    new_row = data.pop(i)  # if name is found pop() entry and put in new_row
                    break
            else:  # if no name match, make new entry
                new_row = [name]
            dollars = input("Please enter a donation amount (ex: 500.05)> ")
            new_row.append(round(float(dollars), 2))  # b/c I don't understand floating point math
            data.append(new_row)
            print(f"Dear {new_row[0]},\n\nThank you for your donation of {new_row[-1]:.2f}.\n\nLove,\nThe Charity Org\n")
        sub = not sub  # leaves subroutine, unless 'list' has been called
    else:
        return


# mode 2 - "create a report"
def create_report():
    # create temp data
    temp_data = []  # resets temp data
    for row in data:
        temp_row = []  # reset temp_row
        temp_total = 0.00  # reset temp_total
        for cell in row:
            if not temp_row:  # first cell - when temp_row is empty
                temp_row.append(cell)  # append donor name, name is always in first cell
            else:
                temp_total += float(cell)  # total gifts, added from cells after first
        temp_row.append(round(float(temp_total), 2))  # append historical total
        temp_row.append(len(row) - 1)  # append number of gifts
        temp_row.append(round(temp_total / (len(row) - 1), 2))  # append avg gift
        temp_data.append(temp_row)  # adds row to temp data structure, will build new data structure by end of for loop

    # sort temp data
    # counter will ensure we've taken one full pass of the data where all rows are in order before quitting
    counter = 0
    temp_row = []
    while counter < (len(temp_data) - 1):  # we will get an out of bounds error if we don't stop at len-1
        counter = 0
        for i in range(len(temp_data) - 1):  # I think this is a bubble sort? It's been a while...
            if temp_data[i][1] < temp_data[i + 1][1]:  # if this row's total is less than the next row's total...
                temp_row = temp_data.pop(i)  # pop() the row...
                temp_data.insert(i + 1, temp_row)  # insert() the row into the next cell
            else:
                counter += 1  # when we get through a whole for loop withought "bubbling" we leave the while loop
                # there's probably a more elegent way to make sure we've fully bubbled, but I don't know it

    # display temp data
    print("Donor Name                | Total Given |   Num Gifts |  Average Gift")
    print("---------------------------------------------------------------------")
    for row in temp_data:
        print("{:<27}{:>14.2f}{:>14}{:>14.2f}".format(*row))
        # if we move the output of func 1 into the main loop, move this one as well
    else:
        return


# mode 3 - "quit"
def end_program():  # exit() and quit() look like they're reserved
    print("Thanks for playing along.")
    return 0  # probably better to exit the main loop than break out of this one so we end main's while loop


# main loop
def main():
    main = 1
    while main:
        # select mode
        mode = ""
        while not mode:
            print("Choose a number:")
            print("(1) Send a Thank You")
            print("(2) Create a Report")
            print("(3) quit")
            mode = input("> ")
            if mode == "1":
                thank_you()
            elif mode == "2":
                create_report()
            elif mode == "3":
                main = end_program()
            else:
                print("Please enter 1, 2, or 3")
                mode = ""


if __name__ == '__main__':
    main()
