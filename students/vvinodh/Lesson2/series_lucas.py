def fib(n):
#initial assignment based on where the series need to start
    a = 2
    b = 1
# If the required index is 0th position print the first lucas number
    if n == 0:
        print (a)
    else:
# Loop to move the latest number to prior and new number to the next calculated variable
        for i in range(n):
                next = a + b
                a = b
                b = next
        print (a)
