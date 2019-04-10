#Slicing Lab

seq = "this is a string"
tup = (2, 54, 13, 12, 5, 32)

def exchange_first_last(seq):
    first = seq[-1] 
    mid = seq[1:-1]
    last = seq[0]
    new_seq = first + mid + last 
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
   assert exchange_first_last(seq) == "ghis is a strint"
   assert other_remove(seq) == "ti sasrn"
   assert first_last_other_remove(seq) == " sas"
   assert reverse(seq) == "gnirts a si siht"
   #assert mid_last_first(seq) == "is a stringthis "
   
   #assert exchange_first_last(tup) == (32, 54, 13, 12, 5, 2)
   assert other_remove(tup) == (2, 13, 5)
   assert first_last_other_remove(tup) == ()
   assert reverse(tup) == (32, 5, 12, 13, 54, 2)
   #assert mid_last_first(tup) == (13, 12, 5, 32, 2, 54)
   
   print("Tests passed!")