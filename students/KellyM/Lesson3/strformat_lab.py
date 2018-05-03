
# Task One

"File_%03d, %.2f, %2.2e, %2.2e" % (2, 123.4567, 10000, 12345.67)


# Task Two

print('file_{:0>3d},{:06.2f},{:07.2e},{:07.2e}'.format(2, 123.4567, 10000, 12345.67))


# Task Three

def display(seq):
   
    return(("the {} numbers are:" + ", ".join(["{}"] * len(seq))).format(len(seq),*seq))


# Task Four

t = (4,30,2017,2,27)
t = ('{:0>2d},{:0>2d},{:0>2d},{:0>2d},{:0>2d}'.format(4,30,2017,2,27))
t = t.split(",")
print(t[3],t[4],t[2],t[0],t[1])

# Task Five

alist = ['oranges',1.3,'lemon',1.1]
fl = alist[0]
f1weight = alist[1]
f2 = alist[2]
f2weight = alist[3]
f'The weight of an {f1} is {f1weight} and the weight of a {f2} is {f2weight}.'
f'The weight of an {f1.upper()} is {f1weight*1.2} and the weight of a {f2.upper()} is {f2weight*1.2}.'

# Task Six

myList = [["First","$99.01", 5,"495.05"],["Second","$9999.01",1,"$999.01"],
["Third","$9.01",1,"$9.01"],["Fourth","$999.01",2,"$1998.02"],["Fifth","$99999.001",1,"$99999.001"]]


print("Item        | Price       |Quantity   |Total")

for item in myList:
    print(item[0], " "*(10-len(item[0])), "|", item[1],
				   " "*(10-len(item[1])), "|", item[2],
				   " "*(7), "|", item[3])
	

# Extra task

for item in t: print("{:5}".format(item))