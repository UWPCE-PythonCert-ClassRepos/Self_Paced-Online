# python3

# fizz_buzz.py


# ---------------------------  START fizz_buzz_1(n)  ---------------------------
def fizz_buzz_1(n):
    """
    using the modulo operator, catching the '3 and 5' first
        then  catching the '3' and finally the '5'
    returns Fizz if n is a multiple of 3
    returns Buzz if n is a multiple of 5
    returns FizzBuzz if n is a multiple of 3 and 5
    returns n otherwise
    """

    if n % 3 == 0 and n % 5 == 0:
        return("FizzBuzz")
    elif n % 3 == 0:
        return("Fizz")
    elif n % 5 == 0:
        return("Buzz")
    else:
        return(n)
# ---------------------------  END fizz_buzz_1(n)  ---------------------------


# ---------------------------  START fizz_buzz_2(n)  ---------------------------
def fizz_buzz_2_helper(i):
    """
    i is divisible by 3 and/or 5
    test if divisible by 3, if not i is positively divisible by 5
    """
    if i % 3 == 0:
        if i % 5 == 0:
            return "FizzBuzz"
        else:
            return "Fizz"
    else:
        return "Buzz"


def fizz_buzz_2(n):
    """
    using the modulo operator
    returns Fizz if n is a multiple of 3
    returns Buzz if n is a multiple of 5
    returns FizzBuzz if n is a multiple of 3 and 5
    returns n otherwise
    """

    if n % 3 == 0 or n % 5 == 0:
        return(fizz_buzz_2_helper(n))
    else:
        return(n)
# ---------------------------  END fizz_buzz_2(n)  ---------------------------


# ---------------------------  START fizz_buzz_3(n)  ---------------------------
def divisible_by_3(n):
    """
    sums up all single digits of n, this becomes a new n,
    if new n is not a single digit, sums up all single digits of new n etc
    when new n is a single digit number, if it is a multiple of 3, (3, 6, or 9)
    the original n is divisible by 3
    """

    while len(str(n)) > 1:
        single_digit_n = [int(i) for i in str(n)]
        n = sum(single_digit_n)

    return n in [3, 6, 9]


def divisible_by_5(n):
    """
    if the last digit in n is 0 or 5, n is divisible by 5
    """

    return int(str(n)[-1]) in [0, 5]


def fizz_buzz_3(n):
    """
    using functions to determine the divisibility, not the modulo operator
    returns Fizz if n is a multiple of 3
    returns Buzz if n is a multiple of 5
    returns FizzBuzz if n is a multiple of 3 and 5
    returns n otherwise
    """

    if divisible_by_3(n) and divisible_by_5(n):
        return("FizzBuzz")
    elif divisible_by_3(n):
        return("Fizz")
    elif divisible_by_5(n):
        return("Buzz")
    else:
        return(n)
# ---------------------------  END fizz_buzz_3(n)  ---------------------------

def fizz_buzz():
    """
    for fizz_buzz1, fizz_buzz_2 and fizz_buzz_3,
    prints out numbers from 1 to 100, except for when the number is a:
    multiples of three when “Fizz” is printed instead of the number
    multiples of five when “Buzz” is printed instead of the number
    multiples of both three and five when “FizzBuzz” is printed
        instead of the number
    + added some grids for presentation
    """
    column_w = 15
    h_div = '-' * column_w
    h_fill = ' ' * column_w
    print("\n+{0}+{0}+{0}+".format(h_div))
    print("|{:^{column_w}}|{:^{column_w}}|{:^{column_w}}|".
    format('fizz_buzz_1:', 'fizz_buzz_2:', 'fizz_buzz_3:', column_w = column_w))
    print("+{0}+{0}+{0}+".format(h_div))
    print("|{0}|{0}|{0}|".format(h_fill))
    print("+{0}+{0}+{0}+".format(h_div))

    for i in range(1, 101):
        f_b1 = fizz_buzz_1(i)
        f_b2 = fizz_buzz_2(i)
        f_b3 = fizz_buzz_3(i)

        assert (f_b1 == f_b2), "If you read this, there is a bug in fizz_buzz_2!"
        assert (f_b1 == f_b3), "If you read this, there is a bug in fizz_buzz_3!"

        print("|{:^{column_w}}|{:^{column_w}}|{:^{column_w}}|".
        format(f_b1, f_b2, f_b3, column_w = column_w))
        if i % 10 == 0:
            print("+{0}+{0}+{0}+".format(h_div))
    print("+{0}+{0}+{0}+\n".format(h_div))


if __name__ == '__main__':
    fizz_buzz()
