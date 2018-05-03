

class SA:
    """generates an array with only non-zero numeric values"""

    def __init__(self, seq):
        self.seq = seq
        self.seq_d = {i: j for i, j in enumerate(seq)}
        self._sparse_arr = ''

    def __getitem__(self, seq, index):
        """gives value of element at index given for specified seq"""
        return seq[index]

    @property
    def sparse_arr(self):
        """getter"""
        return self._sparse_arr

    @sparse_arr.setter
    def sparse_arr(self, value):
        self._sparse_arr = value

    def make_arr(self):
        self._sparse_arr = [v for v in self.seq_d.values() if v != 0]
        return self._sparse_arr

    def get_seq_len(self):
        """gives length of initializing seq"""
        return len(self.seq)
