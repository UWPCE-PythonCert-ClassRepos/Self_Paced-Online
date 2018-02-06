################################PART1###################################
def part1():
    plus = '+'
    minus = '-'
    space = ' '
    vertical = '|'

    print(plus + 4*(space + minus + space) + plus + 4* (space + minus + space) + plus)
    for i in range(4):
        print(vertical + 4*(3*space) + vertical + 4*(3*space) + vertical)
    print(plus + 4*(space + minus + space) + plus + 4* (space + minus + space) + plus)
    for i in range(4):
        print(vertical + 4*(3*space) + vertical + 4*(3*space) + vertical)
    print(plus + 4*(space + minus + space) + plus + 4* (space + minus + space) + plus)
################################PART1###################################

################################PART2###################################
def print_grid(size):
    plus = '+'
    minus = '-'
    space = ' '
    vertical = '|'
    multiplicator = int(size/float(2))

    print(plus + multiplicator*(space + minus + space) + plus + multiplicator* (space + minus + space) + plus)
    for i in range(multiplicator):
        print(vertical + multiplicator*(space + space + space) + vertical + multiplicator* (space + space + space) + vertical)
    print(plus + multiplicator*(space + minus + space) + plus + multiplicator* (space + minus + space) + plus)
    for i in range(multiplicator):
        print(vertical + multiplicator*(space + space + space) + vertical + multiplicator* (space + space + space) + vertical)
    print(plus + multiplicator*(space + minus + space) + plus + multiplicator* (space + minus + space) + plus)

def part2():
    print_grid(8)
################################PART2###################################

################################PART3###################################
def print_grid2(cubesize,cellsize):
    plus = '+'
    minus = '-'
    space = ' '
    vertical = '|'
    multiplicator = cellsize

    for i in range(cubesize):
        print(plus + cubesize * (multiplicator*(space + minus + space) + plus))
        for i in range(multiplicator):
            print(vertical + cubesize*(multiplicator*(space + space + space) + vertical))
    print(plus + cubesize * (multiplicator*(space + minus + space) + plus))


def part3():
    print_grid2(3,4)
################################PART3###################################

part1()
print()
part2()
print()
part3()
