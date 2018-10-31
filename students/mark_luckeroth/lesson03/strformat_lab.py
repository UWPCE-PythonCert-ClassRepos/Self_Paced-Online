#task one
tup = ( 2, 123.4567, 10000, 12345.67)
out = 'file_{:0>3d}: {:3.2f}, {:.2e}, {:.2e}'.format(*tup)
print(out)

#task two
out = f"file_{tup[0]:0>3d}: {tup[1]:3.2f}, {tup[2]:.2e}, {tup[3]:.2e}"
print(out)

#task three
def formatter(tup):
    form_string = "the {:d} numbers are: " + ('{:d}, '*(len(tup)-1)) + '{:d}'
    return form_string.format(len(tup), *tup)

#task four
tup = (4, 30, 2017, 2, 27)
def date_time(tup):
    return f"{tup[3]:0>2d} {tup[4]:0>2d} {tup[2]:4d} {tup[0]:0>2d} {tup[1]:0>2d}"

#task five
l = ['oranges',1.3, 'lemons',1.1]
fruit1 = l[0][:-1]
fruit1_weight = l[1]
fruit2 = l[2][:-1]
fruit2_weight = l[3]
print(f"The weight of an {fruit1.upper()} is {fruit1_weight*1.2} and  the weight of a {fruit2.upper()} is {fruit2_weight*1.2}")

#task six
rows = [['Name','Age','Cost'],
     ['Fiesta','29','$200'],
     ['E30 M3','31','$18,000'],
     ['911 Turbo','1','$120,000']]

padding = 2
cols = [0] * len(rows[0])
for row in rows:
    for i, item in enumerate(row):
        if len(item) > cols[i]:
            cols[i] = len(item)
cols = [x+(2*padding) for x in cols]
cols = "".join(['{:^'+str(x)+'}' for x in cols])
for row in rows:
    print(cols.format(*row))

