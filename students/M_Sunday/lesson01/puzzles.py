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

# string_times
def string_times(str, n):
    return str * n

#print(string_times('Hi', 2))
#print(string_times('Hi', 3))
#print(string_times('Hi', 1))

# front_times
def front_times(str, n):
    if len(str) > 3:
        repeat = str[0:3]
    else:
        repeat = str
    return n * repeat

#print(front_times('Chocolate', 2))
#print(front_times('Chocolate', 3))
#print(front_times('Abc', 3))

# string_bits
def string_bits(str):
    strnew = ''
    for i in range(len(str)):
        if i == 0:
            strnew += str[i]
        elif i % 2 == 0:
            strnew += str[i]
        else:
            pass
    return strnew

#print(string_bits('Hello'))
#print(string_bits('Hi'))
#print(string_bits('Heeololeo'))

# string_splosion
def string_splosion(str):
    strnew = ''
    for i in range(len(str)+1):
        strnew += str[0:i]
    return strnew

#print(string_splosion('Code'))
#print(string_splosion('abc'))
#print(string_splosion('ab'))

# last2
def last2(str):
    last = str[len(str)-2:len(str)]
    count = 0
    for i in range(len(str)-3):
        if (str[i] + str[i+1]) == last:
            count = count + 1
        else:
            pass
    return count

#print(last2('hixxhi'))
#print(last2('xaxxaxaxx'))
#print(last2('axxxaaxx'))

# array_count9
def array_count9(nums):
    count = 0
    for i in nums:
        if i == 9:
            count = count + 1
        else:
            pass
    return count

#print(array_count9([1, 2, 9]))
#print(array_count9([1, 9, 9]))
#print(array_count9([1, 9, 9, 3, 9]))

# array_front9
def array_front9(nums):
    for i in range(0, 3, 1):
        if nums[i] == 9:
            found = True
            break
        else:
            found = False
    return found

#print(array_front9([1, 2, 9, 3, 4]))
#print(array_front9([1, 2, 3, 4, 9]))
#print(array_front9([1, 2, 3, 4, 5]))

# array123
def array123(nums):
    for i in range(len(nums)-2):
        if (nums[i] == 1) and (nums[i+1] == 2) and (nums[i+2] == 3):
            found = True
            break
        else:
            found = False
    return found

#print(array123([1, 1, 2, 3, 1]))
#print(array123([1, 1, 2, 4, 1]))
#print(array123([1, 1, 2, 1, 2, 3]))