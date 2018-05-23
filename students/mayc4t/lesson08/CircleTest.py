#!/usr/bin/env python

import Circle

print ("\n#step 1")
c = Circle.Circle(4)
print( c.radius)


print ("\n#step 2")
c = Circle.Circle(4)
print( c.diameter)

print( "\n#step 3")
c = Circle.Circle(4)
c.diameter = 2
print( c.diameter)
print( c.radius)

print( "\n#step 4")
c = Circle.Circle(2)
print (c.area)
#c4.area = 42

print( "\n#step 5")
c = Circle.Circle.from_diameter(8)
print (c.diameter)
print (c.radius)

print( "\n#step 6")
c = Circle.Circle(4)
print(c)
print(repr(c))
d=eval(repr(c))
print (d)


print( "\n#step 7")
c1= Circle.Circle(2)
c2= Circle.Circle(4)
print(c1 + c2)
print(c2*3)
print(3*c2)

print ("\n#step 8")
print (c1>c2)
print (c1<c2)
print (c1==c2)

circl =[Circle.Circle(6), Circle.Circle(7), Circle.Circle(8),
        Circle.Circle(4), Circle.Circle(0), Circle.Circle(2),
        Circle.Circle(3), Circle.Circle(5), Circle.Circle(9), Circle.Circle(1)]
print( "\n\tORIGINAL circl list\n\t {}".format( circl))

circl.sort()
print( "\n\tSORTED circl list\n\t {}".format( circl))

print( "\nTHE END")


