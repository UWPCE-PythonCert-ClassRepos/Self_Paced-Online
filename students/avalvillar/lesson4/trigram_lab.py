"""
    Author is Antonio V. Alvillar
    Self-Paced-Online Python 210 UWPCE
    December 13th 2018
"""

#This will use the dictonary passed to build a new output
def create_trigram(dictionary):
    import random #Random choices for start and list item needed.
    start = random.choice(list(dictionary)) #Randomaly choose a key to start
    start_list = list(start.split()) #Split the key to add to output list
    output = [start_list[0]] #First word
    output.append(start_list[1]) #Second word
    while start in dictionary: #Loop until there is no key pair found
        #First and second kept separate as second is added to output alone.
        first = list(start.split())[1]
        second = random.choice(dictionary[start])
        start = first + ' ' + second #New starting key of (last two words)
        output.append(second) #Add new string to the output.
    with open('trigram_sherlock.txt', 'w') as out_file:
        out_file.write(' '.join(output))
    '''print()
    print(' '.join(output)) #Print to console for testing
    print()'''

#Store the text file into a list - helper function
def create_list():
    my_list = [] #Create a list of words from the file.
    with open('sherlock.txt', 'r') as in_file: #Open and read the file
        for line in in_file:
            lines = line.strip() #For each line - remove
            words = lines.split() #Split the line on spaces to make words
            for word in words:
                my_list.append(word) #Add each one to the list
    return my_list

#Starting function that will call helper functions as needed.
def begin_trigram():
    first, second, third = 0, 1, 2 #Place holders when bulding the dictionary
    temp_list = create_list() #Call function that gives us back a list
    my_dict = {} #
    size = len(temp_list) - 1
    while third <= size: #Stop before the end of the list.
        key = temp_list[first] + ' ' + temp_list[second] #create key
        if key in my_dict: #If key exist - check key's list
            if temp_list[third] not in my_dict[key]: #If new value - add.
                my_dict[key].append(temp_list[third])
        else:
            my_dict[key] = [temp_list[third]] #New key - add.
        first += 1
        second += 1
        third += 1
    '''#Block used to print the dictionary and count in a readable format.
    for item in my_dict:
        print(item, end=' : ')
        print(my_dict[item])
    print("This is how many dictionary items there are: " + str(len(my_dict)))
    print()
    '''
    create_trigram(my_dict)


#Main function to kick off the script by calling the begin_trigram function.
if __name__ == "__main__":
    begin_trigram()