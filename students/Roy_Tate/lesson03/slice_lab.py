# Author/Student: Roy Tate (githubtater)


str_sequence = "Humpty Dumpty sat and watched a movie"
num_sequence = 1, 2, 3, 4, 5, 6, 7

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)


def exchange_first_last(sequence):
    length = len(sequence)
    first, last = sequence[0], sequence[length-1]
    new_sequence = last + sequence[1:length-1] + first
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
    length = len(sequence)
    thirds = round(length / 3)
    first = sequence[:thirds]
    last = sequence[thirds:]
    middle = sequence[thirds + 1:length - thirds]
    print(length, thirds)
    return middle + last + first


def main():
    print(exchange_first_last(str_sequence))
    print(remove_every_other(str_sequence))
    print(remove_first_and_last_four_and_every_other(str_sequence))
    print(reverse_items(str_sequence))
    print(thirds_middle_last_first(str_sequence))

    # print(exchange_first_last(num_sequence))
    # print(remove_every_other(num_sequence))
    # print(remove_first_and_last_four_and_every_other(num_sequence))
    # print(reverse_items(num_sequence))
    print(thirds_middle_last_first(num_sequence))
    #
    # print(exchange_first_last(a_string))

# Assertion Tests #

    # assert exchange_first_last(a_string) == "ghis is a strint"
    # assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

    assert thirds_middle_last_first('onetwosix') == 'twosixone'

if __name__ == "__main__":
    main()


















































































# Author/Student: Roy Tate (githubtater)
