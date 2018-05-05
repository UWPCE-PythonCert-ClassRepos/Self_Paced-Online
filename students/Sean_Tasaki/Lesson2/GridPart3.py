def gridPatternPart3(rc, s):
    
    x = ' -' * s
    line = '|'
    space = ' ' * (s * 2 + 1)
    plus = '+'
    
    string1 = (line + space) * rc + line + "\n"
   
    string2 = (plus + x + " ") * rc + plus + "\n"
    
    print((string2 + (string1 * s)) * rc + string2)
    
       
gridPatternPart3(5, 3)