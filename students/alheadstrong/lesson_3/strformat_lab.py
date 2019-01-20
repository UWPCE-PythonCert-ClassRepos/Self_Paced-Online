'''Author: Alex Filson
Updated: 1.19.19
String Formatting Lab for Lesson 3
Py210, Online Self-Paced
'''

def taskone(t):
    return 'file_{:0>3d}, {:.2f}, {:.2e}, {:.3e}'.format(t[0],t[1],
                                                        t[2],t[3])

def tasktwo(t):
    return f'file_{t[0]:0>3d}, {t[1]:.2f}, {t[2]:.2e}, {t[3]:.3e}'

tpl = ( 2, 123.4567, 10000, 12345.67)

print(taskone(tpl))
print(tasktwo(tpl))