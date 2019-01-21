class A:
    
    def __init__(self, arg_in):
        self.arg = arg_in
        print("in A constructor")
        
class B(A):
    def __init__(self, arg_in):
        
        self.arg2 = "potatoes"
        print("in B constructor")
        
class C1(B):
    def __init__(self, arg_in):
        A.__init__(self,arg_in)
        print("in C1 constructor")
        
class C2(A):
    def __init__(self, arg_in):
        print("in C2 constructor")
        super().__init__(arg_in)
        
class D(B, C2):
    def __init__(self, arg_in):
        print("in D constructor")
        super().__init__(arg_in)
        
#my_isnt = C1(5)
d_inst = D(3)    
        