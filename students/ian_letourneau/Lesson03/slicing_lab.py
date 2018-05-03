## Ian Letourneau
## 4/26/2018
## A script with various sequencing functions

def exchange_first_last(seq):
    """A function to exchange the first and last entries in a sequence"""
    middle = list(seq)
    middle[0] = seq[-1]
    middle[-1] = seq[0]

    if type(seq) is str:
        return "".join(middle)
    elif type(seq) is tuple:
        return tuple(middle)
    else:
        return middle

def remove_every_other(seq):
    """A function to remove every other entry in a sequence"""
    middle = []
    for index in range(len(seq)):
        if not index%2 or index == 0:
            middle.append(seq[index])

    if type(seq) is str:
        return "".join(middle)
    elif type(seq) is tuple:
        return tuple(middle)
    else:
        return middle

def remove_four(seq):
    """A function that removes the first 4 and last four entries in a sequence,
        and then removes every other entry in the remaining sequence"""
    middle = list(seq)
    del middle[0:4]
    del middle[-4:len(seq)]

    if type(seq) is str:
        return "".join(remove_every_other(middle))
    elif type(seq) is tuple:
        return tuple(remove_every_other(middle))
    else:
        return remove_every_other(middle)

def reverse(seq):
    """A function that reverses a seq"""
    middle = list(seq)
    count = -1
    for index in range(len(seq)):
        middle[index] = seq[count]
        count -= 1

    if type(seq) is str:
        return "".join(middle)
    elif type(seq) is tuple:
        return tuple(middle)
    else:
        return middle

def thirds(seq):
    """A function that splits a sequence into thirds,
            then returns a new sequence using the last, first, and middle thirds"""
    middle = list(seq)
    one = middle[0:int(len(seq)/3)]
    two = middle[int(len(seq)/3):int(len(seq)/3*2)]
    three = middle[int(len(seq)/3*2):len(seq)]
    a_new_sequence = three + one + two

    if type(seq) is str:
        return "".join(a_new_sequence)
    elif type(seq) is tuple:
        return tuple(a_new_sequence)
    else:
        return a_new_sequence

if __name__ == '__main__':
    """A testing block to ensure all functions are operating as expected"""
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 15, 22, 63, 75, 20, 8, 12, 5, 32)
    s_third = "123456789"
    t_third = (1, 2, 3, 4, 5, 6, 7, 8, 9)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 15, 22, 63, 75, 20, 8, 12, 5, 2)

    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 22, 75, 8, 5)

    assert remove_four(a_string) == " sas"
    assert remove_four(a_tuple) == (22, 75)

    assert reverse(a_string) == "gnirts a si siht"
    assert reverse(a_tuple) == (32, 5, 12, 8, 20, 75, 63, 22, 15, 13, 54, 2)

    assert thirds(s_third) == "789123456"
    assert thirds(t_third) == (7, 8, 9, 1, 2, 3, 4, 5, 6)

    print("All tests passed my fellow coders!")