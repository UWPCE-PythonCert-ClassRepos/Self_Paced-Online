#!/usr/bin/env python3
# ##########################################################################
# Written : mayc4t
# Self-paced Python, March 2018

# Goal:
# Learn the basic ins and outs of Python lists.

# ##########################################################################
# Series 1
# 
# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
# Display the list (plain old print() is fine…).

def make_series_1(l1):
    fruit_l1 = list(l1)
    
    # Ask the user for another fruit and add it to the end of the list.
    # Display the list.
    print ("\ns1--- ---\n\t{}".format(fruit_l1))
    inp = input( "\t1. Enter another ANOTHER fruit name : " )
    fruit_l1.append(inp)
    print ("\t2-->{}".format(fruit_l1))
    
    print ("\n\n\t{}".format(fruit_l1) )
    # Ask the user for a number and display the number back to the user and the.
    inp = int(input("\t1. Enter the number of your fruit: "))
    while inp >len(fruit_l1) or inp < 1:
        print ("\nError: Wrong number " )
        inp = int(input("Please re-Enter the number for your fruit : "))
    print( "\t2-->Fruit selected : {fruit}".format(fruit = fruit_l1[inp-1]))
    
    
    # Add another fruit to the beginning of the list using “+” and display the list.
    print ("\n\n\t{}".format(fruit_l1))
    inp = input( "\t1. Enter another ANOTHER fruit name : " )
    temp_list = []
    temp_list.append(inp)
    fruit_l1 = temp_list + fruit_l1
    print ("\t2--> using + : {}".format(fruit_l1))


    # Add another fruit to the beginning of the list using insert() and display the list.
    print ("\n\n\t{}".format(fruit_l1))
    inp = input( "\t1. Enter another ANOTHER fruit name : " )
    fruit_l1.insert(0, inp)
    print ("\t2--> using INSERT : {}".format(fruit_l1))
    
    # Display all the fruits that begin with “P”, using a for loop.
    print ("\n\n\t{}".format(fruit_l1))
    print ("\t: Fruits that begin with P")
    for fruit in fruit_l1:
        if fruit.lower().startswith('p'): print ("\t- ",fruit) 
        
    return fruit_l1





# ##########################################################################
def make_series_2(ll):
    
    fruit_list = list(ll)
    print ("====Original List\n{}".format(fruit_list))
    
    # Remove the last fruit from the list.
    fruit_list.pop()
    print ("\n\n\tRemove the last fruit in the list")
    print ("\t-->{}\n\t-->  No more last item )".format(fruit_list))
    
    # Ask the user for a fruit to delete, find it and delete it.
    print ("\n\n\t{}".format(fruit_list))
    inp = input("\t1. Input the fruit NAME to remove it from the list : ")
    inp = inp.strip()
    for idx, fruit in enumerate(fruit_list):
        if fruit.lower()== inp.lower(): fruit_list.pop(idx)
    print ("\t-->{}\n\t--> {} has been deleted from the list".format(fruit_list, inp))

    # (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
    print ("\n\n\t {}".format(fruit_list))
    fruit_list = fruit_list * 2
    print ("\t1. List (x2) : {}".format(fruit_list))
    inp = input("\t2. Input the fruit NAME (case sensitive) to remove it from the list : ")
    inp = inp.strip() # to remove extra prefix, postfix white space
    finp_cnt = fruit_list.count(inp)
    while( finp_cnt < 1 ):
        inp = input("\t2. REPEAT: Input the fruit NAME (case sensitive) to remove it from the list : ")
        inp = inp.strip() # to remove extra prefix, postfix white space
        finp_cnt = fruit_list.count(inp)
    
    while (finp_cnt > 0 ):
        fruit_list.remove( inp)
        finp_cnt -= 1

    print ("\t3.-->List: {}".format( fruit_list))
    print ("\t-->{}\n\t--> {} is deleted from the list".format(fruit_list, inp))


# ##########################################################################
def make_series_3(l1):
    print ("List from series 1", end='')
    print ( l1 )
    
    fruit_list = list(l1)
    for i in range(len(fruit_list)):fruit_list[i]= fruit_list[i].lower()
    print ("lower case fruit_list : {}".format(fruit_list) )
    
    for idx,fruit in enumerate( l1 ):
        fruit = fruit.lower()
        inp = input( "\tDo you like \"{}\" : ".format( fruit))
        inp = inp.strip()

        while not (inp.lower() == "no" or inp.lower() == "yes"):
            inp = input( "\tREPEAT: Do you like {} ".format( fruit))
            inp = inp.strip()
      
        if inp == "no":
            fruit_list.remove(fruit)
            print ("\t-->", fruit, "has been delelte")
        
        print ("\n\t-->Updated List : {}".format(fruit_list))


# ##########################################################################
# Series 4
# 
# Once more, using the list from series 1:
# 
# Make a copy of the list and reverse the letters in each fruit in the copy.
# Delete the last item of the original list. Display the original list and the copy.
 
def make_series_4(l1):
    print ("\tList from series 1")
    print ( l1, "\n" )

    fruit_list = list(l1)
    for idx, fruit in enumerate(fruit_list):
        ls1 = list(fruit) 
        ls2 = ls1[::-1]
        fr_str=''
        for i in range(len(ls2)): fr_str += ls2[i]
        fruit_list[idx] = fr_str

    l1.pop()
    print("\tOriginal List (after deleting the last item) {}".format(l1))
    print("\tCopy list with each fruit written revered -  {}".format( fruit_list))


 
# ##########################################################################
if __name__ == "__main__":

    l0 = ['Apples' , 'Pears', 'Oranges', 'Peaches']
    print (l0)
    l1 = make_series_1(l0)

    print ("\n\n\n----- SERIES 2 -------")
    make_series_2(l1)

    print ("\n\n\n----- SERIES 3 -------")
    make_series_3(l1)
    
    print ("\n\n\n----- SERIES 4 -------")
    make_series_4(l1)




