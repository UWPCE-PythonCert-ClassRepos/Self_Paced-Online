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

# parrot_trouble
def parrot_trouble(talking, hour):
    if (talking == True) and ((hour < 7) or (hour > 20)):
        return True
    else:
        return False

#print(parrot_trouble(True,6))
#print(parrot_trouble(True,7))
#print(parrot_trouble(False,6))

# makes10
def makes10(a, b):
    if ((a == 10) or (b == 10)) or (a + b == 10):
        return True
    else:
        return False

#print(makes10(9, 10))
#print(makes10(9, 9))
#print(makes10(1, 9))

# near_hundred
def near_hundred(n):
    if (abs(100-n) <= 10) or (abs(200-n) <= 10):
        return True
    else:
        return False

#print(near_hundred(93))
#print(near_hundred(90))
#print(near_hundred(89))

# pos_neg
def pos_neg(a, b, negative):
    if negative == True:
        if (a < 0) and (b < 0):
            return True
        else:
            return False
    else:
        if ((a < 0) and (b > 0)) or ((a > 0) and (b < 0)):
            return True
        else:
            return False

#print(pos_neg(1, -1, False))
#print(pos_neg(-1, 1, False))
#print(pos_neg(-4, -5, True))

# not_string
def not_string(str):
    if str[0:3] != 'not':
        result = 'not ' + str
    else:
        result = str
    return result

#print(not_string('candy'))
#print(not_string('x'))
#print(not_string('not bad'))

# missing_char
def missing_Char(str, n):
    return str[0:n] + str[n+1:len(str)]

#print(missing_Char('kitten', 1))
#print(missing_Char('kitten', 0))
#print(missing_Char('kitten', 4))

# front_back
def front_back(str):
    if len(str) > 1:
        return str[len(str)-1] + str[1:len(str)-1] + str[0]
    else:
        return str

#print(front_back('code'))
#print(front_back('a'))
#print(front_back('ab'))

# front3
def front3(str):
    if len(str) > 3:
        repeat = str[0:3]
    else:
        repeat = str
    return 3 * repeat

#print(front3('Java'))
#print(front3('Chcolate'))
#print(front3('ac'))