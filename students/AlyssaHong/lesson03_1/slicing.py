"""
Author: Alyssa Hong
Date: 10/22/2018
Lesson3 Assignments > Slicing Lab Exercise
"""
#Get the basics of sequence slicing downself.

#1 with the first and last items exchanged.
def exchange_first_last(seq):
    a_new_sequence = seq[-1], seq[0]
    seq[0], seq[-1] = a_new_sequence
    print("result #1:", seq)
    return exchange_first_last

#2 with every other item removed.
def every_other_item_remove(seq):
    count_seq = len(seq)
    del seq[1:int(count_seq-1)]
    print("result #2:", seq)
    return every_other_item_remove

#3 with the first 4 and the last 4 items removed, and then every other item
# in between.
def select_item_and_remove(seq):
    # print(seq[4:-4])
    del seq[3]
    del seq[-4]
    del seq[4:-3]
    print("result #3:", seq)
    return select_item_and_remove

#4 with the elements reversed (just with slicing).
def elements_reverse(seq):
    seq.reverse()
    print("result #4:",seq)
    return elements_reverse

#5 with the middle third, then last third, then the first third in the new order.
def each_third_reorder(seq):
    dividend = len(seq)
    quotient = int(dividend/3)
    middle_third = seq[quotient:quotient+quotient]
    last_third = seq[quotient+quotient:dividend]
    first_third = seq[:quotient]
    print("result #5:", middle_third,last_third,first_third)
    return each_third_reorder


def main():
    # input_range = int(input("Let's input the list range: "))
    # seq1 = list(range(input_range))
    # seq2 = list(range(input_range))
    seq1 = list(range(15))
    seq2 = list(range(15))
    print("the starting list is ", seq1)

    exchange_first_last(seq1)
    every_other_item_remove(seq1)
    select_item_and_remove(seq2)
    elements_reverse(seq2)
    each_third_reorder(seq2)

if __name__ == '__main__':
    main()
