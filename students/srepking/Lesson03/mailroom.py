
def thank_you():
    print('\n''Ok, you chose 1, lets see what we can do.')
    while True:
        name = input('\n''Type the full name to add entry, \'list\' to see list of names, or \'e\' to exit: > ')
        # See if they want a list of names.
        if name != 'list':
            break
        for x in donors:    
            print(x)
    # Add Name to list if not in list
    if name not in donors and name != 'e':
        print('Name is not there, added to the list')
        donors[name] = []
    if name != 'e':
        amount=input('\n''What is the donation amount? or \'e\' to exit >')
        if amount != 'e':
            new_amount = [float(amount)]
            old_amount = donors[name]
            donors[name] = old_amount+new_amount
            print('Thank you so much for the generous gift of ${0:.2f}, {1}!'.format(float(amount),name))


def report():
        print('\n''Ok, you want to create a report, here it is:')
        # Create a new dictionary with Total, number of donations, and average donation amount
        donors_f = {}
        for name, donations in donors.items():
            # Calculate total donation amount
            total = 0
            count = 0
            average = 0
            i = 0
            for i in donations:
                total = total+i
            # Calculate total number of donations, not counting $0
            for i in donations:
                if i != 0:
                    count = count+1
            #Calculate total donation amount
            if count > 0:
                average = total/count
            donors_f[name] = [total, count, average]
        print('\n')
        # Find the longest name in the list to format column width
        name_list = list(donors_f.keys())#creates a list of keys
        name_wi = 11
        for i in name_list:
            if len(i) > name_wi:
                name_wi = (len(i))  # width of name column
        # Find the longest donation amount
        tot_wi = 12
        ave_wi = 12
        num_wi = 12
        for name, summary in donors_f.items():
            if len(str(summary[0])) > tot_wi:
                tot_wi = (len(str(summary[0])))+3# width of total column
            if len(str(summary[1])) > num_wi:
                num_wi = (len(str(summary[1])))+3 #width of number of donations column
            if len(str(int(summary[2]))) > ave_wi:
                ave_wi = (len(str(int(summary[2]))))+3 #width of total average column
        list_sorted = sorted(donors_f,key = donors_f.__getitem__, reverse = True)
        #Print the Table
        print(f"{'Donor Name':{name_wi}}| {'Total Given':^{tot_wi}}| {'Num Gifts':^{num_wi}}| {'Average Gift':^{ave_wi}}")
        print(f"{'-':-^{(name_wi+tot_wi+ave_wi+num_wi+8)}}")
        #print("-")
        for key in list_sorted:
            temp=donors_f[key]
            print(f"{key:{name_wi}}${temp[0]:{tot_wi}}{temp[1]:^{num_wi}}   ${temp[2]:>{ave_wi}.2f}")

        print('\n')
  

if __name__ == '__main__':
    donors= {'Joe Edgar Allen Poe the Third ':[1,4,200],'Jack':[4,5], 'Jill':[4], 'Jake':[.30],'Jim':[1,2,1.04]}
    while True:
        response = input('Type \'1\' to Send a Thank You, \'2\' to Create a Report, or \'3\' to quit?')
        if response == '1':
            thank_you()
        elif response == '2':
            report()
        elif response == '3':
            print('Goodbye!')
            break
        

