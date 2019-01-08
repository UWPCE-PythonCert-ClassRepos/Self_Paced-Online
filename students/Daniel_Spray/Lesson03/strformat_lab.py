def task1(inputs):
    a=str(inputs[0]).zfill(3)
    b=round(inputs[1],2)
    c="{0:.2e}".format(inputs[2])
    d="{0:.2e}".format(inputs[3])
    e=a,b,c,d
    return e
    #print("file_{}: {}, {}, {}".format(a,b,c,d))

def task2(e):
    print(f"file_{e[0]}: {e[1]}, {e[2]}, {e[3]}aw )

def task3(f):
    count=len(f)
    string=str(f)
    numbers=string[1:len(string)-1]
    print(f"the {count} numbers are: {numbers}")
    print(f) 