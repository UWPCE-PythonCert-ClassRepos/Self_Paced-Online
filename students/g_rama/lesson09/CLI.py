#!/usr/bin/env python3


class CLI:

    @staticmethod
    def amount_input():
        amount = float(input("Enter the amount of donation:\n"))
        return amount

    @staticmethod
    def fullname_input():
        fullname = input("Enter the Donor name:\n")
        return fullname

    def menu_selection(self, prompt, dispatch_dict):

        while True:
            try:
                response = input(prompt)
                if dispatch_dict[response]() == "exit menu":
                    break
            except KeyError:
                print("Please enter key as 1 2 3 or 4")

    def exit_menu(self):
        print("Quitting this menu")
        return "exit menu"
