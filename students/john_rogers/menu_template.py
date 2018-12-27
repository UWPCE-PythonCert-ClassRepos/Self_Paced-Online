#!/usr/bin/env python3
"""
Sample template for creating a menu using a dispatch dictionary
Version: .1
Last updated: 12/27/2018
Notes:
"""


def main():
    """
    Main menu prompt and dictionary
    :return:
    """

    main_prompt = (
        "\nWelcome to the main menu!\n"
        "Please pick from the following:\n"
        "1, 2, 3, 4 or 5 to get to sub-menu.\n"
        "Type 'q' to exit the program >> "
    )

    main_dispatch = {
        '1': test_fun1,
        '2': test_fun2,
        '3': test_fun3,
        '4': test_fun4,
        '5': sub_menu,
        'q': exit_menu,
    }

    # Call the main menu:
    menu(main_prompt, main_dispatch)


def menu(prompt, dispatch_dict):
    """
    Sample case for using a dispatch dictionary to create a simple menu
    :return: none
    """
    while True:
        response = input(prompt)
        if dispatch_dict[response]() == 'exit menu':
            break


def exit_menu():
    print('Exiting menu')
    return 'exit menu'


def sub_menu():
    sub_prompt = (
        "\n Welcome to the sub-menu -\n"
        "Please choose from the following:\n"
        "1, 2, or 3 or 'q' to exit >> "
    )

    sub_dispatch = {
        '1': sub_fun1,
        '2': sub_fun2,
        '3': sub_fun3,
        'q': exit_menu,
    }

    menu(sub_prompt, sub_dispatch)


def sub_fun1():
    print('sub-menu function 1')


def sub_fun2():
    print('sub-menu function 2')


def sub_fun3():
    print('sub-menu function 3')


def test_fun1():
    print('test function 1')


def test_fun2():
    print('test function 2')


def test_fun3():
    print('test function 3')


def test_fun4():
    print('test function 4')


if __name__ == '__main__':
    main()