   # Python Concrete Exceptions error examples

import linecache
import sys
import traceback

def PrintException():
    print("Starting to show exceptions . . ."+"\n")
    control = "0"
    traceback.print_exc(file=sys.stdout)
    print("\n")
def Name_Error(): #1 menu item
    print("\n"+"You selected Name_Error."+"\n")
    print("A Name_Error exception in the break_me program is about to occur!")
    try:
        print("\n"+"This is a Name_Error exception example ... "  + nothing)
    except:
        PrintException()
        control = "0"
    finally:
        print("Name_Error function is complete!"+"\n")
def Type_Error(): #2 menu item
    print("\n"+"You selected Type_Error."+"\n")
    print("A Type_Error exception in the break_me program is about to occur!"+"\n")
    i = 0
    try:
        print("oops" + i * 2)
    except:
        PrintException()
        control = "0"
    finally:
        print("Type_Error function is complete!"+"\n")
def Syntax_Error(): #3 menu item
    print("\n"+"You selected Syntax_Error."+"\n")
    try:
        print("This code would not run if there was a Syntax_Error!"+"\n")
        print("Example: whille x%2 == 0:")
    except:
        PrintException()
        control = "0"
    finally:
            print("Syntax_Error function is complete!"+"\n")
def Attribute_Exception_Thrower(): #4 menu item
    try:
        print("\n"+"Trying to throw Attribute Exception next"+"\n")
        myInt = 1
        myInt.append(20) #should throw error
    except:
        print("You will now see the Attribute Exception traceback displayed"+"\n")
        PrintException()
#This starts the main function
control ="0"
print("name is:", __name__)
while control != "x":
    control = input("Which Error Function do you want to run: 1=Name, 2=Type, 3=Syntax, 4=Attribute? or enter 'x' to exit: ")
    if control == "1":
        Name_Error()
    elif control == "2":
        Type_Error()
    elif control == "3":
        Syntax_Error()
    elif control == "4":
            try:
                Attribute_Exception_Thrower()
            except:
                print("This is the exception code running..."+"\n")
            finally:
                print("Attribute_Exception Completed Successfully!"+"\n")
                control = "0"
    else: control = "x"
