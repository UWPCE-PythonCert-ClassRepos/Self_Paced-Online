# wk: cd C:\Users\v-micmcd.Redmond\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson4
# mo: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson4
# hm: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson4
# git add Assignment1_Mailroom.py
# git add mailroom.py
# git commit Assignment1_Mailroom.py
# git commit mailroom.py
# git push
# goto https://github.com/geekwriter2/Self_Paced-Online/tree/master/students/MichaelM/lesson4/
# click Pull request > new pull request


from Lesson04 import mailroom_rev
import importlib

importlib.reload(mailroom_rev)

main_menu = {"ty": mailroom_rev.create_ty_letter, "cr": mailroom_rev.create_report, "q": mailroom_rev.quit,
             "s": mailroom_rev.spam_donors}
main_prompt = ("Main Menu\n"
               "Do you want to:\n"
               "Send a Thank You -ty\n"
               "Create a Report -cr\n"
               "Send Thank You Letters - s\n"
               "Quit -q\n"
               " > ")


def menu_selection(prompt, menu):
    """
    entry point into the program. Funnels user input to a flow control function and exits the user from the program

    {Extended description}

    Parameters:
    prompt: string print statement listing user options

    Returns:
    {none}

    """
    # loop forever
    while True:
        response = input(prompt)
        if response.lower() not in menu:
            print(f"{response} not available. Please make a valid choice.")
        elif response.lower() in menu:
            if menu[response.lower()]() == "q":
                print("that's lunch!")
                break


if __name__ == "__main__":
    menu_selection(main_prompt, main_menu)

