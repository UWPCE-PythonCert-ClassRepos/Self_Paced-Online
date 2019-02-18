# Joshua Bone - UW Python 210 - Lesson 9
# 02/10/2019
# Assignment: Mailroom, Object Oriented

class MenuOption:
    def __init__(self, next_menu=None, token=None, desc=None, *, 
            evaluate=None,
            action=lambda i: None,
            hidden=False
            ):
        self._token = token
        self._desc = desc
        if evaluate is not None:
            self._evaluate = evaluate
        else:
            self._evaluate = lambda i: i == self.token
        self._action = action
        self._next_menu = next_menu
        self._hidden = hidden

    @property
    def token(self):
        return self._token

    @property
    def desc(self):
        return self._desc

    @property
    def evaluate(self):
        return self._evaluate

    @property
    def action(self):
        return self._action

    @property
    def next_menu(self):
        return self._next_menu

    @property
    def hidden(self):
        return self._hidden

    def __str__(self):
        return f"[{self.token}]: {self.desc}"
