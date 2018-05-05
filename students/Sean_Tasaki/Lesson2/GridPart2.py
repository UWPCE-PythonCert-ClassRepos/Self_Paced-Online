def gridPatternPart2(n):
    new = n//2
    x = ' -'
    line = '|'
    plus = '+'
    
    if n % 2 == 0:
        string1 = line + ' ' * n + ' ' + line + ' ' * n + ' ' + line + '\n'
    else:
        string1 = line + ' ' * n + line + ' ' * n + line + '\n'
    
   
    string2 = plus + x * new + ' ' + plus + x * new + ' ' + plus + '\n'
    print(string2 + string1 * new + string2 + string1 * new + string2)
    
       
gridPatternPart2(3)