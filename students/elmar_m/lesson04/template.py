#!/usr/bin/env python3

'''
This is just a personal reminder, kind of collection of idea's what 
might be a good way to structure the code. Subject to change as 
enlightenment proliferates ... :)
'''

var1 = 'foo'
var2 = 'bar'


def func1():
    '''
    Single function acting as building brick. This kind of
    function always should end with a 'return' statement, returning
    an item / object which is then the starting point of subsequent operations. 
    '''
    return 'something'


def func2(a, b):   
    '''
    Single function acting as building brick. This kind of
    function always should end with a 'return' statement, returning
    an item / object which is then the starting point of subsequent operations. 
    '''
    (local vars a, b)
    return an_object
    

def func3():
    '''
    Single function acting as building brick. This kind of
    function always should end with a 'return' statement, returning
    an item / object which is then the starting point of subsequent operations. 
    '''
    return another_object


def main():
    '''
    Here the main action / logic of the program
    happens. This is the place where the building bricks
    are used and put together; where interconnecting steps glue them
    together and other intermediate variables are used when
    necessary.
    Use variables to get the results of functions described above. Pass
    this variables here from step to step.
    The end of the main function should be the end of the program. Not
    necessarily ending in a 'return' statement.
    '''
    foovar = func1()
    bazvar = func2(var1, var2)

    zupvar = bazvar.method().method()
    
    result = zupvar + 'whatever'
    
    print('this is the result of everything', result)


if __name__ == '__main__':
    ''' 
    The 'name equals main' statement should only lead to execution 
    of the single main() function of the program
    '''
    main()






