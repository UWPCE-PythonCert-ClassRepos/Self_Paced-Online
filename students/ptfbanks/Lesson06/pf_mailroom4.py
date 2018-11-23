#!/usr/bin/env python3

#---------------------------
#5 - Mailroom4 updated from feedback to leson 5 entry. 
#---------------------Set-up----------------------------------#
print('Your desktop has been up-dated with the Donations Management II applicaton.\n'
'We trust you will appreciate the added menue options and snappy output.\n'
'select history report option if a list of donors is needed.\n'
'Try out the new features.\n')

#-------Import / Librarys-----------------------------------#
import os

d_dict = {
'Bob Williams': [5580.00, 3245.50, 1000],
'Tom Haskell':[345.05, 3245.90, 243.05],
'Earl Jackson':[4553.45, 45.6, 345.00],
'Les Thomas':[8934.00, 325.00, 3665.00],
'James Black':[154, 1300, 21],
'Ed Jones':[35, 1]}

choice= ("Please select:\n"
    "     1    to enter a new donation\n"
    "     2    for a report of donors and gift history\n"
    "     3    to generate thank you letters, for one or all donors\n"
    "     4    to quit\n"
    " your selection:")

letter = ("Dear {},\n"
   "\t Thank you for your very kind donation(s) totaling $ {}.\n"
   "It will be put to very good use.\n\n"
   "\t\t Sincereley,\n"
   "\t\t   -The Team")

#-------------------------Functions----------------------#
#0.0 Start- user input triggerd by execution
def menu_select(choice):  #select and apply menu
    while True:
        pick=input(choice)  #Ref: Library
        if pick =='4':
            print('So long.....')
            break
        try:     #moved to specific error prone command - corrected Mailroom 3
            menu[pick]()    #Ref: Library
        except KeyError:
            print('command not understood.  Plese try again.\n')            
#        menu_select(choice) #Remove, resolved by Try - corrected Mailroom 3

#1.0 New donation (Menu selection 1)
def new_don(): #New donation entry
    donor = input('Please, enter first and last_name of the donor:')
    amt= input('Please enter the amount of the donation:')
    if amt.isnumeric():
        add_new (donor, amt)
    else:
        print('Something went wrong...')
        new_don()
        
#1.1 New doner (Menu selection 1, new d_dict entry)
def add_new(dnr, dols):  # Create new donor or add to current donor      
    if dnr in d_dict:
        print('Added donation from ', dnr, 'of  $', (dols))
        d_dict[dnr].append(float(dols))
    else:
        d_dict[dnr]=[float(dols)]
    print('\n This donation will be added to Thank You letter sum dollars.\n')

#2.0 Donation History (Menu selection 2)
def hist_rpt():   #Prepare list of donors, sorted by sum donation
    print("|   DonorName    | TotaL Given | Num Gifts   | Avrage Gift |")
    print("|----------------|-------------|-------------|-------------|")
    d_srt = {name: sum(d_dict[name])for name in d_dict} 
    ordered = sorted(d_srt, key=d_srt.__getitem__, reverse=True)
    for name in ordered:
        t_val=d_srt[name]
        n_o_d=len(d_dict[name])
        s_avg= t_val/n_o_d
        print("|{:^16}|{:>13,.02f}|{:^13}|{:>13,.02f}|".format(name, t_val, n_o_d, s_avg))
        print("|----------------|-------------|-------------|-------------|")        
    
#3.0 prepare Thank You etters (Menu selection 3)
def thank_you():  # Prepare single or collective set of thank_ you letters 
    direct = ""
    send = input('Do you want Thank You letters stored as .txt files in a directory? ("y", for yes):')
    if send.lower() == 'y':
        print('OK, a .txt file will be generated. See directory for text files generated.\n')
    #    direct = input('Type directory name (retrun blank for current directory):')
    #---The above line is retained for future design to expand file sending optoins.
    else:
        print('OK, text is be printed on screen below for copy and pasting into an external file.')
    whom = input('For whom do you want to prepare a Thank You letter?  Enter a name or "All":')
    if whom.lower() == 'all':   #Prepare text of T/U letters for all donors showing summary amounts
        for name in d_dict:
            send_where (name, send, direct)     #Ref: 3.1
    else:                                     
        try:
            send_where(whom, send, direct)      #Ref: 3.1
        except KeyError:
            print("\n There is no record of donations by: ", whom, ".  Refresh donor report and try again.")
        #menu_select(choice) #Remove, resolved by Try - corrected Mailroom 3
        
#3.1 Create, fill, and place Thank You note
def send_where (name, send, direct):
    amt = sum(d_dict[name])  #Note: Need to reslove decimal formatting for letter
    if send.lower() == 'y':
        destination=os.path.join(direct,"{}.txt".format(name))
        with open(destination, 'w') as f:
            f.write(letter.format(name, amt))
    else:   #screen display of all T/U letters
        print(letter.format(name, amt))
        
#4.0 Quit (Menu selection 4)  - break-out from while loop in Function 0.0

#Execute
menu = {"1": new_don,
        "2": hist_rpt,
        "3": thank_you,
        "4": exit}          

if __name__ == "__main__":
    menu_select(choice)      #Ref: 0.0 - Start