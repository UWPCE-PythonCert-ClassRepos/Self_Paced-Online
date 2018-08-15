#  MailRoom exercise lesson03 final task
#    - Build, sort, print a table
#--------------------------Global Region-----------------------------------#
donations = [
    ("Bob Williams", 5580.00),
    ("Tom Haskell", 345.05),
    ("Earl Jackson", 4553.45),
    ("Les Thomas", 8934.00),
    ("James Black", 154),
    ("Bob Williams", 3245.50),
    ("Tom Haskell", 3245.90),
    ("Earl Jackson", 45.6),
    ("Les Thomas", 325.00),
    ("James Black", 1300),
    ("Bob Williams", 1000),
    ("Tom Haskell", 243.05),
    ("Earl Jackson", 345.00),
    ("Les Thomas", 3665.00),
    ("James Black", 21)]

#-----------------------------------Define Functions----------------------#
#Prepare list of donors
def get_names(list):
    names = []
    for entry in (list):
        name = entry[0]
        if name not in names:
            names.append(name)
    return(names)
            
def select_Key(table):
    return table[1]

#Create history report
def hist_rpt(dlist):
    names=get_names(donations)  #refresh names of donors
    print("|   DonorName    | TotaL Given | Num Gifts   | Avrage Gift |")
    print("|----------------|-------------|-------------|-------------|")
    rpt=[]      #list for report rows
    tc = 0      #set tuple member ID
    for name in (names):
        dsum =0      #set donor sum
        dc = 0       #set donations count
        tup=[]      #collector for row content
        for entry in (dlist):    #search donations ist
            donor = entry[0]
            if donor == name:
                dc=dc+1
                dval = entry[1]
                dsum = dsum + dval
        davg = dsum/dc         #calculate donor average donation
        rpt.append((name, dsum, dc, davg))  #create table entry
    rpt.sort(key=select_Key, reverse=True)   #sort descending
    for entry in rpt:
        print("|{:^16}|{:>13,.02f}|{:^13}|{:>13,.02f}|".format(*entry))
        print("|----------------|-------------|-------------|-------------|")

def send_thanks(whom, amt):
    print(f'\n Dear {whom} \n') 
    print(f'We are pleased with your generous gift of ${amt}.\n')
    print(f'Take comfort in knowing this will be put to good use.\n\n')
    print('Sincerely,   The Good Group')

#------------------------Mailroom Body of Logic--------------------------------#
#------------------User Interface--------------------------#
print("You have entered the Donation Management screen.")
stp= "c"
while stp != "q":
    stp = input("Do you want to continue? (Enter'c'-continue or 'q'-quit:")
    if stp == "q":
        break
    don_new = input ("Are you adding a new donation?(y/n)")             
    if don_new == "y":
        n_entry=[]
        need_list = input("Do you need a list of donors? (y/n):")
        if need_list == "y":
            print("Pick from a list past doners or add a new doner: \n")
            print(get_names(donations))
        whom = input("\n Enter the donors  (new or past):")
        donation = float(input("Donated amount: "))
        donations.append((whom, donation))
        print("\n 'Got it.  Thanks")
        
    need_rpt = input("\n Will you be needing a donation history report? (y/n)")
    if need_rpt == "y":
        print(hist_rpt(donations))

    need_note = input("\n Do you need to generate a thank you note?  (y/n)")
    if need_note == "y":
        whom = input("\n Name of donor:")
        donation = input("Donated amount: ")
        print("The following is placed in queue for printing or texting:")
        print("\n", send_thanks(whom, donation))
