def exchange_first_last(seq):
    first = seq[0:1]
    last = seq[-1:]
    return last + seq[1:len(seq)-1] + first

def remove_every_other_item(seq):
    return seq[0:-1:2]

def remove_first4_last4(seq):
    return seq[4:-4]

def remove_first4_last4_every_other_item(seq):
    return remove_every_other_item(remove_first4_last4(seq))

def reverse_element(seq):
	  return seq[::-1]

# with the middle third, then last third, then the first third in the new order.
def mid_last_first(seq):
  return seq[len(seq)//3 : len(seq)*2//3] + seq[len(seq)*2//3:] + seq[0:len(seq)//3]

a_string  = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

print(exchange_first_last(a_string))
print(exchange_first_last(a_tuple))

print(remove_every_other_item(a_string))
print(remove_every_other_item(a_tuple))

print(remove_first4_last4_every_other_item(a_string))
print(reverse_element(a_string))

print(mid_last_first(a_string))
print(mid_last_first(a_tuple))
