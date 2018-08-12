#Task1
my_tuple = (2, 123.4567, 10000, 12345.67)
print("file_{0[0]:0>3d} : {0[1]:.2f}, {0[2]:.2e}, {0[3]:.2e}".format(my_tuple))
s1="file_{0[0]:0>3d} : {0[1]:.2f}, {0[2]:.2e}, {0[3]:.2e}".format(my_tuple)

#Task2
s2=f"file_:{my_tuple[0]:0>3d} : {my_tuple[1]:.2f}, {my_tuple[2]:.2e}, {my_tuple[3]:.2e}"

#Task3
def formatter(x):
    fstring = "{:d}"
    for i in range(len(x)-1):
        fstring = fstring + ", " + "{:d}"
    return fstring.format(*x)

#Task4
my_tuple = (4, 30, 2017, 2, 27)
print('{0[3]:0>2d} {0[4]} {0[2]} {0[0]:0>2d} {0[1]}'.format(my_tuple))

#Task5
my_list = ['oranges', 1.3, 'lemons', 1.1]
f"The weight of an {my_list[0][:-1]} is {my_list[1]} and the weight of a {my_list[2][:-1]} is {my_list[3]}"
f"The weight of an {my_list[0][:-1].upper()} is {my_list[1]*1.2} and the weight of a {my_list[2][:-1].upper()} is {my_list[3]*1.2}"

#Task6
names=['Bob', 'Steve', 'Kevin', 'Josephine', 'Aaron']
ages=[13, 15, 29, 40, 30]
costs=['$142.31', '$1255.20', '$13.00', '$23.31', '$14']
print('{:<15}{:<10}{:<20}'.format('Names', 'Age', "Cost"))
for row in range(len(names)):
    print('{:<15}{:<10}{:<20}'.format(names[row],ages[row],costs[row]))

atuple=(1,2,3,4,5,6,7,8,9,10)
print(('{:<5}'*10).format(*atuple))