# Author/Student: Roy Tate (githubtater)

ast = '*'


# Task 1 #

def multi_str_format(num_sequence):
    '''Takes a tuple and prints the numbers in the specified format'''
    print('\n{:*^40}'.format('Task 1 - Multi-string Format'))
    return ('file_' + str(num_sequence[0]).zfill(3) + ': ' "{0:.2f}".format(num_sequence[1]),
          "{:.2e}".format(num_sequence[2]), "{:.2e}".format(num_sequence[3]))


# Task 2 #

def alt_str_format(num_sequence):

    print('\n{:*^40}'.format('Task 2 - Alternate Format'))
    filename = 'file_' + str(num_sequence[0]).zfill(3)
    float_pnt = "{0:.2f}".format(num_sequence[1])
    any_number = "{:.2e}".format(num_sequence[2])
    lotsa_digits = "{:.2e}".format(num_sequence[3])
    return '{filename}: {float_pnt}, {any_number}, {lotsa_digits}'.format(filename=filename,
        float_pnt=float_pnt, any_number=any_number, lotsa_digits=lotsa_digits)


# Task 2 - Continued #

def f_str_format(num_sequence):
    print('\n{:*^40}'.format('Task 2 - Continued'))
    filename = 'file_' + str(num_sequence[0]).zfill(3)
    float_pnt = "{0:.2f}".format(num_sequence[1])
    any_number = "{:.2e}".format(num_sequence[2])
    lotsa_digits = "{:.2e}".format(num_sequence[3])
    return f'{filename}: {float_pnt}, {any_number}, {lotsa_digits}'


# Task 3 - Rewrite #

def rewrite(num_sequence,):
    print('\n{:*^40}'.format('Task 3 - Rewrite'))
    form_string = "{:d}, " * len(num_sequence)
    full_string = "the " + str(len(num_sequence)) + " numbers are: "
    return full_string + form_string.format(*num_sequence)

# Task 4 - Format given tuple #

def format_given_tuple(given_tuple):
    print('\n{:*^40}'.format('Task 4 - Print the Given Tuple'))
    padded_a = str(given_tuple[3])
    padded_b = str(given_tuple[0])
    thirty = str(given_tuple[1])
    year = str(given_tuple[2])
    number1 = str(given_tuple[4])
    return padded_a.zfill(2), number1, year, padded_b.zfill(2), thirty


# Task 5 #

def f_string_practice(given_list):
    print('\n{:*^40}'.format('Task 5 - f-string practice'))
    str_one = given_list[0]
    str_two = given_list[2]
    weight_one = str(given_list[1])
    weight_two = str(given_list[3])
    orig_string = "Original string: The weight of an " + str_one[:len(str_one)-1] + " is " + weight_one + \
                  " and the weight of a " + str_two[:len(str_two)-1] + " is " + weight_two
    print(orig_string)
    multiplier = 1.2
    weight_one_mp = str(given_list[1] * multiplier)
    weight_two_mp = str(given_list[3] * multiplier)
    use_f_string = f"The weight of an {str_one.upper()[:len(str_one)-1]} is {weight_one_mp} and the " \
                   f"weight of a {str_two.upper()[:len(str_two)-1]} is {weight_two_mp}"

    return 'f_string format: ' + use_f_string


# Task 6 #

def task_six_alignment(alignment_string):
    print('\n{:*^40}'.format('Task 6 - string alignment'))
    for name, age, cost in alignment_string:
        print('{:<20}{:10}{:30}'.format('Name: ' + name, 'Age:' + str(age), 'Cost: ' + str(cost)))

# Task 6 - Extra #
def split_ten(sequence):
    print('\n{:*^40}'.format('Task 6 - extra'))
    return '{:5}{:5}'.format(str(sequence[:5]), "\n" + str(sequence[5:]))
    ##it was getting late and I finally gave up on this one liner

def main():
    '''Create a couple of tuples and call each of the above functions'''
    a_tuple = (2, 123.4567, 10000, 12345.67)
    print(multi_str_format(a_tuple))
    print(alt_str_format(a_tuple))
    print(f_str_format(a_tuple))

    num_tuple = (3, 4, 2, 1, 5, 0)
    print(rewrite(num_tuple))

    given_tuple = (4, 30, 2017, 2, 27)
    print(format_given_tuple(given_tuple))

    given_list = ['oranges', 1.3, 'lemons', 1.1]
    print(f_string_practice(given_list))

    name_cost_list = [('Ahmed', 23, 34.2323), ('Arturo', 17, 90234.23423), ('Sally', 38, 23.21), ('Babs', 75, 23)]
    print(task_six_alignment(name_cost_list))

    ten_consecutive = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    print(split_ten(ten_consecutive))


if __name__ == "__main__":
    main()