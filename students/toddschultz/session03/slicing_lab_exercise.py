#with the first and last items exchanged.
def exchanged(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]

#with every other item removed.
def every_other(seq):
    return seq[::2] 

#with the first 4 and the last 4 items removed, and then every other item in between.
def remove_fours_every_other(seq):
    return seq[4:-4:2] 

#with the elements reversed (just with slicing).
def reverse(seq):
    return seq[::-1] 

#with the middle third, then last third, then the first third in the new order.
def thirds_list(seq):
    return seq[3:6] + seq[6:9] + seq[0:3]
def thirds_string_len(seq):
    return seq[int((len(seq) * .34)):int((len(seq) * .67))] + seq[int((len(seq) * .67)):len(seq)] + seq[:int((len(seq) * .34))]

#asserts
assert exchanged("abcdefghijklmnopqrstuvwxyz") == "zbcdefghijklmnopqrstuvwxya"
assert every_other("123456789") == ("13579")
assert remove_fours_every_other("----123456789___") == "1357"
assert reverse("123456789") == "987654321"
assert thirds_list("123456789") == "456789123"





