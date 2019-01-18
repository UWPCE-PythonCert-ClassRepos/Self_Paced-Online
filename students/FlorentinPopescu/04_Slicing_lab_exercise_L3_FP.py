# -*- coding: utf-8 -*-
"""
Created on Tue Jan 8 20:17:44 2019
@author: Florentin Popescu
"""

#===================LESSON_03====================
# Slicing lab exercise---------------------------
#================================================

#------------------------------------------------
# PART A - with the first and last term exchanged
#------------------------------------------------
def exchange_first_last(x):
    if type(x) == str:
        print('String entered:', x)
        if len(x) == 1:
            print('A single character exchanged is the character itself.') 
            return(x)
        else:   
            #Option1
            return "".join([x[-1], x[1:len(x)-1], x[0]])
            #Option2
            #lst = list(x)
            #return "".join([lst[-1]] + lst[1:len(x)-1] + [lst[0]])
            #Option3
            #return x[-1] + x[1:len(x)-1] + x[0]
    elif type(x) == tuple:
        print('Tuple entered:', x)
        return (x[-1],) + x[1:len(x)-1] + (x[0],) 
    elif type(x) == list:
        print('List entered:', x)
        if len(x) == 1:
            print('A single-element list exchanged is the single-element list itself.') 
            return(x)
        #option 1
        return [x[-1]] + x[1:len(x)-1] + [x[0]]
        #option 2
        #return [x.pop()] + x[1:len(x)] + [x.pop(0)]
    elif type(x) == int or type(x) == float:
        print("A single int or float number exchanged is the number itself.")
        return None
    
#tests    
#passing string argument
exchange_first_last('this is a string')
#passing tuple argument
exchange_first_last((2, 54, 13, 12, 5, 32))
#passing list argument
exchange_first_last([2, 54, 13, 12, 5, 32])
#passing single int or float arguments
exchange_first_last(2)

#additional exercises
exchange_first_last('t')
exchange_first_last((2))
exchange_first_last([2])
 
#Note:
# When passing a single float (say, 2.321), one can convert the float into string 
# using str() and then exchange the first character of string '2.321' resulting 
# in string '1.322' and use float('1.322') to convert it back to a number.
#------------------------------------------------

#------------------------------------------------
# PART B - with every other term removed
#------------------------------------------------
def every_other_removed(x):
    if type(x) == str:
        print('String entered:', x)
    elif type(x) == tuple:
        print('Tuple entered:', x)
    elif type(x) == list:
        print('List entered:', x)
    elif type(x) == int or type(x) == float:
        print("Single int or float entered; nothing to remove.")
        return None
    #option1
    #keep characters in the string with even positional index.
    return x[0:len(x):2] 
    #option2    
    #keep characters in the string with odd positional index.  
    #return x[1:len(x):2] 
    
#tests    
#passing string argument
every_other_removed('this is a string')
#passing tuple argument
every_other_removed((2, 54, 13, 12, 5, 32))
#passing list argument
every_other_removed([2, 54, 13, 12, 5, 32])
#passing single int or float arguments
every_other_removed(2)

#------------------------------------------------

#------------------------------------------------
# PART C - with the first 4 and the last 4 items 
#          removed, and then every other item 
#          in between
#------------------------------------------------
def no_first_last_four_every_other_in_between(x, n = 4):
    if type(x) == int or type(x) == float:
        print("Single int or float entered; nothing to remove.")
        return None
    else:
        if len(x) < 8:
            print("Entered object of lenght {} is too short; consider adding more elements.".format(len(x))) 
            return None
        elif len(x) == 8:
            print("After removing first and last four from entered object of lenght {} there will be nothing left in between.".format(len(x))) 
        else:
            if type(x) == str:
                print('String entered:', x)
            elif type(x) == tuple:
                print('Tuple entered:', x)
            elif type(x) == list:
                print('List entered:', x)
            #Option1
            #Keep characters in the string with even positional index.
            return x[n:len(x)-n][0:len(x)-2*n:2]
            #Option2    
            #Keep characters in the string with odd positional index.  
            #return x[n:len(x)-n][1:len(x)-2*n:2]    

