# NameError example
def saySomething():
    print(message)

saySomething()

# TypeError example
def changeSomething():
    hex(zip)

changeSomething()

# SyntaxError example
def 1message():
    print("This will not work.")

1message()

# AttributeError example
def addStuffToTheEnd():
    num = 5
    num.append(6)

addStuffToTheEnd()