#lesson 03 string formatting

#task 1- take tuple and print formatted string "file_002: 123.46, 1.00e+04, 1.23e+04"
#use {:.2f} for float with 2 decimal places
#use {:0>3d} for padding on the left with zeroes for 3 numbers width
#use {:.2e} for exponential with 2 decimal places
tupelo = (2, 123.4567, 10000, 12345.67)
filename = "file_{:0>3d}: {:.2f}, {:.2e}, {:.2e}"
print(filename.format(*tupelo))
print()
print()

#task 2- repeat task 1 with an alternate type of format string
filename = f"file_{tupelo[0]:0>3d}: {tupelo[1]:.2f}, {tupelo[2]:.2e}, {tupelo[3]:.2e}"
print(filename)
print()
print()

#task 3- dynamically rewrite "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3) 
testtup = (1, 2, 3, 4, 5, 6)
testtup2 = (4, 7, 5)
testtup3 = (6, 19, 22, 34)
def strform(tup):
    l = len(tup)
    lst = ""
    for t in tup:
        if t == tup[0]:
            lst += str(t)
        else:
            lst += ", " + str(t)
    statement = f"The {l:d} numbers are: {lst}"
    return statement
print(strform(testtup))
print(strform(testtup2))
print(strform(testtup3))
print()
print()

#task 4- use index numbers to print "02 27 2017 04 30" from (4, 30, 2017, 2, 27)
dttup = (4, 30, 2017, 2, 27)
datetime = f"{dttup[3]:0>2d} {dttup[4]} {dttup[2]} {dttup[0]:0>2d} {dttup[1]}"
print(datetime)
print()
print()

#task 5- use f strings to print "The weight of an orange is 1.3 and the weight of a lemon is 1.1"
info = ["oranges", 1.3, "lemons", 1.1]
fruitinfo = f"The weight of an {(info[0])[:-1]} is {info[1]:.1f} and the weight of a {(info[2])[:-1]} is {info[3]:.1f}"
print(fruitinfo)
#part 2- print fruit in upper case and weights 20% higher
fruitinfo20 = f"The weight of an {((info[0])[:-1]).upper()} is {(info[1]*1.2):.1f} and the weight of a {((info[2])[:-1]).upper()} is {(info[3]*1.2):.1f}"
print(fruitinfo20)
print()
print()

#task 6- use string formatting to print data (name, age, cost) in columns
namedata = ["Trixie", "Lassie", "Polly", "Buddy", "Remy"]
agedata = [4, 2, 7, 4, 1]
costdata = [400, 1000, 200, 500, 1200]
assert len(namedata) == len(agedata)
assert len(agedata) == len(costdata)
zipdata = list(zip(namedata, agedata, costdata))

def maketable(entries):
    l = len(entries)
    print("{:<7} {:^12} {:^5}".format("Dog", "Age", "Adoption Fee"))
    for i in range(l-1):
        print("{:<7} {:^12} {:>7}".format(*entries[i]))

maketable(zipdata)
print()
print()

bonustuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(("{:>5}\n"*10).format(*bonustuple))