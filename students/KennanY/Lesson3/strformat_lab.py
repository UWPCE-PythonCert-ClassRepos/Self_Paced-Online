#STRING FORMAT EXERCISES

#TASK ONE
#Take this tuple ( 2, 123.4567, 10000, 12345.67)
#and produce 'file_002 :   123.46, 1.00e+04, 1.23e+04'

elements = (2, 123.4567, 10000, 12345.67)
print('file_{:03d}: {:0.2f} {:0.2E} {:0.2E}'.format(elements[0], elements[1], elements[2], elements[3]))

#TASK TWO
#Using your results from Task One, repeat the exercise,
#but this time using an alternate type of format string
# (hint: think about alternative ways to use .format()

print(f'file_{elements[0]:0=3}:  {elements[1]:5.2f}, {elements[2]:.2e}, {elements[3]:.2e}')

#TASK 3
#Take an arbitrary number of values and build a dynamic formatter
def formatter(* t):
    myString=' '
    for item in t:
        myString += '{:d},'
    myString = myString[:-1]

    print('the ' + str(len(t)) + ' numbers are ' + myString.format(*t))

formatter(*(12, 6, 9))
formatter(*(21, 44, 5, 9, 7,34))

#TASK 4
# Given ( 4, 30, 2017, 2, 27), print '02 27 2017 04 30'

print('{3:0=2} {4:2} {2:4} {0:0=2} {1:2}'.format(4, 30, 2017, 2, 27))

#TASK 5
#Write and f-string that writes:
# The weight of an orange is 1.3 and the weight of a lemon is 1.1
text=['oranges', 1.3, 'lemons', 1.1]

print(f'The weight of an {text[0]} is {text[1]} and the weight of a  {text[2]} is {text[3]}')
print(f'The weight of an {text[0].upper()} is {text[1]*1.2} and the weight of a  {text[2].upper()} is {text[3]*1.2}')

#TASK 6
headings = ("Product", "Age", "Cost")

products = [
    ["Apple",5,2.59],
    ["Boat",18,217.69],
    ["Car",4,2450],
    ["Chair",100,1290],
    ["Gas",999,100.1234]]

print('{:<20} {:<10} {:<10}'.format(*headings))

for product in products:
    print('{:<20} {:<10} ${:<10}'.format(*product))

