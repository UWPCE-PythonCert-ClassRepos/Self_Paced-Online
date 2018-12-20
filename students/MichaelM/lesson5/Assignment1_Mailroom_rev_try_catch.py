# wk: cd C:\Users\v-micmcd.Redmond\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson5
# mo: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson5
# hm: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson5
# git add Assignment1_mailroom_rev_try_catch.py
# git add mailroom_rev_try_catch.py
# git commit Assignment1_Mailroom_rev.py
# git commit mailroom_rev.py
# git push
# goto https://github.com/geekwriter2/Self_Paced-Online/tree/master/students/MichaelM/lesson4/
# click Pull request > new pull request


from Lesson05 import mailroom_rev_try_catch
import importlib
importlib.reload(mailroom_rev_try_catch)

main_menu = {"ty": mailroom_rev_try_catch.create_ty_letter, "cr": mailroom_rev_try_catch.create_report, "q": mailroom_rev_try_catch.quit,
             "s": mailroom_rev_try_catch.spam_donors}
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
    while True:
        response = input(prompt)
        if response.lower() not in menu:
            print(f"{response} not available. Please make a valid choice.")
        elif response.lower() in menu:
            if menu[response.lower()]() == "q":
                  break


if __name__ == "__main__":
    menu_selection(main_prompt, main_menu)

