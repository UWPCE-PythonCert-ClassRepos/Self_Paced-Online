# Write some functions that take a sequence as an argument, and return a copy of that sequence:
#
#     with the first and last items exchanged.
#     with every other item removed.
#     with the first 4 and the last 4 items removed, and then every other item in between.
#     with the elements reversed (just with slicing).
#     with the middle third, then last third, then the first third in the new order.
#


def exchange_first_last(seq):
    """Invert the first and last element from a sequence"""
    if len(seq) > 1:
        if type(seq) is tuple:
            last_first = (seq[-1], *seq[1:-2], seq[0])
            print(last_first)
        elif type(seq) is str:
            last_first = seq[-1] + seq[1:-2] + seq[0]
            print(last_first)
        elif type(seq) is list:
            last_first = [seq[-1], *seq[1:-2], seq[0]]
            print(last_first)
    else:
        print(seq)


def every_other_remove(seq):
    """Remove every other element from a sequence"""
    if len(seq) > 1:
        if type(seq) is tuple:
            last_first = (seq[::2])
            print(last_first)
        elif type(seq) is str:
            last_first = seq[::2]
            print(last_first)
        elif type(seq) is list:
            last_first = seq[::2]
            print(last_first)
    else:
        print(seq)


def f4_l4_every_other_remove(seq):
    """Remove first 4 and last 4 and remove every other item in between"""
    if len(seq) > 1:
        if type(seq) is tuple:
            f4_l4 = (seq[4:-4:2])
            print(f4_l4)
        elif type(seq) is str:
            f4_l4 = seq[4:-4:2]
            print(f4_l4)
        elif type(seq) is list:
            f4_l4 = [seq[4:-4:2]]
            print(f4_l4)
    else:
        print(seq)


def every_other_remove(seq):
    """Remove every other element from a sequence"""
    if len(seq) > 1:
        if type(seq) is tuple:
            every_other = (seq[::-1])
            print(every_other)
        elif type(seq) is str:
            every_other = seq[::-1]
            print(every_other)
        elif type(seq) is list:
            every_other = seq[::-1]
            print(every_other)
    else:
        print(seq)


def mid_last_first(seq):
    """Middle 3 + Last 3 + first 3"""
    if len(seq) > 1:
        if type(seq) is tuple:
            mid_last_first = (*seq[int(len(seq)/3):int((len(seq)/3)*2):1],*seq[-int(len(seq)/3)::1],*seq[:int(len(seq)/3):1])
            print(mid_last_first)
        elif type(seq) is str:
            mid_last_first = seq[int(len(seq)/3):int((len(seq)/3)*2):1] + seq[-int(len(seq)/3)::1] + seq[:int(len(seq)/3):1]
            print(mid_last_first)
        elif type(seq) is list:
            mid_last_first = [*seq[int(len(seq)/3):int((len(seq)/3)*2):],*seq[-int(len(seq)/3)::],*seq[:int(len(seq)/3):]]
            print(mid_last_first)
    else:
        print(seq)


exchange_first_last([1,4])
exchange_first_last([1,2,3,4])
exchange_first_last((1,2,3,4,5))
exchange_first_last('This is a test string for functions')
exchange_first_last((1,5))
exchange_first_last((1,))
exchange_first_last('m')
every_other_remove((1,2,3,4))
every_other_remove([1,2,3,4])
every_other_remove('This is a test string for functions')
f4_l4_every_other_remove((1,2,3,4,5,6,7,8,9,10,11,12,13,13))
f4_l4_every_other_remove([1,2,3,4,5,6,7,8,9,10,11,12,13,13])
f4_l4_every_other_remove('This is a test string for functions')
every_other_remove((1,2,3,4,5,6,7,8,9,10,11,12,13,13))
mid_last_first((2, 54, 13, 12, 5, 32))
mid_last_first('This is a test string for functions')
mid_last_first([1,2,3,4])


