#!/usr/bin/env python3
# #############################################################################
# Written by: Mayc4t
# March 19, 2018

# #############################################################################
def exchange_first_last(seq):
    """ Exchange the first and last item. """
    if( type(seq) is str):
        stra = seq[-1]
        for i in range(1,len(seq)-1): stra += seq[i]
        stra += seq[0]
        return stra
    else:
        new_seq = []
        new_seq.append( seq[-1] )
        for i in range (1, len(seq)-1): new_seq.append(seq[i] )
        new_seq.append( seq[0])
        if type(seq) is tuple: new_seq = tuple( new_seq)
        return new_seq

# #############################################################################
def remove_every_other(seq):
    """ Remove every other item """ 
    if(type(seq) is str): 
        new_seq = list(seq)
        del(new_seq[1:len(new_seq):2])
        stra=''
        for i in range(len(new_seq)): stra += new_seq[i]
        return stra
    else:
        new_seq = list(seq)
        del( new_seq[1:len(new_seq):2])
        if type(seq) is tuple: new_seq = tuple(new_seq)
        return( new_seq)


# #############################################################################
def remove_f4_l4_every_other(seq):
    """ Remove the first 4 and the last 4 items and then every other item in between."""
    # check if length of seg has to be at least 10
    if len( seq) <= 9:
        print("the seq has to be at last 9 items" )
        pass
    else:
        new_seq = list(seq)
        del(new_seq[0:4:1])
        del(new_seq[-1:-5:-1])
        del( new_seq[1: len(new_seq) : 2])

        if(type(seq) is str): 
            stra=''
            for i in range(len(new_seq)):stra += new_seq[i]
            return stra
        else:
            if type(seq) is tuple: new_seq = tuple(new_seq)
        
        return( new_seq)


# #############################################################################
def reverse_elements(seq):
    """ Revere order in the sequence """
    new_seq = seq[::-1]
    return (new_seq)

# #############################################################################
def reorder_mlf_third(seq):
    """ Remove the first third to the end of the sequence """
    first = seq[0:int(len(seq)/3)]
    rmd   = seq[int(len(seq)/3):len(seq)]
    return (rmd + first)

# #############################################################################
if __name__ == "__main__":
        
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    
    reorder_mlf_third(a_string)
    reorder_mlf_third(a_tuple)
    
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
    
    print ("-------------  hw3 -----------")
    print ( "5. Move the first third to the end of sequence " )
    print ("===The result===" )
    print ("\tInput :", a_string)
    print ("\tOutput:", reorder_mlf_third(a_string))
    print ("\n\tInput :", a_tuple)
    print ("\tOutput:", reorder_mlf_third(a_tuple))
    print ("\n===Assertion: Compare result with what to expect===")
    assert reorder_mlf_third(a_string) == "is a stringthis "
    assert reorder_mlf_third(a_tuple) == (13, 12, 5, 32, 2, 54)
    print ("+++Got it --- reorder_mlf_third(reverse elements : PASS\n\n\n")
    
