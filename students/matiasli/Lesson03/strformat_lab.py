#!/usr/bin/env python3

# series 1
s_format = (2, 123.4567, 10000, 12345.67)
# 'file_002 :   123.46, 1.00e+04, 1.23e+04'

output_string = ('file_{:0>3d} : {:.2f}, {:.2e}, {:.2e}'.format(s_format[0], s_format[1],s_format[2],s_format[3]))

print(output_string)

# Series 2

output_string2 = f"file_{s_format[0]:0>3d} : {s_format[1]:.2f}, {s_format[2]:.2e}, {s_format[3]:.2e}"
print(output_string2)

# Series 3
def series_3(seq):
    length_seq = len(seq)
    format1 =  ((length_seq-1) * "{:d}, ") + "{:d}"
    final_str = "the {} numbers are: {}".format(length_seq, format1)
    print(final_str.format(*seq))
    return(final_str.format(*seq))

# series 4
# given a 5 element tuple

def series_4(seq):
    if(len(seq)!=5):
        print("need a tuple of length 5")
    return ( '{:02d} {:02d} {:02d} {:02d} {:02d}'.format(seq[3], seq[4], seq[2], seq[0], seq[1]))

# series 5
def series_5():

    s5_tuple = ['oranges', 1.3, 'lemons', 1.1]
    
    # output The weight of an orange is 1.3 and the weight of a lemon is 1.1
    f_output = f"The weight of {s5_tuple[0]} is {s5_tuple[1]} and the weight of {s5_tuple[2]} is {s5_tuple[3]}"
    # change the f-string so that it displays the names of the fruit in upper case, and the weight 20% higher (that is 1.2 times higher).
    f_output2 = f"The weight of {(s5_tuple[0]).upper()} is {s5_tuple[1]*1.2} and the weight of {(s5_tuple[2]).upper()} is {s5_tuple[3]*1.2}"
    print(f_output)
    print(f_output)
    return f_output, f_output2

# series 6
# Write some Python code to print a table of several rows, each with a name, an age and a cost.
# Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.

rows = [ ['name', 'age', 'price'], ['bob', 27, 3000], ['cat', 34, 20], ['fergie', 18, 350.01], ['kyle', 67, 2190.01] ]

for row in rows:
    print('{:20}{:>10}{:>20}'.format(*row))


