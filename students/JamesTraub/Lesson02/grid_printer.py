# chose to divide n by 2 to give columns an even width

def print_grid(n):
    pls = '+'
    mns = '-'
    pl = '|'
    spc = ' '
    dventry = n // 2
    grdsz = (dventry * mns)
    spcsz = (dventry * spc)
    plsln = (pls + grdsz + pls + grdsz + pls)
    plline = (pl + spcsz + pl + spcsz + pl)
    print(plsln)
    for i in range(dventry):
        print(plline)
    print(plsln)
    for i in range(dventry):
        print(plline)
    print(plsln)

print_grid(8)
