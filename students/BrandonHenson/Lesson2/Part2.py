def print_grid(n):
    plus = '+'
    minus = '-'
    pipe = '|'
    space = ' '
    numofminus = int(n/2)
    top1 = space+ plus + minus * numofminus + plus + minus * numofminus + plus
    top = plus + minus*numofminus + plus + minus*numofminus + plus
    middle = pipe + space*numofminus + pipe + space*numofminus + pipe
    print(top1,'\n',middle,'\n',top,'\n',middle,'\n',top)

