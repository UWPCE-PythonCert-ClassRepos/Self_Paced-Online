def task_one():
    """Converts (2, 123.4567, 10000, 12345.67) to 'file_002 :   123.46, 1.00e+04, 1.23e+04'"""
    string = (2, 123.4567, 10000, 12345.67)
    print("file_{:03d}: {:.2f}, {:.2e}, {:.2e}".format(string[0], string[1],string[2],string[3]))
    return

def task_two():
    """Converts (2, 123.4567, 10000, 12345.67) to 'file_002 :   123.46, 1.00e+04, 1.23e+04'using f-strings"""
    string = (2, 123.4567, 10000, 12345.67)
    print(f"file_{string[0]:03d}: {string[1]:.2f}, {string[2]:.2e}, {string[3]:.2e}")
    return
    
def task_three(in_tuple):
    """Takes a user input tuple and writes in the form of 'the X numbers are: a, b, c'"""
    l = len(in_tuple)
    form_string = ("The {} numbers are: " + ", ".join(["{}"]*l)).format(l, *in_tuple)
    form_string.format(*in_tuple)
    return form_string.format(*in_tuple)

def task_four(string2):
    """Rewrites a tuple (4, 30, 2017, 2, 27) into '02 27 2017 04 30'"""
    print("{:02d} {:02d} {:02d} {:02d} {:02d}".format(string2[3], string2[4],string2[2],string2[0], string2[1]))
    return

def task_five():
    """Uses f-strings to write a message"""
    string3 = ['orange', 1.3, 'lemon', 1.1]

    print(f"The weight of an {string3[0]} is {string3[1]} and the weight of a {string3[2]} is {string3[3]}")
    print(f"The weight of an {string3[0].upper()} is {string3[1]*1.2} and the weight of a {string3[2].upper()} is {string3[3]*1.2}")
    return

def task_six():
    """Prints a table with Name, Age and Cost. Also given a tuple of ten consecutive numbers, it prints into a column 5 characters wide"""
    table_data = [['Name', 'Age', 'Cost'], ['Robert', '23', '100'], ['Mark', '1000', '2.0'], ['Alice', '20', '1000.02'], ['Bob','32', '10000000'], ['Charles','4', '1'], ['Derek','59', '10000000000000'], ['Billy Bob Bo Bobby Bill Bixworth','59', '25.324']]
    for row in table_data:
      print("{: <40s} {: >5} {: >20}".format(*row))

    tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(("{:5d}" * 10).format(*tuple))
    return

if __name__ == "__main__":
    task_one()
    task_two()
    print(task_three((0,2,3,4)))
    print(task_three((0,2,3)))
    print(task_three((0,2,3,4,9, 15, 2)))
    string2 = (4, 30, 2017, 2, 27)
    task_four(string2)
    task_five()
    task_six()
