def print_grid(n):
    plus="+ "
    dash="- "
    row_1=plus+dash*n
    row=row_1*2+plus
    column_1="| "+"  "*n
    column=column_1*3
    print(row)
    for i in range(2):
        for i in range(n):
            print(column)
        print(row)

def print_grid2(x,y):
    plus="+ "
    dash="- "
    row_1=plus+dash*y
    row=row_1*x+plus
    column_1="| "+"  "*y
    column=column_1*(x+1)
    print(row)
    for i in range(x):
        for i in range(y):
            print(column)
        print(row)
