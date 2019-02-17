
test = (2, 123.4567, 10000, 12345.67)

print("file_{:02d}: {:.2f}, {:.2E}, {:.2E}".format(test[0], test[1], test[2], test[3]))

print("file_{:02d}: {:.2f}, {:.2E}, {:.2E}".format(*test))


def formatter(in_tuple):
    result = "the {:d} numbers are ".format(len(in_tuple))
    result = result + ','.join('{:d}' for x in in_tuple)
    #result = result
    return result.format(*in_tuple)

print(formatter((2,3,5,7,9)))

test2 = ( 4, 30, 2017, 2, 27, 100)
def formatter2(in_tuple):
    sortedT = sorted(in_tuple)
    #result = ','.join('{:02d}' for x in in_tuple)
    result = ','.join(['{:02d}']*len(sortedT))
    return result.format(*sortedT)

print(formatter2(test2))

name = 'Andy'
f'Your name is {name}'

test3 = ['oranges', 1.3, 'lemons', 1.1]

print(f'The weight of an {test3[0].upper()} is {test3[1]*1.2:.3f} and the weight of a {test3[2].upper()} is {test3[3]*.2:3f}')


rows=[]
rows.append(('First', '$99.01', 'Second', '$88.09'))
rows.append(('Third', '$999.01', 'Fourth', '$88.019'))
rows.append(('Fitfh', '$1019.001', 'Sixth', '$888.09'))
rows.append(('Seventh', '$999989.01', 'Eighth', '$88.09'))

for row in rows:
    #t = tuple(row.split(" "))
    print('{:15}{:15}{:15}{:8}'.format(*row))


test = tuple(range(10))
print("{0:<5}{1:<5}{2:<5}{3:<5}{4:<5}{5:<5}{6:<5}{7:<5}{8:<5}{9:<5}".format(*test))