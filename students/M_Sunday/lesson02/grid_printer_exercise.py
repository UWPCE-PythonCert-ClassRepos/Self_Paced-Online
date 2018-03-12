def intcheck(val):
    # This checks if the input value is a non-integer and returns FALSE if it is an integer
    if ((val+1) % 2 == 0) or ((val % 2) == 0):
        return False
    else:
        return True


def grid_print(height=2, width=2, sub_height=4, sub_width=4):
    if intcheck(height):
        print("Error - Invalid Entry of", height, ": Entries Must be Whole Numbers\n")
    elif intcheck(width):
        print("Error - Invalid Entry of", width, ": Entries Must be Whole Numbers\n")
    elif intcheck(sub_height):
        print("Error - Invalid Entry of", sub_height, ": Entries Must be Whole Numbers\n")
    elif intcheck(sub_width):
        print("Error - Invalid Entry of", sub_width, ": Entries Must be Whole Numbers\n")
    else:
        plus = '+ '
        minus = '- '
        space = '  '
        vert = '| '

        bar_type1 = plus + sub_width * minus
        bar_type2 = vert + sub_width * space

        for i in range(height):
            print(width * bar_type1 + plus)
            for j in range(sub_height):
                print(width * bar_type2 + vert)
        print(width * bar_type1 + plus)
        print("\n")

def grid_print_id(n):
    if n == 8:
        grid_print(2, 2, 4, 4)
    elif n == 3:
        grid_print(2, 2, 1, 1)
    elif n == 15:
        grid_print(2, 2, 7, 7)
    else:
        print("Error - Invalid Size: Enter 3, 8, or 15\n")


def grid_print_sub(size, units):
    grid_print(size, size, units, units)


# part 1
print("-----Part 1-----\n")
grid_print()
print("----------------\n\n")


# part 2
print("-----Part 2-----\n")
grid_print_id(3)
grid_print_id(8)
grid_print_id(15)
grid_print_id(16)
print("----------------\n\n")


# part 3
print("-----Part 3-----\n")
grid_print_sub(3, 4)
grid_print_sub(3, 4.9)
grid_print_sub(5, 3)
print("----------------\n\n")
