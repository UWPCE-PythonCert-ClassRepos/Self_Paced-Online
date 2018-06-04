# Lesson 3 - Slicing
# Randy Kline

a_string = "abcdefghijklmnopqrstuvwxyz"
a_tuple = (13, 12, 5, 32, 2, 54);

def exchange_first_last(seq):
  seq_first = seq[0]
  seq_middle = seq[1:-1]
  seq_last = seq[-1]
  if type(seq) is str:
    a_new_sequence = (seq_last+seq_middle+seq_first)
    return a_new_sequence
  else:
    a_new_sequence = (seq_last,seq_middle,seq_first)
  return a_new_sequence

def every_other(seq):
  a_new_sequence = seq[::2]  
  return a_new_sequence

def first4last4(seq):
  a_new_sequence = seq[4:-4:2]  
  return a_new_sequence

def reverse(seq):
  a_new_sequence = seq[::-1]  
  return a_new_sequence

def mid_last_first(seq):
  if (len(seq) % 3 == 0):
    third_len = (len(seq) // 3)
  else:
    third_len = (len(seq) // 3 + 1)
  a_new_sequence = seq[third_len:-third_len] + seq[-third_len:] + seq[:third_len]
  return a_new_sequence

result = exchange_first_last(a_string)
print("\n" + "This is exchange_first_last on a string " + str(result))
result = exchange_first_last(a_tuple)
print("\n" + "This is exchange_first_last on a tuple " + str(result))
result = every_other(a_string)
print("\n" + "This is every_other on a string " + str(result))
result = every_other(a_tuple)
print("\n" + "This is every_other on a tuple " + str(result))
result = first4last4(a_string)
print("\n" + "This is first4last4 on a string " + str(result))
result = first4last4(a_tuple)
print("\n" + "This is first4last4 on a tuple " + str(result))
result = reverse(a_string)
print("\n" + "This is reverse on a string " + str(result))
result = reverse(a_tuple)
print("\n" + "This is reverse on a tuple " + str(result))
result = mid_last_first(a_string)
print("\n" + "This is mid_last_first on a string " + str(result))
result = mid_last_first(a_tuple)
print("\n" + "This is mid_last_first on a tuple " + str(result))
