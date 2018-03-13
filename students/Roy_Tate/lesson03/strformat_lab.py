# Author/Student: Roy Tate (githubtater)

ast = '*'


# Task 1 #

def multi_str_format(num_sequence):
    '''Takes a tuple and prints the numbers in the specified format'''
    print('\n{:*^40}'.format('Task 1 - Multi-string Format'))
    print('file_' + str(num_sequence[0]).zfill(3) + ': ' "{0:.2f}".format(num_sequence[1]),
          "{:.2e}".format(num_sequence[2]), "{:.2e}".format(num_sequence[3]))


# Task 2 #

def alt_str_format(num_sequence):
    ''''''
    print('\n{:*^40}'.format('Task 2 - Alternate Format'))
    filename = 'file_' + str(num_sequence[0]).zfill(3)
    float_pnt = "{0:.2f}".format(num_sequence[1])
    any_number = "{:.2e}".format(num_sequence[2])
    lotsa_digits = "{:.2e}".format(num_sequence[3])
    print('{filename}: {float_pnt}, {any_number}, {lotsa_digits}'.format(filename=filename,
        float_pnt=float_pnt, any_number=any_number, lotsa_digits=lotsa_digits))


# Task 2 - Continued #

def f_str_format(num_sequence):
    print('\n{:*^40}'.format('Task 2 - Continued'))
    filename = 'file_' + str(num_sequence[0]).zfill(3)
    float_pnt = "{0:.2f}".format(num_sequence[1])
    any_number = "{:.2e}".format(num_sequence[2])
    lotsa_digits = "{:.2e}".format(num_sequence[3])
    print(f'{filename}: {float_pnt}, {any_number}, {lotsa_digits}')


# Task 3 - Rewrite #

def rewrite(num_sequence):
    print('\n{:*^40}'.format('Task 3 - Rewrite'))
    digits = '{:d}'
    count = 0
    for numbers in num_sequence:
        count += 1

    print('the ' + str(count) + ' numbers are: ' + digits * count)





def main():
    a_tuple = (2, 123.4567, 10000, 12345.67)
    multi_str_format(a_tuple)
    alt_str_format(a_tuple)
    f_str_format(a_tuple)
    rewrite(a_tuple)

if __name__ == "__main__":
    main()