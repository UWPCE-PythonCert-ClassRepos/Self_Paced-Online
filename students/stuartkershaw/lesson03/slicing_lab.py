def exchange_first_last(seq):
    seq[0], seq[-1] = seq[-1], seq[0]
    return seq

def remove_nth_even(seq):
    return seq[::2]

def return_specified(seq):
    return seq[4:-4:2]

def reverse_sequence(seq):
    return seq[::-1]

def return_specified_thirds(seq):
    index = int(len(seq) / 3)
    seg_end = seq[:index]
    seg_start = seq[index:]
    return seg_start + seg_end


if __name__ == "__main__":
    assert exchange_first_last([1,2,3,4]) == [4,2,3,1]

    assert remove_nth_even([1,2,3,4,5,6]) == [1,3,5]

    assert return_specified([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [4, 6, 8, 10, 12, 14]

    assert reverse_sequence([1,2,3,4]) == [4,3,2,1]

    print(return_specified_thirds([1,2,3,4,5,6]))
    #assert return_specified_thirds([1,2,3,4,5,6]) == [3,4,5,6,1,2]
