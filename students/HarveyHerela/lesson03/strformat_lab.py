#!/usr/bin/env python

def task_one():
    """Task 1: Print out this tuple."""
    t1_tuple = (2, 123.4567, 10000, 12345.67)

    # create a string formatter to produce:
    # 'file_002 :   123.46, 1.00e+04, 1.23e+04'

    print("file_{:0>3d} :   {:.2f}, {:.2e}, {:.3e}".format(t1_tuple[0], t1_tuple[1], t1_tuple[2], t1_tuple[3]))
    
def task_two():
    """Task 2: Same as task 1, but different."""
    t1_tuple = (2, 123.4567, 10000, 12345.67)
    
    print(f"file_{t1_tuple[0]:0>3d} :   {t1_tuple[1]:.2f}, {t1_tuple[2]:.2e}, {t1_tuple[3]:.3e}")

def task_three(tuple_in):
    """Task 3: Print out arbitrary length tuples."""
    t3_str = "the {} numbers are: ".format(len(tuple_in))
    
    if len(tuple_in) > 0:
        t3_str += "{}".format(tuple_in[0]);
    
    for num in tuple_in[1:]:
        t3_str += ", {}".format(num)
    
    return t3_str

def task_four(tuple_in):
    """"Task 4: Given a tuple with 5 elements, i.e.:( 4, 30, 2017, 2, 27)
    print: '02 27 2017 04 30'
    """
    print("{n3:0>2d} {n4:0>2d} {n2:0>2d} {n0:0>2d} {n1:0>2d}".format(
        n0=tuple_in[0], n1=tuple_in[1], n2=tuple_in[2], n3=tuple_in[3], n4=tuple_in[4]))

def task_five():
    """The weight of an orange is 1.3 and the weight of a lemon is 1.1
    Then change the f-string so that it displays the names of the fruit in 
    upper case, and the weight 20% higher (that is 1.2 times higher).
    """
    orange = ("orange", 1.3)
    lemon = ("lemon", 1.1)
    print(f"The weight of an {orange[0]} is {orange[1]} and the weight of a {lemon[0]} is {lemon[1]}")
    print(f"The weight of an {orange[0].upper()} is {orange[1] * 1.2} and the weight of a {lemon[0].upper()} is {lemon[1] * 1.2}")

def task_six():
    """Print a table of several rows, each with a name, an age and a cost. 
    Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.
    
    And for an extra task, given a tuple with 10 consecutive numbers, can you work how to quickly 
    print the tuple in columns that are 5 charaters wide? It's easily done on one short line!
    """
    
    db = list()
    db.append(("Chase", 5, 42))
    db.append(("Marshall", 15, 142))
    db.append(("Zuma", 45, 1042))
    db.append(("Mayor Humdinger", 105, 1))
    db.append(("Captain Turbot", 25, 102542))
    db.append(("Chickaletta", 4, 5412))
    
    for d in db:
        print("{:<20}  {:>3d}  ${:>15.2f}".format(*d))
    
    bonus_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(("{:5d}" * 10).format(*bonus_tuple))

if __name__ == "__main__":
    task_one()
    task_two()
    
    print(task_three(()))
    print(task_three((0,)))
    print(task_three((1, 2, 3)))
    print(task_three((4, 5, 6, 7, 8, 9)))
    
    task_four((4, 30, 2017, 2, 27))
    
    task_five()

    task_six()    
    
