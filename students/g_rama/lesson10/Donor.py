from DonorCollection import DonorCollection


class Donor(DonorCollection):

    def add_data_print_thanks(self, amount, fullname):
        if self.amount_validate(amount):
            super().donors_collection_data.update({fullname: [amount]})
            self.thank_you_letter(fullname, amount)

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
            super().donors_collection_data[fullname].append(amount)
            self.thank_you_letter(fullname, amount)


