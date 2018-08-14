#  Exchange first and last items
def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]


# Remove every other item
def remove_items(seq):
    return seq[::2]


# Remove first 4 and the last 4 items, and then every other item in between
def first_last_four(seq):
    return seq[4:-4:2]


# Reverse the elements (just with slicing)
def reversed_seq(seq):
    return seq[::-1]


# Reorder to the middle third, then last third, then the first third
def seq_in_thirds(seq):
    seq_third = len(seq) // 3
    return seq[seq_third:] + seq[:seq_third]


def main():
    print("Test the slicing functions...")
    # Testing 1
    print("Test exchange_first_last()...")
    string_1 = "this is a string"
    list_1 = (28, 25, 2020, 3)
    assert exchange_first_last(string_1) == "ghis is a strint"
    assert exchange_first_last(list_1) == (3, 25, 2020, 28)
    # Testing 2
    print("Test remove_items()...")
    string_2 = "abcdefghij"
    list_2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    assert remove_items(string_2) == "acegi"
    assert remove_items(list_2) == (1, 3, 5, 7, 9, 11)
    # Testing 3
    print("Test first_last_four()...")
    string_3 = "abcdefghij"
    list_3 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    assert first_last_four(string_3) == "e"
    assert first_last_four(list_3) == (5, 7)
    # Testing 4
    print("Test reversed_seq()...")
    string_4 = "abcdefghij"
    list_4 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    assert reversed_seq(string_4) == "jihgfedcba"
    assert reversed_seq(list_4) == (12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
    # Testing 5
    print("Test seq_in_thirds()...")
    string_5 = "this is a string"
    list_5 = (1, 2, 3, 4, 5, 6, 7)
    assert seq_in_thirds(string_5) == "is a stringthis "
    assert seq_in_thirds(list_5) == (3, 4, 5, 6, 7, 1, 2)


if __name__ == "__main__":
    main()