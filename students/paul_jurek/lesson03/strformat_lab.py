"""module to solve string formatting lab for lesson 3"""
import pytest


# Task 1
"""Write a format string that will take the following four element tuple:
( 2, 123.4567, 10000, 12345.67)
and produce:
'file_002 :   123.46, 1.00e+04, 1.23e+04'"""
input = (2, 123.4567, 10000, 12345.67)
output = f'file_{input[0]:0=3} :   {input[1]:.2f}, {input[2]:.2E}, {input[3]:.3g}'
print(output)

# Task 2
# using standard format to compare with f-strings
output_format = 'file_{:0=3} :   {:.2f}, {:.2E}, {:.3g}'.format(input[0],
                                                                input[1],
                                                                input[2],
                                                                input[3])
print(output_format)


# task 3
def formatter(tup_input):
    """builds string to print out the numbers based off tuple input
    args:
        tup_input: vaiable length tuple with digit inputs
    returns:
        string stating number of items in tuple and listing them out
        this is output as variable"""

    template_str = 'the {} numbers are: '
    n = len(tup_input)
    fillin_str = ', '.join(['{}']*n)
    template_str += fillin_str

    return(template_str.format(n, *tup_input))


@pytest.mark.parametrize("test_input,expected", [
    ((1, 2, 3), 'the 3 numbers are: 1, 2, 3'),
    ((1, 2, 3, 4), 'the 4 numbers are: 1, 2, 3, 4'),
    ((1,), 'the 1 numbers are: 1'),
    ((), 'the 0 numbers are: ')
])
def test_formatter(test_input, expected):
    assert formatter(test_input) == expected

# task 4
"""Given a 5 element tuple:
( 4, 30, 2017, 2, 27)
use string formating to print:
'02 27 2017 04 30'
Hint: use index numbers to specify positions."""
def inside_out(tuple5):
    """funtion to re-order and print input
    args:
        tuple of length 5 containing strings.  Assume all strings and no input checking

    returns:
        str with output of 'tuple[3] tuple[4] tuple[2] tuple[0] tuple[1]' with formatting (see test)
        prints results to console"""
    
    output = f'{tuple5[3]:02} {tuple5[4]:02} {tuple5[2]:04} {tuple5[0]:02} {tuple5[1]:02}'
    print(output)
    return output

def test_inside_out():
    """Given a 5 element tuple:
        ( 4, 30, 2017, 2, 27)
        use string formating to print:
        '02 27 2017 04 30'
        Hint: use index numbers to specify positions."""
    input = ( 4, 30, 2017, 2, 27)
    assert inside_out(input) == '02 27 2017 04 30'

def format_fruit_list(fruits):
    """as part of task 5, this formats fruit lists
    ars:
        fruits: list of fruits which should be divisable by 2.  
            first entry is fruit name and second is weight in some unit
            eg. ['oranges', 1.3, 'lemons', 1.1]
    returns
        string telling fruit name and weight
            eg. The weight of an orange is 1.3 and the weight of a lemon is 1.1
    """
    pass

def test_format_fruit_list():
    """Here’s a task for you: Given the following four element list:
        ['oranges', 1.3, 'lemons', 1.1]
        Write an f-string that will display:
        The weight of an orange is 1.3 and the weight of a lemon is 1.1"""
    assert test_format_fruit_list(['oranges', 1.3, 'lemons', 1.1]) == 'The weight of an orange is 1.3 and the weight of a lemon is 1.1'
