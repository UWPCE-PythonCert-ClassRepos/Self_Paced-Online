# Basics of sequence slicing

# create string and tuple values
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

# define function - accept a sequence and return a copy of sequence with first and last items exchanged
def exchange_first_last(seq):
    # assign first and last value
    first = seq[0]
    last = seq[-1]
    # create a working list
    work_list = list(seq)
    # assign first to last and last to first value
    work_list[0] = last
    work_list[-1] = first
    # test seq type if str convert back to str
    if type(seq) == str:
        # convert list back to string
        outseq = str("".join(work_list))
    else:
        outseq = work_list
    print(outseq)
    
    
    
    
    
    

exchange_first_last(a_string)
exchange_first_last(a_tuple)





# assert tests
#if __name__ == "__main__":
#   # this runs only if run as a script
#   print("Running validation tests")
#   # validate exchange_first_last function returning appropriate value
#   assert exchange_first_last(a_string) == "ghis is a strint"
#   assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
#
#    print("validation tests passed")