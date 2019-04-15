#String Formatting

tup_1 = (2, 123.4567, 10000, 12345.67)
tup_3_3 = (2, 3, 5)
tup_3_5 = (2,3,5,7,9)
tup_4 = (4, 30, 2017, 2, 27)
list_5 = ["oranges", 1.3, "lemons", 1.1]

#Task 1
def format_1(tup):
    """
    
    """
    
    #The "8" in "8.2f" creates 3 spaces between ":   123.46" in the output example
    t1_string = "file_{:03d} : {:8.2f}, {:0.2e}, {:0.2e}"
    f1_string = t1_string.format(*tup)
    return f1_string

#Task2
def format_2(tup):
    """
    
    """

    f2_string = f"file_{tup_1[0]:03d} : {tup_1[1]:8.2f}, {tup_1[2]:0.2e}, {tup_1[3]:0.2e}"
    return f2_string

#Task 3
def format_3(tup):
    """
    
    """
    
    l = len(tup)
    brackets = ", ".join(["{:d}"] * l)
    form_string = "the " + str(l) + " numbers are: " +  brackets
    f3_string = form_string.format(*tup)
    return f3_string

#Task 4
def format_4(tup):
    """
    
    """
    
    string = "Date/Time: {:02d} {:d} {:d} {:02d} {:d}"
    f4_string = string.format(tup[3], tup[4], tup[2], tup[0], tup[1])
    return f4_string

#Task 5
def format_5(list_5):
    """
    
    """
    
    o = list_5[0][:-1]
    o_w = list_5[1]
    l = list_5[2][:-1]
    l_w = list_5[3]

    f5_string = f"The weight of an {o} is {o_w} and the weight of a {l} is {l_w}"
    return f5_string

def alt_format_5(list_5):
    """
    
    """
    
    o = list_5[0][:-1].title()
    o_w = list_5[1] * 1.2
    l = list_5[2][:-1].title()
    l_w = list_5[3] * 1.2
    
    f5_string = f"The weight of an {o} is {o_w} and the weight of a {l} is {l_w}"
    return f5_string

if __name__ == "__main__":
    #Run some tests
    print("Task 1:")
    print(format_1(tup_1))
    print()
    print("Task 2:")
    print(format_2(tup_1))
    print()
    print("Task 3:")
    print(format_3(tup_3_3))
    print(format_3(tup_3_5))
    print()
    print("Task 4:")
    print(format_4(tup_4))
    print()
    print("Task 5:")
    print(format_5(list_5))
    print(alt_format_5(list_5))
    print()
    print("Task 6:")