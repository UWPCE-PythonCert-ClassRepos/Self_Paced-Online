# Author/Student: Roy Tate (githubtater)


str_sequence = "Humpty Dumpty sat and watched a film"
num_sequence = 1, 2, 3, 4, 5, 6, 7

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)


def exchange_first_last(sequence):
    first = sequence[0]
    print('first: ', first)
    last = sequence[-1]
    print('last: ', last)
    middle = sequence[1:len(sequence) -1]
    print(middle)
    new_sequence = last + middle + first
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
    if len(sequence) % 3 == 0:
        segment = int(len(sequence) / 3)
        first = sequence[:segment]
        last = sequence[segment:]
        middle = sequence[segment:segment * 2]
        return middle + last + first
    else:
        print("The input string must be divisible by 3. Current length: ", len(sequence))


def main():
    print('\nExchange first and last:\n',exchange_first_last(str_sequence))
    print('\nRemove every other:\n', remove_every_other(str_sequence))
    print('\nRemove first, last, and every other:\n', remove_first_and_last_four_and_every_other(str_sequence))
    print('\nReverse items:\n', reverse_items(str_sequence))
    print('\nThirds: Middle-Last-First:\n', thirds_middle_last_first(str_sequence))

    print(exchange_first_last(num_sequence))
    # print(remove_every_other(num_sequence))
    # print(remove_first_and_last_four_and_every_other(num_sequence))
    # print(reverse_items(num_sequence))
    # print(thirds_middle_last_first(num_sequence))
    #
    # print(exchange_first_last(a_string))

# Assertion Tests #

    print('\n**** ASSERTION TESTS *****')
    # assert exchange_first_last(a_string) == "ghis is a strint"
    # assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    print('_________END TESTS________')

    # assert thirds_middle_last_first('onetwosix') == 'twosixone'

if __name__ == "__main__":
    main()


















































































# Author/Student: Roy Tate (githubtater)
