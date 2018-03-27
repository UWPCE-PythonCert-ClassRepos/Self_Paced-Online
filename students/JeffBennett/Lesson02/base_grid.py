"""base_grid.py
Print a two cell by two cell grid of cell length 4.  Cell length refers to
total pipes on a left cell edge or total minus signs on a top cell edge.  All
cells are equal squares.
"""
plus = '+'
pipe = '|'

for x in range(2):
    print(2*(plus + ' ' + 4*('- ')) + plus)
    for y in range(4):
        print(2*(pipe + ' ' + 8*(' ')) + pipe)
print(2*(plus + ' ' + 4*('- ')) + plus)
