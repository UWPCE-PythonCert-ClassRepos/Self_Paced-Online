# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 08:06:16 2019

@author: acharch
"""

import sys

Master_List = {"Bill Gates":[1000,2000,3000,4000,5000],
               "Marc Zuckerberg":[1005,2005,3005,4005,5005],
               "Jeff Bezos": [9000,12000],
               "Warren Buffet": [1100,2200,3300,4000,5000],
               "Tim Cook": [100000,300000,400000,500000],
               "Sundar Pichai":[1000],
               "Satya Nadella":[1900,45672,983564,7646,5000,1,2,3],
               "Charith Acharya":[10,80,24,621]}

prompt = "\n".join(('Welcome',
                   'Please select from the following options',
                   '1.Send A Thank You!',
                   '2.Create a report',
                   '3.Send a letter to all participants',
                   '4. Quit'))
def main():
    while True:
        response = int(input(prompt))
        SwitchFuncDict = {1:Thanks,2:Report,3:Letter_to_all,4:Quit}
        SwitchFuncDict.get(response)()

def Thanks():
    Full_Name = input("Please enter the full name".title())
    New_Amount = input("Please enter new amount")
    Amount = int(New_Amount)
    if Full_Name in Master_List.keys():
        Master_List[Full_Name].append(Amount)
        print(Message(Full_Name, New_Amount))        
    elif Full_Name not in Master_List.keys():
        Master_List[Full_Name] = [Amount]
        print(Message(Full_Name, New_Amount))  
      
def Message(Full_Name, New_Amount):
    return(" ".join(["Hello",Full_Name,"Thank you for the donation of",New_Amount]))
    
  
def donor_details():
    """Print donation statistics for each donor"""
    Master_List_2 = {}
    Master_List_2 = {k:[sum(v),len(v), sum(v)/len(v)] for k,v in Master_List.items()}
    Master_List_3  = sorted(Master_List_2 .items(), key = lambda x: x[1], reverse = True)
    for donor in Master_List_3:
        print("{:<20} ${:>12,.2f}{:^12} ${:>12,.2f}".format(donor[0], donor[1][0], donor[1][1], donor[1][2]))
    
       
def Report():
    """Print a list of donors sorted by name, total donated amount, number of donation, and average donation amount"""
    print("{0:<20}{1:>12}{2:>12}{3:>15}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("--------------------------------------------------------------")
    donor_details()


def Report_Totals(i):
    SumI = sum(Master_List[i])
    return(SumI)



def Letter_to_all():
    for i in range(len(Master_List)):
        with open('Letter{}.txt'.format(list(Master_List.keys())[i]),'w') as f:
            f.write("Hello")
            f.write(list(Master_List.keys())[i])
            f.write("Thank you for your donation of")
            f.write(str(sum(list(Master_List.values())[i])))
    
def Quit():
    print("Bye!")
    sys.exit()
    
if __name__ == "__main__":
    main()
    
    