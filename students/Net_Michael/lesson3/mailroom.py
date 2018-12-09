#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Part I

import sys  

def sort_key(donor_db2):
        return donor_db2[0].split(" ")[1]

# update the list of donors and donation
def add_donor():
    new_donor = input("Name of donor?").title()
    if new_donor not in donor_name:
        donor_name.append(new_donor)  
        new_donation1 = input("Amount of donation by {}?".format(new_donor))
        idx = len(donor_name)-1
        new_donation1 = float(new_donation1)
        donation[idx].append(new_donation1)
    elif new_donor in donor_name:
        idx = donor_name.index(new_donor)
        new_donation1 = float(input("Amount of donation?".format(new_donor)))
        donation[idx].append(new_donation1)
    print(f"{new_donor} has made a new donation of {new_donation1}")
    return(new_donor, new_donation1)


# compile donors and donation information
def donors_info():
    
    mm = len(donor_name)
    donor_db2 = [''] * mm
    
    for j in range(mm):
        donor_db2[j] = (donor_name[j], donation[j])
        
    donor_db2 = sorted(donor_db2, key=sort_key)
    return(donor_db2)

# create tabular report 

def create_report():
    mm = len(donor_name)
    data_db2 = []*mm

    print("Name\t\t\tTotal Donation\t\tNum Gifts\tAverage Gift")

    for j in range(mm):
        total_donation = sum(donation[j])
        num_gifts = len(donation[j])
        avg_donation = total_donation/num_gifts
        
        print('{:23}'.format(donor_name[j]),
              '${:>10,.2f}'.format(total_donation),
              '{:>15}'.format(num_gifts),
              '{:10}'.format(""), 
              '${:>10,.2f}'.format(avg_donation))

          
def exit_program():
    return("Done")  


# In[2]:



# Part I
# list of donors and history of the amounts they have donated.

donor_name = ["William Gates, III", 
              "Jeff Bezos", 
              "Paul Allen", 
              "Mark Zuckerberg"]

donation = ( [653772.32, 10020.17, 58796.00],
            [877.33],
            [663.23, 43.87, 1.32], 
            [1663.23, 4300.87, 10432.0])
#part I
# This structure should be populated at first with at least five donors,
#with between 1 and 3 donations each.
#You can store that data structure in the global namespace.

donor_list1 = dict(zip(donor_name, donation))
donor_list1


# In[3]:



# part I (alternatively it can also be stored)
#You can store that data structure in the global namespace.

donor_list2 = donors_info()
donor_list2


# In[4]:


# Part I
#The script should prompt the user (you) to choose from a menu of 3 actions:
#“Send a Thank You”, “Create a Report” or “quit

prompt = "\n".join(("Welcome",
          "Please choose from below options:",
          "1 - Add new donation",  
          "2 - Create a Report ",
          "3 - quit",
          ">>> "))


# In[6]:


# part I execute the code

if donation[len(donation)-1] != []:
    donation += ([],)

if __name__ == '__main__':
    while True:
        response = input(prompt)
        if response == "1":
            addnew_donor = add_donor()
            donor_list2 = donors_info()
            if( len(addnew_donor) > 0 ):
                print("Our institution thank you {name} for your generous gift of ${amount}", "\n"
                       "Thank you,", "\n"
                      "Bay James".format(name=addnew_donor[0], amount=addnew_donor[1]))
            else:
                print("No update on the donation name list")
        elif response == "2":
            create_report()
        elif response == "3":
            print("Done")
            break





