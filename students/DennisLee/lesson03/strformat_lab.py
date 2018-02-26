#!/usr/bin/env python3

A4 = (2, 123.4567, 10000, 12345.67)


def task1():
    print(f"file_{A4[0]:03d} :  {A4[1]:.2f}, {A4[2]:.2e}, {A4[3]:.2e}")

def task2():
    print("file_{0:03d} :  {1:.2f}, {2:.2e}, {3:.2e}".format(
        A4[0], A4[1], A4[2], A4[3]))
    print("file_%03d :  %.2f, %.2e, %.2e" % A4)

def task3(in_tuple):
    s = "here are 4 numbers: {:d}, {:d}, {:d}, {:d}"
    if len(in_tuple) >= 4:
        print(s.format(*in_tuple))

def task4():
    sample_tuple = (4, 30, 2017, 2, 27)
    print("{3:02d} {4} {2} {0:02d} {1}".format(*sample_tuple))

def task5():
    l = ['oranges', 1.3, 'lemons', 1.1]
    s = f"The weight of an {l[0][:-1]} is {l[1]} " \
            + f"and the weight of a {l[2][:-1]} is {l[3]}"
    s2 = f"The weight of an {l[0][:-1].upper()} is {l[1]*1.2} " \
            + f"and the weight of a {l[2][:-1].upper()} is {l[3]*1.2}"
    print(s.format(l))
    print(s2.format(l))

if __name__ == "__main__":
    task5()