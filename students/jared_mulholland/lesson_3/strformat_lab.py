"""
Goal

Task One

    Write a format string that will take the following four element tuple:

        ( 2, 123.4567, 10000, 12345.67)

        and produce:

        'file_002 :   123.46, 1.00e+04, 1.23e+04'

Let’s look at each of the four tuple elements in turn:

The second element is a floating point number. You should display it with 2 decimal places shown.
The third value is an integer, but could be any number. You should display it in scientific notation, with 2 decimal places shown.
The fourth value is a float with a lot of digits – display it in scientific notation with 3 significant figures.

"""

#Task 1

print("file_00{:d}: {:.2f}, {:.2e}, {:.2e}".format(2, 123.4242,10000,12345.67))

#Task 2
#Using your results from Task One, repeat the exercise, but this time using an alternate type of format string 
# (hint: think about alternative ways to use .format() (keywords anyone?), and also consider f-strings if you’ve not used them already).

file = (2, 123.4567, 10000, 12345.67)


print(f"file_00{file[0]:d}: {file[1]:.2f}, {file[2]:.2e}, {file[3]:.2e}")

#Task 3
#Dynamically Building up Format Strings
#Rewrite:
#"the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
#to take an arbitrary number of values.

def formatter(seq):
    l = len(seq)    
    return "The " + str(l) + " numbers are: " + ", ".join(['{}']*l).format(*seq)

#Task 4 
#Given a 5 element tuple: ( 4, 30, 2017, 2, 27)
#use string formating to print:'02 27 2017 04 30'

data = (4,30,2017,2,27)

"{d[3]:02d} {d[4]:02d} {d[2]:4d} {d[0]:02d} {d[1]:02d}".format(d=data)


#Task 5
#f-strings are new to Python (version 3.6), but are very powerful and efficient. This means they are worth understanding and using. 
# And this is made easier than it might be because they use the same, familiar formatting language that is conventionally used in Python (in .format()).

#Here’s a task for you: Given the following four element list:
#['oranges', 1.3, 'lemons', 1.1]

#Write an f-string that will display:
#The weight of an orange is 1.3 and the weight of a lemon is 1.1

#Now see if you can change the f-string so that it displays the names of the fruit in upper case, and the weight 20% higher (that is 1.2 times higher).

s = ['oranges', 1.3, 'lemons', 1.1]

print("\nTask 5\n")

print(f"The weight of an {s[0][:-1]} is {s[1]} and the weight of a {s[2][:-1]} is {s[3]}")

print("\nnames of the fruit in upper case and weight 20 percent higher\n")

print(f"The weight of an {s[0][:-1].upper()} is {s[1]*1.2} and the weight of a {s[2][:-1].upper()} is {s[3]*1.2}")

#Task 6
#Write some Python code to print a table of several rows, each with a name, an age and a cost. 
# Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.

#And for an extra task, given a tuple with 10 consecutive numbers, can you work how to quickly print the tuple in columns that are 5 charaters wide? 
#It’s easily done on one short line!

rows = (("Calvin",8,1000.000313),("Jared", 40, 100.00),("Chase", 10, 35.00000),("James",7,321.001))

print("\nTask6\n")

for row in rows:
    print('{:<10s}{:5d}{:10.2f}'.format(*row))

print("\n")

tup = (1,2,3,4,5,6,7,8,9,10)

for t in tup:
    print('{:05d}'.format(t))
