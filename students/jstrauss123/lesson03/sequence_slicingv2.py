# Basics of sequence slicing

# function - accept a sequence and return a copy of sequence with first and last items exchanged
def exchange_first_last(seq):
    outseq = seq[-1::] + seq[1:-1:] + seq[0:1:]
    return(outseq)
    
    
# function - accept a sequence and return every other item in sequence
def  remove_every_other_item(seq):
    outseq = seq[0:-1:2]
    return(outseq)
    
# function - accept a sequence and manipulate first and last four, return what's left every other
def  first_last_four(seq):    
    outseq = seq[4:-4]
    outseq = outseq[0:-1:2]
    return(outseq)
   
    
# function - accept sequence and return items in reverse    
def reverse_items(seq):
    outseq = seq[::-1]
    return(outseq)
    

# function - accept a sequence, return in new order: middle third/last third/first third
def  return_in_thirds(seq):    
    list_len = (len(seq) // 3)
    outseq = seq[list_len:list_len+list_len:] + seq[list_len+list_len::] + seq[0:list_len:]
    return(outseq)
    
# create string and tuple values
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)    
    

#exchange_first_last(a_string)
#exchange_first_last(a_tuple)
#remove_every_other_item(a_string)
#remove_every_other_item(a_tuple)
#first_last_four(a_string)
#first_last_four(a_tuple)
#reverse_items(a_string)
#reverse_items(a_tuple)
#return_in_thirds(a_string)
#return_in_thirds(a_tuple)




#assert tests
if __name__ == "__main__":
   # this runs only if run as a script
   print("\nRunning validation tests")
   # validate exchange_first_last function returning appropriate value
   assert exchange_first_last(a_string) == "ghis is a strint"
   assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
   assert remove_every_other_item(a_string) == "ti sasrn"
   assert remove_every_other_item(a_tuple) == (2, 13, 5)
   assert first_last_four(a_string) == " sas"
   assert first_last_four(a_tuple) == ()
   assert reverse_items(a_string) == "gnirts a si siht"
   assert reverse_items(a_tuple) == (32, 5, 12, 13, 54, 2)
   assert return_in_thirds(a_string) == "is a stringthis "
   assert return_in_thirds(a_tuple) == (13, 12, 5, 32, 2, 54)
   print("validation tests passed\n")