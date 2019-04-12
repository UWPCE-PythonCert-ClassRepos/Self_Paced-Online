#Slicing Lab

s = "this is a string"
t = (2, 54, 13, 12, 5, 32, 24, 78, 89, 64, 4)
l = [2, 54, 13, 12, 5, 32, 24, 78, 89, 64, 4]

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
    new_seq = seq[::-1]
    return new_seq

def last_first_mid(seq):
    seq_len = int(len(seq) / 3)
    
    first = seq[0:seq_len]
    mid = seq[seq_len:-seq_len]
    last = seq[-seq_len::]
    new_seq = last + first + mid
    return new_seq

if __name__ == "__main__":
    #Run some tests
    assert exchange_first_last(s) == "ghis is a strint"
    assert other_remove(s) == "ti sasrn"
    assert first_last_other_remove(s) == " sas"
    assert reverse(s) == "gnirts a si siht"
    assert last_first_mid(s) == "tringthis is a s"
    
    assert exchange_first_last(t) == (4, 54, 13, 12, 5, 32, 24, 78, 89, 64, 2)
    assert other_remove(t) == (2, 13, 5, 24, 89, 4)
    assert first_last_other_remove(t) == (5, 24)
    assert reverse(t) == (4, 64, 89, 78, 24, 32, 5, 12, 13, 54, 2)
    assert last_first_mid(t) == (89, 64, 4, 2, 54, 13, 12, 5, 32, 24, 78)

    assert exchange_first_last(l) == [4, 54, 13, 12, 5, 32, 24, 78, 89, 64, 2]
    assert other_remove(l) == [2, 13, 5, 24, 89, 4]
    assert first_last_other_remove(l) == [5, 24]
    assert reverse(l) == [4, 64, 89, 78, 24, 32, 5, 12, 13, 54, 2]
    assert last_first_mid(l) == [89, 64, 4, 2, 54, 13, 12, 5, 32, 24, 78]   
    
    print("Tests passed!")