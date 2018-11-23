#!/usr/bin/env python3

print("----- TASK 1 -----")
a_tuple = (2, 123.4567, 10000, 12345.67)
a_string = "file_{:03d} :  {:.2f}, {:.2e}, {:.2e}".format(*a_tuple)
print(a_string)

print("\n----- TASK 2 -----")
(first,second,third,fourth) = a_tuple
b_string = f"file_{first:03d} :  {second:.2f}, {third:.2e}, {fourth:.2e}"
print(b_string)

print("\n----- TASK 3 -----")
def formatter(in_tuple):
    form_string = "{:d}"
    for i in range(len(in_tuple)-1):
        form_string += ", {:d}"
    return form_string.format(*in_tuple)
print(formatter((1,2,3)))
#print(formatter((1,2,3,4,5)))

print("\n----- TASK 4 -----")
d_tuple = (4,30,2017,2,27)
print("{3:02d} {4:02d} {2:04d} {0:02d} {1:02d}".format(*d_tuple))

print("\n---- TASK 5 -----")
a_list = ['oranges',1.3,'lemons',1.1]
f_string = f"The weight of an {a_list[0][:-1].upper()} is {1.2*a_list[1]} "\
           f"and the weight of a {a_list[2][:-1].upper()} is {1.2*a_list[3]}"
print(f_string)

print("\n----- TASK 5 -----")
a_table = [["Ben","Franklin",10,12345.67],
           ["Abraham","Lincoln",20,0.45],
           ["Barack","Obama",30,987.98]]
print("FNAME      LNAME       AGE          COST")
for (fname,lname,age,cost) in a_table:
    print(f"{fname:10s} {lname:10s} {age:3d}    ${cost:10,.2f}")

print("\n----- EXTRA TASK -----")
big_tuple=(1,2,3,4,5,6,7,8,9,10)
print("....x"*10)
print(("{:5d}"*10).format(*big_tuple))