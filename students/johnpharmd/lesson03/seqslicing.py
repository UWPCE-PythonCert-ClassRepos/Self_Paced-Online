def seqxchg(seq):
    """
    This function returns a copy of the sequence passed but with
    the first and last items exchanged.
    """
    # new_seq = [seq[-1], seq[1:-1], seq[0]] -- this failed

    new_seq = None
    if type(seq) == str:
        new_seq = seq[-1] + seq[1:-1] + seq[0]
    
    elif type(seq) == list or type(seq) == tuple:
        new_seq = []
        new_seq.append(seq[-1])
        new_seq.extend(seq[1:-1])
        new_seq.append(seq[0])
        if type(seq) == tuple:
            new_seq = tuple(new_seq)

    return new_seq


def rm_everyother(seq):
    """
    This function returns the sequence passed but with every
    other item removed.
    """
    return seq[::2]


def rm_firstlast4_odds(seq):
    """
    The output from this function is a copy of the sequence passed
    but with the first 4 and last 4 items removed and then only
    every other item of the remaining original sequence.
    """
    new_seq = None
    if type(seq) == str:
        new_seq = seq[4:-5]

    if type(seq) == list or type(seq) == tuple:
        new_seq = []
        for i in range(len(seq)):
            if i > len(seq) - 5:
                break
            if i < 4:
                continue
            new_seq.append(seq[i])
        if type(seq) == tuple:
            new_seq = tuple(new_seq)

    return rm_everyother(new_seq)


def rev(seq):
    """
    This function returns the sequence passed but in reverse order.
    """
    return seq[::-1]


def rearrange(seq):
    """
    The output from this function is the same items in the sequence
    passed but with the order rearranged so that the order in the
    original is replaced with a new order made from the original:
    the middle third, then the last third, then first third.
    """
    new_seq = None
    div = int(len(seq) / 3)
    # original order: seq[ : div] + seq[div : div * 2] + seq[div * 2 :]
    if type(seq) == str:
        new_seq = seq[div : div * 2] + seq[div * 2 : ] + seq[ : div]
    
    if type(seq) == list or type(seq) == tuple:
        new_seq = []
        new_seq.extend(seq[div : div * 2])
        new_seq.extend(seq[div * 2 : ])
        new_seq.extend(seq[ : div])
        if type(seq) == tuple:
            new_seq = tuple(new_seq)

    return new_seq


# Tests
s = 'this is a very very very long string'
l = list(range(18))
t = tuple(range(18))

assert seqxchg(s) == 'ghis is a very very very long strint'
assert seqxchg(t) == (17, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 0)
assert rm_everyother(s) == 'ti savr eyvr ogsrn'
assert rm_everyother(t) == (0, 2, 4, 6, 8, 10, 12, 14, 16)
assert rm_firstlast4_odds(s) == ' savr eyvr ogs'
assert rm_firstlast4_odds(t) == (4, 6, 8, 10, 12)
assert rev(s) == 'gnirts gnol yrev yrev yrev a si siht'
assert rev(t) == (17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
assert rearrange(s) == 'ry very very long stringthis is a ve'
assert rearrange(t) == (6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 0, 1, 2, 3, 4, 5)


if True:
    print('All tests passed.')
