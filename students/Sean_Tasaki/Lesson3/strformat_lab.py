"""
Sean Tasaki
5/10/2018
Lesson03.strformat_lab
"""
def task_one():
   
    tuple1 = (2, 123.4567, 10000, 12345.67)
    
    results = 'file_{:0>4d} : {:3.2f} , {:.2e} , {:03.2e}'.format(*tuple1)
    
    print("Task One results:")
    print(results)


def task_two():
    results = ('file_0002', 123.46, 1.00e+04, 1.23e+04)
    print("Task Two results:")
    print(f'{results[0]:s} :  {results[1]:.2f}, {results[2]:.2e}\, {results[3]:.2e}')


def task_three(tuple):
    list = []
    for i in tuple:
        list.append(i)
    l = len(list)
    print("Task Three results:")
    print(("The {} numbers are: " + ",".join(["{}"] * l)).format(l, * list))


def task_four():
    n = (4, 30, 2017, 2, 27)
    print("{3:02d} {4} {2} {0:02d} {1}".format(*n))


def task_five():
    print("__________Task Five__________")
    list1 = ['oranges', 1.3, 'lemons', 1.1]
    # Write an f-string that will display:
    # The weight of an orange is 1.3 and the weight of a lemon is 1.1
    print(f'The weight of an {list1[0] [:-1]} is {list1[1]} and the weight\
    of a {list1[2] [:-1]} is {list1[3]}')
    print()
    #  displays the names of the fruit in upper case, and the weight 20% higher
    print(f'The weight of an {list1[0] [:-1].upper()} is {list1[1]*1.2} and the\
    weight of a {list1[2] [:-1].upper()} is {list1[3]*1.2}')


def task_six():
    print("__________Task Six__________")
    list_names = ['Brandon', 'Jared', 'Matt', 'John']
    list_ages = [10, 33, 99, 100]
    list_costs = [450.0000, 200000.00, 14.65, 100000.00]
    for i in range(len(list_names)):
        print(f'{list_names[i]:10s} {list_ages[i]:10n} {list_costs[i]:20n}')
