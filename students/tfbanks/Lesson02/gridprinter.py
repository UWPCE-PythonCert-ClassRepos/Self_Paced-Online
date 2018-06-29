# This is the result of manual processes moved into function form.  
# I cleaned up during the process and deleted the old methods so the end result is just the function


def grid (x,y): #Defines a function to print grid to specified dimensions
    p = '+ ' # This prints a + sign
    d = '- ' # This prints a dash
    b = '| ' # this prints a bar
    print ((p + d * x) * y + p) #Prints the first line consiting of p's, d's and b's; creating the box based on x dimension, and repeated y times
    for r in range (y):
        for i in range(x):
            print ((b + '  '*x) * y + b) #Prints the bar section to x dimension, repeated y times
        print ((p + d * x) * y + p) #completes the "squares" and repeats y times
grid (3,4) #Prints a 4 x 4 matrix of 3x3 squares, + being the corners

