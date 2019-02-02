# Slicing LAB
def exchange_first_last(seq):
    """Invert the first and last element from a sequence"""
    if len(seq) > 1:
        if type(seq) is tuple:
            last_first = (seq[-1], *seq[1:-1], seq[0])
            return last_first
        elif type(seq) is str:
            last_first = seq[-1] + seq[1:-1] + seq[0]
            return last_first
        elif type(seq) is list:
            last_first = [seq[-1], *seq[1:-1], seq[0]]
            return last_first
    else:
        return seq


def every_other_remove(seq):
    """Remove every other element from a sequence"""
    if len(seq) > 1:
        if type(seq) is tuple:
            last_first = (seq[::2])
            print(last_first)
            return last_first
        elif type(seq) is str:
            last_first = seq[::2]
            print(last_first)
            return last_first
        elif type(seq) is list:
            last_first = seq[::2]
            print(last_first)
            return last_first
    else:
        return seq


def f4_l4_every_other_remove(seq):
    """Remove first 4 and last 4 and remove every other item in between"""
    if len(seq) > 1:
        if type(seq) is tuple:
            f4_l4 = (seq[4:-4:2])
            print(f4_l4)
            return f4_l4
        elif type(seq) is str:
            f4_l4 = seq[4:-4:2]
            print(f4_l4)
            return f4_l4
        elif type(seq) is list:
            f4_l4 = [seq[4:-4:2]]
            print(f4_l4)
            return f4_l4
    else:
        print(seq)
        return seq


def element_reverse(seq):
    """Reverse the elements"""
    if len(seq) > 1:
        if type(seq) is tuple:
            reverse = (seq[::-1])
            print(reverse)
            return reverse
        elif type(seq) is str:
            reverse = seq[::-1]
            print(reverse)
            return reverse
        elif type(seq) is list:
            reverse = seq[::-1]
            print(reverse)
            return reverse
    else:
        print(seq)
        return seq


def mid_last_first(seq):
    """Middle 3 + Last 3 + first 3"""
    if len(seq) > 1:
        if type(seq) is tuple:
            mid_last_first_v = (*seq[int(len(seq)/3):int((len(seq)/3)*2):1], *seq[-int(len(seq)/3)::1],
                                *seq[:int(len(seq)/3):1])
            print(mid_last_first_v)
            return mid_last_first_v
        elif type(seq) is str:
            mid_last_first_v = seq[int(len(seq)/3):int((len(seq)/3)*2):1] + seq[-int(len(seq)/3)::1]\
                               + seq[:int(len(seq)/3):1]
            print(mid_last_first_v)
            return mid_last_first_v
        elif type(seq) is list:
            mid_last_first_v = [*seq[int(len(seq)/3):int((len(seq)/3)*2):], *seq[-int(len(seq)/3)::],
                                *seq[:int(len(seq)/3):]]
            print(mid_last_first_v)
            return mid_last_first_v
    else:
        print(seq)
        return seq


exchange_first_last([1, 4])
exchange_first_last([1, 2, 3, 4])
exchange_first_last((1, 2, 3, 4, 5))
exchange_first_last('This is a test string for functions')
exchange_first_last((1,5))
exchange_first_last((1,))
exchange_first_last('m')
every_other_remove((1, 2, 3, 4))
every_other_remove([1, 2, 3, 4])
every_other_remove('This is a test string for functions')
f4_l4_every_other_remove((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13))
f4_l4_every_other_remove('This is a test string for functions')
element_reverse((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13))
mid_last_first((2, 54, 13, 12, 5, 32))
mid_last_first('This is a test string for functions')
mid_last_first([1, 2, 3, 4])

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert element_reverse((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13)) == (13, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2,
                                                                            1)

