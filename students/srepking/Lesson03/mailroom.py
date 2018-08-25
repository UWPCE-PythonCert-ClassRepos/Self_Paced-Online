    

donors= {'Joe':[1,4,200],'Jack':[4,5], 'Jill':[40000], 'Jake':[.30],'Jim':[1,2,1.04]}

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
        print('\n''Ok, you want to create a report, lets get on that')
		#Create a new dictionary with Total, number of donations, and average donation amount
        donors_f={}
        for name, donations in donors.items():
            #Calculate total donation amount
            total=0
            count=0
            average=0
            i=0
            for i in donations:
                total=total+i
            #Calculate total number of donations, not counting $0
            for i in donations:
                if i != 0:
                    count=count+1
            #Calculate total donation amount
            average=total/count
            donors_f[name]=[total, count, average]
        print('\n')
        #Find the longest name in the list to format column width
        name_list=list(donors_f.keys())#creates a list of keys
        name_wi=0
        for i in name_list:
            if len(i) > count:
                name_wi=len(i)+2  #width of name column
        #Find the longest donation amount
        tot_wi=0 
        ave_wi=0 
        num_wi=0    
        for name, summary in donors_f.items():
            if len(str(summary[0]))>tot_wi:
                tot_wi=int(len(str(summary[0])))+2# width of total column
            if len(str(summary[1])) > num_wi:
                num_wi = int(len(str(summary[1])))+4 #width of number of donations column
            if len(str(summary[2])) > ave_wi:
                print(str(summary[2]))
                ave_wi = int(len(str(summary[2])))+5 #width of total average column
        list_sorted=sorted(donors_f,key = donors_f.__getitem__, reverse = True)
        for key in list_sorted:
            temp=donors_f[key]
            print(f"{key:{name_wi}}${temp[0]:{tot_wi}}{temp[1]:^{num_wi}}${temp[2]:>{ave_wi}.2f}")

        print('\n')
        print(ave_wi)
        
                    
    
    if response == '3':
        print('Ok, so you want to quit')
        break
    else:
        print('\n''Choose a number again')
        

