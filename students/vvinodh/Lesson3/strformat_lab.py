FOUR_ELE_TUPLE = (2, 123.4567, 10000, 12345.67)


def task1():
    print(f"file_{FOUR_ELE_TUPLE[0]:03d} :  {FOUR_ELE_TUPLE[1]:.2f}, {FOUR_ELE_TUPLE[2]:.2e}, {FOUR_ELE_TUPLE[3]:.2e}")

def task2():
    print("file_%03d :  %.2f, %.2e, %.2e" % FOUR_ELE_TUPLE)

def task3(in_tuple):
    s = "the 3 numbers are: {:d}, {:d}, {:d}"
    return s.format(*in_tuple)

def task4():
    five_ele_tuple = (4, 30, 2017, 2, 27)
    print("{3:02d} {4} {2} {0:02d} {1}".format(*five_ele_tuple))

def task5():
    a = "orange"
    b = 1.3
    c = "lemon"
    d = 1.1
    out = f"The weight of an {a} is {b} and the weight of a {c} is {d}"
    print(out)
    out1 = f"The weight of an {a.upper()} is {b} and the weight of a {c.upper()} is {d*1.2}"
    print(out1)

def task6():

    rows = [
        ['Vinodh', 10, '$10.00'],
        ['Alpha', 20, '$100.00'],
        ['Beta', 30, '$1000.00'],
        ['Gamma', 40, '$10000.00'],
    ]
    for row in rows:
        print('{0:<20}{1:^3}{2:>12}'.format(row[0], row[1], row[2]))

def task6i():
    input = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(('{:<5}'*len(input)).format(*input))