"""
    Author is Antonio V. Alvillar
    Self-Paced-Online Python 210 UWPCE
    November 24th 2018
"""

#Task 1: Format(padding, 2dec, 2dec/scientific, 3 signigicant/scientific)
format_string = "file_{:0>3d}: {:.2f}, {:.2e}, {:.3g}"
#print(format_string.format(2, 123.4567, 10000, 12345.67)) #output to screen

#Task 2: Alternatives (as functions) 1st uses a variable
def alt_formatter(one, two, three, four):
    format_str = "file_{:0>3d}: {:.2f}, {:.2e}, {:.3g}"
    return format_str.format(one, two, three, four)

#2nd No string variable
def alt_formatter2(one, two, three, four):
    return "file_{:0>3d}: {:.2f}, {:.2e}, {:.3g}".format(one, two, three, four)

#3rd using 'f' string (params are passed directly to return string to format)
def f_formatter(one, two, three, four):
    return f"file_{one:0>3d}: {two:.2f}, {three:.2e}, {four:.3g}"

#Task 3: Using string multiplication (fencepost issue - but short)
def formatter_short(in_tuple):
    if type(in_tuple) == int: #If single int then its not a tuple
        return "the 1 number is: {:d}".format(in_tuple) #return single string
    else:
        size = len(in_tuple) #get size of tuple to multiply format params
        format_string = "the " + str(size) + " numbers are: " + "{:d}, " * size
        return format_string.format(*in_tuple)

#Task 3: Alternative string build using loops (best version)
def formatter(in_tuple):
    if type(in_tuple) == int: #If single in then its not a tuple
        return "the 1 number is: {:d}".format(in_tuple) #return single string
    else:
        size = len(in_tuple) #get size of the tuple for the loop
        format_string = "the " + str(size) + " numbers are: " #start string
        for i in range(size-1): #Loop until 1 short of tuple size
            format_string += "{:d}, "
        format_string += "{:d}" #fencepost for last tuple element (no ',' after)
        return format_string.format(*in_tuple)

#Task 4: Only 5 elements expected. Switch positions [0,1] and [3,4] ([2] stays)
def elements_5(pad):
    #F formmating is used to pad with zeros and change indices.
    return f"{pad[3]:0>2d} {pad[4]:0>2d} {pad[2]:0>2d} {pad[0]:0>2d} {pad[1]:0>2d}"

#Task 5: Only 4 elements expected. (display fruit and weight - using F string)
def elements_4(fruits):
    fruit_1 = fruits[0] # If element count was unknown - a loop would suffice
    weight_1 = fruits[1]
    fruit_2 = fruits[2]
    weight_2 = fruits[3]
    output = (
              f"The weight of an {fruit_1[:-1]} is {weight_1} "
              f"and the weight of a {fruit_2[:-1]} is {weight_2}"
              )
    return output

#Task 5: Alternative function (upper case fruits and multiply weight 1.2)
def alt_elements_4(fruits):
    fruit_1 = fruits[0]
    weight_1 = float(fruits[1]) * 1.2 #Increase weight by 20%
    fruit_2 = fruits[2]
    weight_2 = float(fruits[3]) * 1.2 #Increase weight by 20%
    output = (
              f"The weight of an {fruit_1[:-1].upper()} is {weight_1} "
              f"and the weight of a {fruit_2[:-1].upper()} is {weight_2}"
              )
    return output

#Task 6: Display a tuple (of tuples) min 2 tuples (rows) expected then aligned.
def columns(rows):
    #Header row to display the names of the columns expected
    print('\n{:<12}{:>3}{:>14}'.format('NAME', 'AGE', 'COST'))
    #Space padding for each (12 for name, 3 age, 14 cost) (name left aligned)
    for row in rows:
        print('{:<12}{:>3}{:>14}'.format(*row))

#Extra Task: 10 consecutive numbers printed 5 characters wide.
def extra(numbers):
    for num in range(len(numbers)):
        print('{:>5d}'.format(numbers[num]), end='')