# python3

# strformat_lab.py
import operator


def task_one(my_tuple):
    """
    my_tuple: tuple, ( 2, 123.4567, 10000, 12345.67)
    """

    # first item
    file = "{:{padding}>{str_len}}".format(my_tuple[0], padding=0, str_len=3)

    # second item
    two_dec = "{:.2f}".format(my_tuple[1])

    # third item
    int_to_scientific = "{:.2e}".format(my_tuple[2])

    # fourth item
    dec_to_scientific = "{:.2e}".format(my_tuple[3])

    r_string = "file_" + file + " :  " + two_dec + ", "\
        + int_to_scientific + ", " + dec_to_scientific

    return r_string


def task_two(my_tuple):
    """
    my_tuple: tuple, ( 2, 123.4567, 10000, 12345.67)
    """

    # first item
    align = ">"
    file = "{:{padding}{align}{str_len}}".\
        format(my_tuple[0], align=align, padding=0, str_len=3)

    # second item
    dec = "2"
    type_f = "f"  # fixed point
    two_dec = "{:.{dec}{type_f}}".format(my_tuple[1], dec=dec, type_f=type_f)

    # third item
    dec3 = "2"
    type3 = "e"
    int_to_scientific = "{:.{dec}{type_f}}".format(my_tuple[2], dec=dec3, type_f=type3)

    # fourth item
    dec4 = "2"
    type4 = "e"
    dec_to_scientific = "{:.{dec}{type_f}}".format(my_tuple[3], dec=dec4, type_f=type4)

    r_string = "file_" + file + " :  " + two_dec + ", "\
        + int_to_scientific + ", " + dec_to_scientific

    return r_string


# task three
def formatter(my_tuple):
    """
    my_tuple: tuple
    """
    n = len(my_tuple)
    num_holder = "{}, " * (n - 1) + "{}"
    form_string = "the {} numbers are: " + num_holder
    return form_string.format(n, *my_tuple)


def task_four(my_tuple):
    """
    my_tuple: tuple
    my_tuple = ( 4, 30, 2017, 2, 27)  return '02 27 2017 04 30'
    """
    n = len(my_tuple)
    order = 3, 4, 2, 0, 1
    format_string = ""
    for i in range(n):
        format_string += "{" + str(order[i]) + ":{padding}>{str_len}" + "}"
        if i < n - 1:
            format_string += ", "

    return format_string.format(*my_tuple, padding=0, str_len=2)


def task_five(my_list):
    """
    using f-string:
    my_list = ['oranges', 1.3, 'lemons', 1.1]
    Prints: The weight of an orange is 1.3 and the weight of a lemon is 1.1
    Prints: The weight of an ORANGE is 1.56 and the weight of a LEMON is 1.32
    """
    print(f"The weight of an {my_list[0]}, is {my_list[1]} and the weight of "
          + f"a {my_list[2]} is {my_list[3]}")

    print(f"The weight of an {my_list[0].upper()}, is {my_list[1] * 1.2} "
          + f"and the weight of a {my_list[2].upper()} is {my_list[3] * 1.2}")


def task_six():
    """
    name, an age and a cost
    """
    import random

    list_length = random.randint(10, 25)
    rows = []

    for _ in range(list_length):
        name_len = random.randint(4, 15)
        name = ""
        for _ in range(name_len):
            name += chr(random.randint(97, 122))

        age = random.randint(1, 1000000)

        cost = random.randint(1, 100000000)
        rows.append([name, age, cost])

    max_name_len = 0
    max_age = 0
    max_cost = 0
    for row in rows:
        if len(row[0]) > max_name_len:
            max_name_len = len(row[0])
        if row[1] > max_age:
            max_age = row[1]
        if row[2] > max_cost:
            max_cost = row[2]

    str_len_name = max_name_len + 3
    str_len_age = len(str(max_age)) + 3
    str_len_cost = len(str(max_cost)) + 3

    for row in rows:
        name_f = "Name: {:>{str_len_name}}"
        age_f = "    Age: {:>{str_len_age}}"
        cost_f = "    Cost: {:>{str_len_cost}}"
        form = name_f + age_f + cost_f
        print(form.format(*row, str_len_name=str_len_name,
                          str_len_age=str_len_age, str_len_cost=str_len_cost))


if __name__ == '__main__':
    tup = (2, 123.4567, 10000, 12345.67)
    my_tup = (4, 30, 2017, 2, 27)
    my_lst = ['orange', 1.3, 'lemon', 1.1]
    t = "task "
    a = task_one(tup)
    b = task_two(tup)
    field = 15
    o = operator.add
    c = o(t, "one"), a, o(t, "two"), b
    s = f"\n{c[0]:<{field}}: {c[1]}\n{c[2]:<{field}}: {c[3]}\n"
    print(s)

    c = o(t, "three:"), formatter(my_tup)
    s = f"{c[0]:<{field}}: {c[1]}\n"
    print(s)

    c = o(t, "four:"), task_four(my_tup)
    s = f"{c[0]:<{field}}: {c[1]}\n"
    print(s)

    c = o(t, "five:")
    s = f"{c:<{field}}:"
    print(s)
    task_five(my_lst)

    c = o(t, "six:")
    s = f"\n{c:<{field}}:"
    print(s)
    task_six()
