#Write some functions that take a sequence as an argument and return a copy of the sequence.

def exchange_first_last(seq):
    new_seq = seq[-1:] + seq[1:-1] + seq[:1]
    return new_seq

seqtup= (2, 54, 13, 12, 5, 32)
#print(exchange_first_last(seqtup))

def remove_every_other(seq):
    new_seq = seq[0:-1:2]
    return new_seq

seqtup= [2, 54, 13, 12, 5, 32]
print(remove_every_other(seqtup))