#!/usr/bin/env python3

donor_db = [("Wassily Kandinsky", [43928.13, 131.34, 1928.0]),
            ("Jasper Johns", [3134.43, 153.34]),
            ("Mark Rothko", [135353.33]),
            ("Richard Serra", [153757.87, 28457.12, 1293451.0]),
            ("Yves Tanguy", [1534.23, 2542.19])]

prompt = "\n".join(("Type a number from the options below",
        "1 - Send a Thank You",
        "2 - Create a Report",
        "3 - Quit\n"))

def thank_you():
    thanks = True
    while thanks == True:
        user_in = input("Type List to view all donor names, type a current donor name, or type the name of a new donor: ")
        if user_in.lower() == "list": 
            for donor in donor_db:
                print(donor[0])
        else:
            for entry in donor_db:
                if user_in.title() in entry:
                    user_in = user_in.title()    
                    donation = float(input(f"Add a donation amount for {user_in}: $"))
                    donor_db[donor_db.index(entry)][1].append(donation)
                    print(f"\nDear {user_in},\n\nThank you so much for your donation.\n\nSincerely,\n\nThe Mailroom\n")
                    thanks = False
                    break 
            else:
                print("oh no")
                user_in = user_in.title()
                donor_db.append((user_in,[]))
                donation = float(input(f"Add a donation amount for {user_in}: $"))
                donor_db[-1][1].append(donation)
                print(f"\nDear {user_in},\n\nThank you so much for your donation.\n\nSincerely,\n\nThe Mailroom\n")
                thanks = False

def sort_key(database):
    return sum(database[1])

def report():
    sorted_db = sorted(donor_db, key = sort_key, reverse = True)
    print("{:<26}{}{}{}".format("Donor Name", "| Total Given ", "| Num Gifts ", "| Average Gift"))
    print("------------------------------------------------------------------")
    for donor in sorted_db:
        print("{:<27}${:12.2f}{:11}  ${:12.2f}".format(donor[0], sum(donor[1]), len(donor[1]), sum(donor[1])/len(donor[1])))

def main():
    print("Welcome to The Mailroom")
    while True:
        response = input(prompt)
        if response == "1":
            thank_you()
        elif response == "2":
            report()
        elif response == "3":
            print("Thank you for visiting The Mailroom")
            break
        else:
            print("Not a valid option")


if __name__ == '__main__':
    main()
