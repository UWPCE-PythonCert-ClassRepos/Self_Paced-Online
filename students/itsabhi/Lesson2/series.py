
def fibonacci(x):
    """This function prints fibonacci series upto the "x"th index in the list."""
    f_series = [0,1]
    last_var = 1
    second_last_var = 0
    while(len(f_series) <= x):
        next_entry = last_var + second_last_var
        f_series.append(next_entry)
        second_last_var = last_var
        last_var = next_entry
    return(f_series[len(f_series)-1])

def lucas(x):
    """This function prints lucas series upto the "x"th index in the list."""
    l_series = [2,1]
    last_var = 1
    second_last_var = 2
    while(len(l_series) <= x):
        next_entry = last_var + second_last_var
        l_series.append(next_entry)
        second_last_var = last_var
        last_var = next_entry
    return(l_series[len(l_series)-1])

def sum_series(x,y=0,z=1):
    """This function implements fibonacci if only 1 argument is parsed."""
    s_series = [y,z]
    last_var = z
    second_last_var = y
    while(len(s_series) <= x):
        next_entry = last_var + second_last_var
        s_series.append(next_entry)
        second_last_var = last_var
        last_var = next_entry
    return(s_series[len(s_series)-1])



def main():
    nth_value = fibonacci(9)
    print(nth_value)
    nth_value = lucas(5)
    print(nth_value)
    nth_value = sum_series(5,2,1)
    print(nth_value)

    assert fibonacci(9) == 34
    assert lucas(5) == 11
    assert sum_series(5) == 5
    assert sum_series(5,2,1) == 11

if __name__ == '__main__':
    main()
