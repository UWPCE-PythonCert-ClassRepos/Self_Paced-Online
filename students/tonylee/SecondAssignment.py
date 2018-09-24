def exchange_first_last(seq):
    	s = list(seq)
	first = seq[0]
	last = seq[-1]
	s[0] = last
	s[-1] = first
	
	return convert_format(seq, s)

def remove_every_other_item(seq):
	s = list(seq)
        l = []
	i = 0
	while (i < len(s)):
		if i%2 != 0:
			l.append(s[i])
		i = i + 1
	
	return convert_format(seq, l)

def remove_first4_last4_every_other_item(seq):
	s = list(seq)
	del s[0:4]
	del s[len(s)-4:len(s)]
	
	return convert_format(seq, s)
	
def reverse_element(seq):
	s = list(seq)
	r = s[::-1]
	
	return convert_format(r)
	
# with the middle third, then last third, then the first third in the new order.
def mid_last_first(seq):
	s = list(seq)
	length = len(s)
	third = length/3
	
	middle = s[third:length-third]
	last = s[length-third:length]
	first = s[0:third]
	
	l = middle + last + first
	
	return convert_format(seq, l)

def convert_format(seq, value):
	if type(seq) is str:
		newString = "".join(value)
		return newString
		
	if type(seq) is tuple:	
		return tuple(value)
	return value

a_string  = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

print (exchange_first_last(a_string))
print (exchange_first_last(a_tuple))

print (remove_every_other_item(a_string))
print (remove_every_other_item(a_tuple))

print(remove_first4_last4_every_other_item(a_tuple))

print mid_last_first(a_string)
print mid_last_first(a_tuple)