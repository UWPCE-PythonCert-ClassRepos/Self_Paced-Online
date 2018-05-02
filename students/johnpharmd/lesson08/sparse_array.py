

class SA:
    """generates an array with only non-zero numeric values"""

    def __init__(self, seq):
        self.seq = seq
        self.seq_d = {i: j for i, j in enumerate(seq)}
        self._sparse_arr = ''

    @property
    def sparse_arr(self):
        """getter"""
        return self._sparse_arr

    @sparse_arr.setter
    def sparse_arr(self, value):
        self._sparse_arr = value

    def make_arr(self):
        return (item for item in self.seq_d.values() if item != 0)

    def get_len_arr(self):
        pass
