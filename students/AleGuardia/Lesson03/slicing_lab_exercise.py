# Slicing Lab Exercise - Lesson 3 - by Alejandro Guardia


def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[0:1]


def remove_every_other_item(seq):
    return seq[::2]


print(exchange_first_last([1,2,3,4]))
print(remove_every_other_item("0123456"))




