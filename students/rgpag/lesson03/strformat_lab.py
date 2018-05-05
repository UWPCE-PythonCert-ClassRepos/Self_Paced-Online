#Task One
#convert tuple (2,123.4567,10000,12345.67) to 'file_002: 123.46, 1.00e+04, 1.23e+04'
s1='file_{:03}: {:.2f}, {:.2e}, {:.2e}'
a=(2,123.4567,10000,12345.67)
s1.format(*a)

#Task Two
#repeat 'Task One' using f-strings

#NEEED TO COME BACK TO THIS!

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
