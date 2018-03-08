def exchange_first_last(a):
    a_seq = a
    a_new_seq = a_seq[-1:] + a_seq[1:-1] + a_seq[0:1]
    return a_new_seq


def remove_every_other(a):
    a_seq = a
    a_new_seq = a_seq[0::2]
    return a_new_seq


def remove_f4_l4(a):
    a_seq = a
    a_new_seq = a_seq[4:-4]
    return a_new_seq


def reverse_seq(a):
    a_seq = a
    a_new_seq = a_seq[::-1]
    return a_new_seq


def reorder_seq(a):
    a_seq = a
    a_new_seq = a_seq[3:-3] + a_seq[-3:] + a_seq[0:3]
    return a_new_seq


def main():
    lab_string = "this is a string"
    lab_tuple = (2, 54, 13, 12, 5, 32)
    assert exchange_first_last(lab_string) == "ghis is a strint"
    assert exchange_first_last(lab_tuple) == (32, 54, 13, 12, 5, 2)
    assert remove_every_other(lab_string) == "ti sasrn"
    assert remove_every_other(lab_tuple) == (2, 13, 5)
    assert remove_f4_l4(lab_string) == " is a st"
    assert remove_f4_l4(lab_tuple) == ()
    assert reverse_seq(lab_string) == "gnirts a si siht"
    assert reverse_seq(lab_tuple) == (32, 5, 12, 13, 54, 2)
    assert reorder_seq(lab_string) == "s is a stringthi"
    assert reorder_seq(lab_tuple) == (12, 5, 32, 2, 54, 13) #Due to the length of this sequence, middle sequence is empty.


if __name__ == '__main__':
    main()
