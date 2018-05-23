# ------------------------------------------------------------------------
# NAME: MICAH BRAUN

# PROJECT: strformat_lab.py
# PURPOSE: Manipulating strings
# DATE: 5/19/2018
#
# DESCRIPTION: Program manipulates data types for display purposes.
# ------------------------------------------------------------------------

# Data -------------------------------------------------------------------
tuple_vals = (2, 123.4567, 10000, 12345.67)

#   --  Section 1 Data  --

new_str1 = ""

file_val1 = "file_" + "%03d" % tuple_vals[0]  # format for file title

dec_val1 = "%.2f" % tuple_vals[1]  # format float

sci_val1 = "%.2e" % tuple_vals[2]  # format scientific 1

sci_val2 = "%.2e" % tuple_vals[3]  # format scientific 2

#   --  Section 2 Data  --

new_str2 = ""

f_str_file = "file_" + f'{tuple_vals[0]:03d}'  # format file title with f-string
# print(f_str_file)                             # debugging print

f_str_dec = f'{tuple_vals[1]:.2f}'  # 2 dec. format w/ f-string
# print(f_str_dec)

f_str_sci1 = f'{tuple_vals[2]:.2e}'  # sci. notation formatting f-string1
# print(f_str_sci1)

f_str_sci2 = f'{tuple_vals[3]:.2e}'  # sci. notation formatting f-string2


# print(f_str_sci2)

#   --  Section 3 Data  --


def formatter(in_tuple):  # declare function takes tuple as argument
    """Function counts inputs and formats each input into str display"""

    strformat = len(in_tuple)  # counts length of input
    str_Display = "The " + str(strformat) + " numbers are: "  # formatting string with length of tuple
    num_vals = []  # storage container for values

    for nums in in_tuple:  # for-loop to cycle through each value and format
        new_f = f'{nums:.0f}'  # format all w/out decimals
        num_vals += new_f  # add each formatted value to container

    msg = str_Display + str(num_vals).replace("[", '').replace("]", '').replace("'", '')  # full display message

    print(msg)
    return msg


#   --  Section 6 Data  --

#  ---- Part I
header = "-" * 40

data = [['NAME', 'AGE', 'COST'],
        ["Adam", 38, 100000],
        ["Abby", 33, 675.50],
        ["Albert", 25, 50000],
        ["Betsy", 59, 130000],
        ["Brett", 23, 950],
        ["Chris", 43, 500],
        ["Curt", 27, 2000.33],
        ["Clay", 26, 1300],
        ["Denise", 39, 1500],
        ["Damien", 49, 130],
        ["Darleena", 55, 470]]

#  ----  Part II
header2 = "-" * 50
ten_tup = (375, 13, 11122018, 314159, 75, 250, 88, 300, 33, 50)
# -------------------------------------------------------------------------

# Display -------------------------------------------------------------------

#  --  Section 1 Display

print("Section 1 string:")
print()

new_str1 = file_val1 + " :   " + dec_val1 + ", " + sci_val1 + ", " + sci_val2

print(new_str1)
print()

#  --  Section 2 Display
print("Section 2 string:")
print()

new_str2 = f_str_file + " :   " + f_str_dec + ", " + f_str_sci1 + ", " + f_str_sci2

print(new_str2)
print()

#  --  Section 3 Display

print("Section 3 string:")  # display title
print()

formatter((1.123, 3.14159, 1, 1.0, 100.21, 4.215, 3))  # this works fine with 7 elements
formatter((3.0, 4.0))  # this also works with 2 elements
formatter((100.1,))  # this prints out but doesn't format correctly...
# I am not sure why 1 item causes an issue...

#  --  Section 4 Display

print("Section 4 string:")  # display title
print()

fifth_elem = (4, 30, 2017, 2, 27)  # original list
print("Original order:")
print(fifth_elem)

index0 = f'{fifth_elem[0]:02d}'  # format index[0] with leading 0
index3 = f'{fifth_elem[3]:02d}'  # format index[3] with leading 0

reorder = index3 + ", " + str(fifth_elem[4]) + ", " + str(fifth_elem[2]) + ", " + index0 + ", " + str(fifth_elem[1])
print("Re-order:")
print(reorder)

#  --  Section 5 Display

print("Section 4 string:")  # display title
print()

elem_list = ['oranges', 1.3, 'lemons', 1.1]  # original list

fruit1 = elem_list[0]  # store elements from list specifically in named variables
fruit2 = elem_list[2]
weight1 = elem_list[1]
weight2 = elem_list[3]

msg_string = f'The weight of an {fruit1[:-1].upper()} is {weight1 * 1.2} and the weight of a \
{fruit2[:-1].upper()} is {weight2 * 1.2}'  # formatted string

print(msg_string)  # print string

#  --  Section 6 Display

print("Section 6 string 1:")  # display title
print()

for item in range(len(data)):
    if item == 0:
        print(header)
        print('{:<10s}{:>8}{:>14}'.format(str(data[item][0]), data[item][1], data[item][2]))
        print(header)
    else:
        print('{:<10s}{:>8d}{:^24.2f}'.format(str(data[item][0]), int(data[item][1]), float(data[item][2])))

print()
print("Section 6 string 1b Bonus:")  # display title
print()

# last_count = 0

for index, elem in enumerate(ten_tup):  # evaluate index, values in tuple
    if index < 5:  # if index less than 5 (index at 0)
        print('{:>10}'.format(elem) + ", ", end="")  # print first five tuple elements

    if index >= 5:  # else index greater (next five elements)
        if index == 5:  # if index is 5, == start of next line:
            print('\n{:>10}'.format(elem) + ", ", end="")  # print newline and index[5]
        else:
            print('{:>10}'.format(elem) + ", ", end="")  # all other indexes print



