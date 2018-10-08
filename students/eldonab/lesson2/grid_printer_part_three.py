#Here is my solution:

def block(n,m):
    for i in range(n):
        print("+" + (" -")*m, end =" ")
    print(" +")
    for i in range(m):
        for i in range(n):
            print("|"+" "*(m*2), end = " ")
        print(" |")
  
  

def grid(n, m):
    for i in range(n):
        block(n,m)
    for i in range(n):
        print("+" + (" -")*m, end =" ")
    print(" +")







grid(3, 4)
grid(5, 8)