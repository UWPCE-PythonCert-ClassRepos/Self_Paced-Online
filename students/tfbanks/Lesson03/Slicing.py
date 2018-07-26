# Slicing Exercise by tfbanks


def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]


def exchange_every_other_item(seq):
    return seq[::2]


def exchange_every_other_item_minus_4_start_end(seq):
    return seq[4:-4:2]


def exchange_reverse(seq):
    return seq[::-1]


def exchange_mid_last_first(seq):
    split = len(seq)//3
    part_one = seq[:split]
    part_two = seq[split:-split]
    part_three = seq[-split:]
    return part_two + part_three + part_one


my_string = "This string is for this exercise"
my_tuple = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60)

assert exchange_first_last(my_string) == 'ehis string is for this exercisT'
assert exchange_first_last(my_tuple) == (60, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 5)

assert exchange_every_other_item(my_string) == "Ti tigi o hseecs"
assert exchange_every_other_item(my_tuple) == (5, 15, 25, 35, 45, 55)

assert exchange_every_other_item_minus_4_start_end(my_string) == " tigi o hsee"
assert exchange_every_other_item_minus_4_start_end(my_tuple) == (25, 35)

assert exchange_reverse(my_string) == "esicrexe siht rof si gnirts sihT"
assert exchange_reverse(my_tuple) == (60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5)

assert exchange_mid_last_first(my_string) == "g is for this exerciseThis strin"
assert exchange_mid_last_first(my_tuple) == (25, 30, 35, 40, 45, 50, 55, 60, 5, 10, 15, 20)

print('All 5 assertion tests passed for the defined string and tuple')