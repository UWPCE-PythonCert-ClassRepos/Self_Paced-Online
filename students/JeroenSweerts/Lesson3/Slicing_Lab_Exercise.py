a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
food = ['spam', 'eggs', 'ham']




def exchange_first_last(seq):
    """the first and last items exchanged"""
    tipe = type(seq)
    seq = list(seq)
    first = seq[0]
    last = seq[-1]
    a_new_sequence = seq
    a_new_sequence[0] = last
    a_new_sequence[-1] = first
    if tipe == str:
        return ''.join(map(str, a_new_sequence))
    elif tipe == tuple:
        return tuple(a_new_sequence)
    else:
        return a_new_sequence

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert exchange_first_last(food) == ['ham', 'eggs', 'spam']

########################################################################################
def every_other(seq):
    """every other item removed"""
    tipe = type(seq)
    seq = list(seq)
    for i in range(1,len(seq)):
        try:
            del seq[i]
        except:
            break
    if tipe == str:
        return ''.join(map(str, seq))
    elif tipe == tuple:
        return tuple(seq)
    else:
        return seq

assert every_other(a_string) == "ti sasrn"
assert every_other(a_tuple) == (2, 13, 5)
assert every_other(food) == ['spam', 'ham']
#############################################################################################
def f4l4(seq):
    """the first 4 and the last 4 items removed, and then every other item in between"""
    tipe = type(seq)
    seq = list(seq)
    del seq[:4]
    del seq[-4:]
    seq = every_other(seq)
    if tipe == str:
        return ''.join(map(str, seq))
    elif tipe == tuple:
        return tuple(seq)
    else:
        return seq
assert f4l4(range(20)) == [4, 6, 8, 10, 12, 14]

################################################################################################
def reverse(seq):
    """the elements reversed (just with slicing)"""
    tipe = type(seq)
    seq = list(seq)
    seq = seq[::-1]
    if tipe == str:
        return ''.join(map(str, seq))
    elif tipe == tuple:
        return tuple(seq)
    else:
        return seq

assert reverse(a_string) == 'gnirts a si siht'
assert reverse(range(20)) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
#########################################################################################################
def mlf_third(seq):
    """the middle third, then last third, then the first third in the new order"""
    tipe = type(seq)
    seq = list(seq)
    first_third = seq[:int(len(seq)/3)]
    middle_third = seq[int(len(seq)/3):2*int(len(seq)/3)]
    print(middle_third)
    last_third = seq[int(2*int(len(seq)/3)):]
    seq = []
    for el in middle_third:
        seq.append(el)
    for el in last_third:
        seq.append(el)
    for el in first_third:
        seq.append(el)

    if tipe == str:
        return ''.join(map(str, seq))
    elif tipe == tuple:
        return tuple(seq)
    else:
        return seq

assert mlf_third(range(9)) == [3, 4, 5, 6, 7, 8, 0, 1, 2]
assert mlf_third(a_string) == "is a stringthis "


print(exchange_first_last(a_string))
print(exchange_first_last(a_tuple))
print(exchange_first_last(food))
print(exchange_first_last(range(10)))

print(every_other(a_string))
print(every_other(a_tuple))
print(every_other(food))
print(every_other(range(10)))

print(f4l4(a_string))
print(f4l4(a_tuple))
print(f4l4(food))
print(f4l4(range(20)))

print(reverse(a_string))
print(reverse(a_tuple))
print(reverse(food))
print(reverse(range(20)))

print((mlf_third(range(9))))
print((mlf_third(a_string)))
