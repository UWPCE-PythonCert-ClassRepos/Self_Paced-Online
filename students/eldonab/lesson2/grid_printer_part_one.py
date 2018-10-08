
# First Method:
# def grid_printer(n):
#     if n%2 == 0:
#         print("+" + " -"*(n//2) + " +"+ " -"*(n//2)+ " +")
#         for i in range(n//2):
#             print(("|" + (n+1)*" " + "|" + (n+1)*" " + "|"))
#         print("+" + " -"*(n//2) + " +"+ " -"*(n//2)+ " +")
#         for i in range(n//2):
#             print(("|" + (n+1)*" " + "|" + (n+1)*" " + "|"))
#         print("+" + " -"*(n//2) + " +"+ " -"*(n//2)+ " +")
#     elif n%2 != 0:
#         print("+" + " -"*((n-1)//2) + " +" + " -"*((n-1)//2) + " +")
#         for i in range((n-1)//2):
#             print(("|" + " "*n+ "|" + " "*n + "|"))
#         print("+" + " -"*((n-1)//2) + " +" + " -"*((n-1)//2) + " +")
#         for i in range((n-1)//2):
#             print(("|" + " "*n + "|" + " "*n + "|"))
#         print("+" + " -"*((n-1)//2) + " +" + " -"*((n-1)//2) + " +")




# grid_printer(9)
# grid_printer(8)

# Second Method - the same code as above after some refractoring.
def row_even(n):
    print("+" + " -"*(n//2) + " +"+ " -"*(n//2)+ " +")

def column_even(n):
    print(("|" + (n+1)*" " + "|" + (n+1)*" " + "|"))

def row_odd(n):
     print("+" + " -"*((n-1)//2) + " +" + " -"*((n-1)//2) + " +")

def column_odd(n):
      print(("|" + " "*n + "|" + " "*n + "|"))


def grid_printer(n):
    if n%2 == 0:
        row_even(n)
        for i in range(n//2):
            column_even(n)
        row_even(n)
        for i in range(n//2):
            column_even(n)
        row_even(n)
    if n%2 != 0:
        row_odd(n)
        for i in range((n-1)//2):
            column_odd(n)
        row_odd(n)
        for i in range((n-1)//2):
            column_odd(n)
        row_odd(n)

grid_printer(8)
grid_printer(15)
