def taskone():
    tuple = (2, 123.4567, 10000, 12345.67)
    result = "File_{:0>3} :{:0.2f} , {:.2E} , {:.2E} ".format(2, 123.4567, 10000, 12345.67)
    return result

def tasktwo():
    results = ('File_002', 123.46, 1.00e+04, 1.23e+04)
    print(f'{results[0]:s}:  {results[1]:.2f}, {results[2]:.2e}, {results[3]:.2e}')


def taskthree(list):
    l = len(list)
    print(("The {} numbers are: " + ",".join(["{}"] * l)).format(l, * list))


def taskfour():
    x = (4,30,2017, 2, 27)

    print("{3:02d} {4} {2} {0:02d} {1}".format(*x))
    
def taskfive():
    list =['orange',1.3,'lemon', 1.1]

    print(f'The weight of an {list[0]:s} is {list[1]} and the weight of a {list[2]:s} is {list[3]}')
    """ string with fruit in all caps and weight multiplied by 1.2"""
    print(f'The weight of an {list[0].upper():s} is {list[1]*1.2} and the weight of a {list[2].upper():s} is {list[3]*1.2}')

    def tasksix():
    list_names = ['Nep', 'Dude', 'Hulk', 'Road-dog']
    list_ages = [45, 27, 40, 60]
    list_costs = [600.00, 1500.00, 19.99, 9.99]
    for i in range(len(list_names)):
        print(f'{list_names[i]:10s} {list_ages[i]:10n} {list_costs[i]:15n}')
