    

donors= {'Joe':[1,4,200],'Jack':[4,5], 'Jill':[400], 'Jake':[.30],'Jim':[1,2,1.04]}

while True:
    response=input('Type 1 to Send a Thank You, 2 to Create a Report, or 3 to quit?')

    if response == '1':
        print('Ok, you chose 1, lets see what we can do.')
        while True:
            name=input('Type the full name? > ')
            #See if they want a list of names.
            if name != 'list':
                break
            for x in donors:    
                print(x)
    #Add Name to list if not in list
        if name not in donors:
            print('Name is not there, added to the list')
            donors[name]=[0]
        amount=input('\n''What is the donation amount?')
        new_amount=[float(amount)]
        old_amount=donors[name]
        donors[name]=old_amount+new_amount
        print('Thank you so much for the generous gift of ${0:.2f}, {1}!'.format(float(amount),name))
    
    if response == '2':
        print('Ok, you chose 2, lets get on that')
    
    if response == '3':
        print('Ok, so you want to quit')
        break
    else:
        print('\n''Choose a number again')
        

