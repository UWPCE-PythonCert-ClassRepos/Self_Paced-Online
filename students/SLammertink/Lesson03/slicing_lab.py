# Author: SLammertink
# Lesson 3 Slicing Lab

# Function with the first and last items exchanged.

def first_last(x):
    return x[-1:] + x[1:-1] + x[:1]


# Function with every other item removed.

def rem_every_other(y):
    return y[::2]

# Function with the first 4 and the last 4 items removed, and then every other item in between.

def rem_first_last_every_other(z):
    return z[4:-4:2]

# Function with the elements reversed (just with slicing).

def reversed(a):
    return a[::-1]

# Function with the middle third, then last third, then the first third in the new order.

def third_in_new_order(b):
    return b[len(b)//3:] + b[:len(b)//3]

# Assert the functions.
a_string = "I love Python programming"
a_tuple = (2, 54, 13, 12, 5, 32)

if __name__ == "__main__":
    assert first_last(a_string) == 'g love Python programminI'
    assert first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert rem_every_other(a_string) == 'Ilv yhnpormig'
    assert rem_every_other(a_tuple) == (2, 13, 5)
    assert rem_first_last_every_other(a_string) == 'v yhnporm'
    assert rem_first_last_every_other(a_tuple) == ()
    assert reversed(a_string) == 'gnimmargorp nohtyP evol I'
    assert third_in_new_order(a_string) == 'ython programmingI love P'
    assert third_in_new_order(a_tuple) == (13, 12, 5, 32, 2, 54)


