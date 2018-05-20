class Donor():
    def __init__(self, title, gift):
        self.name = title
        self.history = []
        if type(gift) == int or type(gift) == float:
            self.history.append(round(gift, 2))
        elif type(gift) == list:
            for x in gift:
                self.history.append(round(x, 2))

    def __len__(self):
        return len(self_history)

    @property
    def avg_gift(self):
        return sum(self.history)/len(self.history)

    @property
    def sum_gift(self):
        return sum(self.history)

    @property
    def info(self):
        return (self.name, len(self.history), self.avg_gift, self.sum_gift)

    def add_gift(self, value):
        self.history.append(round(value, 2))

    def challenge(self, factor, min_gift=None, max_gift=None):
        if min_gift is None:
            min_gift = min(self.history)
        if max_gift is None:
            max_gift = max(self.history)
        filt_hist = list(filter(lambda x: x >= min_gift and x <= max_gift,
                                self.history))
        remain_hist = list(filter(lambda x: x < min_gift or x > max_gift,
                                  self.history))
        filt_hist = list(map(lambda x: x*factor, filt_hist))
        return Donor("*"+self.name, filt_hist+remain_hist)

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
