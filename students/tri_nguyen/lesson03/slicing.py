# -------------------------------------------#
# Student:   Tri Nguyen
# Instructor: Natasha Aleksandrova
# Date:  08-Feb-2018
# -------------------------------------------#

# Write some functions that take a sequence as an
# argument, and return a copy of that sequence:
# 1. With the first and the last item exchanged
# 2. With every other item removed
# 3. With the first 4 and the last 4 items removed
# and then every other item in between
# 4. With the elements reversed (just slicing)
# 5. With the middle third, the last third, then
# the first third in the new order

# Part 1:

def exchange_first_last(seq):
    '''
        this function takes a sequence (seq) and return
        a copy with the first and the last item exchanged        
    '''
    if len(seq) <= 1:
        exchanged_seq = 'Sequence has 0 or 1 value. Unable to compute.'
    else:
        exchanged_seq = seq[-1:] + seq[1:len(seq) - 1] + seq[:1]
    return exchanged_seq
    
# Part 2:

def remove_every_other(seq):
    '''
        this function takes a sequence (seq) and return
        a copy with every other item removed    
    '''
    
    container = []
    
    if len(seq) <= 1:
        return 'Sequence has 0 or 1 value. Unable to compute.'
    else:
        for idx, item in enumerate(seq):
            if not idx % 2:
                container.append(str(item))
         
    return ' '.join(container)

# With every other item removed can also be rewritten
# as below re_every_other() function

def re_every_other(seq):
    '''
        this function takes a sequence (seq) and return
        a copy with the first and the last item exchanged        
    '''
    
    if len(seq) <= 1:
        return 'Sequence has 0 or 1 value. Unable to compute.'
    else:
        return seq[::2]


# Part 3:

def first_last_four(seq):
    '''
        this function takes a sequence (seq) and return
        a copy with the first 4 and the last 4 items removed
        and then every other item in between        
    '''

    if len(seq) <= 1:
        return 'Sequence has 0 or 1 value. Unable to compute.'
    else:
        return seq[4:len(seq) - 4:2]

# Part 4

def reverse_seq(seq):
    '''
        this function takes a sequence (seq) and return
        a copy with the elements reversed (just slicing)       
    '''

    if len(seq) <= 1:
        return 'Sequence has 0 or 1 value. Unable to compute.'
    else:
        return seq[::-1]

# Part 5

def mid_last_first(seq):
    '''
        this function takes a sequence (seq) and return
        a copy with the middle third, the last third, then
        the first third in the new order
    '''
    
    if len(seq) <= 1:
        return 'Sequence has 0 or 1 value. Unable to compute.'
    else:
        first_third = seq[0:round(len(seq)/3)]
        middle_third = seq[round(len(seq)/3):round(len(seq)/3) + round(len(seq)/3)]
        last_third = seq[round(len(seq)/3) + round(len(seq)/3):]
        
        return middle_third + last_third + first_third

# Testing

a_string = 'this is a string'
a_tuple = (2, 54, 13, 12, 5, 32)
longer_tup = tuple(range(1, 20))

# Test 1. With the first and the last item exchanged

assert exchange_first_last(a_string) == 'ghis is a strint'
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

# Test 2. With every other item removed

assert re_every_other(a_string) == 'ti sasrn'
assert re_every_other(a_tuple) == (2, 13, 5)

# Test 3. With the first 4 and the last 4 items removed
# and then every other item in between

assert first_last_four(a_string) == ' sas'
print(longer_tup)
assert first_last_four(longer_tup) == (5, 7, 9, 11, 13, 15)
print('Run after "assert" for Test #3')
print(first_last_four(longer_tup))

# Test 4. With the elements reversed (just slicing)

assert reverse_seq(a_string) == 'gnirts a si siht'
assert reverse_seq(a_tuple) == (32, 5, 12, 13, 54, 2)

# Test 5. With the middle third, the last third, then
# the first third in the new order
print(mid_last_first(a_string))

assert mid_last_first(a_string) == 'is a stringthis'
assert mid_last_first(a_tuple) == (13, 12, 5, 32, 2, 54)
