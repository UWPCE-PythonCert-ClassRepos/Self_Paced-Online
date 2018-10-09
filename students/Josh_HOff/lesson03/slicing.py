a_string = 'testing a string with words'
a_tuple = (8, 6, 7, 5, 3, 0, 9, 10, 302, 42, 39, 89, 29, 17)
a_list = ['wow', 6, 14, 'testing', 103, 'extra', 5, 10, 18, "more", 105]

def first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]

def rm_every_other(seq):
    return seq[::2]
    
def four_every_other(seq):
    return seq[4:-4:2]
    
def reversing(seq):
    return seq[::-1]
    
def thirds(seq):
    a = int(len(seq) / 3)
    return seq[a:(a*2)] + seq[(a*2):] + seq[:a]
    
assert first_last(a_string) == 'sesting a string with wordt'
assert first_last(a_tuple) == (17, 6, 7, 5, 3, 0, 9, 10, 302, 42, 39, 89, 29, 8)
assert first_last(a_list) == [105, 6, 14, 'testing', 103, 'extra', 5, 10, 18, "more", 'wow']
        
assert rm_every_other(a_string) == 'tsigasrn ihwrs'
assert rm_every_other(a_tuple) == (8, 7, 3, 9, 302, 39, 29)
assert rm_every_other(a_list) == ['wow', 14, 103, 5, 18, 105]

assert four_every_other(a_string) == 'igasrn ihw'
assert four_every_other(a_tuple) == (3, 9, 302)
assert four_every_other(a_list) == [103, 5]

assert reversing(a_string) == 'sdrow htiw gnirts a gnitset'
assert reversing(a_tuple) == (17, 29, 89, 39, 42, 302, 10, 9, 0, 3, 5, 7, 6, 8)
assert reversing(a_list) == [105, 'more', 18, 10, 5, 'extra', 103, 'testing', 14, 6, 'wow']

assert thirds(a_string) == ' string with wordstesting a'
assert thirds(a_tuple) == (3, 0, 9, 10, 302, 42, 39, 89, 29, 17, 8, 6, 7, 5)
assert thirds(a_list) == ['testing', 103, 'extra', 5, 10, 18, "more", 105, 'wow', 6, 14]