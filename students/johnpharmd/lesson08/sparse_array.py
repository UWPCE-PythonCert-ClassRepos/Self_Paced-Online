

class SA:
    """generates a 2D array with only non-zero numeric values"""

    def __init__(self, seq):
        self.seq = seq
        self.seq_dictionary = {seq.index(item)-1: str(item) for item in seq
                               if item != 0}
        # self.seq_dictionary[0] = 'nil'

    def make_array(self):
        print('self.seq is', self.seq)
        print('self.seq_dictionary is', self.seq_dictionary)
        return '[' + ', '.join(self.seq_dictionary.values()) + ']'
