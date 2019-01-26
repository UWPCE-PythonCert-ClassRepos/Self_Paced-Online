def task_one(t):
    """Use 'format' to return variety of string formats."""
    return 'file_{:0>3d}, {:.2f}, {:.2e}, {:.3e}'.format(*t)


def task_two(t):
    """Use 'f-string' to return same string formatting as task one"""
    return f'file_{t[0]:0>3d}, {t[1]:.2f}, {t[2]:.2e}, {t[3]:.3e}'


def task_three(t):
    """Return variable length string listing elements of tuple t."""
    if len(t) == 0:
        return "there are no numbers"
    elif len(t) == 1:
        return f'the number is {t[0]}'
    else:
        form_string = ["the {} numbers are: {}"]
        for i in range(len(t)-1):
            form_string.append('{}')
        form_string = ", ".join(form_string)
        return form_string.format(len(t), *t)


def task_four(t):
    """Given 5 element tuple, return a string with each element at a specific position and format"""
    return f'{t[3]:0>2d} {t[4]} {t[2]} {t[0]:0>2d} {t[1]}'


def task_five(t):
    """Use f-strings to display altered names of fruit and altered weights"""
    print(f'The weight of an {t[0][:-1].upper()} is {t[1]*1.2} and the weight of a {t[2][:-1].upper()} is {t[3]*1.2}')


def task_six(t):
    """Display data in columns that resize depending on number of characters."""
    mtl = []
    for i in range(len(t[0])):
        tl = 0
        for row in t:
            if len(row[i]) > tl:
                tl = len(row[i])
        mtl.append(tl+3)

    form_string = []
    for i in mtl:
        form_string.append('{:'+str(i)+'}')
    form_string = ''.join(form_string)

    for row in range(len(t)):
        print(form_string.format(*t[row]))

    '''Print 10 element tuple in columns 5 characters wide'''
    t10 = (1, 2, 3, 4, 5678, 67, 7, 8234, 9, 10)
    print(('{:<5}'*len(t10)).format(*t10))


def main():
    print(task_one((2, 123.4567, 10000, 12345.67)))
    print(task_two((2, 123.4567, 10000, 12345.67)))
    print(task_three((1, 2, 3, 4, 5)))
    print(task_four((4, 30, 2017, 2, 27)))
    task_five(['oranges', 1.3, 'lemons', 1.1])
    task_six((('Name', 'Age', 'Cost'), ('Todd', '24', '$8888.09'), ('Nancy', '8', '$9999999.02'),
              ('Methuselah', '969', '$9.99')))


if __name__ == '__main__':
    main()
