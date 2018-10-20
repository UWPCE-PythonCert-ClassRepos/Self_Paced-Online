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
a = ( 4, 30, 2017, 2, 27)
print(f'{a[3]:>02} {a[4]} {a[2]} {a[0]:>02} {a[1]}')

#task 5
e = ['oranges', 1.3, 'lemons', 1.1]
print(f'the weight of an {e[0][:-1]} is {e[1]} and the weight of a {e[2][:-1]} is {e[3]}')

#task 6
rows = (('Josh', 27, 9001.27), ('Tatsiana', 30, 20009.29), ('Ralph', 50, 40.378934), ('Joey', 24, 12000985.49834))

for i in rows:
    print(f'{i[0]:<8} {i[1]} ${i[2]}')
    
t = (100, 200, 300, 400, 500, 600, 700, 800, 900, 1000)
for i in t:
    print(f'{i:<5}', end='')

#print(rows[0][0], rows[0][1])
#for i in rows:
#for i in rows:
#    print(i)
#    print('{:20}{:18}{:20}{:18}'.format(*i))