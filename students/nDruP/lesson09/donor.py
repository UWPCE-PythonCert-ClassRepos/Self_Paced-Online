class Donor():
    def __init__(self, title, gift):
        self._name = title
        self._history = []
        if type(gift) == int or type(gift) == float:
            self._history.append(round(gift, 2))
        elif type(gift) == list:
            for x in gift:
                self._history.append(round(x, 2))

    def __len__(self):
        return len(self._history)

    @property
    def name(self):
        return self._name

    @property
    def history(self):
        return self._history

    @property
    def avg_gift(self):
        return sum(self._history)/len(self._history)

    @property
    def sum_gift(self):
        return sum(self._history)

    @property
    def info(self):
        return (self.name, len(self.history), self.avg_gift, self.sum_gift)

    def add_gift(self, value):
        self._history.append(round(value, 2))

    def thank_u_letter_str(self, new_gift=False):
        divider = "\n" + "*" * 50 + "\n"
        thank_u_letter = divider + f"Dearest {self.name},\n"
        if new_gift:
            thank_gift = self.history[len(self.history)-1]
            thank_u_letter += "\tThank you for your most recent donation of"
        else:
            thank_gift = self.sum_gift
            thank_u_letter += "\tThank you for your lifetime total of "
        thank_u_letter += (f" ${thank_gift:.2f}!\n"
                           "We will use your donation(s) to create real "
                           "living Pokemon.\n"
                           "You now have our eternal loyalty. Use it wisely.\n"
                           "Sincerely,\n"
                           f"We're a Pyramid Scheme & so is {self.name}" +
                           divider)
        return thank_u_letter
