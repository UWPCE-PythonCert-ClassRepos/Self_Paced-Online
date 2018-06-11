#lesson 03 mailroom part 1
#!/usr/bin/env python3

#starting list of 5+ donors and 1-3 donations each
donors = ["John Travolta", "Jane Fonda", "Judy Blume", "Joey Tribbiani", "Jenny Gump"]
amounts = [(5000, 7500), (10000, 8000, 6500), (3000, 3000), (9000,), (10300, 13750, 12500)]

#prompt user for actions: send a thank you, create a report, quit
#thank you: ask for name, add to list if needed, ask for amount, add to list
#report: print report of each donor with total donated, number of donations, average donation
#quit: exit

def menu():
    flag = True
    while flag == True:
        choice = input("Please choose an action: \n1) Send a thank you \n2) Create a report \n3) Quit \n")
        if choice == "1":
            name = intro()
            value = donation(name)
            card(name, value)
            flag = True
        elif choice == "2":
            report()
            flag = True
        else:
            flag = False
    else:
        quit()

def intro():
    addressee = input("\nTo whom would you like to send a thank you? ")
    if addressee == "list":
        print(donors)
        addressee = input("\nTo whom would you like to send a thank you? ")
        if addressee not in donors:
            donors.append(addressee)
            amounts.append(())
            return addressee
        else:
            return addressee
    elif addressee not in donors:
        donors.append(addressee)
        amounts.append(())
        return addressee
    else:
        return addressee    
def donation(n):
    if n == "quit":
        print()
        pass
    else:
        dollars = input("What is the donation amount? ")
        if dollars == "quit":
            donors.remove(n)
            print()
            pass
        elif int(dollars) < (10 ** 6):
            position = donors.index(n)
            a = amounts[position]
            a = a + (int(dollars),)
            amounts[position] = a
            return dollars
        else:
            print("\nNice try, Moneybags.\n")
            quit()
def card(n, v):
    if v == None:
        pass
    else:
        print("\nThank you, %s, for supporting The Brave Heart Foundation. Your generous donation of $%s will make a positive, life-changing impact for teens nationwide.\n" % (n, v))
def quit():
    pass

def report():
    print()
    print("{:<20} {:<15} {:^12} {:<15}".format("Donor", "Total Given", "Number", "Average Given"))
    for i in range(len(donors)):
        tot = sum(amounts[i])
        num = len(amounts[i])
        print("{:<20} ${:^15.2f} {:^12} ${:^15.2f}".format(donors[i], tot, num, tot/num))
    print()
    
    
if __name__ == '__main__':
    menu()



