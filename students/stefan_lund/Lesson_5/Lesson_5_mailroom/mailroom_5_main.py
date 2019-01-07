#!/usr/bin/env python3

"""mailroom Lesson 5,
    changing previous code to reflect Lesson 5
    Style and Naming:   changing names to make the code more readable and
                        understandable when I go back and read it to myself
    Modules:            importing modules
                        importlib.reload, module1 and module2 are both using
                        module3, does both module1 and module2 have to do
                        importlib.reload?
    Exceptions:         was only able to do it when reading and writing data
                        from and to a file.
    Comprehension:      changed code where I could to make a one-liner with
                        the help of comprehensions
    Collections Module: have not used it, have to play with it more to see
                        where it would make sense to use.

    Donor Data:         Changed the original information to contain information
                        about date and amount of donations instead of
                        only total cumulative amount and number of times a
                        donation was made.
"""

import importlib
import mailroom_5_functions
import mailroom_5_read_write_data
importlib.reload(mailroom_5_functions)
importlib.reload(mailroom_5_read_write_data)


def ask_questions():

    """
    displays the "start" or the "thank you" menu according to current option
    default when script starts is "start" menu
    when "Quit" is chosen, script terminates at the quit function
    """

    start = {"a": "send a thank you",
             "b": "create a report",
             "c": "send letters to everyone",
             "d": "quit"}

    thank_you = {"a": "main menu",
                 "b": "list of names",
                 "c": "enter name",
                 "d": "quit"}

    menu = {"start": start, "thank_you": thank_you}

    switch_option = menu["start"]
    while True:
        good = False
        while not good:
            # while loop continues until user enters a value from the switch menu
            print("\nYour options are:\n")

            for letter_key, action in switch_option.items():
                option_line = f"{letter_key}.)  {action}"
                print(option_line)

            answer = input("\nEnter letter according to your choice: ")

            # check to see if the "answer" letter is one of the keys in the
            # switch_option dictionary, good becomes the corresponding dict value
            # and the loop is broken. If answer is not in dict, default set at
            # False is maintained as the value of good.
            good = switch_option.get(answer, False)
            if not good:
                print("Choice is one of these: ", switch_option.keys())

        good_method = "_".join(good.split())
        method_to_call = getattr(mailroom_5_functions, good_method)
        # method = methods_created_by_scripts_in_module.get(good_method)

        option = method_to_call()
        switch_option = menu[option]

# def main_mailroom():
#     local_data_file = "mailroom_5_data.json"
#     # set the data_file in mailroom_5_read_write_data file to local_data_file
#     mailroom_5_read_write_data.data_file = local_data_file
#
#     # set data in mailroom_5_read_write_data file to data read from the local_data_file
#     mailroom_5_read_write_data.data = mailroom_5_read_write_data.get_data_from(local_data_file)
#
#
#     ask_questions()


if __name__ == '__main__':

    local_data_file = "mailroom_5_data.json"
    # set the data_file in mailroom_5_read_write_data file to local_data_file
    mailroom_5_read_write_data.data_file = local_data_file

    # set data in mailroom_5_read_write_data file to data read from the local_data_file
    mailroom_5_read_write_data.data = mailroom_5_read_write_data.get_data_from(local_data_file)


    ask_questions()


# initial donor data for Lesson 5:
#
# names = {
#     "William Gates, III":
#         {"2018/12/17": 300000.00,
#          "2018/06/07": 353784.49},
#
#     "Mark Zuckerberg":
#         {"2018/03/04": 5000.00,
#          "2018/04/14": 5000.00,
#          "2018/05/24": 6396.10},
#
#     "Jeff Bezos":
#         {"2018/07/28": 877.33},
#
#     "Paul Allen":
#         {"2018/02/03": 200,
#          "2018/08/13": 200,
#          "2018/11/28": 308.42}
#     }
