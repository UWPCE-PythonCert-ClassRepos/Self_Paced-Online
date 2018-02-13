from decimal import Decimal
from collections import namedtuple

#def is_number(s):
#    """determines if string is number"""
#    try:
#        float(s)
#        return True
#    except ValueError:
#        return False

def format_numbers(a):
    """formats 4 number tuple to different number formats for each element"""
    if len(a) != 4: # or (lambda x: not is_number(x) for x in a):
        print("tuple must have length 4")

    lead_zero = "%03d" % a[0]
    float_value = '%.2f' % Decimal(a[1])
    scientific1 = '%.2e' % Decimal(a[2])
    scientific2 = '%.3e' % Decimal(a[3])
    return (lead_zero, float_value, scientific1, scientific2)

def task1(a):
    """format 4 element tuple ( 2, 123.4567, 10000, 12345.67) to 'file_002 :   123.46, 1.00e+04, 1.23e+04'"""
    mod_a = format_numbers(a)
    out_string = "file_{0} :   {1}, {2}, {3}".format(*mod_a)
    print(out_string)
    return out_string

def task2(a):
    """format 4 element tuple using fstring"""
    (lead_zero, float_value, scientific1, scientific2) = format_numbers(a)
    out_string = f"file_{lead_zero} :   {float_value}, {scientific1}, {scientific2}"
    print(out_string)
    return out_string

def task3(a):
    """build dynamic string from list"""
    num_string = ', '.join(str(num) for num in a)
    out_string = "the numbers are: {}".format(num_string)
    print(out_string)
    return out_string

def task4(a):
    """Given a 5 element tuple: ( 4, 30, 2017, 2, 27) use string formating to print: '02 27 2017 04 30'"""
    month = '%02d' % a[3]
    day = '%02d' % a[4]
    year = a[2]
    hour = '%02d' % a[0]
    minute = '%02d' % a[1]
    out_string = f"{month} {day} {year} {hour} {minute}"
    print(out_string)
    return out_string

def increase_weight(weight):
    """multiply weight by 1.2"""
    return '%.1f' % Decimal(weight * 1.2)

def format_fruit(fruit):
    """make fruit singular and make upper case"""
    if fruit.endswith('s'):
        fruit = fruit[:-1]
    return fruit.upper()

def task5(a):
    """writes fstring that formats four element list ['oranges', 1.3, 'lemons', 1.1] as:
       'The weight of an ORANGE is 1.6 and the weight of a LEMON is 1.3'
       fruit names are changed to upper and weights increased by 20%"""
    (fruit1, weight1, fruit2, weight2) = a
    out_string = f"The weight of an {format_fruit(fruit1)} is {increase_weight(weight1)} and the weight of a {format_fruit(fruit2)} is {increase_weight(weight2)}"
    print(out_string)
    return(out_string)

def task6(a):
    """print a table of several rows, a argument is list of tuples, each tuple with a name, an age and a cost"""
    out_string = "{:20} {:3} {:5}".format('Name','Age','Cost') + '\n' 
    for t in a:
        out_string += "{:20} {:3} {:5}".format(t.name,t.age,t.cost) + '\n'
        
    print(out_string)
    return out_string

def extra_task(a):
    """given a tuple with 10 consecutive numbers, can you work how to quickly print the tuple in columns that are 5 charaters wide"""
    out_string = '\n'.join("{:5}".format(num) for num in a)
    print(out_string)
    return out_string



if __name__ == '__main__':
    print('task1')
    a = ( 2, 123.4567, 10000, 12345.67 )
    assert task1(a) == 'file_002 :   123.46, 1.00e+04, 1.235e+04'

    print('task2')
    assert task2(a) == 'file_002 :   123.46, 1.00e+04, 1.235e+04'    

    print('task3')
    b = ( 1, 2, 5, 7 )
    assert task3(b) == 'the numbers are: 1, 2, 5, 7'

    print('task4')
    c = ( 4, 30, 2017, 2, 27)
    assert task4(c) == '02 27 2017 04 30'

    print('task 5')
    d = ['oranges', 1.3, 'lemons', 1.1]
    assert task5(d) == 'The weight of an ORANGE is 1.6 and the weight of a LEMON is 1.3'

    print('task 6')
    SaleItem = namedtuple('SaleItem',['name','age','cost'])
    item1 = SaleItem('Babe Ruth',80,5000)
    item2 = SaleItem('Ken Griffey Jr',30,1000)
    item3 = SaleItem('Mark McGuire',30,800)
    item4 = SaleItem('Barry Bonds',25,1100)
    item_list = [item1,item2,item3,item4]
    task6(item_list)

    print('extra task')
    e = (100,120,150,900,1300,5000,10000,15000,85000,99000)
    extra_task(e)

    print('all tests passed')


