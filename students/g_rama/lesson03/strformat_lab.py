# Task One

tuple_t = (2, 123.4567, 10000, 12345.67)
print('file_00{:} :  {:.2f}, {:.2e}, {:.2e}'.format(*tuple_t))

# Task two

print(f"file_00{tuple_t[0]} :  {tuple_t[1]:.2f}, {tuple_t[2]:.2e}, {tuple_t[3]:.2e}".format(*tuple_t))

# Task three


def formatter(*args):
    temp_s1 = "The {} numbers are:".format(len(*args), *args)
    for _ in range(len(*args)-1):
        temp_s1 += "{},".format(args[0][_])
    return temp_s1+"{}".format(args[0][len(*args)-1])


print(formatter((3, 4, 5, 6, 7, 9)))

# Task Four

test_tuple = (4, 30, 2017, 2, 27)
print("{:0>2} {} {} {:0>2} {}".format(test_tuple[3], test_tuple[4], test_tuple[2], test_tuple[0], test_tuple[1]))

# Task Five

task_five = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {task_five[0][:-1]} is {task_five[1]}  and the weight of a {task_five[2][:-1]} "
      f"is {task_five[3]}")
print(f"The weight of an {task_five[0][:-1].upper()} is {task_five[1]*1.2}  and the weight of a {task_five[2][:-1].upper()}"
      f" is {task_five[3]*1.2}")

# Task Six

table_data = (("John", 24, "$2000.3"), ("Susan", 30, "$2000988.3"), ("Terry", 26, "$70056988.3"))

for _ in range(len(table_data)):
    print('{:10}{:10}{:>20}'.format(*table_data[_]))