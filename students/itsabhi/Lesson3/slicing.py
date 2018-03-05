def exchange_first_last(a):
    a_seq = a
    a_new_seq = a_seq[-1:] + a_seq[1:-1] + a_seq[0:1]
    return a_new_seq


def main():
    lab_string = "this is a string"
    lab_tuple = (2, 54, 13, 12, 5, 32)
    assert exchange_first_last(lab_string) == "ghis is a strint"
    assert exchange_first_last(lab_tuple) == (32, 54, 13, 12, 5, 2)


if __name__ == '__main__':
    main()
