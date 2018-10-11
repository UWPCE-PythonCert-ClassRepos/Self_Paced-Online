
def exchange_first_last(seq):
    '''Exchanges first and last items. returns new string'''
    return seq[-1:] + seq[1:-1] + seq[0:1]


def every_other_item(seq):
    """ returns the sequence with every other item removed"""
    return seq[0 : len(seq) :2]


def first_last_four_removed(seq):
    """returns sequence with first and last 4 items removed and display every other letter"""
    return seq[4:-4:2]

def reverse_sequence(seq):
    """returns the sequence in reverse using slicing"""
    return seq[::-1]

def middle_last_first(seq):
    one_third = int(len(seq)/3) 
    first = seq[0:one_third]
    middle = seq[one_third: int(one_third*2)]
    last = seq[int(one_third*2):]
    return middle + last + first


if __name__ == '__main__':
     
    a_string = "If it ain't broke, don't fix it"
    a_tuple = (1,2,3,4,5,6,7,8,9,10)

    assert(exchange_first_last(a_string))=="tf it ain't broke, don't fix iI"
   

    assert (every_other_item(a_string)) == "I tantboe o' i t"
    

    assert (first_last_four_removed(a_string)) == "tantboe o' i"
   

    assert (middle_last_first(a_string)) == "t broke, don't fix itIf it ain'"
    
    print("testing complete")