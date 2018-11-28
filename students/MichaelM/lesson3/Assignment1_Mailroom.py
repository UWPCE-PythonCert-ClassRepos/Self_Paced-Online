# wk: cd C:\Users\v-micmcd.Redmond\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson3
# mo: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson3
# hm: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson3
# git add Assignment1_Mailroom.py
# git add mailroom.py
# git commit Assignment1_Mailroom.py
# git commit mailroom.py
# git push
# goto https://github.com/geekwriter2/Self_Paced-Online/tree/master/students/MichaelM/lesson3/
# click Pull request > new pull request


import mailroom
import importlib
importlib.reload(mailroom)


def begin():
    """
        entry point into the program. Funnels user input to a flow control function and exits the user from the program

        {Extended description}

        Parameters:
        {none]

        Returns:
        {none}

        """
    print("Welcome to the mailroom.")
    while True:
        response_1 = input(
             "Do you want to:\nSend a Thank You -ty\nCreate a Report -cr\nQuit -q\n > ")
        if response_1.lower() == "q":
            print("That's lunch!")
            break
        elif response_1.lower() in ["ty", "cr"]:
            flow_control(response_1)


def flow_control(usr_action):
    """
        handles logic and controls which functions are called based on user input.

        {Extended description}

        Parameters:
        usr_action (string): currently two strings: ty|cr

        Returns:
        {none}

        """
    ua = usr_action.lower()
    if ua == "ty":
        response_2 = input(
            "Please enter a name.\n-type 'list' to view a list of donors\n-type in a "
            "new a new donor name to add to list > ")
        mailroom.create_ty_letter(response_2)
    elif ua == "cr":
        mailroom.create_report()


if __name__ == "__main__":
    begin()


