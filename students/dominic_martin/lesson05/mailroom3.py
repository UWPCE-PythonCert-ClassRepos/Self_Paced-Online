#!usr/bin/env/Python 3
import sys
import prompt_module as pm

names = ['Ted Bayer', 'Panfila Alvarez', 'JR Reid', 'Simon Laplace', 'Jennifer Meyers']
donations = [500, 700, 330, 440, 800]
names_donations = {name: donation for name, donation in zip(names, donations)}   
 

def send_thanks():
    """Print a thank you message to the selected person."""
    while True:
        try:
            choose_response = int(input(pm.choose_prompt))
            print("\n" + names[choose_response - 1] + ", thanks for your donation." +"\n")
        except:
            print("Try again with a number between 1 and 5.")
            continue
        else:
            break

def thanks_everyone():
    """Open and write a .txt file with a thank you message for every person."""
    for key in names_donations.keys():
        with open('%s.txt'%(key,), 'w') as f:
            f.write(key  + "\n\nThanks for your donation!\n\nAll the Best,\n\nThe Mailroom Team") 

def gen_report():
    """Generate a report containing all names and donations."""
    print()
    width1 = 27
    p = ('Name:', 'Amount:')
    print(f'{p[0]:{width1}}{p[1]:{width1}}')
    for name, donation in names_donations.items():
        print(f'{name:{width1}}{"$"+str(donation):{width1}}')

def exit_program():
    """Exit the program."""
    print("\nThanks for using The Mailroom Application!  Goodbye!")
    sys.exit()

def main():
    """Prompt user to make a choice at the start of program."""
    while True:
        try:
            response = input(pm.prompt)
            switch_func_dict = {
            "1": send_thanks,
            "2": thanks_everyone,
            "3": gen_report,
            "4": exit_program,
            }
            switch_func_dict.get(response)()
        except TypeError:
            print("\nTry again! Input must be an integer between 1 and 4.\n")
            continue

main()