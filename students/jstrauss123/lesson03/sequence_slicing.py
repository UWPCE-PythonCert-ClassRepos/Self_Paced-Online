# Basics of sequence slicing

# create string and tuple values
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

# define function - accept a sequence and return a copy of sequence with first and last items exchanged
def exchange_first_last(seq):
    first = seq[0]
    last = seq[-1]
    print("first is: ", first, " last is: ", last)
    # need to break a string apart
    for i in a_string:
        work_tuple = [",".join(seq)]
        print(work_tuple)
    # use assignment to replace first with last and last with first
    #work_tuple[0] = last
    #work_tuple[-1] = first
    #print(work_tuple)
    
    
    
    

exchange_first_last(a_string)
#exchange_first_last(a_tuple)





# assert tests
#if __name__ == "__main__":
#   # this runs only if run as a script
#   print("Running validation tests")
#   # validate exchange_first_last function returning appropriate value
#   assert exchange_first_last(a_string) == "ghis is a strint"
#   assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
#
#    print("validation tests passed")