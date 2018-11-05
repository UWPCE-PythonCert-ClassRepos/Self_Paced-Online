## NEIMA SCHAFI, LESSON 3 Assignment - strformat.py (string formatting)

##TASK 1 - output: 'file_002 :   123.46, 1.00e+04, 1.23e+04'
t = (2, 123.4567, 10000, 12345.67)
print('file_{:03d}'.format(t[0]) + ' :' + '   {:.2f},'.format(t[1]) + ' {:.2e},'.format(t[2]) + ' {:.2e}'.format(t[3]))

##TASK 2 - redo task 1 but use different formatting method
print('file_%03d :   %.2f, %.2e, %.2e '%(t[0],t[1],t[2],t[3]))

##TASK 3 - dynamic formatting
def formatter(p):
    """this is a function to dynamically create a string"""
    return 'the {:d}'.format(len(p)) + ' numbers are:' + ','.join('%2d' % v for v in p )

##TASK 4 - using indexing combined with formatting
m = (4, 30, 2017, 2, 27)
print('{:02d} {:02d} {:02d} {:02d} {:02d}'.format(m[3],m[4],m[2],m[0],m[1]))

##TASK 5 - using f-string
n = ['oranges', 1.3, 'lemons', 1.1]
orang = n[0]
lemon = n[2]
print(f'The weight of an {orang[:-1]} is {n[1]} and the weight of a {lemon[:-1]} is {n[3]} ')
print(f'The weight of an {orang[:-1].upper()} is {n[1]*1.2} and the weight of a {lemon[:-1].upper()} is {n[3]*1.2} ')

##TASK 6 - Data to columns
row = (('hamburgers', '11', '$1000.00'), ('hotdogs', '15', '$100.34'), ('cheddar', '30', '$1.60', 'waterworld', '4', '$10.00'))
print('{:20}{:>10}{:>20}'.format("Name","Age","Cost"))
for item in row: print('{:20}{:>10}{:>20}'.format(*item))

# And for an extra task, given a tuple with 10 consecutive numbers
con = {1,2,3,4,5,6,7,8,9,10}
for i in con: print('{:5}'.format(i))
####END OF ASSIGNMENT
