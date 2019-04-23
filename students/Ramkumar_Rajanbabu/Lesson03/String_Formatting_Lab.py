#String Formatting Lab

tup_1 = (2, 123.4567, 10000, 12345.67)
tup_3_3 = (2, 3, 5)
tup_3_5 = (2,3,5,7,9)
tup_4 = (4, 30, 2017, 2, 27)
list_5 = ["oranges", 1.3, "lemons", 1.1]

def format_1(tup):
    """Runs task 1 of taking a tuple and producing a string. 
    
    Args:
        tup: 4 element tuple
    Returns: 
        f1_string: a format string
    
    """
    
    #The "8" in "8.2f" creates 3 spaces between ":   123.46" in the output example
    t1_string = "file_{:03d} : {:8.2f}, {:0.2e}, {:0.2e}"
    f1_string = t1_string.format(*tup)
    return f1_string

def format_2(tup):
    """Runs task 2 of doing task 1 in an alternate method, using f-string. 
    
    Args:
        tup: 4 element tuple
    Returns: 
        f2_string: a format string
    
    """

    f2_string = f"file_{tup_1[0]:03d} : {tup_1[1]:8.2f}, {tup_1[2]:0.2e}, {tup_1[3]:0.2e}"
    return f2_string

def format_3(tup):
    """Runs task 3 of dynamically building format strings.
    
    Args:
        tup: a tuple
    Returns: 
        f3_string: a format string
    
    """
    
    l = len(tup)
    brackets = ", ".join(["{:d}"] * l)
    form_string = "the " + str(l) + " numbers are: " +  brackets
    f3_string = form_string.format(*tup)
    return f3_string

def format_4(tup):
    """Runs task 4 of using string formatting to print date/time string.
    
    Args:
        tup: 5 element tuple
    Returns: 
        f4_string: a format string
    
    """
    
    string = "Date/Time: {:02d} {:d} {:d} {:02d} {:d}"
    f4_string = string.format(tup[3], tup[4], tup[2], tup[0], tup[1])
    return f4_string

def format_5(list_5):
    """Runs task 5 of writing a f-string.
    
    Args:
        list_5: 4 element list.
    Returns: 
        f5_string: a format string
    
    """
    
    o = list_5[0][:-1]
    o_w = list_5[1]
    l = list_5[2][:-1]
    l_w = list_5[3]

    f5_string = f"The weight of an {o} is {o_w} and the weight of a {l} is {l_w}"
    return f5_string

def alt_format_5(list_5):
    """Runs task 5 of writing a f-string, changing name and weight variable.
    
    Args:
        list_5: 4 element list.
    Returns: 
        f5_string: a format string
    
    """
    
    o = list_5[0][:-1].title()
    o_w = list_5[1] * 1.2
    l = list_5[2][:-1].title()
    l_w = list_5[3] * 1.2
    
    f5_string = f"The weight of an {o} is {o_w} and the weight of a {l} is {l_w}"
    return f5_string

def format_6():
    """Runs task 6 of printing a table of several rows, each with a name, an age and a cost. 
    
    Args:
        None
    Returns: 
        None
    
    """
    
    title_string = "{:<10s} | {:<3s} | {:8s}".format("Name", "Age", "Cost")
    title_bar = len(title_string) * "-"
    
    print(title_string)
    print(title_bar)
    print("{:<10s} | {:>3d} |${:>8d}".format("Ram", 28, 2500800))
    print("{:<10s} | {:>3d} |${:>8d}".format("Tom", 112, 13000))
    print("{:<10s} | {:>3d} |${:>8d}".format("Bob", 3, 20))
    
if __name__ == "__main__":
    #Perform tasks 1-6
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
    format_6()