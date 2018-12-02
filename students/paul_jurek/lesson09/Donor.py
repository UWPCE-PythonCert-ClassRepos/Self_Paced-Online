"""donor class controlling donor behavior"""

class Donor:
    """donor giving to organization"""

    def __init__(self, id, firstname=None, lastname=None):
        if isinstance(int(id), int):
            self.id = id
        else:
            raise ValueError('id input must be interpretted as integer')
        self.firstname = firstname
        self.lastname = lastname
