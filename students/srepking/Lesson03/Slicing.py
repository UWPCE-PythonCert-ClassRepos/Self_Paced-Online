def first_to_last(x):
    """Pass a sequence to swap first and last entries."""
    new_list = x[-1:] + x[1:-1] + x[0:1]
    return new_list

print('Swap first to last')
print(first_to_last([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 2, 13, 14, 15, 16]))


def remove_every_other(x):
    """Remove every other item in list"""
    new_list = x[0::2]
    return new_list


print('Remove Every Other')
print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 2, 13, 14, 15, 16]))


def four_and_four(x):
    """With the first 4 and the last 4 items removed, and then every other
    item in between"""
    return x[4:-4:2]


print('Trim first four and last four, then return every other')
print(four_and_four([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 2, 13, 14, 15, 16]))


def reverse_list(x):
    """Returns the list in reverse order."""
    return x[::-1]


print('Return the reverse list')
print(reverse_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 2, 13, 14, 15, 16]))


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


print('Creates a list with the middle third and last third, then the first third in the new order')
print(thirds([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 2, 13, 14, 15, 16, 17, 18]))

