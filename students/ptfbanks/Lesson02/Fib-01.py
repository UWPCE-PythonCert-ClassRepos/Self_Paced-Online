t=(input("I will Prepare for you the Fibonacci or Lucas series of numbers.  Which series woiuld you lke? (Enter F, or L): "))
m=int(input("for how many values? (max 20): "))
if m>=20:
    m=20
def series (t,m):
    """Prepare a sequence of Fibonacci or values"""
    """and return the series up to the selected (nth) member in that series"""
    x=0
    y=1
    if t=="L":
        x=2
        print("The Lucas series is:")
    else:
        print("Fibbonacii series is:")
    for i in range (m+1):
            print(x)
            z=x+y
            x=y
            y=z
series (t,m)

