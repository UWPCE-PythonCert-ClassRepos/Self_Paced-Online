# ------------------- Task One -------------------

print('file_{0:0>3}: {1:0.2f}, {2:.2E}, {3:.2E}'.format(2, 123.4567, 10000, 12345.67))

# ------------------- Task Two -------------------

one = 2
two = 123.4567
three = 10000
four = 12345.67

print(f'file_{one:0>3}: {two:0.2f}, {three:.2E}, {four:.2E}')

# ------------------- Task Three -------------------


def formatter(in_tuple):
    form_string = "the " + str(len(in_tuple)) + " numbers are: " + ((len(in_tuple) - 1) * '{:d}, ') + '{:d}'
    return form_string.format(*in_tuple)

tuple_1 = (1, 2, 3, 4, 5)
tuple_2 = (49, 48, 47)
print(formatter(tuple_1))
print(formatter(tuple_2))

# ------------------- Task Four -------------------


def five_elements(in_tuple):
    five_string = '{3:0>2} {4:0>2} {2} {0:0>2} {1:0>2}'
    print(five_string.format(*in_tuple))

five_tuple = (4, 30, 2017, 2, 27)
five_elements(five_tuple)

# ------------------- Task Five  -------------------

a = ['oranges', 1.3, 'lemons', 1.1]

# Normal version
print(f'The weight of an {a[0].rstrip("s")} is {a[1]} and the weight of a {a[2].rstrip("s")} is {a[3]}.')

# Upper case/1.2x multiplier version
print(f'The weight of an {a[0].rstrip("s").upper()} is {a[1]*1.2} '
      f'and the weight of a {a[2].rstrip("s").upper()} is {a[3]*1.2}.')

# ------------------- Task Six -------------------

names = ('Name', '---', 'Jonathan', 'Lauren', 'Keith', 'Jesse', 'Arnold Schwarzenegger')
ages = ('Age', '---', '31', '32', '29', '27', '70')
costs = ('Cost', '---', '$9984.85', '$759.37', '$19.38', '$9.47', '$184982.73')

x = len(max(names, key=len)) + 2
y = len(max(ages, key=len)) + 2
z = len(max(costs, key=len)) + 2

for item in range(len(names)):
    print(f'{names[item]:{x}} {ages[item]:{y}} {costs[item]:{z}}')
