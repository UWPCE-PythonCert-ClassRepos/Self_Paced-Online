def task1(inputs=(2,123.4567,10000,12345.67)):
    a=str(inputs[0]).zfill(3)
    b=round(inputs[1],2)
    c="{0:.2e}".format(inputs[2])
    d="{0:.2e}".format(inputs[3])
    e=a,b,c,d
    print("file_{}: {}, {}, {}".format(a,b,c,d))
    return e

def task2(e):
    string=f"file_{e[0]}: {e[1]}, {e[2]}, {e[3]}"
    print(string)
    return string

def task3(f=(1,2,3)):
    g="{:d}, "*(len(f)-1)+"{:d}"
    h=g.format(*f)
    string = "the {:d} numbers are: {}".format(len(f), h)
    print(string)
    return string

def task4(i=(4, 30, 2017, 2, 27)):
    j=str(i[3]).zfill(2)+" "+str(i[4]).zfill(2)+" "+str(i[2]).zfill(4)+" "+str(i[0]).zfill(2)+" "+str(i[1]).zfill(2)
    print(j)
    return j

def task5(k=['oranges', 1.3, 'lemons', 1.1]):
    string=f"The weight of an {k[0][:-1]} is {k[1]} and the weight of a {k[2][:-1]} is {k[3]}"
    string2=f"The weight of an {(k[0][:-1]).upper()} is {k[1]*1.2} and the weight of a {(k[2][:-1]).upper()} is {k[3]*1.2}"
    print(string)
    print(string2)
    return string


def task61(l=(['Daniel', '55', '$88.09'],['Alex','27', '$624.26'],['James','35', '$55555.01'],['Myles','15', '$753354.34'])):
    for row in l:
        print("{:<20}{:<20}{:<20}".format(*row))

def task62(m=(1,2,3,4,5,6,7,8,9,0)):
    print(("{:<5}"*len(m)).format(*m))