from Donors import Donors
from CLI import CLI


class Donor(Donors):

    def add_data_print_thanks(self, amount, fullname):
        if self.amount_validate(amount):
            super().donors_data.update({fullname: [amount]})
            self.thank_you_letter(fullname, amount)

    def thank_you(self):
        """Send a thank you letter"""
        fullname = CLI.fullname_input()
        if fullname.isalpha():
            if fullname == str("list"):
                super().display_donors()
            elif fullname in super().donors_data.keys():
                amount = CLI.amount_input()
                self.update_data_print_thanks(amount, fullname)
            else:
                try:
                    amount = CLI.amount_input()
                    self.add_data_print_thanks(amount, fullname)
                except ValueError:
                    print("Enter the correct amount in integer")
        else:
            print("Enter the donor name correctly")

    def amount_validate(self, amount):
        if amount < 0:
            print("Enter the correct amount with out negitives")
        else:
            return True

    def thank_you_letter(self, donor_name, amount):
        """Send a thank you letter"""
        print(f"Thank you {donor_name} for donating {amount} dollars generously.")
        return f"Thank you {donor_name} for donating {amount} dollars generously."

    def update_data_print_thanks(self, amount, fullname):
        if self.amount_validate(amount):
            super().donors_data[fullname].append(amount)
            self.thank_you_letter(fullname, amount)


