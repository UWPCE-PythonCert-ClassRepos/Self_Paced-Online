# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 14:17:18 2019

@author: acharch
"""

#MailRoom Part 1
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 20:48:25 2019

@author: acharch
"""

import sys

Master_List = [("Bill Gates", [1000,2000,3000,4000,5000]),
          ("Marc Zuckerberg", [1005,2005,3005,4005,5005]),
          ("Jeff Bezos", [9000,12000]),
          ("Warren Buffet", [1100,2200,3300,4000,5000]),
          ("Tim Cook", [100000,300000,400000,500000]),
          ("Sundar Pichai",[1000]),
          ("Satya Nadella",[1900,45672,983564,7646,5000,1,2,3]),
          ("Charith Acharya",[10,80,24,621])]

prompt = "\n".join(('Welcome',
                   'Please select from the following options',
                   '1.Send A Thank You!',
                   '2.Create a report',
                   '3.Quit'))
def main():
    while True:
        response = input(prompt)  
        if response == "1":
            Thanks()
        elif response == "2":
            Report()
        elif response == "3":
            Quit()
        else:
            print("Not a valid option!")

def Thanks():
    Full_Name = input("Please enter the full name".title())
    New_Amount = input("Please enter new amount")
    Amount = int(New_Amount)
    flag = 0
    for i in range(len(Master_List)):
        if Full_Name in Master_List[i][0]:
            Master_List[i][1].append(Amount)
            print(" ".join(["Hello",Full_Name,"Thank you for the donation of",New_Amount]))
            flag = 1
    if  flag == 0:
        Master_List.append((Full_Name,[int(New_Amount)]))
        print(" ".join(["Hello",Full_Name,"Thank you for the donation of",New_Amount])) 

def Report():
    Total_List = []
    for i in range(len(Master_List)):
        Total = sum(Master_List[i][1])
        Count = len(Master_List[i][1])
        Average = Total/Count
        Total_List.append([Master_List[i][0],Total, Count, Average])
    print("Donor Name" + "' '*15" + "|" + "Total Given" + "|" + "|" + "Num Gifts" + "|" + "|" + "Avergae Gift" + "|") 
    
def Quit():
    print("Bye!")
    sys.exit()
    
if __name__ == "__main__":
    main()
    
Master_List
