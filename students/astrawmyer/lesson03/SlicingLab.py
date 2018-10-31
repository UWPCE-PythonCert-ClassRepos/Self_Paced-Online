#Write some functions that take a sequence as an argument and return a copy of the sequence.

def exchange_first_last(seq):
    new_seq = seq[-1:] + seq[1:-1] + seq[:1]
    return new_seq


#print(exchange_first_last(seqtup))

def remove_every_other(seq):
    new_seq = seq[0:-1:2]
    return new_seq


#print(remove_every_other(seqtup))

def remove_4(seq):
    new_seq = seq[4:-4:2]
    return new_seq


def reverse(seq):
    new_seq = seq[::-1]
    return new_seq


def thirds(seq):
    length = len(seq)
    new_seq = seq[int(length/3):] + seq[0:int(length/3)]
    return new_seq

seqtup= (2, 54, 13, 12, 5, 33, 25, 58, 32, 1, 2, 3, 4, 5)
print(remove_4(seqtup))
