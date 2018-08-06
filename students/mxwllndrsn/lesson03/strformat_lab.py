#uw python 210
#lesson 03
#max anderson

#string lab

#task 1
def str_format():

    atuple = (2, 123.4567, 10000, 12345.67)

    print('file_{:03d}: {:.2f}, {:.2e}, {:.2e}'.format(*atuple))

#task 1.1
def alt_format():

    atuple = (2, 123.4567, 10000, 12345.67)

    print(f'file_{atuple[0]:03d}: {atuple[1]:.2f},' + \
                f' {atuple[2]:.2e}, {atuple[3]:.2e}')
    #how would you go about generating this for fstrings?

#task 2
def arb_number():

    atuple = (2, 5, 6, 3, 2, 1)

    l = len(atuple)

    print('The {} numbers are: '.format(l) + \
          ', '.join(['{}']*l).format(*atuple))

#task fun
def form_string():

    form_string = "{:d}, {:.2e}"
    nums = (69, 69)
    print(form_string.format(*nums))

    print(f'this is an f string ' + ' '.join(f'{x:.2e}'for x in nums))

#task 3
def formatter(intuple):

    l = len(intuple)
    form_string = 'The {} numbers are: ' + ', '.join(['{}']*l)

    return form_string.format(l, *intuple)

#task 4
def five_el():

    tuple5 = (4, 30, 2017, 2, 27)

    print('{3:02d} {4} {2} {0:02d} {1}'.format(*tuple5))

#task 5
def fruit_string():

    f = ['oranges', 1.3, 'lemons', 1.1]

    print(f'The weight of an {f[0]} is {f[1]:.1f}' + \
          f' and the weight of a {f[2]} is {f[3]:.1f}')
    print()
    print(f'The weight of an {f[0].upper()} is {f[1]*1.2:.1f}' + \
          f' and the weight of a {f[2].upper()} is {f[3]*1.2:.1f}')
    #same q, how to pass tuple to fstring and replace by index
    #instead of being so verbose

#task 6
def alignment():

  #  atuple = (2234, 5, 26, 333, 44442, 133, 2)

 #   l = len(atuple)
 #   width = 10

#    print('\n'.join(['{:<{width}}']*l).format(*atuple, width = width))

    rows = ('Name', 'Age', 72, 'Cost', '$', 82342.3423002)

    for row in rows:
        print('{:10}{:<5}{:<10}{:<6}{:<2}{:.2f}'.format(*rows))

def quick_tup():

    #if you passed this tup in then yeah it would be a one liner
    tup = (0,1,2,3,4,5,6,7,8,9)

    print(''.join(['{:<5}']*len(tup)).format(*tup))
    #neat