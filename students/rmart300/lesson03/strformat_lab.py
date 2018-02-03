from decimal import Decimal

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

#Write a format string that will take the following four element tuple:
#( 2, 123.4567, 10000, 12345.67)
#and produce:
#'file_002 :   123.46, 1.00e+04, 1.23e+04'
def task1(a):
    if len(a) != 4 or (lambda x: not is_number(x) for x in a):
        print("tuple must have length 4 and be data type float")

    lead_zero = 'file_{}'.format("%03d" % a[0])
    float_value = '%.2f' % Decimal(a[1])
    scientific1 = '%.2E' % Decimal(a[2])
    scientific2 = '%.2E' % Decimal(a[3])
    print("{0} :   {1}, {2}, {3}".format(lead_zero,float_value,scientific1,scientific2))
    return "{0} :   {1}, {2}, {3}".format(lead_zero,float_value,scientific1,scientific2)

if __name__ == '__main__':
    a = ( 2, 123.4567, 10000, 12345.67 )
    assert task1(a) == 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    

