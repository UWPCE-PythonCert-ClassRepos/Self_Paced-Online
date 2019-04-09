#!/usr/bin/env python3

"""Demonstrate pythons string formatting features"""

tupl = (2, 123.4567, 10000, 12345.67)
formatter_task_one = "file_{:03d}: {:.2f}, {:.2e}, {:03.2e}".format

def formatter_task_two(tupl):
    """Format the tuple into a string as in task 1 using an f string"""
    file_string = (
        f"file_{str(tupl[0]).zfill(3)}: {tupl[1]:.2f}, {tupl[2]:.2e}, {tupl[3]:03.2e}"
        )
    return file_string

tupl3_1 = (2,3,5)
tupl3_2 = (2,3,5,7,9)
def formatter_task_three(in_tuple):
    """Dynamically build a formatt string to accept a tuple of any length

    The output for tuple of longth X should look like
    "The X numbers are: Val1, Val2, ...., ValX"
    """
    form_string = f"The {len(in_tuple)} numbers are: {(', ').join(['{}']*len(in_tuple))}"
    return form_string.format(*in_tuple)

tupl4 = ( 4, 30, 2017, 2, 27)
def formatter_task_four(in_5tuple):
    """Rearrange a 5 element tuple and add some zero padding"""
    #Could just generate the format string,
    #but i sorta like the documentation that comes with a function
    #end usage looks the same, just a bit more verbose creating it
    form_string = "{3:02d} {4} {2} {0:02d} {1}".format(*in_5tuple)
    return form_string

list5 = ['oranges', 1.3, 'lemons', 1.1]
def formatter_task_five(in_4list):
    """An f-string that will format fruit weights:

    The weight of an orange is 1.3 and the weight of a lemon is 1.1
    """
    form_string = (
        f"The weight of an {in_4list[0][:-1]} is {in_4list[1]} "
        f"and the weight of a {in_4list[2][:-1]} is {in_4list[3]}"
        )
    return form_string



def formatter_task_five_caps_heavier(in_4list):
    """display the names of the fruit in upper case, and the weight 1.2 times higher"""
    form_string = (
        f"The weight of an {in_4list[0][:-1].capitalize()} is {in_4list[1]*1.2} "
        f"and the weight of a {in_4list[2][:-1].capitalize()} is {in_4list[3]*1.2}"
        )
    return form_string



rows6 = (
    ('First', '$99.01', 'Second', '$88.09'),
    ('First', '$99999.01', 'Second', '$8888.09'),
    ('First', '$999.01', 'Second', '$8.09'),
    ('First', '$99.01', 'Second', '$888.09')
    )
def formatter_align_columns(tuple_of_rows):
    """print a PRETTY table of several rows, each with a name, an age and a cost"""
    row_list = []
    for row in tuple_of_rows:
        row_list.append("{0:20}{1:>10}{4:^10}{2:20}{3:>12}".format(*row, "|"))
    form_string = ('\n'.join(row_list))
    return form_string

def tests():
    """Test the string fomrtting functions"""
    assert(formatter_task_one(*tupl) == 'file_002: 123.46, 1.00e+04, 1.23e+04')
    assert(formatter_task_two(tupl) == 'file_002: 123.46, 1.00e+04, 1.23e+04')
    assert(formatter_task_three(tupl3_1) == 'The 3 numbers are: 2, 3, 5')
    assert(formatter_task_three(tupl3_2) == 'The 5 numbers are: 2, 3, 5, 7, 9')
    assert(formatter_task_four(tupl4) == '02 27 2017 04 30')
    assert(formatter_task_five(list5) == (
        'The weight of an orange is 1.3 and the weight of a lemon is 1.1'))
    assert(formatter_task_five_caps_heavier(list5) == (
        'The weight of an Orange is 1.56 and the weight of a Lemon is 1.32'))
    pass

def exercise_demo(func_in, task_num, *args_in):
    """Print the lesson, exercise and task before demonstrating completion"""
    print(f'Lesson3: Series Exercise - Task {task_num}')
    print(f'{func_in.__doc__}')
    for arg in args_in:
        print(func_in(arg))
    print("")

if __name__ == "__main__":
    tests()
    print('Lesson3: String Formatting Exercise')
    print('Lesson3: Task One')
    print(formatter_task_one(*tupl))
    print('')
    exercise_demo(formatter_task_two, 'Two', tupl)
    exercise_demo(formatter_task_three, 'Three', tupl3_1,tupl3_2)
    exercise_demo(formatter_task_four, 'Four', tupl4)
    exercise_demo(formatter_task_five, '5.1', list5)
    exercise_demo(formatter_task_five_caps_heavier, '5.2', list5)
    exercise_demo(formatter_align_columns, '6', rows6)

