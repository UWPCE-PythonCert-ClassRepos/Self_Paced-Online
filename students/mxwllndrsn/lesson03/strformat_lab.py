#uw python 210
#lesson 03
#max anderson

#string lab

def str_format():

    atuple = (2, 123.4567, 10000, 12345.67)

    print('file_00{:d}: {:.2f}, {:.2e}, {:.2e}'.format(*atuple))

def alt_format():

    atuple = (2, 123.4567, 10000, 12345.67)

    print(f'file_00{atuple[0]}: {atuple[1]:.2f},' + \
                f' {atuple[2]:.2e}, {atuple[3]:.2e}')


def arb_number():

    atuple = (2, 5, 6, 3, 2, 1)

    l = len(atuple)

    print('The {} numbers are: '.format(l) + \
          ', '.join(['{}']*l).format(*atuple))

def form_string():

    form_string = "{:d}, {:.2e}"
    nums = (69, 69)
    print(form_string.format(*nums))

    print(f'this is an f string ' + ' '.join(f'{x:.2e}'for x in nums))

def formatter(intuple):

    l = len(intuple)
    form_string = 'The {} numbers are: ' + ', '.join(['{}']*l)

    return form_string.format(l, *intuple)