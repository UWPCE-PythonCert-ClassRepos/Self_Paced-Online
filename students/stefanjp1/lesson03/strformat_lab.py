#!/usr/bin/env python3

# Task 1
print( "file_{:0<3}: {:.2f}, {:.2e}, {:.2e}".format(2, 123.4567, 10000, 12345.67) )


# Task 2
file = 2
d1 = 123.4567
d2 = 10000
d3 = 12345.67

print( "file_{:0<3}: {:.2f}, {:.2e}, {:.2e}".format(file, d1, d2, d3) )


# Task 3
def formatter(output):
    l = len(output)
    
    format_string = "the {:d} numbers are: " + ", ".join(["{:d}"] * l)
    
    print(format_string.format(l, *output))

t = (1,2,3)

formatter(t)


# Task 4
t = (4, 30, 2017, 2, 27)

print("{3:02d} {4} {2} {0:02d} {1}".format(*t))


# Task 5
t = ['oranges', 1.3, 'lemons', 1.1]

print( f"The weight of an {t[0][:-1]} is {t[1]} and the weight of a {t[2][:-1]} is {t[3]}" )

print( f"The weight of an {t[0][:-1].upper()} is {t[1] * 1.2} and the weight of a {t[2][:-1].upper()} is {t[3] * 1.2}" )


# Task 6
rows = [['Mark', 9, '$88.09'],
        ['Mason', 10, '$8888.09'],
        ['Madeline', 18, '$8.09'],
        ['Matt', 22, '$888.09']]



for row in rows:
    print( '{:15}{:<5d}{:10}'.format(*row) )
    
t = (0,1,2,3,4,5,6,7,8,9)
print( ''.join(['{:<5d}'] * len(t)).format(*t) )