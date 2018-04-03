'''
Brandon Henson
3/31/18
Lesson 2 Part 1
Making a grid
Brandon ChangedFunGrid to fun_grid 4/1/18
'''


def fun_grid():
    # define a bunch of characters that are used
    # plus symbol used in the tops
    plus = '+'
#   minus symbol used in the tops
    minus = '-'
#   line symbol used for the columns
    pipe = '|'
#   space used everywhere
    space = ' '
#   concatenated symbols to make the horizontal "tops" as I call them
    horiz = plus + minus*4 + plus + minus*4 + plus
#   concatenated symbols to make the sides
    vert = pipe + space*4 + pipe + space*4 + pipe
#   print our grid
    print(horiz)
    print(vert)
    print(vert)
    print(vert)
    print(vert)
    print(horiz)
    print(vert)
    print(vert)
    print(vert)
    print(vert)
    print(horiz)
#   call the function
fun_grid()
