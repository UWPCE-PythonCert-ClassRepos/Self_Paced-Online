#List Lab

def series_1():
    """Runs series 1 tests. 
    
    Args: 
        None
    Returns: 
        None
        
    """
    
    list1 = ["Apples", "Pears", "Oranges", "Peaches"] #Create a list
    print("Current List:", list1, "\n") #Display list and then a new line

    fruit = str(input("Enter the fruit to add to the list: ")) #Ask user to add fruit to list
    list1.append(fruit) #Add fruit to end of list
    print("New List:", list1, "\n") #Display list and then a new line
    
    num = int(input("Enter the number to choose the fruit from the list: ")) #Ask user to choose number for fruit
    num -= 1 #Using -1 since items in list is chosen from index of 0
    if num < 0 : 
        print("Please enter a number of 1 or above.\n", ) #User can't choose 0 as an option
    else:
        print("Chosen Fruit:", list1[num], "\n") #Display list and then a new line
        #print(list1[num]) #Display list    
    
    list2 = ["Pineapple"] #Creating a new list to add item to existing list
    list1 = list2 + list1 #Adding item to the beginning of the list
    print("New List with Plus Method:", list1, "\n") #Display list and then a new line
    
    list1.insert(0, "Watermelon") #Using insert to add item to beginning of list
    print("New List with Insert Method:", list1, "\n") #Display list and then a new line
    
    print("Fruits that start with P:")
    for fruit in list1: #For every fruit in the list
        if fruit.startswith("P"): #If statement looks for fruits that start with P
            print(fruit, end="\n") #Prints the fruit from the list
    print()

def series_2():
    """Runs series 2 tests. 
    
    Args: 
        None
    Returns: 
        None
        
    """
    
    list1 = ["Apples", "Pears", "Oranges", "Peaches"] #Create a list
    print("Current List:", list1, "\n") #Display list and then a new line    
    
    list1.pop() #removes last item in list
    print("New List:", list1, "\n") #Display list and then a new line
    
    answer = str(input("Enter the name of the fruit to delete: "))
    if answer == "Apples":
        list1.remove("Apples")
    elif answer == "Pears":
        list1.remove("Pears")
    elif answer == "Oranges":
        list1.remove("Oranges")
    elif answer == "Peaches":
        list1.remove("Peaches")
    else:
        print("Please choose a fruit to delete that is within the list.\n")
    print("New List:", list1, "\n") #Display list and then a new line
    
def series_3():
    """Runs series 3 tests. 
    
    Args: 
        None
    Returns: 
        None
        
    """
    
    list1 = ["Apples", "Pears", "Oranges", "Peaches"] #Create a list
    print("Current List:", list1, "\n") #Display list and then a new line    
    
    for fruit in list1:
        answer = input("Do you like " + fruit.lower() + "? ")
        while answer != "yes" and answer != "no":
            answer = input("Please answer between yes or no.\n")
        if answer == "no": 
            list1.remove(fruit)
    print("New List:", list1, "\n") #Display list and then a new line
    
def series_4():
    """Runs series 4 tests. 
    
    Args: 
        None
    Returns: 
        None
        
    """
    
    list1 = ["Apples", "Pears", "Oranges", "Peaches"] #Create a list
    print("Current List:", list1, "\n") #Display list and then a new line
    
    fruits = [item[::-1] for item in list1] #Reverse each item in the list but order stays the same
    list1.pop()
    print("New List in Reverse:", fruits, "\n") #Display list and then a new line
    print("Original List:", list1, "\n") #Display list and then a new line
    
if __name__ == "__main__":
    #Perform series 1-4
    print("***************************************************************************")
    print("Series 1: ")
    series_1()
    print("***************************************************************************")
    print("Series 2: ")
    series_2()
    print("***************************************************************************")
    print("Series 3: ")
    series_3()    
    print("***************************************************************************")
    print("Series 4: ")
    series_4()
    print("***************************************************************************")