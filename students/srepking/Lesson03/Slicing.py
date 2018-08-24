def first_to_last(x):
    """Pass a sequence to swap first and last entries."""
    new_list = x[-1:] + x[1:-1] + x[0:1]
    return new_list


def remove_every_other(x):
    """Remove every other item in list"""
    new_list = x[0::2]
    return new_list


def four_and_four(x):
    """With the first 4 and the last 4 items removed, and then every other
    item in between"""
    return x[4:-4:2]


def reverse_list(x):
    """Returns the list in reverse order."""
    return x[::-1]


def thirds(x):
    """Creates a list with the middle third and last third, then the first
    third in the new order"""
    if len(x) % 3 == 0:
        # if list is divisible by three, make a new list out of the last two thirds.
        third = int(len(x)/3)
        new_list = (x[-(2*third):])
        # If the new list is divisible by three, take the first third in the new list.
        if len(new_list) % 3 ==0:
            new_third = int(len(new_list)/3)
            return new_list[0:new_third]
        else:
            print("Your list is not divisible by three the second time.")
    else:
        print('This list is not divisible by three')
    return

