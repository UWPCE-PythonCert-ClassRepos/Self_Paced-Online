'''Author: Alex Filson
Updated: 1.19.19
String Formatting Lab for Lesson 3
Py210, Online Self-Paced
'''

def taskone(t):
    '''Use 'format' to return variety of string formats.'''
    return 'file_{:0>3d}, {:.2f}, {:.2e}, {:.3e}'.format(*t)

def tasktwo(t):
    '''Use 'f-string' to return same string formatting as task one'''
    return f'file_{t[0]:0>3d}, {t[1]:.2f}, {t[2]:.2e}, {t[3]:.3e}'

def taskthree(t):
    if len(t) == 0:
        return "there are no numbers"
    elif len(t) == 1:
        return f'the number is {t[0]}'
    else:
        form_string = ["the {} numbers are: {}"]
        for i in range(len(t)-1):
            form_string.append('{}')
        form_string = " ".join(form_string)
        return form_string.format(len(t),*t)

def taskfour(t):
    return f'{t[3]:0>2d} {t[4]} {t[2]} {t[0]:0>2d} {t[1]}'

def taskfive(t):
    return f'''The weight of an {t[0][:-1].upper()} is {t[1]*1.2} and the weight
             of a {t[2][:-1].upper()} is {t[3]*1.2}'''




tpl = ( 2, 123.4567, 10000, 12345.67)

print(taskone(tpl))
print(tasktwo(tpl))
print(taskthree(tpl))
print(taskfour((4,30,2017,2,27)))
print(taskfive(['oranges',1.3,'lemons',1.1]))