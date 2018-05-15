def print_grid(a):
    line = '- '
    plus = '+'
    pipe = '|'
    spacing = ' '
    spacing = spacing * a * 2
    piping = pipe+spacing
    piping_full = piping * (a + 1)
    line_print = line * a
    full_line = plus+line_print
    for i in range(a):
        print('')
        for i in range(a):
            print(full_line,end='')
        print(plus,end='')
        for j in range(a):
            print('')
            print(piping_full,end='')
    print('')
    for l in range(a):

            print(full_line,end='')
    print(plus,end='')







