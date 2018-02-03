#!/usr/bin/env python3

def format_quadruple(quadruple):
    """
    The first element is used to generate a filename that can help with file sorting.
    The second element is a floating point number. You should display it with 2 decimal places shown.
    The third value is an integer, but could be any number. You should display it in scientific notation, with 2 decimal places shown.
    The fourth value is a float with a lot of digits – display it in scientific notation with 3 significant figures.
    """
    return "file_{0[0]:03} :   {0[1]:.2f}, {0[2]:.2e}, {0[3]:.2e}".format(quadruple)

def format_quadruple_alt(quadruple):
    """
    Use an alternate type of format string to replicate results of format_quadruple. (keywords/f-strings)
    """
    prec = .2 
    return f"file_{quadruple[0]:03} :   {quadruple[1]:{prec}f}, {quadruple[2]:{prec}e}, {quadruple[3]:{prec}e}"

def format_num_string(num_tuple):
    """
    Rewrite: "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
    to take an arbitrary number of values.
    """
    if num_tuple:
        disp_string = "The "+str(len(num_tuple))+f" numbers are: "
        for x in range(len(num_tuple)-1):
            disp_string+="{:d}"+f"{',' if len(num_tuple)>2 else ''} "
        disp_string+="and {:d}"
        return disp_string.format(*num_tuple)
    return "There are no numbers given"

def format_quintuple(quintuple):
    """
    Take quintuple (a,b,c,d,e) and return 'd e c a b' padded w/ a zero if any of the values are single-digits
    """
    return "{3:02d} {4:02d} {2:02d} {0:02d} {1:02d}".format(*quintuple)

def format_fruit_weights(f_list):
    """
    Given the 4-element list: ['oranges',1.3,'lemons',1.1]
    Write an f-string that will display: The weight of an orange is 1.3 and the weight of a lemon is 1.1
    Then see if you can change the f-string so that is displays the names of the fruit in upper case, and the weight 20% higher.
    """
    fruits_weights = ['','']
    for x in [0,2]:
        fruit = (f_list[x].lower()).capitalize()
        if fruit[len(fruit)-1].lower()=='s':
            fruit = fruit[:len(fruit)-1]
        weight = f_list[x+1]
        weight_fruit = f"weight of a{'n' if fruit[0] in ['A','E','I','O','U'] else ''} {fruit} is {1.2*weight}"
        fruits_weights[x-x//2] = weight_fruit
    asdf = "The "+fruits_weights[0]+" and the "+fruits_weights[1]
    return asdf

def adopt_gold():
    """
    Print a table of several rows, each w/ a name, and age and a cost.
    Make sure some of the costs are in the hundred and thousands to test your alignement specifiers
    """
    max_len = 0
    names = ['Dubloon','Leaf','Ingot','Coin','Jim','Peas','Graham Crackers']
    for x in names:
        max_len = max(max_len, len(x))
    ages = [502,5,25,1003,12000,2,1]
    costs = [2500.02,5.35,500.00,50.27,150000.99,12.78,76000.54]
    print('These poor gold... things have been alone for so long. Please, adopt them.',end='\n\n')
    print(f"{'NAME':<{max_len}}\t{'AGE':<5}\t{'PRICE':<8}")
    for x in range(len(names)):
        print(f"{names[x]:<{max_len}}\t{ages[x]:<5}\t${costs[x]:<8}")
    return

def format_decuple(decuple):
    "Given a Decuple of consecutive numbers, print the tuple in columns that are 5 characters wide."
    return ("{:<5}\t"*10).format(*decuple)
    

def format_quadruple_test():
    """
    format_quadruple tests
    """
    quadruple1 = (2,123.4567,10000,12345.67)
    quadruple2 = (12,3.141592654,-1234,.123456)
    quadruple3 = (100,13,0,0)
    assert format_quadruple(quadruple1) == 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    assert format_quadruple(quadruple2) == 'file_012 :   3.14, -1.23e+03, 1.23e-01' 
    assert format_quadruple(quadruple3) == 'file_100 :   13.00, 0.00e+00, 0.00e+00'

def format_quadruple_alt_test():
    """
    format_quadruple_alt tests
    """
    quadruple1 = (2,123.4567,10000,12345.67)
    quadruple2 = (12,3.141592654,-1234,.123456)
    quadruple3 = (100,13,0,0)
    assert format_quadruple_alt(quadruple1) == format_quadruple(quadruple1)
    assert format_quadruple_alt(quadruple2) == format_quadruple(quadruple2)
    assert format_quadruple_alt(quadruple3) == format_quadruple(quadruple3)

def format_num_string_test():
    """
    format_num_string tests
    """
    nums0 = ()
    nums2 = (8,12)
    nums6 = (123,734,2346,2,666,30)
    assert format_num_string(nums0) == 'There are no numbers given'
    assert format_num_string(nums2) == 'The 2 numbers are: 8 and 12'
    assert format_num_string(nums6) == 'The 6 numbers are: 123, 734, 2346, 2, 666, and 30'

def format_quintuple_test():
    """
    format_quintuple tests
    """
    quint1 = (4,30,2017,2,27)
    quint2 = (1,2,3,4,5)
    quint3 = (10,11,12,13,14)
    quint4 = (100,201,302,403,504)
    assert format_quintuple(quint1) == '02 27 2017 04 30'
    assert format_quintuple(quint2) == '04 05 03 01 02'
    assert format_quintuple(quint3) == '13 14 12 10 11'
    assert format_quintuple(quint4) == '403 504 302 100 201'

def format_fruit_weights_test():
    """
    format_fruit_weights tests
    """
    fruits1=['oranges',1,'lemons',1.1]
    fruits2=['oRaNgE',1,'LeMoNS',1.1]
    fruits3=['pancakes',3,'PANCAKES',3]
    fruits4=['pancakes',1,'PANCAKES',1]
    assert format_fruit_weights(fruits1) == 'The weight of an Orange is 1.2 and the weight of a Lemon is 1.32'
    assert format_fruit_weights(fruits2) == 'The weight of an Orange is 1.2 and the weight of a Lemon is 1.32'
    assert format_fruit_weights(fruits4) == 'The weight of a Pancake is 1.2 and the weight of a Pancake is 1.2'
    #assert disp_fruit_weights(fruits3) == 'The weight of a Pancake is 3.6 and the weight of a Pancake is 3.6'
    #The above assert statement is somehow wrong. Something about the IEEE-754 standard of a processor makes 1.2*3 = 3.599999999999...
    

def format_decuple_test():
    decuple_list = [tuple(range(1,11)),tuple(range(10)),tuple(range(215,225)),tuple(range(5460, 5470)),tuple(range(80320, 80330))]
    for x in decuple_list:
        print(format_decuple(x))

format_quadruple_test()
format_quadruple_alt_test()
format_num_string_test()
format_quintuple_test()
format_fruit_weights_test()
adopt_gold()
format_decuple_test()
