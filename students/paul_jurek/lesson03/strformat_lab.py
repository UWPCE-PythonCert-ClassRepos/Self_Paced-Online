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
