#Task One
#convert tuple (2,123.4567,10000,12345.67) to 'file_002: 123.46, 1.00e+04, 1.23e+04'
s1='file_{:03}: {:.2f}, {:.2e}, {:.2e}'
a=(2,123.4567,10000,12345.67)
s1.format(*a)

#Task Two
#repeat 'Task One' using f-strings
a=(2,123.4567,10000,12345.67)
f'file_{a[0]:03}: {a[1]:.2f}, {a[2]:.2e}, {a[3]:.2e}'

#Task Three
def formatter(nums):
	x=len(nums)
	s1 = "there are {:d} numbers and they are:".format(x)
	L=(['{:d}'])*len(nums)
	L2=', '.join(L)
	s2=L2.format(*nums)
	s3=" ".join((s1,s2))
	return s3

#Task Four
#Given 5 element tuple: (4,30,2017,2,27) use string formatting to print '02 27 2017 04 30'
nums=(4,30,2017,2,27)
'{3:02},{4},{2},{0:02},{1}'.format(*nums)


#Task Five
a=['orange',1.3,'lemon',1.1]
f"the weight of an {a[0].lower()} is {a[1]} and the weight of a {a[2]} is {a[3]}"
f"the weight of an {a[0].upper()} is {a[1]*1.2} and the weight of a {a[2].upper()} is {a[3]*1.2}"

#Task Six
name = ['Kalamazoo', 'Joe', 'Dave', 'Michigan', 'Blue', 'Go']
age = [10,5,100,250,7,23]
cost = [10,10,1500,20000,5,25]

s='{:<10}{:<10}{:<10}'
for i in range(len(name)):
    temp = [name[i],age[i],cost[i]]
    print(s.format(*temp))




