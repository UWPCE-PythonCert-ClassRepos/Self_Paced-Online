def flip_first_last(seq):
    orig = tuple(seq)  # make a tuple so this stays safe
    new = list(seq)  # make a list to mess around with
    new[0] = orig[-1]  # make first value of new list last value of old list
    new[-1] = orig[0]  # make last value of new list first value of old list
    return new


def remove_ev_other(seq):
    return seq[::2]  # skips every other value


def ev_other_middle(seq):
    return seq[4:-4:2]  # skips first 4 values, ends 4 from end, skips every other value


def reversed(seq):
    return seq[::-1]


def thirds(seq):
    cutter = seq[len(seq)//3:len(seq)*2//3] + seq[len(seq)*2//3:] + seq[:len(seq)//3]
    return cutter
