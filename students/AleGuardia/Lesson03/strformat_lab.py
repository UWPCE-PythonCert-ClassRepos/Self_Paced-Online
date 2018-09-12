#!/usr/bin/env python3

# Task One

print('file_{:0>3d}: {:.2f}, {:.2e}, {:.2e}'.format(2, 123.4567, 10000, 12345.67))

# Task Two

element_tuple = (2, 123.4567, 10000, 12345.67)
print('file_{:0>3d}: {:.2f}, {:.2e}, {:.2e}'.format(*element_tuple))
print(f'file_{element_tuple[0]:0>3d}: {element_tuple[1]:.2f}, {element_tuple[2]:.2e}, {element_tuple[3]:.2e}')

# Task Three

def formatter(in_tuple):
    form_string = f"the {len(in_tuple)} numbers are: {'{} '*len(in_tuple)}"
    return form_string.format(*in_tuple)

print(formatter((1,2,3,4,5,6)))

