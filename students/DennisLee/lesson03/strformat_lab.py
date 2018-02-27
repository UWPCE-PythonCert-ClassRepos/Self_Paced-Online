#!/usr/bin/env python3

# sample tuple to format for tasks 1 and 2
A4 = (2, 123.4567, 10000, 12345.67)


def task1():
    print(f"file_{A4[0]:03d} :  {A4[1]:.2f}, {A4[2]:.2e}, {A4[3]:.2e}")

def task2():
    print("file_{0:03d} :  {1:.2f}, {2:.2e}, {3:.2e}".format(
        A4[0], A4[1], A4[2], A4[3]))
    print("file_%03d :  %.2f, %.2e, %.2e" % A4)

def task3(input_tuple):
    # Print out 4 numbers from a tuple, if possible
    s = "Here are 4 numbers: {:d}, {:d}, {:d}, {:d}"
    if len(input_tuple) >= 4:
        print(s.format(*input_tuple))
    else:
        print("This tuple has less than 4 numbers, so it can't be formatted: ",
                input_tuple)

def task4():
    sample_tuple = (4, 30, 2017, 2, 27)
    print("{3:02d} {4} {2} {0:02d} {1}".format(*sample_tuple))

def task5():
    # Print out string variations of the weight of two fruits
    l = ['oranges', 1.3, 'lemons', 1.1]
    s = f"The weight of an {l[0][:-1]} is {l[1]} " \
            + f"and the weight of a {l[2][:-1]} is {l[3]}"
    s2 = f"The weight of an {l[0][:-1].upper()} is {l[1]*1.2} " \
            + f"and the weight of a {l[2][:-1].upper()} is {l[3]*1.2}"
    print(s.format(l))
    print(s2.format(l))

def task6(*name_age_cost):
    # Print out a multi-row table of names, ages, and costs
    format_function = "{:<30s} | {:>5d} | ${:>14,.2f}".format
    print("Name                           |   Age |            Cost")
    print("-------------------------------|-------|----------------")
    for row in name_age_cost:
        if len(row) >= 3:
            print(format_function(*row))
    
def task7(*ten_numbers):
    # print a random range of ten numbers in rows with 5-character wide columns
    for num_range in ten_numbers:
        print(("{:>5d}" * 10).format(*num_range))


if __name__ == "__main__":
    linefeeds = '\n' * 5

    print(linefeeds, "\tTASK 1")
    task1()
    input("\nPress Enter to continue to task 2:")

    print(linefeeds, "\tTASK 2")
    task2()
    input("\nPress Enter to continue to task 3:")

    # Call task 3 with 3-, 6-, and 4-value tuples ... the 3-value tuple
    # should fail
    print(linefeeds, "\tTASK 3")
    task3((547395, 34251, 23414))
    task3((547395, 34251, 23414, 5849, 352134, 65532))
    task3((5, 4, 3, 2))
    input("\nPress Enter to continue to task 4:")

    print(linefeeds, "\tTASK 4")
    task4()
    input("\nPress Enter to continue to task 5:")

    print(linefeeds, "\tTASK 5")
    task5()
    input("\nPress Enter to continue to task 6:")

    print(linefeeds, "\tTASK 6")
    task6(('Abraham Lincoln', 96, 34194138.32),
          ('Victor Baby Alligator', 5, .5),
          ('Tony the Frosted Flakes Tiger', 40, 1257.46, 'Grahams', 5454984.2),
          ('Mister Misterioso', 18, 8499843),
          ('Scooby Dee', 29),
          ('Barney Flintstone', 78, 57.09))
    input("\nPress Enter to continue to task 7:")

    print(linefeeds, "\tTASK 7")
    task7(range(1028, 1038), 
          range(0, 10), 
          range(243, 253), 
          range(77, 87))