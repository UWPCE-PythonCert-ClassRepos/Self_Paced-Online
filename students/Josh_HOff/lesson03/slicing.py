a_string = 'testing a string with words'
a_tuple = (8, 6, 7, 5, 3, 0, 9, 10, 302, 42, 39, 89, 29, 17)
a_list = ['wow', 6, 14, 'testing', 103, 'extra', 5, 10, 18, "more", 105]

def first_last(seq):
    if type(seq) is str:
        return seq[-1] + seq[1:-1] + seq[:1]
    if type(seq) is tuple:
        return (seq[-1],) + (seq[1:-1]) + (seq[:1])
    if type(seq) is list:
        seq[0], seq[-1] = seq[-1], seq[0]
        return seq

def rm_every_other(seq):
    return seq[::2]
    
def four_every_other(seq):
    return seq[4:-4:2]
    
def reversing(seq):
    return seq[::-1]
    
def thirds(seq):
    a = int(len(seq) / 3)
    print(a)
    if type(seq) is str:
        return seq[a:(a*2)] + seq[(a*2):] + seq[:a]
    if type(seq) is tuple or type(seq) is list:
        return (seq[a:(a*2)]) + (seq[(a*2):]) + (seq[:a])