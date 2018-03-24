# Goal
# 
# 
# Get the basics of sequence slicing down.
# 
# Tasks
# 
# Write some functions that take a sequence as an argument, and return a copy of that sequence:
# 
# with the elements reversed (just with slicing).
# with the middle third, then last third, then the first third in the new order.
# NOTE: These should work with ANY sequence – but you can use strings to test, if you like.
# 
# Your functions should look like:
# 
# def exchange_first_last(seq):
#     return a_new_sequence
# Tests:
# 
# a_string = "this is a string"
# a_tuple = (2, 54, 13, 12, 5, 32)
# 
#assert exchange_first_last(a_string) == "ghis is a strint"
#assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

# ################################################################
# with the first and last items exchanged.
def exchange_first_last(seq):
    if( type(seq) is str):
        stra = seq[-1]
        for i in range(1,len(seq)-1):
            stra += seq[i]
        stra += seq[0]
        return stra
    else:
        new_seq = []
        new_seq.append( seq[-1] )
        for i in range (1, len(seq)-1): new_seq.append(seq[i] )
        new_seq.append( seq[0])
        if type(seq) is tuple: new_seq = tuple( new_seq)

        return new_seq

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

print ("-------------  hw3 -----------")
print ( "1. Exchange first for last" )
print ("===The result===" )
print ("\tInput :", a_string)
print ("\tOutput:", exchange_first_last(a_string))
print ("\n\tInput :", a_tuple)
print ("\tOutput:", exchange_first_last(a_tuple))
print ("\n===Assertion: Compare result with what to expect===")
assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
print ("+++Got it --- exchange_first_last : PASS\n\n\n")



# ################################################################
# with every other item removed.
def remove_every_other(seq):
    if(type(seq) is str): 
        new_seq = list(seq)
        #print (new_seq)
        del(new_seq[1:len(new_seq):2])
        #print (new_seq) 
        stra=''
        for i in range(len(new_seq)): stra += new_seq[i]
        #print(stra)
        return stra
    else:
        new_seq = list(seq)
        #print ("\t\t:",new_seq)
        del( new_seq[1:len(new_seq):2])
        #print ("\t\t:",new_seq)
        if type(seq) is tuple:
            new_seq = tuple(new_seq)
        #print ("\t\tTuple:", new_seq)
        return( new_seq)

print ("-------------  hw3 -----------")
print ( "2. remove_every_otherReverse the sequence " )
print ("===The result===" )
print ("\tInput :", a_string)
print ("\tOutput:", remove_every_other(a_string))
print ("\n\tInput :", a_tuple)
print ("\tOutput:", remove_every_other(a_tuple))
print ("\n===Assertion: Compare result with what to expect===")
assert remove_every_other(a_string) == "ti sasrn"
assert remove_every_other(a_tuple) ==  (2, 13, 5)
print ("+++Got it --- remove_every_other: PASS\n\n\n")




# ################################################################
#with the first 4 and the last 4 items removed, and then every other item in between.
def remove_f4_l4_every_other(seq):
    # check if length of seg has to be at least 10
    if len( seq) <= 9:
        print("the seq has to be at last 9 items" )
        pass
    else:
        new_seq = list(seq)
        # delete first 4
        del(new_seq[0:4:1])
        #print( new_seq)

        # delete last 4
        del(new_seq[-1:-5:-1])
        #print (new_seq) 
        
        # remove every other
        del( new_seq[1: len(new_seq) : 2])
        #print (new_seq)

        if(type(seq) is str): 
            stra=''
            for i in range(len(new_seq)):stra += new_seq[i]
            return stra
        else:
            if type(seq) is tuple: new_seq = tuple(new_seq)
        
        return( new_seq)

cur_tuple = a_tuple*2
print ("-------------  hw3 -----------")
print ( "3. remove_f4_l4_every_other " )
print ("===The result===" )
print ("\tInput :", a_string)
print ("\tOutput:", remove_f4_l4_every_other(a_string))
print ("\n\tInput :", a_tuple)
print ("\tOutput:",  remove_f4_l4_every_other(a_tuple * 2))
print ("\n===Assertion: Compare result with what to expect===")
assert remove_f4_l4_every_other(a_string)== " sas"
assert remove_f4_l4_every_other(a_tuple*2) ==  (5, 2)
print ("+++Got it --- remove_f4_l4_every_other: PASS\n\n\n")

#print ("\n\tAssertion: got here, remove first 4, last 4 and every other: ")
#print("\n\n\n")
#['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 's', 't', 'r', 'i', 'n', 'g']
#[                  , ' ', 'i', 's', ' ', 'a', ' ', 's', 't', 'r', 'i', 'n', 'g']

#['                 , ' ', 'i', 's', ' ', 'a', ' ', 's', 't',                   ]
#['                 , ' ',      's',      'a',      `'s',                   ]

#['                 , ' ',      's',      'a',      `'s',                   ]
#['                 , ' sas',                   ]
#" st"

# ################################################################
# with the first and last items exchanged.
def reverse_elements(seq):
    new_seq = seq[::-1]
    return (new_seq)

print ("-------------  hw3 -----------")
print ( "4. Reverse the sequence " )
print ("===The result===" )
print ("\tInput :", a_string)
print ("\tOutput:", reverse_elements(a_string))
print ("\n\tInput :", a_tuple)
print ("\tOutput:", reverse_elements(a_tuple))
print ("\n===Assertion: Compare result with what to expect===")
assert reverse_elements(a_string) == "gnirts a si siht"
assert reverse_elements(a_tuple) == (32, 5, 12, 13, 54, 2)
print ("+++Got it --- reverse elements : PASS\n\n\n")


# ################################################################
#with the middle third, then last third, then the first third in the new order.
