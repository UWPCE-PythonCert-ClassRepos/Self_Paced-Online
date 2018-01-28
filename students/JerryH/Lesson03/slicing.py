def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]

def every_other(seq):
    return seq[::2]

def remove_first_last(seq):
    return seq[4:-4:2]

def reverse_elements(seq):
    return seq[-1::-1]

def mid_last_first(seq):
    return seq[(len(seq)//2)+2:(len(seq)//2)+3] + seq[-3:-2] + seq[2:3]
