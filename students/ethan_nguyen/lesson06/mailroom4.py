
import sys, os
import pytest

#create a donor_db as a dict
donor_db = {"William Gates, III": [653772.32, 12.17],
            "Jeff Bezos": [877.33],
            "Paul Allen": [663.23, 43.87, 1.32],
            "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
            "Donald Trump": [50000.24, 1002]
}

prompt = "\n".join(("Welcome to the mail room",
          "Please choose from below options:",
          "S - Send a Thank You",
          "C - Create a Report",
          "L - Send letters to all donors"
          "Q - Exit"
          ">>> "))


def view_donors():
    print("\n".join(donor_db))

def quit_program():
    print ("Thank you. Bye!")
    sys.exit(0)  # exit the interactive script

#function to make sure input name is letters only and longer than 2 characters
def validate_name():
    while (True):
        try:
            input_Name = str(input("Please enter a name > "))
            if (len(input_Name) > 2 and input_Name.isalpha()):
                break
            else:
                raise TypeError
        except TypeError:
            print("Letters only or longer name, please.")
    
    return input_Name

#function to make sure input amount is numeric
def validate_amount(input_Name):
    while (True):
        try:
            input_Amount = input(f"{input_Name} please input amount > ")
            value = float(input_Amount)
            break
        except ValueError:
            print('Valid amount, please')
    return value

def send_thank_you():

    input_name = validate_name()
    while("list" in input_name):
        for d in sorted(donor_db.keys()):
            print(d)

        input_name = validate_name()

    is_NewDonor = False

    if input_name not in donor_db:
        is_NewDonor = True

    value = validate_amount(input_name)

    print(create_thank_you_note(input_name, value))

    #add Donor if he/she is not in donor_db
    if is_NewDonor:
        add_new_donor(input_name, float(value))
    else:
        #select_Donor.append(float(value))
        #donor_db[input_Name] = select_Donor
        update_amount(input_name, float(value))

def create_thank_you_note(name, value):
    return f'Dear {name}, \n Thank you for your very kind donation of ${value:,.2f} \n \
        It will be put to very good use. \n Sincerely, \n -UW'

def update_amount(name, amount):
    """function to update amount given a name"""
    donor_db[name].append(amount)

def add_new_donor(name, amount):
    """function to add a new donor"""
    donor_db[name] =[amount]

def sort_key(donor):
    return sum(donor[1])

def get_report():
    sort_Donor = sorted(donor_db.items(), key=sort_key, reverse = True)
    rows = list()
    for d in sort_Donor:
        rows.append("{:<25} ${:>12,.2f}{:>22}{:<10}${:>12,.2f}".format(d[0], sum(d[1]), len(d[1]), '',sum(d[1])/len(d[1])))
    return rows

def display_report():
    for r in get_report():
        print(r)

def create_report():

    space=''
    print(f'Donor Name {space:<15}| Total Given {space:<10}| Num Gifts {space:<9}| Average Gift {space:<19}')
    print("-"*85)
    #sort_Donor = sorted(donor_db.items(), key=lambda x: x[1], reverse = True)
    display_report()

def get_letter_text(name, amount):
    """Get letter text for file content"""
    return f'Dear {name}, \n Thank you for your very kind donation of ${float(sum(amount)):,.2f} \n \
        It will be put to very good use. \n Sincerely, \n -UW'

def create_letter(path, letter_name, letter):
    """Create letter"""
    with open(f'{path}/{letter_name}.txt', 'w') as f:
        f.write(letter) 

def send_letters():

    path = os.getcwd()
    for k,v in donor_db.items():
        create_letter(path, k, get_letter_text(k, v))
    
    print("Done!")

def test_get_report():
    expected = "{:<25} ${:>12,.2f}{:>22}{:<10}${:>12,.2f}".format("Paul Allen", 708.42, 3, '',236.14)

    result = get_report()
    assert expected in result

def test_get_report_count():

    result = get_report()        
    assert len(result) == 5

def test_get_letter_text():
    expected = "Dear World, \n Thank you for your very kind donation of $300.00 \n \
        It will be put to very good use. \n Sincerely, \n -UW"
    assert get_letter_text("World", [100, 200]) == expected

def test_create_letter():
    expected = os.path.join(os.getcwd(), "World.txt")
    create_letter(os.getcwd(), "World", "Dear World, \n Thank you for your very kind donation of $300.00 \n \
        It will be put to very good use. \n Sincerely, \n -UW")
    assert os.path.isfile(expected)

def test_create_thank_you_note():
    expected = 'Dear Ethan, \n Thank you for your very kind donation of $10,000.00 \n \
        It will be put to very good use. \n Sincerely, \n -UW'
    
    assert create_thank_you_note("Ethan", 10000) == expected

def test_add_new_donor():

    add_new_donor('Ethan', 10000)
    expected_key, expected_value =  "Ethan", [10000]

    assert expected_key in donor_db and expected_value == donor_db[expected_key]

def test_update_amount():

    update_amount("Ethan", 100)
    expected_key, expected_value =  "Ethan", [10000, 100]
    assert expected_key in donor_db and expected_value == donor_db[expected_key]

if __name__ == "__main__":
    
    arg_dict = {'S':send_thank_you, 'C':create_report, 'L':send_letters}

    while True:
        response = input("Please select S for \"Send a Thank You\" C for \"Create a Report\" L for \"Send Letters\" or Q to quit >").upper()
        arg_dict.get(response, quit_program)()
