#!/usr/bin/env python3

# Task One

seq_in = (2, 123.4567, 10000, 12345.67)

file_out = ''.join(['file_', format(seq_in[0], '03')])
float_dec_out = format(seq_in[1], '.2f')
sci_out = format(seq_in[2], '.2e')
sci_sig_out = format(seq_in[3], '.2e')

out_msg = '{}: {}, {}, {}'.format(file_out, float_dec_out, sci_out,
                                  sci_sig_out)

print(out_msg)

# Task Two

file_out_alt = f"file_{seq_in[0]:03}"
float_dec_out_alt = f"{seq_in[1]:.2f}"
sci_out_alt = f"{seq_in[2]:.2e}"
sci_sig_out_alt = f"{seq_in[3]:.2e}"

out_msg_alt = f"{file_out_alt}: {float_dec_out_alt}, {sci_out_alt}" \
               "{sci_sig_out_alt}"

print(out_msg_alt)

# Task Three


def formatter(tuple_in):
    t = tuple_in
    fstring = []
    for i in t:
        fstring.append('{:d}')
    out_msg = 'the {} numbers are: '.format(len(t))
    return out_msg + ', '.join(fstring).format(*t)


print(formatter((2, 3, 5, 7, 9)))

# Task Four


def formatter_four(tuple_in):
    t = tuple_in
    collect = []
    collect.append(format(t[3], '02'))
    collect.append(str(t[4]))
    collect.append(str(t[2]))
    collect.append(format(t[0], '02'))
    collect.append(str(t[1]))
    return ' '.join(collect)


print(formatter_four((4, 30, 2017, 2, 27)))

# Task Five

fstring_list = ['oranges', 1.3, 'lemons', 1.1]

fstring_text = f"The weight of an {fstring_list[0][:-1].upper()} " \
               f"is {fstring_list[1] * 1.2} and the weight of a " \
               f"{fstring_list[2][:-1].upper()} is {fstring_list[3] * 1.2}"

print(fstring_text)

# Task Six


def set_table(list_in):
    rows = list_in
    for row in rows:
        print('{:20}{:>10}{:>10}'.format(*row))


test_list = [
    ('Standard Aged', '5 years', '$25'),
    ('Middle Aged', '15 years', '$300'),
    ('Rediculously Aged', '100 years', '$14000')
]

set_table(test_list)


# Task Six (Extra)

nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(('{:5d}' * len(nums)).format(*nums))
