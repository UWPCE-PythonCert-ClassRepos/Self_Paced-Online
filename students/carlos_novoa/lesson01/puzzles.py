#!/usr/bin/env python

"""
Lesson1, Task 2: Puzzles
"""

# ::::: Warmup-1 ::::: #


def sleep_in(weekday, vacation):
    return(not weekday or vacation)


def monkey_trouble(a_smile, b_smile):
    return ((a_smile and b_smile) or (not a_smile and not b_smile))


def sum_double(a, b):
    return (a+b)*2 if a == b else a+b


def diff21(n):
    return (n - 21)*2 if n > 21 else 21 - n


def parrot_trouble(talking, hour):
    if (talking and hour < 7):
        return True
    elif (talking and hour > 20):
        return True
    else:
        return False


def makes10(a, b):
    return ((a == 10 or b == 10) or (a + b) == 10)


def near_hundred(n):
    return (abs(n - 100) <= 10 or abs(n - 200) <= 10)


def pos_neg(a, b, negative):
    if negative:
        return (a < 0 and b < 0)
    else:
        return ((a < 0 and b > 0) or (a > 0 and b < 0))


def not_string(str):
    if (str.split()[0] == 'not'):
        return str
    else:
        return 'not {}'.format(str)


def missing_char(str, n):
    return '{}{}'.format(str[:n], str[n+1:])


def front_back(str):
    if (len(str) > 1):
        return '{}{}{}'.format(str[-1], str[1:-1], str[0])
    else:
        return str


def front3(str):
    return str[:3] * 3


# ::::: Warmup-2 ::::: #


def string_times(str, n):
    return str * n if n > 0 else ''


def front_times(str, n):
    return str[:3]*n


def string_bits(str):
    return ''.join(list(str)[::2])


def string_splosion(str):
    result = ""
    for i in range(len(str)):
        result = result + str[:i+1]
    return result


def last2(str):
    if len(str) < 4:
        return 0
    substr = str[0:len(str)-2]
    last2 = str[len(str)-2:]
    count = 0
    for i in range(len(substr)):
        sub = str[i:i+2]
        if sub == last2:
            count = count + 1

    return count


def array_count9(nums):
    return nums.count(9)


def array_front9(nums):
    return 9 in nums[0:4]


def array123(nums):
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False


def string_match(a, b):
    shorter = min(len(a), len(b))
    count = 0

    for i in range(shorter-1):
        a_sub = a[i:i+2]
        b_sub = b[i:i+2]
        if a_sub == b_sub:
            count = count + 1
    return count


# ::::: String-1 ::::: #


def hello_name(name):
    return 'Hello ' + name + '!'


def make_abba(a, b):
    return a + b + b + a


def make_tags(tag, word):
    return '<{}>{}</{}>'.format(tag, word, tag)


def make_out_word(out, word):
    index = len(out)/2
    return out[:index] + word + out[index:]


def extra_end(str):
    return str[len(str)-2:len(str)]*3


def first_two(str):
    return str[:2]


def first_half(str):
    if(len(str) >= 2 and len(str) % 2 == 0):
        return str[:len(str) / 2]
    else:
        return str


def without_end(str):
    return str[1:-1]


def non_start(a, b):
    return a[1:]+b[1:]


def combo_string(a, b):
    short_str = a if len(a) < len(b) else b
    long_str = b if len(b) > len(a) else a
    return short_str + long_str + short_str


def left2(str):
    return str[2:]+str[0:2]


# ::::: List-1 ::::: #


def first_last6(nums):
    return (nums[0] == 6 or nums[len(nums)-1] == 6)


def same_first_last(nums):
    return (len(nums) > 0 and (nums[0] == nums[len(nums)-1]))


def make_pi():
    return [3, 1, 4]


def common_end(a, b):
    return (a[0] == b[0] or a[len(a) - 1] == b[len(b) - 1])


def sum3(nums):
    return sum(nums)


def rotate_left3(nums):
    result = list()
    for i in range(len(nums)+2):
        result.insert(i, nums[i-2])
        if (i == len(nums)-1):
            break
    return result


def reverse3(nums):
    return nums[::-1]


def max_end3(nums):
    larger = max(nums[0], nums[2])
    for i in range(len(nums)):
        nums[i] = larger
    return nums


def sum2(nums):
    return sum(nums[0:2])


def middle_way(a, b):
    return [a[1], b[1]]


def make_ends(nums):
    return [nums[0], nums[len(nums)-1]]


def has23(nums):
    return True if 2 in nums or 3 in nums else False


# ::::: Logic-1 ::::: #


def cigar_party(cigars, is_weekend):
    if (is_weekend):
        return (cigars >= 40)
    else:
        return cigars in range(40, 61)


def date_fashion(you, date):
    if (you <= 2 or date <= 2):
        return 0
    elif (you >= 8 or date >= 8):
        return 2
    else:
        return 1


def squirrel_play(temp, is_summer):
    if (is_summer):
        return temp in range(60, 101)
    else:
        return temp in range(60, 91)


def caught_speeding(speed, is_birthday):
    speed = speed-5 if is_birthday else speed
    if (speed <= 60):
        return 0
    elif (speed >= 81):
        return 2
    else:
        return 1


def sorta_sum(a, b):
    return sum([a, b]) if sum([a, b]) not in range(10, 20) else 20


def alarm_clock(day, vacation):
    if (vacation and (day == 0 or day == 6)):
        return 'off'
    elif (vacation and day in range(1, 6)):
        return '10:00'
    elif (day in range(1, 6)):
        return '7:00'
    else:
        return '10:00'


def love6(a, b):
    if (a == 6 or b == 6):
        return True
    if (abs(a-b) == 6 or a+b == 6):
        return True
    else:
        return False


def in1to10(n, outside_mode):
    if (outside_mode and (n <= 1 or n >= 10)):
        return True
    elif (not outside_mode and (n >= 1 and n <= 10)):
        return True
    else:
        return False


def near_ten(num):
    mod_10 = num % 10
    return mod_10 <= 2 or mod_10 >= 8


def make_bricks(small, big, goal):
    if (small+big*5 < goal):
        return False
    if (small < goal % 5):
        return False
    return True


def lone_sum(a, b, c):
    if (a == b == c):
        return 0
    elif (a == b):
        return c
    elif (b == c):
        return a
    elif (a == c):
        return b
    else:
        return a+b+c


def lucky_sum(a, b, c):
    ll = [a, b, c]
    l_s = 0
    for i in range(len(ll)):
        if (ll[i] == 13):
            break
        l_s = l_s+ll[i]
    return l_s


def fix_teen(n):
    if (n == 15 or n == 16):
        return n
    elif (n >= 13 and n <= 19):
        return 0
    else:
        return n


def no_teen_sum(a, b, c):
    s = 0
    for item in [a, b, c]:
        s = s + fix_teen(item)
    return s
