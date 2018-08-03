#uw python 210
#lesson 03
#max anderson

#slicing lab

def switch_firstlast(seq):

    return seq[-1:] + seq[1:len(seq)-1] + seq[0:1]

def remove_alternating(seq):

    return seq[0:len(seq):2]

def alternating_mid(seq):

    return seq[4:len(seq)-4:2]

def reverses(seq):

    return seq[::-1]

def third_order(seq):

    a = len(seq)//3

    return seq[a:] + seq[:a]

if __name__ == '__main__':

    astring = 'this is a string'
    atuple = (2, 55, 33, 66, 23, 77, 99, 123)

    print()
    print('Running Tests...')

    assert switch_firstlast(astring) == 'ghis is a strint'
    assert switch_firstlast(atuple) == (123, 55, 33, 66, 23, 77, 99, 2)

    assert remove_alternating(astring) == 'ti sasrn'
    assert remove_alternating(atuple) == (2, 33, 23, 99)

    assert alternating_mid(astring) == ' sas'
    assert alternating_mid(atuple) ==  ()

    assert reverses(astring) == 'gnirts a si siht'
    assert reverses(atuple) == (123, 99, 77, 23, 66, 33, 55, 2)

    assert third_order(astring) == 'is a stringthis '
    assert third_order(atuple) == (33, 66, 23, 77, 99, 123, 2, 55)


    print('All Tests Passed.')