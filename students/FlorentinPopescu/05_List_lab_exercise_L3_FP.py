# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 21:26:32 2019
@author: Florentin Popescu
"""

#===================LESSON_03====================
# List lab exercise---------------------------
#================================================
import copy 
#function to search for the fruit in the basket 
def search_fruit(bsk, fruit):
     for i in range(len(bsk)):    
        if bsk[i] == fruit:
            flag = True
            position = i
            return flag, position
        elif i == len(bsk)-1 and bsk[i] != fruit:
            flag = False
            return flag, 
        
#function to converst every string in a list of strings to lowercase
def upper_to_lower(bsk):
    basket_lowercase = []
    for fruit in bsk:
        fruit = fruit.lower()
        basket_lowercase.append(fruit)
    return basket_lowercase 

#================================================
# SERIES 1
#================================================
basket = ["Apples", "Pears", "Oranges", "Peaches"]
print('The fruits in our basket today:\n', basket)
#------------------------------------------------

look_up = True
while look_up: 
    fruit_to_add_at_end = input('\nPlease add a new fruit to the basket:>>\n')
    #gardian
    fruit_to_add_at_end = fruit_to_add_at_end.lstrip().rstrip()
    if search_fruit(basket, fruit_to_add_at_end)[0]:
       print("\nFruit already exist in the basket and will not be appended.\n")     
    elif not search_fruit(basket, fruit_to_add_at_end)[0]:
        basket.append(fruit_to_add_at_end)
        print('\nThis is the updated basket of fruits with the newly added fruit at the end:\n', basket)
        look_up = False
#------------------------------------------------

number_in_range = True
while number_in_range:
    fruit_number = input("\nPlease enter an integer between 1 and {} to display the fruit in that position in the basket:>>\n".format(len(basket)))
    #gardian
    fruit_number = fruit_number.lstrip().rstrip()
    try:
        if 1 <= int(fruit_number) <= len(basket):
            print("The fruit in position {} in our basket {} is '{}'\n".format(fruit_number, basket, basket[int(fruit_number)-1]))
            number_in_range = False
        else: 
           print("There is no fruit in such position in the basket, please re-eneter a number between 1 and {}:>>\n".format(len(basket)))
    except:
        #print("\n")
        print('Please enter an integer!:>>\n')
#------------------------------------------------
        
look_up = True
while look_up: 
    first_fruit_added_to_begining = input('Please add a new fruit to the basket:>>\n')
    #gardian
    first_fruit_added_to_begining = first_fruit_added_to_begining.lstrip().rstrip()
    if search_fruit(basket, first_fruit_added_to_begining)[0]:
        print('Fruit already exist in the basket and will not be added.\n')     
    elif not search_fruit(basket, first_fruit_added_to_begining)[0]:
        basket = [first_fruit_added_to_begining] + basket   #addition creates a new instance of the list
        print('This is the updated basket of fruits with the newly added fruit at the begining:\n', basket)
        look_up = False
#------------------------------------------------

look_up = True
while look_up: 
    second_fruit_added_to_begining = input('\nLet us add another fruit to the basket:>>\n')
    #gardian
    second_fruit_added_to_begining = second_fruit_added_to_begining.lstrip().rstrip()
    if search_fruit(basket, second_fruit_added_to_begining)[0]:
        print('Fruit already exist in the basket and will not be added\n')     
    elif not search_fruit(basket, second_fruit_added_to_begining)[0]:
        basket.insert(0, second_fruit_added_to_begining.lstrip().rstrip()) #insert() mutates the list
        print('This is the updated basket of fruits with the newly added fruit at the begining:\n', basket)
        #print("\n")
        look_up = False

#nmaking an alias of output list of Series 1 for use in Series3 and Series 4
basket_series1 = copy.deepcopy(basket)
#------------------------------------------------
        
print("Here are the fruits in the basket which names start with 'P':\n")    
#Option1 - loop over items
for fruit in basket:
    if fruit[0] == "P":
        #print("\n")
        print(fruit)
        print("\n")
#Option2 - loop over positional indices
#for i in range(len(basket)-1):    
#    if basket[i][0] == "P":
#        print(basket[i]) 

#================================================
# SERIES 2
#================================================
print("Here is the basket that we filled yesterday:\n{}\n" .format(basket))
#------------------------------------------------

print("Today we remove last fruit '{}'.\n".format(basket.pop()))
#------------------------------------------------

print('This is the basket after last fruit has been removed:\n', basket)
#------------------------------------------------
            
look_up = True
while look_up: 
    fruit_to_remove = input("\nPlease the name of fruit to be removed:>>\n") 
    #gardian
    fruit_to_remove = fruit_to_remove.lstrip().rstrip()
    if search_fruit(basket, fruit_to_remove)[0]:
        print('Fruit exist in the basket and will be removed\n')
        del basket[search_fruit(basket, fruit_to_remove)[1]]
        print('After we removed the fruit {}, this is what is left in the baskets:\n{}\n'.format(fruit_to_remove, basket))
        #print("\n")
        look_up = False  
    elif not search_fruit(basket, fruit_to_remove)[0]:
        print("Fruit with the name entered does not exist in the basket. Please reenter.\n")
#--------------------------------------------------
#print("\n")
print("Magically our basket doubled overtime such that now it is \n{}\n".format(basket*2))
#print("\n")
basket2 = basket*2

look_up = True
while look_up: 
    fruit_to_remove = input("Please the name of fruit to be removed:>>\n") 
    #gardian
    fruit_to_remove = fruit_to_remove.lstrip().rstrip()
    if search_fruit(basket2, fruit_to_remove)[0]:
        print('Fruit exist in the basket\n')
        indexes = [search_fruit(basket2, fruit_to_remove)[1], 
                   search_fruit(basket2, fruit_to_remove)[1] + len(basket2)//2]
        for index in sorted(indexes, reverse=True):
            del basket2[index]
        #del basket2[find_fruit(basket2, fruit_to_remove)[1]]
        #del basket2[find_fruit(basket2, fruit_to_remove)[1] + len(basket) -1]
        print('After we removed all ocurences of fruit {}, this is what is left in the double basket:\n{}'.format(fruit_to_remove, basket2))
        look_up = False  
    elif not search_fruit(basket2, fruit_to_remove)[0]:
        print("Fruit with the name entered does not exist in the basket. Please reenter.\n")
        #print("\n")
#------------------------------------------------           

#================================================
# SERIES 3
#================================================

#basket_lowercase = upper_to_lower(basket_start)
basket_lowercase = upper_to_lower(basket_series1)
j = 1
while j <= len(basket_lowercase):
    print('Do you like {}?\n'.format(basket_lowercase[j-1]))
    rerun = True
    while rerun:
        try:
            answer = input("Depending on preference, please type 'yes' or 'no':>>\n")
            if answer == 'yes':
                #gardian
                answer = answer.lstrip().rstrip()
                #print("\n")
                print("It is great you like '{}' so we'll keep it in our basket\n{}\n".format(basket_lowercase[j-1], basket_lowercase))
                rerun = False
            elif answer == 'no':
                #gardian
                answer = answer.lstrip().rstrip()
                #print("\n")
                print("Ok, will remove '{}' from basket.\n".format(basket_lowercase[j-1]))
                basket_lowercase.remove(basket_lowercase[j-1])
                print("This is our basket after removal:\n{}\n".format(basket_lowercase))
                j -= 1
                rerun = False
        except:
            print("Wrong answer; please type 'yes' or 'no'.\n")
    j += 1
#------------------------------------------------           
print("Just a reminder; this is our basket after expressing all preferences regarding fruits:\n{}\n".format(basket_lowercase))        

#================================================
# SERIES 4
#================================================

basket_series1_copy = basket_series1.copy()
for idx, fruit in enumerate(basket_series1_copy):
    fruit = fruit[::-1]
    basket_series1_copy[idx] = fruit
    
#------------------------------------------------           
#Option1 - using pop()
basket_series1.pop()
#Option2 - using slicing
#basket_series1 = basket_series1[:-1]
#Option3 - using del
#del basket_series1[-1]
#print("\n")
print("This is the original list after removing last element: \n{}, \nand this is the copy: \n{}\n".format(basket_series1, basket_series1_copy))

input("Press enter to exit ;)")
#============================================
# END
#============================================
