"""Ian Sahlberg
Assignment 3 String Format
Python 210
12/27/2018"""

#Task One

four = (2, 123.4567, 10000, 12345.67)
print("file_{:0>3} : {:>8.2f}, {:.2e}, {:.3g}".format(four[0],four[1], four[2],four[3]))

#Task Two

print(f"file_{four[0]:0>3} : {four[1]:>8.2f}, {four[2]:.2e}, {four[3]:.3g}")

#Task Three

def formatter(in_tuple):
    """Returns formatted string based on tuple length"""
    bracket_count = ", ".join(["{}"]*len(in_tuple))
    return "The " + str(len(in_tuple)) +" numbers are: " + bracket_count.format(*in_tuple)
    #print("The " + str(len(in_tuple)) + " numbers are:" + ",".join("{}"*len(in_tuple)).format(*in_tuple))


print(formatter((1,2,3,4,5)))

#Task Four

five_tup = (4, 30, 2017, 2, 27)

print(f"{five_tup[3]:0>2} {five_tup[4]} {five_tup[2]} {five_tup[0]:0>2} {five_tup[1]}")

#Task Five

four_e = ['oranges', 1.3, 'lemons', 1.1]

print(f'The weight of an {four_e[0][:-1].upper()} is {four_e[1]*1.2} and the weight of a {four_e[2][:-1].upper()} is {four_e[3]*1.2}')

#Task 6

#print table
profile = [['Bob', '26', '126.00'],['JuanitaClarita', '5', '126,000,000'], ['Ronathan', '75', '100,000'], ['Sir Marcus','33', '33']]

for file in profile:
    print('{:<20}{:<10}{:<8}'.format(*file))


#5 character column
ten = (1,2,3,4,5,6,7,8,9,10)
print(", ".join(["{:>5}"]*len(ten)).format(*ten))


