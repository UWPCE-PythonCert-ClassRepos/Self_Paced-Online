# lesson01 task 2 - puzzles

# sleep_in
def sleep_in(weekday, vacation):
    if (weekday != True) or (vacation == True):
        return True
    else:
        return False

#print(sleep_in(False, False))
#print(sleep_in(True, False))
#print(sleep_in(False, True))

# monkey_trouble
def monkey_trouble(a_smile, b_smile):
    if (a_smile == True and b_smile == True) or (a_smile == False and b_smile == False):
        return True
    else:
        return False

#print(monkey_trouble(True, True))
#print(monkey_trouble(False, False))
#print(monkey_trouble(True, False))

# sum_double
def sum_double(a, b):
    if a == b:
        return 4*a
    else:
        return a + b

#print(sum_double(1, 2))
#print(sum_double(3, 2))
#print(sum_double(2, 2))

# diff21
def diff21(n):
    diff = abs(21 - n)
    if diff <= 21:
        return diff
    else:
        return 2 * diff

#print(diff21(19))
#print(diff21(10))
#print(diff21(21))