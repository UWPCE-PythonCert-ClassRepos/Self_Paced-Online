#-------------------------------------------------#
# Title: String Formatting
# Dev:   LDenney
# Date:  October 10, 2018
# ChangeLog: (Who, When, What)
#   Laura Denney, 10/10/18, Created File
#   Laura Denney, 10/11/18, Modified File
#-------------------------------------------------#

#task 1------------------------------------------
def task1():
    tupl =  (2, 123.4567, 10000, 12345.67)
    str = "file_{:03d}:  {:.2f}, {:.2e}, {:3.2e}".format(*tupl)
    print(str)

#task 2------------------------------------------
def task2():
    tupl =  (2, 123.4567, 10000, 12345.67)
    str2 = f"file_{tupl[0]:03d}:  {tupl[1]:.2f}, {tupl[2]:.2e}, {tupl[3]:3.2e}"
    print(str2)

#task 3------------------------------------------

def formatter(in_tuple):
    leng = len(in_tuple)
    fstring = "the {:d} numbers are: " + ", ".join(["{:d}"] * leng)
    return fstring.format(leng, *in_tuple)

#task 4------------------------------------------
def task4():
    tupl = (4, 30, 2017, 2, 27)
    str = f"'{tupl[3]:02d} {tupl[-1]} {tupl[2]} {tupl[0]:02d} {tupl[1]}'"
    print(str)

#task 5------------------------------------------
def task5():
    lst = ['oranges', 1.3, 'lemons', 1.1]
    fstring = f"The weight of an {lst[0][:-1]} is {lst[1]} and the weight of a {lst[2][:-1]} is {lst[-1]}"
    print(fstring)
    fstring2 = f"The weight of an {lst[0][:-1].upper()} is {lst[1] *1.2} and the weight of a {lst[2][:-1].upper()} is {lst[-1]*1.2}"
    print(fstring2)

#task 6------------------------------------------
def task6():
    tabl = [["Name", "Age", "Cost"], ["Apple", "10", "$0.99"],
            ["Kiwi", "2", "$876.50"], ["Banana", "55", "$1000.99"]]
    for row in tabl:
        print("{:>10}{:>10}{:>10}".format(*row))

if __name__ == "__main__":
    task1()
    task2()
    formatter((1,2,3,4,5))
    task4()
    task5()
    task6()
