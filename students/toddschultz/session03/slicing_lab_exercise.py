#with the first and last items exchanged.
def exchanged_string(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]
exchanged_string("abcdefghijklmnopqrstuvwxyz")

def exchanged_tuple(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]
exchanged_tuple(("airplane", "boat", "car", "donkey", "elevator", "frigate", "glider", "hovercraft", "inflatable"))

#with every other item removed.
def every_other_tuple(seq):
    return seq[::2] 
every_other_tuple(("apple", "banana", "Corn", "Date", "Elderberry", "Fig", "Grape", "Honeydew", "Imbe"))

def every_other_string(seq):
    return seq[::2] 
every_other_string("123456789")

#with the first 4 and the last 4 items removed, and then every other item in between.
def remove_fours_every_other_string(seq):
    return seq[4:-4:2] 
remove_fours_every_other_string("----123456789----")

def remove_fours_every_other_list(seq):
    return seq[4:-4:2] 
remove_fours_every_other_list(list(range(20)))

#with the elements reversed (just with slicing).
def reversed_tuple(seq):
    return seq[::-1] 
reversed_tuple(("apple", "banana", "Corn", "Date", "Elderberry", "Fig", "Grape", "Honeydew", "Imbe"))

def reversed_list(seq):
    return seq[::-1] 
reversed_list(list(range(20)))

#with the middle third, then last third, then the first third in the new order.
def thirds_list(seq):
    return seq[3:6] + seq[6:9] + seq[0:3]
thirds_list(["apple", "banana", "Corn", "Date", "Elderberry", "Fig", "Grape", "Honeydew", "Imbe"])

def thirds_string(seq):
    return seq[3:6] + seq[6:9] + seq[0:3]
thirds_string("123456789")

def thirds_string_len(seq):
    return seq[int((len(seq) * .34)):int((len(seq) * .67))] + seq[int((len(seq) * .67)):len(seq)] + seq[:int((len(seq) * .34))]
thirds_string_len("123456789")
