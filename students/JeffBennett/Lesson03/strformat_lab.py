#!/usr/bin/env python3

# Task One
'file_{0:0=3}:  {1:5.2f}, {2:.2e}, {3:.2e}'.format
(2, 123.4567, 10000, 12345.67)

# Task Two
data = [2, 123.4567, 10000, 12345.67]
f'file_{data[0]:0=3}:  {data[1]:5.2f}, {data[2]:.2e}, {data[3]:.2e}'

# Task Three

# Task Four
'{3:0=2} {4:2} {2:4} {0:0=2} {1:2}'.format(4, 30, 2017, 2, 27)

# Task Five
data = ['oranges', 1.3, 'lemons', 1.1]
f'The weight of an {data[0][:6]} is {data[1]} and the weight of a
data{[2][:5]} is {data[3]}'
f'The weight of an {data[0][:6].upper()} is {data[1]*1.2} and the weight of a
{data[2][:5].upper()} is {data[3]*1.2}'

# Task Six
port_wines = [
    ["Graham's Old Tawney", 20, 52.99],
    ["Graham's Vintage", 38, 119.99],
    ["Graham's Tawney", 90, 1000],
    ["Prazo de Roriz", 4, 11.95],
    ["Ficklin Tawney", 10, 29.99],
    ["Porto Reccua", 6, 8.95]]
print('{0:25}{1:3}        {2:7}'.format('Port Wine', 'Age', 'Price'))
print('-' * 42)
for row in port_wines:
    print('{0:25s}{1:3d}    $ {2:7.2f}'.format(*row))
