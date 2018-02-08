
def exchange_first_last(seq):
    if type(seq) is str:
        y = seq[-1] + seq[1:-1] + seq[0]
        new_string = y
        return print(new_string)

    elif type(seq) is tuple:
        x = list(seq)
        last_item = [x[-1]]
        middle_items = x[1:-1]
        first_item = [x[0]]
        new_list = last_item + middle_items + first_item
        new_tuple = tuple(new_list)
        return print(new_tuple)

    else:
        last_item2 = seq[-1]
        middle_items2 = seq[1:-1]
        first_item2 = seq[0]
        new_list2 = last_item2 + middle_items2 + first_item2
        return print(new_list2)


def remove_every_other(seq):
    if type(seq) is str:
        y = seq[0::2]
        new_string = y
        return print(new_string)

    elif type(seq) is tuple:
        x = list(seq)
        new_list = x[0::2]
        new_tuple = tuple(new_list)
        return print(new_tuple)

    else:
        new_list2 = seq[0::2]
        return print(new_list2)


def first_last_four_every_other_remove():
    return



def reverse():
    return


def middle_last_first():
    return

hello = "hello world"

remove_every_other(hello)
