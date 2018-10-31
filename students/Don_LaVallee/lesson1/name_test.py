
def fun1(x, y):
    print("In the function now and Name is: ", __name__)
    return x + y
def test1(x, y):
    print ("Test Passed when result is 5: ")
    return x + y
    #this code will always run as __main__

print("Name outside code block is:", __name__)
print("We are still inside the main block")

if __name__ == "__main__":
    print("Inside main block, so block will only run as script . . . ")
    print("Function is called to return pair value key for exit: ", fun1(1,2))
    print("I put unit test code under this and call as script. . . ")
    print("Result Correct?", test1(2,3))
