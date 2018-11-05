#Jon Cracolici
#Lesson03 String Formatting Lab
#UW Python Cert
#
#Task 1
n=(2,123.4567,10000,12345.67)
def filenamegen(n):
    """This function creates filenames using a tuple as input."""
    name = "file_"+f'{n[0]:03}'+" :"+f'{n[1]:10.02f}'+", "+f'{n[2]:.2e}'+", "+f'{n[3]:.2e}'
    print(name)
    
filenamegen(n)
#
#Task 2
def filenamegen2(n):
    """This function creates filenames using a tuple as input."""
    name = "file_{:03} : {:10.02f}, {:.2e} , {:.2e}".format(*n)
    print(name)
    
filenamegen2(n)
#
#Task 3
def formatter(n):
    a = "the {} numbers are: {}, {}, {}".format(len(n),*n)
    return a
formatter(n)
#
#Task 4
x= (4, 30, 2017, 4, 27)
t4 = f'{x[4]:02}' +" "+ f'{x[3]:02}' +" "+ f'{x[2]:02}' +" "+ f'{x[0]:02}' +" "+ f'{x[1]:02}'
print(t4)
#
#Task 5
y = ['oranges', 1.3, 'lemons', 1.1]
#a = y[0]
#a = a[:-1]
#print(a)
t51 = f'The weight of an {y[0][:-1]} is {y[1]} and the weight of a {y[2][:-1]} is {y[3]}'
print(t51)
t52 = f'The weight of an {y[0][:-1].upper()} is {1.2*y[1]} and the weight of a {y[2][:-1].upper()} is {1.2*y[3]}'
print(t52)
#
#Task 6
row1=('Steven', 27, 2700.00)
row2=('Adam', 35, 67000.00)
row3=('Amy', 40, 210.00)
rows = [row1, row2, row3]
for row in rows:
    print('{:20}{:>10.0f}{:>10.2f}'.format(*row))
#
#Extra Task
z=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print((len(z)*'{:5}').format(*z))