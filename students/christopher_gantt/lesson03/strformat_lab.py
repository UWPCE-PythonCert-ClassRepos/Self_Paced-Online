#Task One
my_tuple = (2, 123.4567, 10000, 12345.67)
print("file_{:0>3d}:   {:.2f}, {:.2e}, {:.2e}".format(my_tuple[0],my_tuple[1],my_tuple[2],my_tuple[3]))


#Task Two
print(f"file_{my_tuple[0]:0>3d}:   {my_tuple[1]:.2f}, {my_tuple[2]:.2e}, {my_tuple[3]:.2e}")


#Task Three
def formatter(in_tuple):
    l = len(in_tuple)
    format_string = "The {} numbers are: " + ", ".join(["{}"] * l)
    return format_string.format(l, *in_tuple)

t = (1,2,3)
assert formatter(t) == "The 3 numbers are: 1, 2, 3"
assert formatter((3,4,5,6,2,4,7,3,5)) == "The 9 numbers are: 3, 4, 5, 6, 2, 4, 7, 3, 5"


#Task Four
five_tuple = (4, 30, 2017, 2, 27)
print("{:0>2d} {} {} {:0>2d} {}".format(five_tuple[3], five_tuple[4], five_tuple[2], five_tuple[0], five_tuple[1]))


#Task Five
my_list = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {my_list[0][:-1]} is {my_list[1]} and the weight of a {my_list[2][:-1]} is {my_list[3]}")
print(f"The weight of an {my_list[0][:-1].upper()} is {my_list[1]*1.2} and the weight of a {my_list[2][:-1].upper()} is {my_list[3]*1.2}")


#Task Six
print("{:17}{:9}{:>12}".format("Jesse", "Age 25", "$3000000"))
print("{:17}{:9}{:>12}".format("Chi", "Age 3", "$5"))
print("{:17}{:9}{:>12}".format("Christopher", "Age 103", "$10000"))

ten_numbers = (1,2,3,4,5,6,7,8,9,10)
print(("{:5d}"*10).format(*ten_numbers))

