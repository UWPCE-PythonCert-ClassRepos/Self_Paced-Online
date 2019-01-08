def task1(inputs):
    a=str(inputs[0]).zfill(3)
    b=round(inputs[1],2)
    c="{0:.2e}".format(inputs[2])
    d="{0:.2e}".format(inputs[3])
    e=a,b,c,d
    return e
    #print("file_{}: {}, {}, {}".format(a,b,c,d))

def task2(e):
    string=f"file_{e[0]}: {e[1]}, {e[2]}, {e[3]}"
    print(string)
    return string

def task3(f):
    g="{:d}, "*(len(f)-1)+"{:d}"
    h=g.format(*f)
    string = "the {:d} numbers are: {}".format(len(f), h)
    return string
    print(string)

def task4(i):
    j=str(i[3]).zfill(2)+" "+str(i[4]).zfill(2)+" "+str(i[2]).zfill(4)+" "+str(i[0]).zfill(2)+" "+str(i[1]).zfill(2)
    print(j)
    return j