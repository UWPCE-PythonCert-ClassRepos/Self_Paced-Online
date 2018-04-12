def printnewrow(size):
    plus = "+"
    minus = "-"
    bar = "|"
    i = size
    while(i>0):
        print (bar + " "*size + bar  + " "*size + bar)
        i -= 1

def draw_grid(x,y):
    
    plus = "+"
    minus = "-"
    bar = "|"
    print (plus + minus*y + plus + minus*y + plus)
    while (x>0):
        x -= 1
        printnewrow(y)
        print (plus + minus*y + plus + minus*y + plus)


def main():
    draw_grid(2,4)

if __name__ == "__main__":
    main()
    
