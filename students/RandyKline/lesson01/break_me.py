def keyArgFunc(empname, emprole):
    print ("Emp Name: ", empname)
    print ("Emp Role: ", emprole)
    return;
print("This call works")
keyArgFunc(empname = "Randy",emprole = "King")
#print("This call raises NameError")
#keyArgFunc(Randy,King)

def typeErrFunc(myInt, myStr):
    print ("integer: ", myInt)
    print ("string: ", myStr)
    return;
#print("This call works")
#typeErrFunc(myInt = 3,myStr = "King Randy")
#print("This call raises syntax error")
#eval typeErrFunc(myInt = 3,myStr = "King Randy")
#print("This call raises type error")
#typeErrFunc(myInt = "Randy", myStr = float([0,1,2,3]))
print("The following function raises Syntax error")
def attFunc(empname, emprole):
    print ("Emp Name: ", empname)
    print ("Emp Role: ", emprole)
    print ("Attribute: ", emprole.sister)
    return;
print("The following raises the AttributeError")
attFunc(empname = "Randy", emprole = "Master")
