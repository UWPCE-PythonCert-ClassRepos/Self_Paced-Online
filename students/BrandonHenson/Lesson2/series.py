def fibonacci(n):
    """This function prints out the digit in the Fibonacci series that is in the index number defined by the parameter."""
    fibo_list = [0,1]
    for i in range(2, n+1):
        x = fibo_list[i-2] + fibo_list[i-1]
        fibo_list.append(x)
    #printed to test if I'm getting the index number
    #print(fibo_list[n])
    return fibo_list[n]




def lucas(n):
    """This function prints out the digit in the lucas series that is in the index number defined by the parameter."""
    luc_list = [2,1]
    for i in range(2, n+1):
        x = luc_list[i-2] + luc_list[i-1]
        luc_list.append(x)
    #printed to test if I'm getting the index number
    #print(luc_list[n])
    return luc_list[n]

lucas(5)