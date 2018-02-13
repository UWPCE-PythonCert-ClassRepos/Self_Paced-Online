tuple1 =( 2, 123.4567, 10000, 12345.67)
#task1
def task1(atuple):
    print("file_{}: {:.2f}, {:.2e}, {:.2e} ".format(str(atuple[0]).zfill(3),atuple[1], atuple[2], atuple[3]))

task1(tuple1)
#task2
def task2(atuple):
    filename= atuple[0]
    number1 = atuple[1]
    number2 = atuple[2]
    number3 = atuple[3]
    print(f'file_{filename:0>3d}: {number1:.2f}, {number2:.2e}, {number3:2e}')

task2(tuple1)

t1=(1,2,3,4,5,6)
t2=(1,2,3,4)
#task3
def formatter(atuple):
    lenth_str = len(atuple)
    output_str= f'the {lenth_str} number are '+ ("{:d}, "*(lenth_str-1)+"{:d}").format(*atuple)
    return output_str

formatter(t1)
formatter(t2)

#task4
t1 =( 4, 30, 2017, 2, 27)
def task4(atuple):
    return '{3:02d} {4:02d} {2:04d} {0:02d} {1:02d}'.format(*atuple)

task4(t1)

#task5
l1= ['oranges', 1.3, 'lemons', 1.1]
def task5(alist):
    output_str=f'The weight of an {alist[0]} is {alist[1]} and the weight of a {alist[2]} is {alist[3]}'
    return output_str
task5(l1)

#task5 extra
l1= ['oranges', 1.3, 'lemons', 1.1]
def task5_extra(alist):
    output_str=f'The weight of an {alist[0].upper()} is {alist[1]*1.2} and the weight of a {alist[2].upper()} is {alist[3]*1.2}'
    return output_str
task5_extra(l1)

#task6
table1 = [['Name1', 26, 800], ['Name2', 35, 2400],['Name3', 55, 7000], ['Name4', 17, 500]]

def task6(atable):
    for line in atable:
        output_str = f'{line[0]:<15}{line[1]:<15}${line[2]:<15}'
        print(output_str)

task6(table1)

#task6 extra
t3=(1,2,3,4,5,6,7,8,9,10)
def task6_extra(atuple):
    print(('{:5}'*len(atuple)).format(*atuple))
task6_extra(t3)
