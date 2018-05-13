# ------------------------------------------------------------------------
# Dev: MICAH BRAUN 
# PURPOSE: 
# DATE: <DATE>
# ChangeLog:
# DESCRIPTION:
# 
# 
#
# ------------------------------------------------------------------------
# In the break_me.py file write four simple Python functions:

# Each function, when called, should cause an exception to happen
# Each function should result in one of the four most common exceptions you’ll find.
# for review: NameError, TypeError, SyntaxError, AttributeError

def N_Error():
    try:
        myVal = 2*2

        prrint("myVal is 4!")

    except Exception as e:
        return myVal

def T_Error():
    try:
        value_1 = 5
        value_2 = '5'

        final_Val = value_1 + value_2
    except Exception as e:
        return  final_Val


def A_Error():

    myVal = 8

    myVal.append(4)

    return myVal

def S_Error():

    x = 1

    y =3
    result = 0
    if(x < y)

        print("YEP!")
        result = 1
    else:
        print("NOPE!")
        result = 0
    return result

# Display -------------------------------------------------------------------

try:
    print(N_Error())

except Exception as e:
    print(e, "NameError: name 'myyVal' is not defined")

try:
    print(T_Error())

except Exception as e:
    print(e, "TypeError: unsupported operand type(s) for +: 'int' and 'str'")

try:
    print(S_Error())

except Exception as e:
    print(e, "SyntaxError: SyntaxError: invalid syntax.")

try:
    print(A_Error())

except Exception as e:
    print(e, "AttributeError: 'int' object has no attribute 'append'.")

