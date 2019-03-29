from DonorCollection import DonorCollection
from CLI import CLI


class Donor(DonorCollection):

    def __init__(self, fullname, amount):
        self.fullname = fullname
        self.amount = amount

    def thank_you_letter(self):
        """Send a thank you letter"""
        print(f"Thank you {self.fullname} for donating {self.amount} dollars generously.")
        return f"Thank you {self.fullname} for donating {self.amount} dollars generously."

    def add_data_print_thanks(self):
        if self.amount_validate():
            super().donors_collection_data.update({self.fullname: [self.amount]})
            self.thank_you_letter()

    def amount_validate(self):
        if self.amount < 0:
            print("Enter the correct amount with out negitives")
        else:
            return True

    def update_data_print_thanks(self):
        if self.amount_validate():
            super().donors_collection_data[self.fullname].append(self.amount)
            self.thank_you_letter()


