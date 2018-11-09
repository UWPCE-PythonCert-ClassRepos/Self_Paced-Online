# execute with comand `python strformat_lab.py`

print("\n--------- Task One ---------")
my_tuple = (2, 123.4567, 10000, 12345.67)
print("file_{:03d}: {:.2f}, {:.2e}, {:.2e}".format(*my_tuple))

print("\n--------- Task Two ---------")
print(f"file_{my_tuple[0]:03d}: {my_tuple[1]:.2f}, {my_tuple[2]:.2e}, "
              f"{my_tuple[3]:.2e}")

print("\n--------- Task Three ---------")

def formatter(in_tuple):
    
    form_string = "The {:d} numbers are: " + ",".join(["{:d}"] * len(in_tuple))
    return form_string.format(len(in_tuple), *in_tuple)

tuple_1 = (1,2,3)
tuple_2 = (4,6,2,7,6)
tuple_3 = (2,7,5,9,6,4,3,2)

print(formatter(tuple_1))
print(formatter(tuple_2))
print(formatter(tuple_3))

print("\n--------- Task Four ---------")
in_tuple = (4, 30, 2017, 2, 27)
print("{:02d} {:02d} {:d} {:02d} {:02d}".format(in_tuple[3],
      in_tuple[4], in_tuple[2], in_tuple[0], in_tuple[1]))

print("\n--------- Task Five ---------")
mylist = ['oranges',1.3,'lemons',1.1]
print(f"The weight of an {mylist[0][:-1]} is {mylist[1]:.1f}"
        f" and the weight of a {mylist[2][:-1]} is {mylist[3]:.1f}")
print(f"The weight of an {mylist[0][:-1].upper()} is {1.2 * mylist[1]:.1f}"
    f" and the weight of a {mylist[2][:-1].upper()} is {1.2 * mylist[3]:.1f}")

print("\n--------- Task Six ---------")

table_strings = [("Michelle", "Anderson", '23', '$3000.12'),
                 ("John", "Doe", '42', '$500.00'),
                 ("Jane", "Doe", '38', '$200.87'),
                 ("Brad", "Smith", '23', '$30000.12')]
     
for tuples in table_strings:
    print("{:<15}{:<15}{:>4}{:>12}".format(*tuples))


in_tuple = (0,1,2,3,4,5,6,7,8,9)
print()
print("".join(len(in_tuple) * ["{:^5d}"]).format(*in_tuple))



