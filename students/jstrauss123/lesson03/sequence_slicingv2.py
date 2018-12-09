# Basics of sequence slicing

# function - accept a sequence and return a copy of sequence with first and last items exchanged
def exchange_first_last(seq):
    work_list = seq
    work_list1 = work_list[-1::] 
    work_list2 = work_list[1:-1:]
    work_list3 = work_list[0:1:]
    outseq = work_list1 + work_list2 + work_list3
    return(outseq)
    
    
# function - accept a sequence and return every other item in sequence
def  remove_every_other_item(seq):
    work_list = seq
    work_list1 = work_list[0:-1:2]
    outseq = work_list1
    return(outseq)
    
# function - accept a sequence and manipulate first and last four, return what's left every other
def  first_last_four(seq):    
    work_list = list(seq)
    # remove first and last four items from list
    work_list = work_list[4:-4]
    # remove every other from list
    work_list = work_list[0:-1:2]
    if type(seq) == str:
        # convert list back to string
        outseq = str("".join(work_list))
    elif type(seq) == tuple:
        outseq = tuple(work_list)
    else:
        outseq = work_list
    return(outseq)
   
    
# function - accept sequence and return items in reverse    
def reverse_items(seq):
    work_list = list(seq)
    # reverse list
    work_list = work_list[::-1]
    if type(seq) == str:
        # convert list back to string
        outseq = str("".join(work_list))
    elif type(seq) == tuple:
        outseq = tuple(work_list)
    else:
        outseq = work_list
    return(outseq)
    

# function - accept a sequence, return in new order: middle third/last third/first third
def  return_in_thirds(seq):    
    work_list = list(seq)
    # determine length of list and divide by 3
    list_len = (len(work_list) // 3)
    # assign first third to list1 and remove from orig list
    work_list1 = work_list[0:list_len]
    work_list = work_list[list_len:]
    # assign next third to list2 and remove from orig list
    work_list2 = work_list[0:list_len]
    work_list = work_list[list_len:]
    # assign the remainder to list3
    work_list3 = work_list
    # assign thirds by middle (2), last (3) and first (1)
    work_list = work_list2 + work_list3 + work_list1
    outseq = work_list
    if type(seq) == str:
        # convert list back to string
        outseq = str("".join(work_list))
    elif type(seq) == tuple:
        # convert list back to tuple
        outseq = tuple(work_list)
    else:
        outseq = work_list
    return(outseq)
    
# create string and tuple values
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)    
    

#exchange_first_last(a_string)
#exchange_first_last(a_tuple)
remove_every_other_item(a_string)
remove_every_other_item(a_tuple)
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