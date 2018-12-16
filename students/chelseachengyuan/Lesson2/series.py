# def fibonacci(n):
#     x=0
#     y=1
#     if n == 0:
#         return x
#     elif n==1:
#         return y
#     else:
#         for i in range (0,n-1):
#             z=x+y
#             x=y
#             y=z
#
#         return y
# print(fibonacci(3))

# def lucas(n):
#     x=2
#     y=1
#     if n == 0:
#         return x
#     elif n==1:
#         return y
#     else:
#         for i in range (0,n-1):
#             z=x+y
#             x=y
#             y=z
#
#         return y
# print(lucas(4))



def sum_series(n,x=0,y=1):

    if n == 0:
        return x
    elif n==1:
        return y
    else:
        for i in range (0,n-1):
            z=x+y
            x=y
            y=z

        return y
print(sum_series(4))