################################################################################
# Dictionaries 1
################################################################################
def dictionaries_1():
    # 1: Create dictionary.
    chris_dict = {
        'name':     'Chris',
        'city':     'Seattle',
        'cake':     'Chocolate'
    }
    # 2: Display dictionary.
    print(chris_dict)
    # 3: Delete cake entry from dictionary.
    del chris_dict['cake']
    # 4: Display dictionary.
    print(chris_dict)
    # 5: Add an entry for “fruit” with “Mango” and display the dictionary.
    chris_dict['fruit'] = "Mango"
    print(chris_dict)
    # 6: Display the dictionary keys.
    print(', '.join(chris_dict))
    # 7: Display the dictionary values.
    print(', '.join(chris_dict.values()))
    # 8: Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
    if 'cake' in chris_dict.keys():
        print(True)
    else:
        print("Cake not in dict keys.")
    # 9: Display whether or not “Mango” is a value in the dictionary (i.e. True).
    if 'Mango' in chris_dict.values():
        print(True)
    else:
        print("Mango not in dict values.")

################################################################################
# Dictionaries 2
################################################################################
