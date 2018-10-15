"""module to solve string formatting lab for lesson 3"""

# Task 1
"""Write a format string that will take the following four element tuple:
( 2, 123.4567, 10000, 12345.67)
and produce:
'file_002 :   123.46, 1.00e+04, 1.23e+04'"""
input = ( 2, 123.4567, 10000, 12345.67)
output = f'file_{input[0]:0=3} :   {input[1]:.2f}, {input[2]:.2E}, {input[3]:.3g}'
print(output)