#!/usr/bin/env python3
# Lesson 3, Mailroom

# Donor data
donors = [
    ["Homer Simpson", 253.64, 772.50, 99.99],
    ["Ned Flanders", 1200.25, 850.35],
    ["Edna Krabappel", 55.43, 118.67, 75.23],
    ["Moe Szylak", 54.23],
    ["Martin Prince", 12.22, 19.56]
]

def send_thanx():
    pass

def create_report():
    pass

if __name__ == "__main__":
    while True:
        print("Please choose one of these options:")
        print("  1 - Send a Thank You")
        print("  2 - Create a Report")
        print("  3 - Quit")
        choice = input("Enter your selection => ")
        
        if choice == "1":
            send_thanx()
        elif choice == "2":
            create_report()
        elif choice == "3":
            break;
