#!/usr/bin/env python3
#---------------------Set-up----------------------------------#
#  MailRoom II exercise lesson 04
print('Your desktop has been up-dated with the Donations Management II applicaton.\n'
'We trust you will appreciate the added menue options and snappy output.\n'
'select history report option if a list of donors is needed.\n'
'Try out the new features.\n')

import os #opens access to file creation and placement

#-------Library and definitions-----------------------------------#
d_dict = {
'Bob Williams': [5580.00, 3245.50, 1000],
'Tom Haskell':[345.05, 3245.90, 243.05],
'Earl Jackson':[4553.45, 45.6, 345.00],
'Les Thomas':[8934.00, 325.00, 3665.00],
'James Black':[154, 1300, 21],
'Ed Jones':[35, 1]}

# experimental course exercise - recorded, but not applied:
#d_name = {'first_name': 'Bob', 'last_name': 'Williams'}
#print('My name is {first_name} {last_name}'.format(**d_name))

choice= ("Please select:\n"
    "     1    to enter a new donation (and send a thank you letter)\n"
    "     2    for a report of donors and gift history\n"
    "     3    to generatea thank you letters for all doners \n"
    "     4    to quit\n"
    " your selection:")

letter = ("Dear {},\n"
   "\t Thank you for your very kind donation of $ {}.\n"
   "It will be put to very good use.\n\n"
   "\t\t Sincereley,\n"
   "\t\t   -The Team")

#-------------------------------Functions----------------------#

def hist_rpt():   #Prepare list of donors, sorted by sum donation
    print("|   DonorName    | TotaL Given | Num Gifts   | Avrage Gift |")
    print("|----------------|-------------|-------------|-------------|")
    d_srt = {}
    for name in d_dict:
        tot = sum(d_dict[name])
        d_srt[name]=tot
    ordered = sorted(d_srt, key=d_srt.__getitem__, reverse=True)
    for name in ordered:
        t_val=d_srt[name]
        n_o_d=len(d_dict[name])
        s_avg= t_val/n_o_d
        print("|{:^16}|{:>13,.02f}|{:^13}|{:>13,.02f}|".format(name, t_val, n_o_d, s_avg))
        print("|----------------|-------------|-------------|-------------|")        
    
def menu_select(choice):  #select and apply menu  (build in entry audit)
    while True:
        pick=input(choice)
        while pick not in['1', '2', '3', '4']:
            menu_select(choice)
        if pick =='4':
            print('So long.....')
            break
        menu[pick]()   
    
def thank_you(whom, dols):  # Prepare single or collective set of thank_ you letters 
    send = input('Do you wnat thak You letters stored as .txt files in a directory? (y/n):')
    if send == "y":
#       direct = input('Type directory name (retrun blank for current directory):')
#  The line above was to build sub-diector of current. 'coiuld not figure this one out.        
        direct = ""
    if whom =='***':#Prepare text of T/U letters for all donors showing summary amounts
        for name in d_dict:
            amt = sum(d_dict[name])
            if send == "y":
                destination=os.path.join(direct,"{}.txt".format(name))
                with open(destination, 'w') as f:
                    f.write(letter.format(name, amt))
            else: #screen display of all T/U letters
                print(letter.format(name, amt))
    else: #Prepare single T/U letter in text form, for a single donation
        if send == "y":
            destination=os.path.join(direct,"{}.txt".format(whom))
            with open(destination, 'w') as f:
                f.write(letter.format(whom, dols))
        else:  #screen display of single T/U letters
            print(letter.format(whom, dols))          
    if send == "y":
        print('\n Done. See directory for text files generated.\n')
#outfile = open(whom+'.txt', 'w')
        
        
def thank_all(): #label request for generating all T/U letters
    thank_you('***','$$$')

def add_new(dnr, dols):  # Create new donor or add to current donor      
    if dnr in d_dict:
        print('---', dnr)
        d_dict[dnr].append(float(dols))
    else:
        d_dict[dnr]=[float(dols)]
    print('A Thank You letter is automatically prepared for each new donation.')
    thank_you(dnr, dols)
    
def new_don(): #New donation entry
    donor = input('Please, enter first and last_name of the donor:')
    amt= input('Please enter the amount of the donation:')
    if amt.isnumeric():
        add_new (donor, amt)
    else:
        print('Something went wrong...')
        new_don()
  
menu = {"1": new_don,  #menud directs Function calls
        "2": hist_rpt,
        "3": thank_all,
        "4": exit}                   

if __name__ == "__main__":
    menu_select(choice)