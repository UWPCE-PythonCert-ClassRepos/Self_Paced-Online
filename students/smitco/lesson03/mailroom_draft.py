#lesson 03 mailroom part 1
#!/usr/bin/env python3

#starting list of 5+ donors and 1-3 donations each
donors = ["John", "Jane", "Judith", "Joseph", "Jenny"]
amounts = [(5000, 7500), (10000, 8000, 6500), (3000, 3000), (9000,), (10300, 13750, 12500)]

#prompt user for actions: send a thank you, create a report, quit
#thank you: ask for name, add to list if needed, ask for amount, add to list
#report:
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
            flag = False
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
    dollars = input("What is the donation amount? ")
    if int(dollars) < (10 ** 6):
        position = donors.index(n)
        a = amounts[position]
        a = a + (int(dollars),)
        amounts[position] = a
        return dollars
    else:
        print("\nNice try, Moneybags.")
        quit()
def card(n, v):
    print("\nThank you, %s, for supporting The Derek Zoolander School for Kids Who Can't Read Good and Want to Do Other Stuff Good Too. Here, we teach kids that there's more to life than being really, really ridiculously good-looking. Because of your generous donation of $%s, we will be able to build a center that is not for ants but can fit real children.\n" % (n, v))
def quit():
    pass

        
        
        
if __name__ == '__main__':        
    menu()



