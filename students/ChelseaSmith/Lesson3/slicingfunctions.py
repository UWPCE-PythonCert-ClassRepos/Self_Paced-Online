def flip_first_last(seq):
    orig = tuple(seq)
    new = list(seq)
    new[0] = orig[-1]
    new[-1] = orig[0]
    return new


def remove_ev_other(seq):
    return seq[::2]


def ev_other_middle(seq):
    return seq[4:-4:2]


def reversed(seq):
    return seq[::-1]


def thirds(seq):
    cutter = seq[len(seq)//3:len(seq)*2//3] + seq[len(seq)*2//3:] + seq[:len(seq)//3]
    return cutter
