#!/usr/bin/env python3

#Task 1


x=(2,123.467,10000,12345.67)

'file{:0>4d}: {:3.2f},{:.2e},{:03.2e}'.format(*x)


#Task 2

'file{:-6d}: {:3.0f},{:10d},{:^6f}'.format(*x)

#Task 3

def formatter(in_tuple):
    form_string="{:d}"*(len(in_tuple))
    return "The {} numbers are:".format(len(in_tuple))+form_string.format(*in_tuple)


#Task 4


x=(4,30,2017,2,27)

print("0{3} {4} {2} 0{0} {1}".format(*x))

#Task 5

z=['oranges',1.3,'lemons',1.1]

f"The weight of an {z[0][:-1]} is {z[1]} and the weight of a {z[2][:-1]} is {z[3]}."

f"The weight of an {z[0][:-1].upper()} is {z[1]*1.2} and the weight of a {z[2][:-1].upper()} is {z[3]*1.2}."

#Task 6

a1=('John', '4', '$11000.00')
a2=('Jane', '42', '$10.00')
a3=('Bob','75','$2304.00')


def table(a,b,c):
    print('{:>10}{:>10}{:>15}'.format(*a))
    print('{:>10}{:>10}{:>15}'.format(*b))
    print('{:>10}{:>10}{:>15}'.format(*c))

table(a1,a2,a3)

h=(1,2,3,4,5,6,7,8,9,0)

print(('{:>5}\n'*10).format(*h))