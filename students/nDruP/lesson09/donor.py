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

    def add_gift(self, value):
        self._history.append(round(value,2))
