#!/usr/bin/env python

#Task One
str_tuple = (2,123.4567, 10000, 12345.67)
print('file_{:03d}: {:.2f}, {:.2e}, {:.2e}'.format(*str_tuple))


#Task Two
print('file_%03d: %.2f, %.2e, %.2e' %str_tuple[:])
print(f'file_{str_tuple[0]:03d}: {str_tuple[1]:.2f}, {str_tuple[2]:.2e}, '
      f'{str_tuple[3]:.2e}')

#Task Three
def formatter(nums_tuple):
    """Return a formatted string of nums"""
    num_len = len(nums_tuple)
    format_string = 'the {} numbers are: ' + ', '.join(['{}'] * num_len)
    return format_string.format(num_len, *nums_tuple)

    
#Task Four
a = (4, 30, 2017, 2, 27)
print('{:02d} {} {} {:02d} {}'.format(a[-2],a[-1],a[2],a[0],a[1]))


#Task Five
b = ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an {b[0][:-1]} is {b[1]} and the weight of a {b[2][:-1]}'
      f' is {b[3]}')
print(f'The weight of an {b[0][:-1].upper()} is {b[1]*1.2} and the weight of '
      f'a {b[2][:-1].upper()} is {b[3]*1.2}')
    
    
#Task Six
print('\n{:^10} | {:^6} | {:^10}'.format('Name','Age','Cost'))
print('-' * 32)
print('{:10} | {:>6d} | ${:>8,.0f}'.format('Civic',25,999))
print('{:10} | {:>6d} | ${:>8,.0f}'.format('Tundra',12,9000))
print('{:10} | {:>6d} | ${:>8,.0f}'.format('WRX',5,30000))
print('{:10} | {:>6d} | ${:>8,.0f}'.format('GT3RS',2,150000))

c = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(('{:5}' * len(d)).format(*c))