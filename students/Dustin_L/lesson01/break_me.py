#!/usr/bin/env python3

def name_error():
    '''
    This function generates a NameError
    '''

    print(undefined_var)


def type_error():
    '''
    This function generates a TypeError
    '''

    s = 'string'
    x = 5
    return s + x


def syntax_error():
    '''
    This function generates a SyntaxError
    '''

    x = 5
    y = 10
    return x =!= y


def attributte_error():
    '''
    This function generates an AttributeError
    '''

    s = 'test'
    return s.generate_attribute_error()


if __name__ == '__main__':
    name_error()
    type_error()
    syntax_error()
    attributte_error()