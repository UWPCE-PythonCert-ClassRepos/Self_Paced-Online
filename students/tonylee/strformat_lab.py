def task_one():
    print("Task One")
    test_tuple = (2, 123.4567, 10000, 12345.67)
    print(f'file_{test_tuple[0]:03d} :  {test_tuple[1]:.2f}, {test_tuple[2]:.2e}, {test_tuple[3]:.2e}')

def task_two():
    print("Task Two")
    test_tuple = (2, 123.4567, 10000, 12345.67)
    print("file_{0:03d} :  {1:.2f}, {2:.2e}, {3:.2e}".format(test_tuple[0], test_tuple[1], test_tuple[2], test_tuple[3]))

def formatter(in_tuple):
    return "the 4 numbers are: {:d}, {:d}, {:d}, {:d}".format(*in_tuple)

def task_three():
    print("Task Three")
    test_tuple = ( 3, 4, 5, 6)
    print(formatter(test_tuple))

def task_four():
    print("Task Four")
    test_tuple = ( 4, 30, 2017, 2, 27)
    print("'{:02d} {:02d} {} {:02d} {:02d}'".format(test_tuple[3], test_tuple[4], test_tuple[2], test_tuple[0], test_tuple[1]))

def task_five():
    print("Task Five")
    test_list = ['oranges', 1.3, 'lemons', 1.1]
    print(f"The weight of an {test_list[0]} is {test_list[1]} and the weight of a {test_list[2]} is {test_list[3]}")
    print(f"The weight of an {test_list[0].upper()} is {test_list[1]*1.2} and the weight of a {test_list[2].upper()} is {test_list[3]*1.2}")

def task_six():
    print("Task Six")
    names = ['Tony', 'Andrew', 'Bill']
    age = [50, 55, 45]
    cost = [100.00, 300.00, 200]
    print("Name         Age     Cost")
    for i in range(3):
        print("{:8} {:6} {:11.2f}".format(names[i], age[i], cost[i]))

def bonus_task():
    print("Bonus Task")
    test_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    for i in test_tuple:
      print("{:5}".format(i))

task_one()
task_two()
task_three()
task_four()
task_five()
task_six()
bonus_task()
