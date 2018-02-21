# prints a static grid

def pluses_print():
    pluses = "+ - - - - + - - - - +"
    print(pluses)

def pipe_print():
    pipe_count = 4
    pipes = "|         |         |"
    
    while pipe_count>0:
        print(pipes)
        pipe_count = pipe_count-1
        
pluses_print()
pipe_print()
pluses_print()
pipe_print()
pluses_print()
