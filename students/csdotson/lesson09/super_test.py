# Super Test 1
# class A():
#     def __init__(self):
#         print("in A __init__")
#         print("self's class is:", self.__class__)
#         s = super().__init__()
#
# class B():
#     def __init__(self):
#         print("in B __init__")
#         print("self's class is:", self.__class__)
#         s = super().__init__()
#
# class C():
#     def __init__(self):
#         print("in C __init__")
#         print("self's class is:", self.__class__)
#         s = super().__init__()
#
# class D(C, B, A):
#     def __init__(self):
#         print("in D __init__")
#         print("self's class is:", self.__class__)
#         s = super().__init__()

# Super Test 2
class Base():
    def this(self):
        pass # just so there is a base class that has the method

class A(Base):
    def this(self):
        print("in A.this")
        super().this()

class B(Base):
    def this(self):
        print("in B.this")
        super().this()

class C(A, B):
    def this(self):
        print("in C.this")
        # super().this()
        A.this(self)
