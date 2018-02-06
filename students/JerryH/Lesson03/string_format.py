from decimal import Decimal

#Task 1 & 2
def task1():
    t = ( 2, 123.4567, 10000, 12345.67)

    if t[0] < 10:
        t0 = "file_00{}".format(str(t[0]))
    elif t[0] < 100:
        t0 = "file_0{}".format(str(t[0]))
    else:
        t0 = "file_{}".format(str(t[0]))

    t1 = '{0:.2f}'.format(t[1])
    t2 = '%.2E' % Decimal(t[2])
    t3 = '%.2E' % Decimal(t[3])

    print("{}: {}, {}, {}".format(t0, t1, t2, t3))
#Task 2
    print(f"{t0}: {t1}, {t2}, {t3}")

#Task 3
def formatter(in_tuple):
    form_string = "{:d}, " * (len(in_tuple)-1) + "{:d}"
    return "The {} numbers are: ".format(len(in_tuple)) + form_string.format(*in_tuple)

#Task 4
def task4():
    t = ( 4, 30, 2017, 2, 27)
    print("0{} {} {} 0{} {}".format(t[3],t[4],t[2],t[0],t[1]))

#Task 5
def task5():
    f = ['orange', 1.3, 'lemon', 1.1]
    #Display: The weight of an orange is 1.3 and the weight of a lemon is 1.1
    print(f"The weight of an {f[0]} is {f[1]} and the weight of a {f[2]} is {f[3]}")
    #Print name of the fruit in upper case and the weight 20% higher
    print(f"The weight of an {f[0].upper()} is {f[1]*1.2} and the weight of a {f[2].upper()} is {f[3]*1.2}")

#Task 6
def task6():
    s1 = ['Jason', '26', '$100.99']
    s2 = ['Al', '65', '$1800.49']
    s3 = ['Mark', '6', '$10.12']
    s4 = ['Terry', '34', '$7800.99']
    s_list = [s1,s2,s3,s4]

    for s in s_list:
        print("{:15}{:10}{:20}".format(*s))

    t = (11,12,13,14,15,16,17,18,19,20)
    print(("{:5} " * 9 + "{:5}").format(*t))
