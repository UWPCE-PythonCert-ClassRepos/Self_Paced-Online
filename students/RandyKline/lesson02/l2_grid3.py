def print_grid3(m,n):
# Need this comment because I can't for the life of me remember the details of this function
# print grid that is m columns by m rows, with each square being n x n.
  gr_size = m
  sq_size = n
  for i in range(gr_size):
    for j in range(sq_size + 1):
      if j == 0:
        print(('+ ' + ("- "*sq_size + '+ ') * gr_size))
      else:
        print(('|' + (("  "*sq_size) + " |") * gr_size))

  print(('+ ' + ("- "*sq_size + '+ ') * gr_size))
    
print_grid3(9,4)
