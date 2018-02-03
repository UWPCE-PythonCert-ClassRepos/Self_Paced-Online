def gprint(number, unit):
    '''
    print a grid with <number> rows and 
    columns and <unit> width and height.
    '''

    aPart = '+' + unit * '-'
    bPart = '|' + unit * ' '

    aFull = number * aPart + '+'
    bFull = number * bPart + '|'

    print(aFull)

    for n in range(number):
        for i in range(unit):
            print(bFull)
        print(aFull)

if __name__ == '__main__':
    print('i wanna be a module, please import me!')
