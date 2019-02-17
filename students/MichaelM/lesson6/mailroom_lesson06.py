# wk: cd C:\Users\
# v-micmcd.Redmond\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson06
# mo: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson6
# hm: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson6
# git add mailroom_lesson06_module.py
# git add mailroom_lesson06.py
# git add test_mailroom_lesson06.py
# git commit mailroom_lesson06_module.py
# git commit mailroom_lesson06.py
# git commit test_mailroom_lesson06.py
# git push
# goto https://github.com/geekwriter2/Self_Paced-Online/tree/master/students/MichaelM/lesson5/
# click Pull request > new pull request

import os
from Lesson06 import mailroom_lesson06_module as mr
import importlib

importlib.reload(mr)

tmp_directory = "{}/tmp/".format(os.getcwd())
main_prompt = ("-Main Menu-\n"
               "Do you want to:\n"
               "Send a Thank You -ty\n"
               "Create a Report -cr\n"
               "Send Thank You Letters - s\n"
               "Quit -q\n"
               " >>")
main_menu = {"cr", "q", "s", "ty"}


def menu_selection(prompt, menu):
    while True:
        response = input(prompt)
        if response.lower() not in menu:
            print(f"'{response}' not available. Please make a valid choice.\n")
        elif response.lower() in menu:
            if response.lower() == "ty":
                user_response_ty = input(
                    "- type 'list' to view a list of donors\n- type 'new' to "
                    "add a donor to the list\n- type in an existing donor to add a new donation >>")
                if user_response_ty == "list":
                    mr.function_calls("ty", "list")
                elif user_response_ty == "new":
                    response_donor_name = input("What is the donor's name? >>")
                    donation_amt = obtain_donation_amt(response_donor_name)
                    mr.function_calls("ty", "new", response_donor_name, "", donation_amt)
                elif response.lower() != "list" and response.lower() != "new":
                    donation_amt = obtain_donation_amt(response_donor_name)
                    mr.function_calls("ty", "add_to_donor", response_donor_name, "", donation_amt)
            elif response.lower() == "cr":
                mr.function_calls("cr", "", "", "")
            elif response.lower() == "s":
                mr.function_calls("s", "", "", tmp_directory)
            elif response.lower() == "q":
                break


def obtain_donation_amt(donor_name):
    """
            prompts user for a donation amount and returns that amount

            Parameters:
            donor_name: string the donor name

            Returns:
            response_donation_amt: float the donation
            """
    response_donation_amt = 0.0
    while True:
        try:
            response_donation_amt = float(
                input("How much is {}'s donation? >>".format(donor_name.title())))
        except ValueError:
            print("Please enter the donation in dollars")
        else:
            break
    return response_donation_amt


if __name__ == "__main__":
    menu_selection(main_prompt, main_menu)
"""
    entry point into the program. Funnels user input to a flow control function and exits the user from the program

    {Extended description}

    Parameters:
    prompt: string print statement listing user options

    Returns:
    {none}

    """


