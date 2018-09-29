#standard 8x8 grid
def grid():
    plus_ = '+ '
    dash_ = '- '
    line_ = '|'
    spaces_9 = '         '
    print(plus_ + (dash_ * 4) + plus_ + dash_ * 4 + plus_)
    print(line_ + spaces_9 + line_ + spaces_9 + line_)
    print(line_ + spaces_9 + line_ + spaces_9 + line_)
    print(line_ + spaces_9 + line_ + spaces_9 + line_)
    print(line_ + spaces_9 + line_ + spaces_9 + line_)
    print(plus_ + (dash_ * 4) + plus_ + dash_ * 4 + plus_)
    print(line_ + spaces_9 + line_ + spaces_9 + line_)
    print(line_ + spaces_9 + line_ + spaces_9 + line_)
    print(line_ + spaces_9 + line_ + spaces_9 + line_)
    print(line_ + spaces_9 + line_ + spaces_9 + line_)
    print(plus_ + (dash_ * 4) + plus_ + dash_ * 4 + plus_)

#custom grid depending on number that is input
def print_grid(n):
    plus_ = '+ '
    dash_ = '- '
    line_ = '|'
    if n % 2 == 0:
        spaces_ = ' ' * (n + 1)
    else:
        spaces_ = ' ' * n
    if n % 2 == 1:
        n -= 1
    mid = n / 2
    mid = int(mid)
    print(plus_ + (dash_ * mid) + plus_ + (dash_ * mid) + plus_)
    for x in range(0, n):
        print(line_ + spaces_ + line_ + spaces_ + line_)
        if mid == x + 1:
            print(plus_ + (dash_ * mid) + plus_ + (dash_ * mid) + plus_)
    print(plus_ + (dash_ * mid) + plus_ + (dash_ * mid) + plus_)