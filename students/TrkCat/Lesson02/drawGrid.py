def gridPart1():
    """Print a specific center divided 9 x 9 grid"""
    for line in range(21):
        if not line % 10:
            print('+' + ' -' * 4 + ' + ' + '- ' * 4 + '+')
        elif line % 2:
            print(' ' * 21)
        else:
            print('|' + ' ' * 9 + '|' + ' ' * 9 + '|')
            
            
def gridPart2(n):
    """Print a center divided n x n grid"""
    n = (n // 2) * 2 + 1
    gridSize = 2 * n + 2
    for line in range(gridSize + 1):
        if not line % (n + 1):
            print('+','- ' * (n // 2) + '+','- ' * (n // 2) + '+')
        elif line % 2:
            print(' ' * gridSize)
        else:
            print('|' + ' ' * n + '|' + ' ' * n + '|')    
    
    
def gridPart3(b,n):
    """Print an n x n grid repeated b x b times"""
    gridSize = 2 * n + 2
    for line in range(b * gridSize + 1):
        if not line % gridSize:
            print('+' + (' -' * n + ' +') * b)
        elif line % 2:
            print(' ' * (b * gridSize))
        else:
            print('|' + ('  ' * n + ' |') * b)   