# Write some functions that take a sequence as an argument, and return a copy of that sequence:

#1.  with the first and last items exchanged.

def first_last(seq):
    '''Return a copy of seq with the first and last items exchanged.'''
    return seq[-1:] + seq[1:-1] + seq[:1]

  


#2. with every other item removed.
def every_other(seq):
    '''Return a copy of seq with every other item removed.'''
    return seq[::2]


# 3. with the first 4 and the last 4 items removed, and then every other item in between.
def first_last_four(seq):
    '''Return a copy of seq with the first and last 4 items removed, and then every other item in between'''
    return seq[4:-4:2]

# 4. with the elements reversed (just with slicing).

def reversed(seq):
    '''Return a copy of seq with elements reversed'''
    return seq[::-1]

# 5. with the middle third, then last third, then the first third in the new order.

def third(seq):
    '''Return a copy of seq with the middle third, then last third, then the first third in the new order.'''
    n = (len(seq))//3
    return seq[n:-n]+seq[-n:]+seq[:n]

#Tests:
#We define new variables setting them to various types of sequences. In our case, it is a string, a tuple and a list. 
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# Assert statements to test our first_last function: checks whether the function returns a copy of the given sequence with 
#the first and last items exchanged.

assert first_last(a_string) == "ghis is a strint", "assert statement failed"
assert first_last(a_tuple) == (32, 54, 13, 12, 5, 2), "assert statement failed"
assert first_last(a_list) == [16, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1],  "assert statement failed"

# Assert statements to test our every_other function: checks whether the function returns a copy of  the given argument with 
#every other item removed. 

assert every_other(a_string) == "ti sasrn", "assert statement failed"
assert every_other(a_tuple) == (2, 13, 5)
assert every_other(a_list) == [1, 3, 5, 7, 9, 11, 13, 15], "assert statement failed"

#Assert statements to test our first_last_four function. Checks whether the function return a copy of the given argument
# with the first and last 4 items removed, and then every other item in between.

assert first_last_four(a_string) == " sas", "assert statement failed"
assert first_last_four(a_tuple) == (), "assert statement failed"
assert first_last_four((1, 2, 3, 4, 5, "d", "e", 6, 7, 8, 9, 10, 11, 12)) == (5, 'e', 7), "assert statement failed"
assert first_last_four(a_list) == [5, 7, 9, 11], "assert statement failed"

#Assert statements to test our reversed function: checks whether the function returns the given argument with its elements reversed.elements
assert reversed(a_string) == "gnirts a si siht", "assert statement failed"
assert reversed(a_tuple) == (32, 5, 12, 13, 54, 2), "assert statement failed"
assert reversed(a_list) == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], "assert statement failed"

#Assert statements to test our third function: checks whether it returns the provided argument with 
#the middle third, then last third and then the first third in the new order.the
assert third(a_string) == "is a stringthis ", "assert statement failed"  
assert third(a_tuple) == (13, 12, 5, 32, 2, 54), "assert statement failed"
assert third(a_list) == [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 5], "assert statement failed"
