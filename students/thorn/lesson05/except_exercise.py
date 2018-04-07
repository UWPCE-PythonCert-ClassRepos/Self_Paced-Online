"""
An exercise in playing with Exceptions.
Make lots of try/except blocks for fun and profit.

Make sure to catch specifically the error you find, rather than all errors.
"""

from except_test import fun, more_fun, last_fun


# Figure out what the exception is, catch it and while still
# in that catch block, try again with the second item in the list
first_try = ['spam', 'cheese', 'mr death']
try:
    joke = fun(first_try[0])
except NameError:
    print(f"Whoops there is no joke for {first_try[0]}")

# Here is a try/except block. Add an else that prints not_joke
try:
    not_joke = fun(first_try[2])
except SyntaxError:
    print('Run Away!')
else:
    print(not_joke)

# What did that do? You can think of else in this context, as well as in
# loops as meaning: "else if nothing went wrong"
# (no breaks in  loops, no exceptions in try blocks)

# Figure out what the exception is, catch it and in that same block
#
# try calling the more_fun function with the 2nd language in the list,
# again assigning it to next_joke.
#
# If there are no exceptions, call the more_fun function with the last
# language in the list regardless of whether there was an exception

# Finally, while still in the try/except block and regardless of whether
# there were any exceptions, call the function last_fun with no
# parameters. (pun intended)

"""
GOAL:
1 - Whoops! there is no joke for: spam

2 - Customer: Not much of a cheese shop really, is it?
3 - Shopkeeper: Finest in the district, sir.
4 - Customer: And what leads you to that conclusion?
5 - Shopkeeper: Well, it's so clean.
6 - Customer:  It's certainly uncontaminated by cheese.
"""

langs = ['java', 'c', 'python']

try:
    # Bad --> Test[5] out of range
    more_fun(langs[0])
except IndexError:
    more_fun(langs[1])
# Except will trigger -> else
else:
    more_fun(langs[2])
# Post exception block
finally:
    last_fun()



