#! /usr/bin/env python3

def convert():
    my_tuple = ( 2, 123.4567, 10000, 12345.67)
    str_first = "{:0>3d}".format(my_tuple[0])
    str_second = "{:.2f}".format(my_tuple[1])
    str_third = "{:.2e}".format(my_tuple[2])
    str_fourth = "{:.2e}".format(my_tuple[3])
    print("file"+str_first + ": " + str_second + "," + str_third + "," + str_fourth)

def convert1():
    my_tuple = ( 2, 123.4567, 10000, 12345.67)
    str_first = "{:0>3d}".format(my_tuple[0])
    str_second = "{:.2f}".format(my_tuple[1])
    str_third = "{:.2e}".format(my_tuple[2])
    str_fourth = "{:.2e}".format(my_tuple[3])

    print("file{}:,{},{},{}".format(str_first,str_second,str_third,str_fourth))
    print(f"file{str_first}:,{str_second},{str_third},{str_fourth}") #using f-strings


def formatter(in_tuple):
    nums = in_tuple
    var_string = ""
    i = 0
    while i < len(nums)-1:
        var_string = "{:d}" + "," + var_string
        i += 1
    var_string += "{:d}"
    print(var_string)
    return var_string.format(*nums)


def convert3(in_tuple):
    nums = in_tuple
    in_string = "{:02d} {} {} {:02d} {}".format(nums[3],nums[4],nums[2],nums[0],nums[1])
    print(in_string)


def task5():
    fruit_lb = ['oranges', 1.3, 'lemons', 1.1]
    o = fruit_lb[0][0:-1]
    l = fruit_lb[2][0:-1]

    sentence = f"The weight of an {o} is {fruit_lb[1]} and the weight of a {l} is {fruit_lb[3]}"
    print(sentence)
    mod_sentence = f"The weight of an {o.upper()} is {fruit_lb[1]*1.2} and the weight of a {l.upper()} is {fruit_lb[3]*1.2}"
    print(mod_sentence)


def task6():

    nottoday = 'moonshine 1 $1.99'
    longday = 'pint 10 $5.99'
    saturday = 'bourbon 18 $29.99'
    graduationday = 'singlemalt 100 $109.99'
    someday = 'reserve 1000 $1000.001'
    occasions = [nottoday, longday, saturday, graduationday, someday]
    for day in occasions:
        print('{:>20s}{:>20s}{:>20s}'.format(day.split()[0], day.split()[1], day.split()[2]))

    num_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print('{:5d} {:5d} {:5d} {:5d} {:5d} {:5d} {:5d} {:5d} {:5d} {:5d}'.format(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def main():
    convert()
    convert1()
    in_tuple = (2,3,5,7,9)
    form_string = formatter(in_tuple)
    print(form_string)
    in_tuple1 = (4, 30, 2017, 2, 27)
    convert3(in_tuple1)
    task5()
    task6()

if __name__ == '__main__':
    main()
