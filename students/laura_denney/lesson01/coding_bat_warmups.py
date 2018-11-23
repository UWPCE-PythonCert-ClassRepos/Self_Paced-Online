def sleep_in(weekday, vacation):
  if vacation is True:
    return True
  elif weekday is False:
    return True
  else:
    return False

def monkey_trouble(a_smile, b_smile):
  if a_smile == b_smile:
    return True
  else:
    return False

def sum_double(a, b):
  if a == b:
    return 2*(a +b)
  else:
    return a + b

def diff21(n):
  if n>21:
    return 2 *abs(21-n)
  else:
    return abs(21-n)

def parrot_trouble(talking, hour):
  if (hour < 7 or hour > 20) and talking is True:
    return True
  else:
    return False

def makes10(a, b):
  if a == 10 or b == 10:
    return True
  elif a + b == 10:
    return True
  else:
    return False

def near_hundred(n):
  if abs(n - 100) <= 10:
    return True
  elif abs(n - 200) <= 10:
    return True
  else: return False

def pos_neg(a, b, negative):
  if negative is True:
    if (a < 0 and b < 0):
      return True
    else: return False
  elif a < 0 and b > 0:
    return True
  elif a > 0 and b < 0:
    return True
  else:
    return False

def not_string(str):
  if str[:3]=="not":
    return str
  else:
    return "not " + str

def missing_char(str, n):
  return str[:n] + str[n+1:]

def front_back(str):
  if len(str) <=1:
    return str
  first = str[0]
  last = str[len(str)-1]
  return last + str[1:len(str)-1] + first

def front3(str):
  if len(str) <=3:
    return str*3
  else: return str[:3]*3

def string_times(str, n):
  return str * n

def front_times(str, n):
  if len(str) <=3:
    return str*n
  else: return str[:3]*n

def string_bits(str):
  newstr = ""
  for x in range(0, len(str)):
    if x % 2 == 0:
      newstr += str[x]
  return newstr

def string_splosion(str):
  newstr = ""
  for i in range(0,len(str)+1):
    newstr+= str[:i]
  return newstr

def last2(str):
  lasttwo=str[-2:]
  count = 0
  for x in range(0,len(str)-2):
    if str[x:x+2]== lasttwo:
      count+=1
  return count

def array_count9(nums):
  count = 0
  for x in nums:
    if x == 9:
      count+=1
  return count

def array_front9(nums):
  if len(nums) <= 4:
    return 9 in nums
  elif 9 in nums[:4]:
    return True
  else: return False

def array123(nums):
  for x in range(0,len(nums)):
    lst = nums[x:x+3]
    if lst == [1,2,3]:
      return True
  return False

def string_match(a, b):
  count = 0
  for x in range(0,min(len(a), len(b))-1):
    if a[x:x+2] == b[x:x+2]:
      count +=1
  return count