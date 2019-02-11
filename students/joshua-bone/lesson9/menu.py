# Joshua Bone - UW Python 210 - Lesson 9
# 02/10/2019
# Assignment: Mailroom, Object Oriented

from menu_option import MenuOption

class Menu:
    def __init__(self, 
            title="Menu", 
            instr=("Please select from the following options:",),
            default=None):
        self._title = title
        self._instr = instr
        self._options = []
        self._default = default if default is not None else MenuOption(self)

    @property
    def title(self):
        return self._title

    @property
    def instr(self):
        return self._instr

    @property
    def options(self):
        return tuple(self._options)

    @property
    def default(self):
        return self._default

    def add_options(self, options):
        self._options.extend(options)

    def add_option(self, option):
        self._options.append(option)

    def evaluate(self, token):
        next_menu = self.default.next_menu
        do_action = self.default.action
        for o in self.options:
            if o.evaluate(token):
                next_menu = o.next_menu
                do_action = o.action
                break
        return do_action(token), next_menu



