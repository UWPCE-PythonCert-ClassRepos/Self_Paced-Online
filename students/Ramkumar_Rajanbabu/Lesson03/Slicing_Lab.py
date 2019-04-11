#Slicing Lab

s = "this is a string"
t = (2, 54, 13, 12, 5, 32)
l = [2, 54, 13, 12, 5, 32]

def exchange_first_last(seq):
    if seq == tuple(seq):
        first = seq[0],
        mid = seq[1:-1]
        last = seq[-1],
    elif seq == list(seq):
        first = [seq[0]]
        mid = seq[1:-1]
        last = [seq[-1]]
    else:
        first = seq[0]
        mid = seq[1:-1]
        last = seq[-1]
    new_seq = last + mid + first 
    return new_seq

def other_remove(seq):
    new_seq = seq[::2]
    return new_seq

def first_last_other_remove(seq):
    new_seq = seq[4:-4:2]
    return new_seq

def reverse(seq):
    a_new_seq = seq[::-1]
    return a_new_seq

def mid_last_first(seq):
    pass

if __name__ == "__main__":
    #Run some tests
    assert exchange_first_last(s) == "ghis is a strint"
    assert other_remove(s) == "ti sasrn"
    assert first_last_other_remove(s) == " sas"
    assert reverse(s) == "gnirts a si siht"
    #assert mid_last_first(s) == "is a sthis "
    
    assert exchange_first_last(t) == (32, 54, 13, 12, 5, 2)
    assert other_remove(t) == (2, 13, 5)
    assert first_last_other_remove(t) == ()
    assert reverse(t) == (32, 5, 12, 13, 54, 2)
    #assert mid_last_first(t) == (13, 12, 5, 32, 2, 54)

    assert exchange_first_last(l) == [32, 54, 13, 12, 5, 2]
    assert other_remove(l) == [2, 13, 5]
    assert first_last_other_remove(l) == []
    assert reverse(l) == [32, 5, 12, 13, 54, 2]
    #assert mid_last_first(l) == [13, 12, 5, 32, 2, 54]    
    
    print("Tests passed!")