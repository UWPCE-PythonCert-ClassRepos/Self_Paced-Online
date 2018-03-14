# Author/Student: Roy Tate (githubtater)

def exchange_first_last(sequence):
    new_sequence = sequence[-1] + sequence[1:len(sequence) - 1] + sequence[0]
    return new_sequence


def remove_every_other(sequence):
    return sequence[::2]


def remove_first_and_last_four_and_every_other(sequence):
    length = len(sequence)
    new_sequence = sequence[4:length-4]
    return new_sequence[::2]


def reverse_items(sequence):
    return sequence[::-1]


def thirds_middle_last_first(sequence):
    segment = len(sequence) // 3
    first = sequence[:segment]
    last = sequence[segment:]
    middle = sequence[segment:segment]
    return middle + last + first


def main():
    str_sequence = "Humpty Dumpty sat and watched a film"
    num_sequence = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15

    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    print('\nExchange first and last:\n', exchange_first_last(str_sequence))
    print('\nRemove every other:\n', remove_every_other(str_sequence))
    print('\nRemove first, last, and every other:\n', remove_first_and_last_four_and_every_other(str_sequence))
    print('\nReverse items:\n', reverse_items(str_sequence))
    print('\nThirds: Middle-Last-First:\n', thirds_middle_last_first(str_sequence))

    # print('\nExchange first and last:\n', exchange_first_last(num_sequence))
    print('\nRemove every other:\n', remove_every_other(num_sequence))
    print('\nRemove first, last, and every other:\n', remove_first_and_last_four_and_every_other(num_sequence))
    print('\nReverse items:\n', reverse_items(num_sequence))
    print('\nThirds: Middle-Last-First:\n', thirds_middle_last_first(num_sequence))
    #


# Assertion Tests #

    print('\n**** ASSERTION TESTS *****')
    assert exchange_first_last(a_string) == "ghis is a strint"
    # assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert thirds_middle_last_first('onetwosix') == 'twosixone'
    print('_________END TESTS________')




if __name__ == "__main__":
    main()


















































































# Author/Student: Roy Tate (githubtater)
