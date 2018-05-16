# ------------------------------------------------------------------------
# NAME: MICAH BRAUN
# PROJECT: Series.py
# PURPOSE: To return number series.
#
# DATE: 05/14/2018
#
# DESCRIPTION: Returns and prints Fibonacci, Lucas, and a custom (mixture)
#              of both sequences based upon given criteria.
#
# ------------------------------------------------------------------------

#----------------------------------- Data --------------------------------

line_1 = (" * " * 25)                                      # formatting for header
line_2a = (" " * 34)
line_2 = ("NUMBERS")
line_3 = (" * " * 25)

header = line_1 + '\n' + line_2a + line_2 + '\n' + line_3 + '\n'    # header combined

#--------------------------------- Processing ----------------------------

# FIBONACCI
def fibonacci(n):
    """Return the nth value in the Fibonacci series"""
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return (fibonacci(n-2)+fibonacci(n-1))


# LUCAS
def lucas(n):
    """Return the nth value in the Lucas series"""
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return (lucas(n - 1) + lucas(n - 2))

def sum_string(n, param=None):
    """Sum-Series function, meant to cross between both above functions depending on
    whether optional second argument passed in or not"""
    if param == None:
        if n == 0:
            return n
        elif n == 1:
            return n

        else:
            return (fibonacci(n-2)+fibonacci(n-1))

    elif param != None:
        if n == 0:
            return 2
        elif n == 1:
            return 1
        else:
            return lucas(n -1) + lucas(n -2)

#--------------------------------- Display ----------------------------
print(header)
print()


print("                        ----  Fibonacci Numbers ---- \n")
fib_number = int(input("Input a value to see the Fibonacci series at index n (your entry): "))
for i in range(fib_number):
    print(fibonacci(i))
    print()

print("                        ----  Lucas Numbers ---- \n")
lucas_number = int(input("Input a value to see the Lucas number series at index n (your entry): "))

for i in range(lucas_number):
    print(lucas(i))
    print()


print("                        ----  Sum-Series Numbers ---- \n")
sum_number = int(input("Input a value to see the Sum-Series number at index n (your entry): "))

for i in range(sum_number):
    print(sum_string(i))
    print()
