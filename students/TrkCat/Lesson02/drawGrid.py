def grid_part1():
    """Print a specific center divided 9 x 9 grid"""
    for line in range(21):
        if not line % 10:
            print('+' + ' -' * 4 + ' + ' + '- ' * 4 + '+')
        elif line % 2:
            print(' ' * 21)
        else:
            print('|' + ' ' * 9 + '|' + ' ' * 9 + '|')
            
            
def grid_part2(n):
    """Print a center divided n x n grid"""
    n = (n // 2) * 2 + 1
    grid_size = 2 * n + 2
    for line in range(grid_size + 1):
        if not line % (n + 1):
            print('+','- ' * (n // 2) + '+','- ' * (n // 2) + '+')
        elif line % 2:
            print(' ' * grid_size)
        else:
            print('|' + ' ' * n + '|' + ' ' * n + '|')    
    
    
def grid_part3(b,n):
    """Print an n x n grid repeated b x b times"""
    grid_size = 2 * n + 2
    for line in range(b * grid_size + 1):
        if not line % grid_size:
            print('+' + (' -' * n + ' +') * b)
        elif line % 2:
            print(' ' * (b * grid_size))
        else:
            print('|' + ('  ' * n + ' |') * b)   