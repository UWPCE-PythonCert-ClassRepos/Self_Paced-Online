class SparseArray(object):

    def __init__(self, my_list=None):
        if my_list is not None:
            self._my_list = my_list

        else:
            self._my_list = []

    def __len__(self):
        return(len(self._my_list))

    def __getitem__(self, ind):
        try:
            return self._my_list[ind]
        except IndexError:
            print("Index out of range, returning 0")
            return 0

    def __setitem__(self, ind, val):
        if self._my_list[ind] == val:
            print("that is already the value")
        else:
            self._my_list[ind] = val

    def __delitem__(self, ind):
        del self._my_list[ind]

    def __repr__(self):
        return("{}".format(self._my_list))


def main():
    sa = SparseArray([1, 2, 0, 0, 0, 0, 3, 0, 0, 4])
    print(sa)
    print(len(sa))
    print(sa[5])
    sa[5] = 12
    print(sa[5])
    del sa[4]
    print(sa)
    sa[3] = 0
    val = sa[13]
    print(val)
if __name__ == '__main__':
    main()
