Lesson 3 directory contains two scripts: list_lab and strformat_lab
Ross Martin

list_lab

Series 1
Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
Display the list (plain old print() is fine…).
Ask the user for another fruit and add it to the end of the list.
Display the list.
Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
Add another fruit to the beginning of the list using “+” and display the list.
Add another fruit to the beginning of the list using insert() and display the list.
Display all the fruits that begin with “P”, using a for loop.

Series 2
Using the list created in series 1 above:

Display the list.
Remove the last fruit from the list.
Display the list.
Ask the user for a fruit to delete, find it and delete it.
(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)

Series 3
Again, using the list from series 1:

Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
For each “no”, delete that fruit from the list.
For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
Display the list.

Series 4
Once more, using the list from series 1:

Make a copy of the list and reverse the letters in each fruit in the copy.
Delete the last item of the original list. Display the original list and the copy.

strformat_lab
def format_numbers(a):
    """formats 4 number tuple to different number formats for each element"""

def task1(a):
    """format 4 element tuple ( 2, 123.4567, 10000, 12345.67) to 'file_002 :   123.46, 1.00e+04, 1.23e+04'"""

def task2(a):
    """format 4 element tuple using fstring"""

def task3(a):
    """build dynamic string from list"""

def task4(a):
    """Given a 5 element tuple: ( 4, 30, 2017, 2, 27) use string formating to print: '02 27 2017 04 30'"""

def increase_weight(weight):
    """multiply weight by 1.2"""

def format_fruit(fruit):
    """make fruit singular and make upper case"""

def task5(a):
    """writes fstring that formats four element list ['oranges', 1.3, 'lemons', 1.1] as:
       'The weight of an ORANGE is 1.6 and the weight of a LEMON is 1.3'
       fruit names are changed to upper and weights increased by 20%"""

def task6(a):
    """print a table of several rows, a argument is list of tuples, each tuple with a name, an age and a cost"""

def extra_task(a):
    """given a tuple with 10 consecutive numbers, can you work how to quickly print the tuple in columns that are 5 charaters wide"""

