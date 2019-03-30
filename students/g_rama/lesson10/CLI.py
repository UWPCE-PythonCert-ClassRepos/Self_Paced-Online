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

    def mulfactor_input():
        factor = float(input("Enter the multiplying factor genorously agreed by philonthropists:\n"))
        return factor

    def min_donation_input():
        min_donation = float(input("Enter the minimum donation amount to which factor to be applied:\n"))
        return min_donation

    def max_donation_input():
        max_donation = float(input("Enter the maximum donation amount to which factor to be applied:\n"))
        return max_donation


    def menu_selection(self, prompt, dispatch_dict):

        while True:
            try:
                response = input(prompt)
                if dispatch_dict[response]() == "exit menu":
                    break
            except KeyError:
                print("Please enter key as 1 2 3 4 or 5")

    def exit_menu(self):
        print("Quitting this menu")
        return "exit menu"
