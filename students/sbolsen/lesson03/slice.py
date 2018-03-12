def first_last_exchanged(sequence):
    sequence[0], sequence[-1] = sequence[-1], sequence[0]
    return sequence

def elements_reversed(sequence):
    return sequence[::-1]

def thirds(sequence):
    a_list = []
    for i in sequence:
        a_list.append(i)
    section = int(len(a_list) / 3)
    first = a_list[:section]
    third = a_list[section * 2:section * 3]
    second = a_list[section:section * 2]
    return second + third + first

def every_other(sequence):
    return sequence[1::2]

def four_and_four(sequence):
    b = sequence[4:-4]
    c = b[1::2]
    return c

a_list = ['31', '32', '33', '34', '35']
longer_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

assert first_last_exchanged(a_list) == ['35', '32', '33', '34', '31']
assert elements_reversed(['31', '32', '33', '34', '35']) == ['35', '34', '33', '32', '31']
assert thirds(range(1,13)) == [5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4]
assert every_other(longer_list) == ['2', '4', '6', '8', '10']
assert four_and_four(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']) == ['6', '8', '10', '12']
