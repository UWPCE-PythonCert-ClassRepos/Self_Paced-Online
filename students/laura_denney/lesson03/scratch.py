def swap_first_last(lst):
    first = lst[0]
    last = lst[-1]
    if type(lst) == tuple:
        return (last,) + lst[1:-1] + (first,)
    elif type(lst) == list:
        return [last] + lst[1:-1] + [first]
