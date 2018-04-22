# Brandon Henson
# Lesson 3
# StrFormat
# 4/6/18


def task_one():
    print("__________Task One__________")
    # Write a format string that will take the following four element tuple:
    tuple1 = (2, 123.4567, 10000, 12345.67)
    # and produce
    formatted = 'file_{:0>4d} : {:3.2f} , {:.2e} , {:03.2e}'.format(*tuple1)
    # 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    print(formatted)


def task_two():
    # Using your results from Task One, repeat the exercise,
    # but this time using an alternate type of format string
    # (hint: think about alternative ways to use .format() (keywords anyone?)
    # and also consider f-strings
    # if you’ve not used them already)
    print("__________Task Two__________")
    tuple_results = ('file_0002', 123.46, 1.00e+04, 1.23e+04)
    print(f'{tuple_results[0]:s} :  {tuple_results[1]:.2f}, \
    {tuple_results[2]:.2e}\, {tuple_results[3]:.2e}')


def task_three(tuple1):
    print("__________Task Three__________")
    # Rewrite to take an arbitrary number of values.
    # "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
    seq = []
    for i in tuple1:
        seq.append(i)
    l = len(seq)
    print(("The {} numbers are: " + ",".join(["{}"] * l)).format(l, * seq))


def task_four():
    print("__________Task Four__________")
    five_numbers = (4, 30, 2017, 2, 27)
    print("{3:02d} {4} {2} {0:02d} {1}".format(*five_numbers))


def task_five():
    print("__________Task Five__________")
    list1 = ['oranges', 1.3, 'lemons', 1.1]
    # Write an f-string that will display:
    # The weight of an orange is 1.3 and the weight of a lemon is 1.1
    print(f'The weight of an {list1[0] [:-1]} is {list1[1]} and the weight\
    of a {list1[2] [:-1]} is {list1[3]}')
    print()
    #  displays the names of the fruit in upper case, and the weight 20% higher
    print(f'The weight of an {list1[0] [:-1].upper()} is {list1[1]*1.2} and the\
    weight of a {list1[2] [:-1].upper()} is {list1[3]*1.2}')


def task_six():
    print("__________Task Six__________")
    list_names = ['Brandon', 'Jared', 'Matt', 'John']
    list_ages = [10, 33, 99, 100]
    list_costs = [450.0000, 200000.00, 14.65, 100000.00]
    for i in range(len(list_names)):
        print(f'{list_names[i]:10s} {list_ages[i]:10n} {list_costs[i]:20n}')

