def exchange_first_last(seq):
    return seq[-1:]+seq[1:-1]+seq[0:1]

def remove_every_other(seq):
    return seq[::2]

def remove_first_last_4_then_every_other(seq):
    return seq[4:-4:2]

def reverse(seq):
    return seq[::-1]

def mid_last_first(seq):
    n=int(len(seq)/3)
    return seq[n:n*2]+seq[n*2:]+seq[:n]

if __name__ == "__main__":
    a_string = "this is a string"
    a_tuple = (2,54,13,12,5,32)
    a_list = [1,2,3,4,5,6,7,8,9,10]

    print("Test: Exchange first and last item",end='...')
    assert exchange_first_last(a_string)=="ghis is a strint"
    assert exchange_first_last(a_tuple)==(32,54,13,12,5,2)
    assert exchange_first_last(a_list)==[10,2,3,4,5,6,7,8,9,1]
    print("passed")

    print("Test: Remove every other item",end='...')
    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 5)
    assert remove_every_other(a_list) == [1, 3, 5, 7, 9]
    print("passed")

    print("Test: Remove first and last 4 then every other item",end='...')
    assert remove_first_last_4_then_every_other(a_string)==" sas"
    assert remove_first_last_4_then_every_other(a_tuple)==()
    assert remove_first_last_4_then_every_other(a_list)==[5]
    print("passed")

    print("Test: Reverse items",end='...')
    assert reverse(a_string) == "gnirts a si siht"
    assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert reverse(a_list) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("passed")

    print("Test: Middle third, last third, first third",end='...')
    assert mid_last_first(a_string) == "is a stringthis "
    assert mid_last_first(a_tuple) == (13, 12, 5, 32, 2, 54)
    assert mid_last_first(a_list) == [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
    print("passed")
