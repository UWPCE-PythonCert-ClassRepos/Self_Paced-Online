# Function to create NameError exception
def test_name_error():
    return foo

# Function to create TypeError exception
def test_type_error():
    x = 5
    y = "Hello"
    return x + y

# Function to create SyntaxError exception
def test_syntax_error():
   # print("Hello"
    return

# Function to create AttributeError exception
def test_attribute_error():
    name = "thor"
    name = name.capitilize
    print(name)
    return


test_name_error()
#test_type_error()
#test_syntax_error()
#test_attribute_error()