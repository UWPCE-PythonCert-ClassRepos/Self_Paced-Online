# chose to divide n by 2 to give columns an even width

def print_grid(n,s):
    pls = '+'
    mns = '-'
    pl = '|'
    spc = ' '
    dventry = s
    grdsz = (dventry * mns)
    spcsz = (dventry * spc)
    plsln = (pls + grdsz + pls + grdsz + pls)
    plline = (pl + spcsz + pl + spcsz + pl)
    for b in range(n):
        print(plsln)
        for r in range(n):
            print(plline)
    print(plsln)

print_grid(4,6)
