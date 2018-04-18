"""
Slicing Lab Assignment
"""
def exchange_first_last(seq):
    """function to switch first and last elements"""
    new_seq = seq[-1:] + seq[1:-1] + seq[:1]

    return new_seq


def every_other(seq):
    """print everyother element"""
    if isinstance(seq, tuple):
        print(seq[::2])
        return tuple(seq[::2])

    elif isinstance(seq, str):
        print(seq[::2])
        return str(seq[::2])

    print(seq[::2])
    return seq[::2]


def four_in_to_four_out(seq):
    """function to start four elements in print every other till four elements from end"""
    print(seq[4:-4:2])
    return seq[4:-4:2]


def reverse_seq(seq):
    """print series reversed"""
    print(seq[::-1])
    return seq[::-1]


def switch_thirds(seq):
    """print first third, second third and third third in new order"""
    new_seq = seq
    if isinstance(seq, tuple):
        list(new_seq)
    third_length = int((len(seq) // 3))
    #switched = new_seq[2*third_length:] + \
        #new_seq[:third_length] + new_seq[third_length:2*third_length]
    switched = seq[third_length:] + seq[:third_length]
    #if isinstance(seq, tuple):
        #tuple(switched)
    print(switched)
    return switched


if __name__ == '__main__':
    """ Tests"""
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

    assert every_other(a_string) == "ti sasrn"
    assert every_other(a_tuple) == (2, 13, 5)

    assert four_in_to_four_out(a_string) == ' sas'
    assert four_in_to_four_out(a_tuple) == ()

    assert reverse_seq(a_string) == "gnirts a si siht"
    assert reverse_seq(a_tuple) == (32, 5, 12, 13, 54, 2)

    assert switch_thirds(a_string) == "is a stringthis "
    assert switch_thirds(a_tuple) == (13, 12, 5, 32, 2, 54)
