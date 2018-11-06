def print_4by4_grid(n):
    """Print a 4-by-4 grid with each block size n."""
    
    if (n <= 0) or (n - n//1 > 0):
        return
    
    horizontal_line = '+ ' + n * '- ' + '+ ' + n * '- ' + '+'
    vertical_line = '| ' + n * '  ' + '| ' + n * '  ' + '|'
    
    print(horizontal_line)
    
    for block in range(2):
        
        for k in range(n):
            print(vertical_line)
       
        print(horizontal_line)
        

def print_grid(n_blocks,size):
    """Prints a n_blocks-by-n_blocks grid with each block size "size"."""
    
    if (n_blocks <= 0) or (size <= 0) or (
        n_blocks - n_blocks//1 > 0) or (size - size//1 > 0):
        return
    
    horizontal_line = n_blocks * ('+ ' + size * '- ') + '+'
    vertical_line = n_blocks * ('| ' + size * '  ') + '|'
    
    print(horizontal_line)
    
    for block in range(n_blocks):
        
        for k in range(size):
            print(vertical_line)
            
        print(horizontal_line)