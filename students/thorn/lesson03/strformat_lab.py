""" #!/usr/bin/env python3 """

"""
Thomas Horn
- String Formatting Lab
"""

import random

def task_one(in_tuple = (2, 123.4567, 10000, 12345.67)):
    """ 
    Takes a tuple as a parameter and formats its members to the following:
    'file_002 :   123.46, 1.00e+04, 1.23e+04'
    1: Generates a filename.
    2: Float displayed with 2 decimal places.
    3: Integer displayed in scientific notation with 2 decimal places.
    4: Float displayed in scientific notation to 3 sig figs.
    """
    new_tuple = "file_{:03d} : {:.02f}, {:.2E}, {:.2E}".format(in_tuple[0], in_tuple[1], in_tuple[2], in_tuple[3])
    print("Task One: " + new_tuple)
    return new_tuple

def task_two(in_tuple = (2, 123.4567, 10000, 12345.67)):
    """ 
    Returns the same as task_one but using an alternate formatting method.
    F strings in this case.
    """
    new_tuple = f"file_{in_tuple[0]:03d} : {in_tuple[1]:.02f}, {in_tuple[2]:.2E}, {in_tuple[3]:.2E}"
    print("Task Two: " + new_tuple)
    return new_tuple

def task_three(in_tuple):
    """
    Rewrites "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3) to take an
    arbitrary amount of values.
    """
    in_tuple_length = len(in_tuple)
    # Create format string.
    base_add = "{:d}, "
    base_string = f"The {in_tuple_length} numbers are: {base_add * in_tuple_length}"
    print(f"Task 3: {base_string.format(*in_tuple)}")
    return base_string.format(*in_tuple)
    
def task_four(in_tuple = (4, 30, 2017, 2, 27)):
    """ 
    Takes a tuple and [0][1][2][3][4] and returns [3][4][2][0][1] with a 0
    padding for single digit numbers.
    Final output: '02 27 2017 04 30'
    """
    new_tuple = "{3:02d} {4} {2} {0:02d} {1}".format(*in_tuple)
    print("Task 4: " + new_tuple)
    return new_tuple

def task_five(in_list = ['oranges', 1.3, 'lemons', 1.1]):
    """ 
    Takes a four element list ['oranges', 1.3, 'lemons', 1.1] and displays
    "The weight of an orange is 1.3 and the weight of a lemon is 1.1" with
    f-strings.
    It then displays the names of the fruit in upper case, and the weight 20% 
    higher.
    """
    # Eliminate the end 's'.
    new_list = []
    for item in in_list:
        try:
            if item[-1].lower() == 's':
                new_item = item[:-1]
                new_list.append(new_item)
        except TypeError:
            new_list.append(item)
    first_string = f"The weight of an {new_list[0]} is {new_list[1]} and the weight of a {new_list[2]} is {new_list[3]}."
    print(first_string)

    # Capitalize strings and multiple numbers by 1.2.
    for index, item in enumerate(new_list):
        if type(item) == str:
            new_list[index] = item.upper()
        if type(item) == int or type(item) == float:
            new_list[index] = item * 1.2
    second_string = f"The weight of an {new_list[0]} is {new_list[1]} and the weight of a {new_list[2]} is {new_list[3]}."
    print(second_string)

    return first_string, second_string

def task_six():
    """ 
    Prints a formatted table.
    Then prints a tuple of 10 numbers and prints it in 5 character wide columns.
    """
    max_length = 0
    table = [['Name', 'Price', 'Type'], 
             ['Honda', 100.05, 'Car'],
             ['Toyota', 3001.22, 'Motorcycle'],
             ['BMW', 40005.13, 'SUV']]
    # Could use a max_length of the longest item in the list, but not necessary.
    for row in table:
        print("{: <10} {: >10} {:>20}".format(*row))

    # Print tuple with 5 character column.  Tuple is known to be 10 wide.
    in_tuple = tuple((x for x in range(10)))
    output_string = "{:5d} " * 10
    print(output_string.format(*in_tuple))
    

task_one()
task_two()

# Create tuple of random length.
list_base = []
tup_length = random.randint(1, 15)
for i in range(tup_length):
    list_base.append(i)
out_tuple = tuple(list_base)
task_three(out_tuple)

task_four()
task_five()
task_six()