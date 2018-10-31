#coding_bat_string1

def hello_name(name):
  return "Hello " + name + "!"

def make_abba(a, b):
  return a + b + b + a

def make_tags(tag, word):
  return "<" + tag + ">" + word + "</" + tag + ">"

def make_out_word(out, word):
  return out[:2] + word + out[2:]

def extra_end(str):
  return 3 * str[-2:]

def first_two(str):
  if len(str) <= 2:
    return str
  else:
    return str[:2]

def first_half(str):
  return str[:len(str)/2]

def without_end(str):
  return str[1:-1]

def combo_string(a, b):
  lena, lenb = len(a), len(b)
  if lena < lenb:
    return a + b + a
  else:
    return b + a + b

def non_start(a, b):
  return a[1:] + b[1:]

def left2(str):
  first2 = str[:2]
  return str[2:] + first2
