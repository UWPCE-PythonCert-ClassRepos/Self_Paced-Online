# Write some functions that take a sequence as an argument, and return a copy of that sequence:

# with the first and last items exchanged.
# with every other item removed.
# with the first 4 and the last 4 items removed, and then every other item in between.
# with the elements reversed (just with slicing).
# with the middle third, then last third, then the first third in the new order.

tuple_seq = (10,20,30,40,50,60,70,80,90,100,110,120,130,140,150)
string_seq = "Larger than life Jack Pepsi."

def exchange_first_last(seq):
    """ Create a function with the first and last items exchanged. """
    a_new_seq1 = seq[-1:] + seq[1:-1] + seq[0:1]
    print(a_new_seq1)
    return a_new_seq1


#exchange_first_last(tuple_seq)



def remove_every_other(seq):
    """ Create a function with every other item removed. """
    a_new_seq2 = seq[1::2]
    print(a_new_seq2)
    return a_new_seq2


# remove_every_other(tuple_seq)


def remove_firstLast4_every_other(seq):
   """ Create a function with the first 4 and 
   the last 4 items removed, and then every other item in between. """
   first_last_removed = seq[4:-4]
   a_new_seq3 = first_last_removed[1::2]
   print(a_new_seq3)
   return a_new_seq3


# remove_firstLast4_every_other(tuple_seq)



def reversed_elements(seq):
    """ Create a function with every other item removed. """
    a_new_seq4 = seq[::-1]
    print(a_new_seq4)
    return a_new_seq4


# reversed_elements(tuple_seq)


def middle_last_first_third(seq):
    """ Create a function with the middle third, then last third, 
    then the first third in the new order. """
    a_new_seq5 = seq[int(len(seq) / 3):int((len(seq) / 3) * 2)] + seq[-int(len(seq) / 3):] + seq[:int(len(seq) / 3)]
    print(a_new_seq5)
    return a_new_seq5


# middle_last_first_third(tuple_seq)


""" Function tests """

assert exchange_first_last(tuple_seq) == (150, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 10)
assert exchange_first_last(string_seq) == ".arger than life Jack PepsiL"

assert remove_every_other(tuple_seq) == (20, 40, 60, 80, 100, 120, 140)
assert remove_every_other(string_seq) == "agrta ieJc es."

assert remove_firstLast4_every_other(tuple_seq) == (60, 80, 100)
assert remove_firstLast4_every_other(string_seq) == "rta ieJc e"

assert reversed_elements(tuple_seq) == (150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10)
assert reversed_elements(string_seq) == ".ispeP kcaJ efil naht regraL"

assert middle_last_first_third(tuple_seq) == (60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 10, 20, 30, 40, 50)
assert middle_last_first_third(string_seq) == "an life Jck Pepsi.Larger th"
