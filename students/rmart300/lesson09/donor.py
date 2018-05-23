

class Donor(object):

    def __init__(self, name):

        try:
            name.split()[1]
        except IndexError as e:
            print('The first and last name of donor must be provided\n')
            raise
        else:
            self.first_name = name.split()[0]
            self.last_name = name.split()[1]

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

