# Joshua Bone - UW Python 210 - Lesson 3
# 12/20/2018
# String Formatting Lab Exercise


def formatter(t):
    return (f'the {len(t):d} numbers are: ' +
            ', '.join(['{:d}'] * len(t)).format(*t))


if __name__ == "__main__":
    # Task One
    test_case_1 = (2, 123.4567, 10000, 12345.67)
    exp_1 = 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    act_1 = "file_{:0>3d} : {:8.2f}, {:.2e}, {:.2e}".format(*test_case_1)
    assert(exp_1 == act_1)

    # Task Two
    a, b, c, d = test_case_1
    act_2 = f"file_{a:0>3d} : {b:8.2f}, {c:.2e}, {d:.2e}"
    assert(exp_1 == act_2)

    # Task Three
    test_case_3a = (2, 3, 5)
    test_case_3b = (2, 3, 5, 7, 9)
    exp_3a = 'the 3 numbers are: 2, 3, 5'
    exp_3b = 'the 5 numbers are: 2, 3, 5, 7, 9'
    assert(formatter(test_case_3a) == exp_3a)
    assert(formatter(test_case_3b) == exp_3b)

    # Task Four
    a, b, c, d, e = 4, 30, 2017, 2, 27
    exp_4 = '02 27 2017 04 30'
    act_4 = f'{d:0>2d} {e:d} {c:d} {a:0>2d} {b:d}'
    assert(exp_4 == act_4)

    # Task Five
    test_case_5 = ['oranges', 1.3, 'lemons', 1.1]
    exp_5a = 'The weight of an orange is 1.3 and the weight of a lemon is 1.1'
    a, b, c, d, = test_case_5
    act_5a = (f'The weight of an {a[0:-1]} is {b:.1f} and ' +
              f'the weight of a {c[0:-1]} is {d:.1f}')
    assert(exp_5a == act_5a)

    exp_5b = 'The weight of an ORANGE is 1.6 and the weight of a LEMON is 1.3'
    act_5b = (f'The weight of an {a[0:-1].upper()} is {b * 1.2:.1f} and ' +
              f'the weight of a {c[0:-1].upper()} is {d * 1.2:.1f}')
    assert(exp_5b == act_5b)

    # Task Six
    test_case_6a = (("Heidi", 101, 123.45),
                    ("Cherry", 37, 5678.90),
                    ("Vaya", 6, 10200.12))
    exp_6a = ("Heidi   101    123.45\n" +
              "Cherry   37   5678.90\n" +
              "Vaya      6  10200.12")
    act_6a = '\n'.join(("{:8}{:3}{:10.2f}".format(*r) for r in test_case_6a))
    assert(exp_6a == act_6a)

    test_case_6b = tuple(range(10))
    exp_6b = "    0    1    2    3    4    5    6    7    8    9"
    act_6b = ("{:5d}" * len(test_case_6b)).format(*test_case_6b)
    assert(exp_6b == act_6b)
    print("Tests passed.")

