def print_grid2(n):

  j = n//2
  if (n % 2) != 0:
    x = n + 2
    n = n - 1
  else:
    x = n + 3

  for i in range(x):
    if i == 0:
      print('+ ' + ("- "*j) + '+ ' + ("- "*j) + "+")
    elif i == j + 1:
      print('+ ' + ("- "*j) + '+ ' + ("- "*j) + "+")
    elif i == x - 1:
      print('+ ' + ("- "*j) + '+ ' + ("- "*j) + "+")
    else:
      print('| ' + (" "*(n)) + '| ' + (" "*(n)) + "|")

print_grid2(5)
