"""
Sean Tasaki
5/18/2018
Lesson05.mailroom_part_3
"""

donor_full_list = [['Bob Dylan', 120000.00, 3, 40000.00], ['Leonard Cohen', 600.00, 2, 300.00], ['Soren Kierkegaard', 1000.00, 2, 500.00], ['Italo Calvino', 20000.00, 4, 5000.00], ['Florence Feist', 300.00, 3, 100.00]]
donor_name_list = []
for x in donor_full_list:
    donor_name_list.append(x[0])


def main_menu():
    main_menu_dict = {'1': thank_you, '2': create_report, '3': create_thank_you_letters, '4': quit}
    main_prompt = "Enter 1-4 from the following options: (1) Send a Thank You to a Donor, (2) Create a Report, (3) Write a Thank You Letter to All Donors (4) Quit\n >> "  
    main_menu_response(main_prompt, main_menu_dict)

def main_menu_response(prompt, main_menu_dict):
    try:
        while True:
            response = input(prompt)
            main_menu_dict.get(response)()
            if main_menu_dict[response]() == "exit menu":
                exit()
    except TypeError:
        print("Enter a number between 1-4.")    
        return main_menu()

def thank_you():
    name = input("Enter the first and last name of the donor or enter 'list' to see a list of previous donor names or enter Q to exit to main menu\n> ")
    try:
        if name.lower() == 'list':
            print(donor_name_list)
            thank_you()
        elif name.upper() == 'Q':
            main_menu()
        
        elif name.title() in donor_name_list:
            for donor in donor_full_list:
                if donor[0].casefold() == name.casefold():
                    amount = input(f"{name.title()} is a previous donor. Enter the donation amount.\n>> ")
                    if amount.lower() == 'q':
                        thank_you()
                    else:
                        donor[1] += float(amount)
                        donor[2] += 1
                        donor[3] = float(donor[1]/donor[2])
                        print(f"Thank you {name.title()} for your genereous donation of ${float(amount):.2f}.")
                        thank_you()
               
        elif name.title() not in donor_name_list:
            amount = input(f"{name.title()} is a new donor. Enter the donation amount.\n>> ")
            if amount.lower() == 'q':
                thank_you()
            else:            
                donor_full_list.append([name.title(), float(amount), 1, float(amount)])
                donor_name_list.append(name.title())
                print(f"Thank you {name.title()} for your genereous donation of ${float(amount):.2f}.")
                thank_you()
    except ValueError:
        print("Invalid input. Please enter a numerical donation amount.")
        return thank_you()
    print()
    main_menu()

def quit():
    return "exit menu"

def create_report():
    donor_full_list.sort(key = lambda x: x[1], reverse = True)
    print("Donor Name           |   Total Given   |   Num Gifts  |    Average Gift")
    print("-----------------------------------------------------------------------")
    for x in donor_full_list:
        print(f"{x[0]:20} ${x[1]:>17.2f}    {x[2]:>6}     ${x[3]:>16.2f}")  
    main_menu()

def create_thank_you_letters():
    # Creates a letter for each donor that gets a file in the working dir based on donor's name.
    try:
        # Separate donors based on whether they gave multiple donations or a single donation
        file_donor_names=  [(donor[0] + '.txt') for donor in donor_full_list]
        file_object_for_donations = [open(file, 'w') for file in file_donor_names]
        for count, donor in enumerate(donor_full_list):
            file_object_for_donations[count].write(thank_you_letter_template(donor)) 
        

    except IOError:
        print("There was an error with creating the letter files")
    else:
        print("Thank you letters created. Look in the directory for the new files.")
        main_menu()
    finally: 
        for file in file_object_for_donations:
            file.close()
def thank_you_letter_template(list):
    if list[2] > 1:
        return "Dear {},\nThank you for your {} generous donations of ${:.2f}. Your support helps our charity stay in business.\n\nSincerely,\n-The Team".format(list[0], list[2], list[1])
    else:
        return "Dear {},\nThank you for your generous donation of ${:.2f}. Your support helps our charity stay in business.\n\nSincerely,\n-The Team".format(list[0], list[2], list[1])

if __name__ == '__main__':
    main_menu()