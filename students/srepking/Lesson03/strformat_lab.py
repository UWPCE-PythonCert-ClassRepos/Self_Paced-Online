#Start Task 1
my_tuple = (2, 123.4567, 10000, 12345.67)

s = "file_{0:}:  {1:.2f}, {2:.2e}, {3:.3e}"

print(s.format(str(my_tuple[0]).zfill(3),my_tuple[1],my_tuple[2],my_tuple[3]))


# Start Task 2
s = "file_{file_n:}:  {num1:.2f}, {num2:.2e}, {num3:.3e}"

print(s.format(file_n = str(my_tuple[0]).zfill(3),
num1 = my_tuple[1], num2=my_tuple[2], num3=my_tuple[3]))

print('\n''This is the start of Task 3')


# Start Task 3
def formatter(t):
    # Takes a tuple and the function returns a message.
    new_list = []
    a = 0
    while a<len(t):
        new_list.append('{:d}')
        a=a+1
    s = ",".join(new_list)
    first = 'the {num} numbers are: '.format(num=len(t))
    second = s.format(*t)
    return f"{first}{second}"


print(formatter((2,3,4,5,6,7,8)))


# Start of Task 4
print('\n''This is the beginning of Task 4')
y = (4,30,2017,2,27)
 
print("{} {} {} {} {}".format((str(y[3])).zfill(2),
str(y[4]).zfill(2), str(y[2]).zfill(2), str(y[0]).zfill(2), str(y[1])).zfill(2))

# Start of Task 5
print('\n''This is the beginning of Task 5')

our_list = ['orange', 1.3, 'lemon', 1.1]
print(f"The weight of an {our_list[0]} is {our_list[1]} \
and the weight of a {our_list[2]} is {our_list[3]}")

print('\n''Fruits in upper case and the weight 20% higher')
print(f"The weight of an {our_list[0].upper()} is {our_list[1]*1.2} \
and the weight of a {our_list[2].upper()} is {our_list[3]*1.2}")

# Start of Task 6
print('\n''This is the beginning of Task 6')
name = ('Buick', 'Honda', 'Porcheeeeeeee')
column_width_name = int(len(str(max(name))))+2
age = (20, 18000, 2)
column_width_age = int(len(str(max(age))))+2
cost = ('$2', '$200', '$200000')
for idx, number in enumerate(name):
    print(f"{name[idx]:{column_width_name}}{age[idx]:<{column_width_age}d} {cost[idx]:}")
