def exchange_first_last(seq):
    """Exchange first and last elements of input sequence with 
    length>1"""
    return seq[-1:] + seq[1:-1] + seq[:1]


def remove_every_other(seq):
    """Remove every other sequence element, starting at element 1"""
    return seq[::2]


def rm4_and_every_other(seq):
    """Remove first and last 4 elements, then every other element"""
    return remove_every_other(seq[4:-4])


def reverse_seq(seq):
    """Return reversed sequence"""
    return seq[::-1]


def reorder_thirds(seq):
    """Return middle third, then last third, then first third"""
    seq_slice = len(seq)//3
    return seq[seq_slice:] + seq[:seq_slice]

test_string = 'this is a test string'
short_string = 'abc'
test_list = ['this', 'is', 'my', 'test', 'list']

assert exchange_first_last(test_string) == 'ghis is a test strint'
assert exchange_first_last(short_string) == 'cba'
assert exchange_first_last(test_list) == ['list', 'is', 'my', 'test', 'this']

assert remove_every_other(test_string) == 'ti sats tig'
assert remove_every_other(short_string) == 'ac'
assert remove_every_other(test_list) == ['this', 'my', 'list']

assert rm4_and_every_other(test_string) == ' sats t'
assert rm4_and_every_other(short_string) == ''
assert rm4_and_every_other(test_list) == []

assert reverse_seq(test_string) == 'gnirts tset a si siht'
assert reverse_seq(short_string) == 'cba'
assert reverse_seq(test_list) == ['list', 'test', 'my', 'is', 'this']

assert reorder_thirds(test_string) == ' a test stringthis is'
assert reorder_thirds(short_string) == 'bca'
assert reorder_thirds(test_list) == ['is', 'my', 'test', 'list', 'this']
