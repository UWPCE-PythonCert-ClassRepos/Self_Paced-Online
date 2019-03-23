# Lesson 03 answers - part 1
import math

# to call, load file in ipython: import l3_tasks.py, then call function with argument
def exchange_first_last(seq):
    seq_length = len(seq)
    if seq_length > 0:
        a_new_sequence = seq[-1:] + seq[1:-1] + seq[:1]
    else:
        a_new_sequence = seq
    return a_new_sequence

def every_other_removed(seq):
    seq_length = len(seq)
    if seq_length < 2:
        return seq
    a_new_sequence = seq[::2]
    return a_new_sequence


def first4_and_last4_every_other_removed(seq):
    seq_length = len(seq)
    if seq_length < 9:
        return []
    a_new_sequence = seq[4:-4:2]
    return a_new_sequence

def reverse_seq(seq):
        return seq[::-1]

def mid_last_first(seq):
    seq_length = len(seq)

    a_new_sequence = seq[math.floor(seq_length/3):2*math.floor(seq_length/3)] + seq[2*math.floor(seq_length/3):] + seq[:math.floor(seq_length/3)]
    return a_new_sequence

if __name__ == "__main__":
    # this will only print if run as a script
    print("running tests")
    assert exchange_first_last('this is a string') == 'ghis is a strint', "replace first and last letter"
    assert exchange_first_last((2, 54, 13, 12, 5, 32)) == (32, 54, 13, 12, 5, 2)

    assert every_other_removed('this is a string') == 'ti sasrn', "remove every other letter"

    assert first4_and_last4_every_other_removed('this is a string') == ' sas', "remove first and last four and every other"

    assert reverse_seq('this is a string') == 'gnirts a si siht', "reverse order"

    assert mid_last_first('this is a string') == 'is a stringthis ', "mid last first"
    assert mid_last_first((2, 54, 13, 12, 5, 32)) == (13, 12, 5, 32, 2, 54)

    print("the tests pass")

