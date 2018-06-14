# slicing_sequence.py implements the Lesson 3 - Slicing Lab Exercise assignment from UWPCE Python Programming

intro = '''UWPCE Python Programming: Lesson 3 Assignment -- Slicing Lab Exercise
Functions that take a sequence as an argument then return a copy of that sequence
with modifications:
1. exchange_first_last(seq): the first and last items exchanged
2. remove_alternate_item(seq): every other item removed
3. remove_first_last_4_alternate_item(seq): the first 4 and the last 4 items removed, and then every other item in between
4. reverse_slice(seq): the elements reversed (just with slicing)
5. mid_last_first(seq): the middle third, then last third, then the first third in the new order
'''
print(intro)

# seq = ["Four", "score", "and", "seven", "years", "ago"]
# seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# seq = ("Four score and seven years ago")
# print("Test sequence: seq = ", seq)


def exchange_first_last(seq):
    return seq[-1:]+seq[1:-1]+seq[:1]

def remove_alternate_item(seq):
    return seq[0:len(seq)-1:2]

def remove_first_last_4_alternate_item(seq):
    return seq[4:-4:2]

def reverse_slice(seq):
    return seq[::-1]

def mid_last_first(seq):
    return seq[len(seq)//3:-len(seq)//3] + seq[-len(seq)//3:] + seq[:len(seq)//3]

'''TESTS'''

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

assert remove_alternate_item(a_string) == "ti sasrn"
assert remove_alternate_item(a_tuple) == (2, 13, 5)

assert remove_first_last_4_alternate_item(a_string) == " sas"
assert remove_first_last_4_alternate_item(a_tuple) == ()

assert reverse_slice(a_string) == "gnirts a si siht"
assert reverse_slice(a_tuple) == (32, 5, 12, 13, 54, 2)

assert mid_last_first(a_string) == "is a stringthis "
assert mid_last_first(a_tuple) == (13, 12, 5, 32, 2, 54)
