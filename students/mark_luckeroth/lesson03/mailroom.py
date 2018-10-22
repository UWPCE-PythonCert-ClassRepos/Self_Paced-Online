#!/usr/bin/env python3

Names = ['Peter','Paul','Mary','Jake','Raj']
Donations = [[10., 10., 10.],
            [5., 50000., 5., 5.],
            [100.],
            [123., 456., 789.],
            [60., 600000.]]

def Thanks():
    while True:
        Name = input('Please enter the Full Name of the donor: ')
        if Name == 'list':
            print(Names)
            continue
        else:
            break
    if Name not in Names:
        Names.append(Name)
        Donation = float(input('Please enter the amount of the donation: '))
        Donations.append([Donation])
    else:
        ind = Names.index(Name)
        Donation = float(input('Please enter the amount of the donation: '))
        Donations[ind].append(Donation)
    print(f'Dear {Name}:')
    print(f'Thank you for your donation of ${Donation:.2f} to our charity.')
    print(f'Your contribution will do a great deal to help our worthy cause')

def Report():
    title_str = '{:<20s}|{:^13}|{:^11}|{:>13}'
    bar_str = '-'*60
    entry_str = '{:<20s} ${:>12} {:>11} ${:>12}'
    Total_Given = totals(Donations)
    Num = count(Donations)
    avg = averages(Total_Given, Num)
    sort_given = sorted(Total_Given)[::-1]
    print(title_str.format('Donor Name','Total Given','Num Gifts','Average Gift'))
    print(bar_str)
    for item in sort_given:
        index = Total_Given.index(item)
        print(entry_str.format(*(Names[index], Total_Given[index], Num[index], avg[index])))

def totals(Donations):
    totals = []
    for i, row in enumerate(Donations):
        row_total = 0
        for item in row:
            row_total = row_total+item
        totals.append(row_total)
    return totals

def count(Donations):
    count = []
    for row in Donations:
        count.append(len(row))
    return count

def averages(totals, count):
    return [x/y for x,y in zip(totals,count)]

if __name__ == '__main__':
    while True:
        while True:
            choice = input("would you like to: 'Send a Thank You','Create a Report', or 'quit'? ")
            if choice not in ['Send a Thank You','Create a Report','quit']:
                print("You must enter command from list: 'Send a Thank You','Create a Report','quit'")
                continue
            else:
                break
        if choice == "Send a Thank You":
            Thanks()
            continue
        if choice == "Create a Report":
            Report()
            continue
        if choice == 'quit':
            break

