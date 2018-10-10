#task 1
fnames = (2, 123.4567, 10000, 12345.67)

print('file_{:>03}: {:.2f}, {:.2e}, {:.2e}'.format(fnames[0], fnames[1], fnames[2], fnames[3]))
#task 2
print(f'file_{fnames[0]:>03}: {fnames[1]:.2f}, {fnames[2]:.2e}, {fnames[3]:.2e}')

#task 3
def formatter(nums):
    form_string = '{:d}, ' * len(nums)
    print(('the {:d} numbers are: ' + form_string).format(len(nums), *nums)[:-2])
#task 4