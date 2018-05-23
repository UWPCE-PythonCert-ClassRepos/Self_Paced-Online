"""
Print a two-row by two-column grid of cells of length 4.
Cell length refers to number of pipes on a left cell edge or number of
minus signs on a top cell edge.  Cells are formed by the intersection of
rows and columns.
"""
plus = '+'
pipe = '|'

for x in range(2):
    print(2*(plus + ' ' + 4*('- ')) + plus)
    for y in range(4):
        print(2*(pipe + ' ' + 8*(' ')) + pipe)
print(2*(plus + ' ' + 4*('- ')) + plus)
