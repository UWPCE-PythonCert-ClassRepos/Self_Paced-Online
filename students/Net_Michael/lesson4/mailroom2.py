#!/usr/bin/env python
# coding: utf-8
import os
import io
import pathlib
import shutil
import re
from collections import defaultdict

# list of donors and history of the amounts they have donated

def prompt(var):
    if var == 1:
        print("Donors Report")
        report = create_report(donors_dir_path, total_report="yes")
    elif var == 2:
        print("List of individual donations")
        report = create_report(donors_dir_path, indiv_report="yes")
    elif var == 3:
        print("Send a Thank You to a single donor.")
        report = create_report(donors_dir_path, thank_one = "yes")
    elif var == 4:
        print("Send Thank you letters to all donors")
        report = create_report(donors_dir_path, thank_all = "yes")
    else:
        print("Exit")  

        
def create_report(donors_dir_path, 
                  total_report = "no",
                  indiv_report = "no",
                  thank_all = "no",
                  thank_one = "no"):
    report_wd = os.getcwd()
    os.chdir(donors_dir_path)
    donors = defaultdict(list)
    
    with open("donationlist.txt") as donor_list:
        for line in donor_list:
            donor_sel = line.strip()
            Donation = dict([tuple(str(donor_sel).split(" : "))])
            for k, v in Donation.items():
                donors[k].append(v)
    
    donor_names = list(donors.keys())[1:]
    all_donations = list(donors.values())[1:]
    
    ll = len(all_donations)
    donation_list = [[]] * ll
    
    if(indiv_report.lower() == "yes"):
        donor_list1 = dict(zip(donor_names, all_donations))
        print(donor_list1)
    
    elif(total_report.lower() == "yes"):

        print("Name\t\t\tTotal Donation\t\tNum Gifts\tAverage Gift")
        for jj in range(ll):
            donation = [ float(item) for index, item in enumerate(",".join(all_donations[jj]).split(","))]
            donor_name = eval(donor_names[jj])
            total_donation = sum(donation)
            num_gifts = len(donation)
            avg_donation = total_donation/num_gifts
            print ('{:23}'.format(donor_name),
                    '${:^6,.2f}'.format(total_donation),
                    '{:20}'.format(num_gifts),
                    '{:14}'.format(""), 
                    '${:^6,.2f}'.format(avg_donation))
    elif(thank_all.lower() == "yes"):   
        for jj in range(ll):
            donation = [ float(item) for index, item in enumerate(",".join(all_donations[jj]).split(","))]
            donor_name = eval(donor_names[jj])
            total_donation = sum(donation)
            print('''
            
                  Dear {}, 
                  
                  Thank you for your very kind donation of ${:,.2f}.
                  
                  It will be put to very good use. 
       
                                        Sincerely,
                                          -The Team'''.format(donor_name,total_donation)) 
    elif(thank_one.lower() == "yes"):
        quest = input("Do you have the donor name? (yes/no)" )
        quest.lower()
        if quest == "no":
            print("Please select full name from report")
        if quest == "yes":
            donor_sel = input("Please give first and last name").title()
            print(" If you don't see the letter for {}, please check the report".format(donor_sel))
            for jj in range(ll):
                donation = [ float(item) for index, item in enumerate(",".join(all_donations[jj]).split(","))]
                donor_name = eval(donor_names[jj])
                if donor_name in donor_sel:
                    dd = len(donation)-1
                    total_donation = donation[dd]
                    print('''
                    
                    Dear {}, 
                    Thank you for your very kind donation of ${:,.2f}.                  
                    
                    It will be put to very good use. 
       
                                        Sincerely,
                                          -The Team'''.format(donor_name,total_donation))
          
    os.chdir(report_wd)
  
# In[6]:


# var = 1 is for donors total summary donation Report
# var = 2 is for List of individual donations
# var = 3 is for send a Thank You to a single donor
# var = 4 is for send Thank you letters to all donors
        
donors_dir_path = '/Users/Netsanet/Desktop/UW_courses/UWpython/Self_Paced-Online/students/Net_Michael/session04/donors'
if __name__ == "__main__":
    prompt(var = 1)
    prompt(var = 2)
    prompt(var = 3)
    prompt(var = 4)
    prompt(var = 5)
    


# In[ ]:




