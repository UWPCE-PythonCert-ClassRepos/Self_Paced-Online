#Lesson 3 Assignment 3
#Write functions that format strings
#Jason Virtue 01/24/2019
#UW Self Paced Python Course

#Task One String Format

a_list = ( 2, 123.4567, 10000, 12345.67)
b_list = "file_002 :   123.46, 1.00e+04, 1.23e+04"

def format_list(seq):
    return "file_{:03d} :   {:.2f}, {:.2e}, {:.2e}".format(*seq)

print(format_list(a_list))

#Unit Test
assert format_list(a_list) == b_list

#Task Two Alternative format strings

def format_list(seq):
    return f"file_{a_list[0]:03d} :   {a_list[1]:.2f}, {a_list[2]:.2e}, {a_list[3]:.2e}"

print(format_list(a_list))

#Unit Test
assert format_list(a_list) == b_list

#Task Three Display variable lenght tuples in a string
a_tuple = [1,2,3,4,5,6,7]

def display_item(seq):
    l = len(seq)
    print(("the {} numbers are: " + ", ".join(["{}"] * l)).format(l,*seq))

display_item(a_tuple)

#Task Four Reformat five element tuple

b_tuple = [4,30,2017,2,27]
def arrange_list(seq):
    return "{:02d}".format(seq[3]) + " {}".format(seq[4]) + " {}".format(seq[2]) + " {:02d}".format(seq[0]) + " {}".format(seq[1])

print(arrange_list(b_tuple))

assert arrange_list(b_tuple) == "02 27 2017 04 30"

#Task Five f-string formatting
c_tuple = ['oranges', 1.3, 'lemons', 1.1]
def fstring_format(seq):
    return f"The weight of an {c_tuple[0]} is {c_tuple[1]} and the weight of a {c_tuple[2]} is {c_tuple[3]}"

print(fstring_format(c_tuple))

def fstring_revise(seq):
    return f"The weight of an {c_tuple[0].upper()} is {c_tuple[1]*1.2} and the weight of a {c_tuple[2].upper()} is {c_tuple[3]*1.2}"

print(fstring_revise(c_tuple))

#Task Six print tabular format for name age and cost
d_list = (("Mustang", 5, 5000),("Camaro", 10, 2000),("Trans-am", 15, 1000))

for num in d_list:
    print("{:<10s}{:5d}{:10.2f}".format(*num))
print("\n")

d_tuple = [1,2,3,4,5,6,7,8,9,10]
for num in d_tuple:
    print('{:05d}'.format(num))