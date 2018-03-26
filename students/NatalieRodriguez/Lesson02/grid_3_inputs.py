def row(a):
    print("+", end=" ")
    for i in range(a-1):
        print("- "*c + "+", end=" ")
    print("- "*c + "+" )

def column(a):
    print("|", end=" ")
    for i in range(a-1):
        print(" "*(c*2) + "|", end=" ")
    print(" "*(c*2) + "|" )

def func(a,b):
    row(a)
    for i in range(b):
        for i in range(c):
            column(a)
        row(a)

a=int(input("Columns: "))
b=int(input("Rows: "))
c=int(input("Insides: "))
func(a,b)


