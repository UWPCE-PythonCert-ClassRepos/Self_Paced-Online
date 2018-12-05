##part1
a=4
b=4
c=2


print('+' + (a*' -' + ' +')*c)
print((('|' + (a* '  ' + ' |')*c +'\n')*a+('+' + (a*' -' + ' +')*c+'\n'))*c)


##part2
def grid(x):
    a=x//2
    b=x//2
    c=2

    print('+' + (a*' -' + ' +')*c)
    print((('|' + (a* '  ' + ' |')*c +'\n')*a+('+' + (a*' -' + ' +')*c+'\n'))*c)
grid(15)

#part3
def grid(x,y):
    a=y
    b=y
    c=x

    print('+' + (a*' -' + ' +')*c)
    print((('|' + (a* '  ' + ' |')*c +'\n')*a+('+' + (a*' -' + ' +')*c+'\n'))*c)
grid(5,3)


