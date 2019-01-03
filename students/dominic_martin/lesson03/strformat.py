#!/usr/bin/env Python 3

t = (2, 123.4567, 10000, 12345.67)
u = t[1:]
v = ()

msg = "File_002: {:.2f}, {:.2e}, {:.2e}".format(*u)

# '''	Task One '''

print(msg)
print()

'''	Task Two '''

print(f"{msg}")

'''	Task Three '''

a = input("Please enter in no more than five numeric values."
	"Separate each value by a comma.\n"
	"Enter your values:")
b = tuple(int(a) for a in a.split(','))

# print(b)


'''	Task Four'''

k = (4, 30, 2017, 2, 27)
l = (k[3], k[4], k[2], k[0], k[1])

msg1 = "{:02d}, {:d}, {:d}, {:02d}, {:d}".format(*l)
print(msg1)




'''	Task Five'''

p = ['oranges', 1.3, 'lemons', 1.1]


q = (f"The weight of {p[0]} is {p[1]} and the\n"
	f"weight of {p[2]} is {p[3]}.")

u = (f"The weight of {p[0].upper()} is {p[1]*1.2} and the\n"
	f"weight of {p[2].upper()} is {p[3]*1.2}.")


print(q)

print(u)

'''	Task Six '''

width = 10

p = ('Name', 'Squat', 'Bench Press', 'Deadlift','Total')
p1 = ('Ed', '1005', '574', '918', '2497')
p2 = ('Louie', '789', '515', '770', '2001')
p3 = ('Matt', '1101', '660', '901', '2662')
o = f'{p[0]:{width}}{p[1]:{width + 1}}{p[2]:{width + 7}}{p[3]:{width + 4}}{p[4]:{width}}'
o1 = f'{p1[0]:{width}}{p1[1]:{width + 1}}{p1[2]:{width + 7}}{p1[3]:{width + 4}}{p1[4]:{width}}'
o2 = f'{p2[0]:{width}}{p2[1]:{width + 1}}{p2[2]:{width + 7}}{p2[3]:{width + 4}}{p2[4]:{width}}'
o3 = f'{p3[0]:{width}}{p3[1]:{width + 1}}{p3[2]:{width + 7}}{p3[3]:{width + 4}}{p3[4]:{width}}'
print(o)
print(o1)
print(o2)
print(o3)





