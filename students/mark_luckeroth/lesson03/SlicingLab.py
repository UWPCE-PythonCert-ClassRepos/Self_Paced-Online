def exchange_first_last(seq):
    if len(seq) == 1:
        return seq
    else:
        return seq[-1:] + seq[1:-1] + seq[:1]

def everyother(seq):
    return seq[::2]

def middle_everyother(seq):
    return seq[4:-4:2]

def reverse(seq):
    return seq[::-1]

def mid_last_first(seq):
    n = len(seq)//3
    return seq[n:] + seq[:n]

#Test Block
strg = "This is a string"
l = ['one', 'two','three','4','5','6','7','8','9','0','twenty']
tup = (1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,15,15,15,15)

assert exchange_first_last(strg) == 'ghis is a strinT'
assert everyother(strg) == 'Ti sasrn'
assert middle_everyother(strg) == ' sas'
assert reverse(l) == ['twenty', '0', '9', '8', '7', '6', '5', '4', 'three', 'two', 'one']
assert mid_last_first(tup) == (7, 8, 9, 0, 11, 12, 13, 14, 15, 15, 15, 15, 15, 1, 2, 3, 4, 5, 6)
