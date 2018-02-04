from decimal import Decimal

def is_number(s):
    """determines if string is number"""
    try:
        float(s)
        return True
    except ValueError:
        return False

def format_numbers(a):
    """formats 4 number tuple to different number formats for each element"""
    if len(a) != 4: # or (lambda x: not is_number(x) for x in a):
        print("tuple must have length 4 and be data type float")

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

if __name__ == '__main__':
    a = ( 2, 123.4567, 10000, 12345.67 )
    assert task1(a) == 'file_002 :   123.46, 1.00e+04, 1.235e+04'
    assert task2(a) == 'file_002 :   123.46, 1.00e+04, 1.235e+04'    
    b = ( 1, 2, 5, 7 )
    assert task3(b) == 'the numbers are: 1, 2, 5, 7'
    c = ( 4, 30, 2017, 2, 27)
    assert task4(c) == '02 27 2017 04 30'
    print('all tests passed')


