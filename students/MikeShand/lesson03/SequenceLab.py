

def exchange(seq):
    return seq[-1:]+seq[1:-1]+seq[:1]

def half(seq):
    return seq[0::2]

def stubby_half(seq):
    return seq[4:-4:2]

def reverse(seq):
    return seq[::-1]

def three_way(seq):
    n=(len(seq))//3
    return seq[n:-n]+seq[-n:]+seq[:n]


test_string='012345678'
test_tuple=tuple(range(9))

assert exchange(test_string)== "812345670"
assert exchange(test_tuple)==(8,1,2,3,4,5,6,7,0)
assert half(test_string)=='02468'
assert half(test_tuple)==(0,2,4,6,8)
assert stubby_half(test_string)=='4'
assert stubby_half(test_tuple)==(4,)
assert reverse(test_string)=='876543210'
assert reverse(test_tuple)==(8,7,6,5,4,3,2,1,0)
assert three_way(test_string)=='345678012'
assert three_way(test_tuple)==(3,4,5,6,7,8,0,1,2)
