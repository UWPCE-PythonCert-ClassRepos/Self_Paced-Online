def fibonacci(n):
    c = 1
    a, b = 0, c
    if n == 0:
        return 0
    for i in range(n-1):
        a, b = b, a + b
    return b


def lucas(n):
    c = 2
    a, b = 0, c
    if n == 0:
        return 0
    for i in range(n-1):
        a, b = b, a + b
    return b

#printing fibonacci results
print ("Fibonacci series:")
print fibonacci(0)
print fibonacci(1)
print fibonacci(2)
print fibonacci(3)
print fibonacci(4)
print fibonacci(5)
print fibonacci(6)
print fibonacci(7)
print fibonacci(8)
print fibonacci(9)
print fibonacci(10)
print ("...")


#printing lucas results
print ("Lucas series:")
print lucas(0)
print lucas(1)
print lucas(2)
print lucas(3)
print lucas(4)
print lucas(5)
print lucas(6)
print lucas(7)
print lucas(8)
print lucas(9)
print lucas(10)
print ("...")