#tests
#passing string argument
no_first_last_four_every_other_in_between('this is a string')
no_first_last_four_every_other_in_between('this is a very long string')
#passing tuple argument
no_first_last_four_every_other_in_between((2, 54, 13, 12, 5, 32, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
#passing list argument
no_first_last_four_every_other_in_between([2, 54, 13, 12, 5, 32, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#passing single int or float arguments
no_first_last_four_every_other_in_between(2)

#additional tests
no_first_last_four_every_other_in_between('abcdefg')
no_first_last_four_every_other_in_between('abcdefgh')
no_first_last_four_every_other_in_between((2, 54, 13, 12, 5, 32, 1))
no_first_last_four_every_other_in_between((2, 54, 13, 12, 5, 32, 1, 2))
no_first_last_four_every_other_in_between([2, 54, 13, 12, 5, 32, 1])
no_first_last_four_every_other_in_between([2, 54, 13, 12, 5, 32, 1, 2])
#------------------------------------------------

#------------------------------------------------
# PART D - with the elements 
#          (characters/words if stings?) 
#          reversed (with slicing)
#------------------------------------------------
'''
a) character elements reversed
'''
def reverse_elements(x):
    if type(x) == str:
        print('String entered:', x)
    elif type(x) == tuple:
        print('Tuple entered:', x)
    elif type(x) == list:
        print('List entered:', x)
        #alternative to slicing - reversing list in place 
        #x.reverse()
        #return x
    elif type(x) == int or type(x) == float:
        print("Single int or float entered; {} \nReverse of a number is the number itself.". format(x))
        return x
    return x[::-1]
   
#test
#passing string argument
reverse_elements('this is a string')
#passing tuple argument
reverse_elements((2, 54, 13, 12, 5, 32))
#passing list argument
reverse_elements(x= [2, 54, 13, 12, 5, 32])
#passing single int or float arguments
reverse_elements(2)

'''
b) word elements reversed (strings only)
'''
def reverse_words(x):
    if type(x) == str:
        print('String entered:', x)
        return ' '.join(x.split()[::-1])
    else:
        print("Please enter a string.")
        return None
#test
reverse_words('this is a string')
#------------------------------------------------

#------------------------------------------------
# PART E - with the middle third, then last 
#          third, then the first third
#          in the new order 
#------------------------------------------------
def mid_last_first(x):
    if type(x) == int or type(x) == float:
       raise Warning("Single int or float entered; no slicing!")
       return None
    else:
       l, cut = len(x), len(x)//3 
       #gardians & warnings:
       if l >= 3:
           if l % 3 == 0:
               print('Object lenght > 3 and multiple of 3; all three cuts will have equal length.')
           else: 
               print('Object length > 3 but not multiple of 3; the last third will be longer than the first and second third.')
       else:
           print('since object length is less than 3 it cannot be cutted in three parts of equal lenght: please add more elements to object')
           return None
        #code; string
       if type(x) == str:
           print('String "{}" of lenght {} entered.'.format(x, l))
           if l == 3:
               return ''.join([''.join(x[1]), 
                        ''.join(x[2]),
                        ''.join(x[0])
                            ]) 
           elif l == 4 or l == 5:
               return ''.join([''.join(x[1]), 
                         ''.join(x[2:]),
                         ''.join(x[0])
                             ]) 
           else:    
               return ' '.join([''.join(x[cut:2*cut]), 
                             ''.join(x[2*cut:]),
                             ''.join(x[0:cut])
                             ])
        #code; tuple
       elif type(x) == tuple:
           print('Tuple {} of lenght {} entered.'.format(x, l))
           if l == 3:
               return (x[1],) + (x[2],) + (x[0],) 
           elif l == 4 or l == 5:
               return (x[1],) + x[2:] + (x[0],)
           else:
               return x[cut:2*cut] + x[2*cut:] + x[0:cut]
       #code; list    
       elif type(x) == list:
           print('List {} of lenght {} entered.'.format(x, l))
           return x[cut:2*cut] + x[2*cut:] + x[0:cut]  
        
    
#test
#passing string argument
mid_last_first('this is a string')
#passing tuple argument
mid_last_first((2, 54, 13, 12, 5, 32))
#passing list argument
mid_last_first([2, 54, 13, 12, 5, 32])
#passing single int or float arguments
mid_last_first(2)

#additional tests; <objects with lenght smaller than six>
#passing string argument
mid_last_first('t')
mid_last_first('th')
mid_last_first('thi')
mid_last_first('this')
#passing tuple argument
mid_last_first((2))
mid_last_first((2, 54))
mid_last_first((2, 54, 13))
mid_last_first((2, 54, 13, 12))
mid_last_first((2, 54, 13, 12, 5))
#passing list argument
mid_last_first([2])
mid_last_first([2, 54])
mid_last_first([2, 54, 13])
mid_last_first([2, 54, 13, 12])
mid_last_first([2, 54, 13, 12, 5])

#============================================
# END
#============================================