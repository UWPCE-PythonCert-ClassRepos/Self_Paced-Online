#Grid Printer exercise
def print_grid(n):
    if n%2 == 0:
        row2_size=n+1
    else: row2_size=n

    plus='+ '
    minus='- '
    y='|'
    z=' '


    row=plus + minus*(n/2) + plus + minus*(n/2) + plus
    row2=y + z*(row2_size) + y + z*(row2_size) + y

    print(row)

    for x in xrange(n/2):
        print(row2)

    print(row)

    for x in xrange(n/2):
        print(row2)

    print(row)

print_grid(3)
