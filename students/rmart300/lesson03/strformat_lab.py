from decimal import Decimal

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def format_numbers(a):
    if len(a) != 4: # or (lambda x: not is_number(x) for x in a):
        print("tuple must have length 4 and be data type float")

    lead_zero = "%03d" % a[0]
    float_value = '%.2f' % Decimal(a[1])
    scientific1 = '%.2e' % Decimal(a[2])
    scientific2 = '%.3e' % Decimal(a[3])
    return (lead_zero, float_value, scientific1, scientific2)

#Write a format string that will take the following four element tuple:
#( 2, 123.4567, 10000, 12345.67)
#and produce:
#'file_002 :   123.46, 1.00e+04, 1.23e+04'
def task1(a):
    mod_a = format_numbers(a)
    out_string = "file_{0} :   {1}, {2}, {3}".format(*mod_a)
    print(out_string)
    return out_string

def task2(a):
    (lead_zero, float_value, scientific1, scientific2) = format_numbers(a)
    out_string = f"file_{lead_zero} :   {float_value}, {scientific1}, {scientific2}"
    print(out_string)
    return out_string

if __name__ == '__main__':
    a = ( 2, 123.4567, 10000, 12345.67 )
    assert task1(a) == 'file_002 :   123.46, 1.00e+04, 1.235e+04'
    assert task2(a) == 'file_002 :   123.46, 1.00e+04, 1.235e+04'    
    print('all tests passed'
