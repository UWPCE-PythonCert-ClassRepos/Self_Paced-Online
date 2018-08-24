#Start Task 1
my_tuple=(2, 123.4567, 10000, 12345.67)

s= "file_{0:}:  {1:.2f}, {2:.2e}, {3:.3e}"

print(s.format(str(my_tuple[0]).zfill(3),my_tuple[1],my_tuple[2],my_tuple[3]))

#Start Task 2
s= "file_{file_n:}:  {num1:.2f}, {num2:.2e}, {num3:.3e}"

print(s.format(file_n = str(my_tuple[0]).zfill(3), num1=my_tuple[1], num2=my_tuple[2], num3=my_tuple[3]))