## Ian Letourneau
## 5/2/2018
## A script to run multiple tasks utilizing string formatting

#Task One: Utilize string formatting to print a string in a specific output format
print ('file{:0>3} :    {:.2f}, {:.2e}, {:.2e}'.format(2, 123.4567, 10000, 12345.67))

#Task Two: Utilize string formatting to print the string from Task One using keywords
print ('file{:{pad}} :    {:{flt}}, {:{science}}, {:{science}}'.format(2,  123.4567, 10000, 12345.67, pad='0>3', flt='.2f', science='.2e'))

#Task Three: Utilize string formatting to run a function that returns a formatted string from a tuple of unspecified length
def formatter(t):
    fstring = "the " + str(len(t)) + " numbers are:"
    for i in range(0,len(t)):
        fstring += " {:d}"
        if i < len(t)-1:
            fstring += ","
    return (fstring.format(*t))

#Task Four: Utilize indexes to format and print a string from an unordered tuple
print ('{3:0>2}, {4}, {2}, {0:0>2}, {1}'.format(4, 30, 2017, 2, 27))

#Task Five: Utilize fstrings to format string and then apply string operations and print new string
things = ['orange', 1.3, 'lemon', 1.1]
print(f"The weight of an {things[0]} is {things[1]} and the weight of a {things[2]} is {things[3]}")
print(f"The weight of an {things[0].upper()} is {(things[1]*1.2)} and the weight of a {things[2].upper()} is {(things[3]*1.2)}")

#Task Six: Print a neat, aligned table with varying length names and numbers. Extra task, print a 10 item tuple using one short formatting line.
name = ['Jimmy', 'Joe', 'Barb']
age = [22, 33, 44]
cost = [67, 448, 1098]

print ('{:<10}{:<10}{:<10}'.format('Name', 'Age', 'Cost'))
for i in range(0,len(name)):
    print ('{:<10}{:<10}{:<10}'.format(name[i], age[i], cost[i]))

extra_tuple = (23, 45, 678, 2, 1166, 79, 90, 901, 546, 10)
print (("{:<5}"*10).format(*extra_tuple))
