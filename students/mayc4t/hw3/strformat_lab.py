#!/usr/bin/env python3
# ###############################################################################
# Written by: Mayc4t
# March 19, 2018


def task_3_dynamic_formatter(seq):
    """ Dynamically Building up Format Strings. """

    # this is just note to myself
    # hint build from the video

    # list of a item * 4 : ["{}"] * 4. Replace 4 with len of something
    # ["{}"] * 4  to have a list of 4 items
    #       ["{}"].format (seq) --> seq this will be just the first value
    # want to have ', ' between items  --> use join
    # also list object( *seq) has no attribute 'format
    # format is just for str, therefore use str.join( sequence) to return a string
    #       ('. '.join(["{}"])*l). format(*seq)
    # "inside double quote can only real string or {}"
    # That's why we have to  +   for the formular of ', '.join ....
    # add another () out of the whole string.  format things
    #
    # or quick and easy way to remember just use hydrid c + python
    # ("there are %s days of a week. They are %s" % (len(days), ("{}, " * len(days)))).format(*days)[0:-2]

    l = len(seq)
    print (("\tThere are {} days in a week.\n\tThey are:" +
            ', '.join(["{}"] * l)).format(l, *seq))



# ###############################################################################
if __name__ == "__main__":

    print ("\n\n\nTASK 1")
    print ("String format for decimal, scientific number")
    seq_0 = (2, 123.4567, 10000, 12345.67)

    str_1 = ""
    str_1 = "file_" + ("{:03d}".format(seq_0[0])) + ':   '
    str_1 += ("{:.2f}".format(seq_0[1])) + ', '
    str_1 += ("{:.2e}".format(seq_0[2])) + ', '
    str_1 += ("{:4.2e}".format(seq_0[3]))
    print ("\tOrginal tuple: {}".format(seq_0))
    print ("\tResult :\t", end='')
    print (str_1)

    print ("\nTASK 2")
    print ("Altertively,  format string for decimal, scientific number using f-string")
    lst_2 = str_1.split()
    print(f"\tResult :\t{lst_2[0]}   {lst_2[1]} {lst_2[2]} {lst_2[3]}")

    print ("\nTASK 3")
    print("Build a dynamic string")
    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
    l = len(days)
    print (("\tThere are {} days in a week.\n\tThey are:" +
            ', '.join(["{}"] * l)).format(l, *days))

    print ("\nTASK 4")
    print ("Format using index")
    print ("\tThe new order is \n\t'{3} {4} {2} {0} {1}'".format(
        4, 30, 2017, 2, 27))

    print ("\nTASK 5")
    print("Format string using f-string, expression for f-string")
    list_4 = ['oranges', 1.3, 'lemons', 1.1]
    print(f"\tThe weight of an {list_4[0]} is  {list_4[1]} and the weight of a {list_4[2]} is {list_4[3]}")
    print(f"\tThe weight of an {list_4[0].upper()} is  {list_4[1]*1.2} and the weight of a {list_4[2].upper()} is {list_4[3]*1.2}")

    print ("TASK 6\n")
    print ("Format a table, with string width specifier")
    line0 = ('NAME', 'AGE', 'COST')
    line1 = ('Lily', 38, 0.99)
    line2 = ('Maymay', 2, 123456789.02)
    line3 = ('Meow',   6, 3456789.87)
    line4 = ('Orr',   99, 2344.22)
    line5 = ('Huynh', 101, 233.22)
    line6 = ('Johnston', 58, 23433.24)
    line7 = ('Vitamix', 2, 399.99)
    line8 = ('Instanpot', 0.5, 159.99)
    line9 = ('IphoneX', 0.3, 1000.99)
    line10 = ('Nexus6', 1, 599.99)
    table = (line0, line1, line2, line3, line4, line5,
             line6, line7, line8, line9, line10)

    for idx, line in enumerate(table):
        # note to myself
        # (type(table): tuple, type(line): tupble)
        if idx == 0:
            print (("{}" + "{:<20}{:^5}{:>30}").format("    ", * line))
        else:
            print(("{:2}  " + "{:<20}{:>3}{:>30}").format(idx, *line))

    print ("\n\nTASK 6 +")
    print ("print a tuple number into a comlumn with predefined width")
    a = tuple(list(range(10)))
    print(''.join(["{:>5}\n"]*len(a)).format(*a))
