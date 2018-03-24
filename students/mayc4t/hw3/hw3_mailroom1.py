#!/usr/bin/env python3

# Goal:
# 
# You work in the mail room at a local charity. Part of your job is to write incredibly boring, repetitive emails thanking your donors for their generous gifts. You are tired of doing this over and over again, so you’ve decided to let Python help you out of a jam and do your work for you.
# 
# The Program
# 
# Write a small command-line script called mailroom.py. This script should be executable. The script should accomplish the following goals:


dn0 = ['Lily Maycat', [200]]
dn1 = ['Lulu Lemon' , [10000, 100000, 1000000]]
dn2 = ['Marc Jacobs', [20000, 2000000]]
dn3 = ['Kate Spade' , [30000, 30000, 30000 ]]
dn4 = ['Luis Vuiton', [44000, 40000]]
dn5 = ['Bobbi Brown', [10000000]]
dn_table = [dn0, dn1, dn2, dn3, dn4]

# Sending a Thank You
# If the user (you) selects ‘Send a Thank You’, prompt for a Full Name.
# If the user types ‘list’, show them a list of the donor names and re-prompt
# If the user types a name not in the list, add that name to the data structure and use it.
# If the user types a name in the list, use it.
# Once a name has been selected, prompt for a donation amount.
# Turn the amount into a number – it is OK at this point for the program to crash if someone types a bogus amount.
# Once an amount has been given, add that amount to the donation history of the selected user.
# Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.
# It is fine (for now) to forget new donors once the script quits running.
# 


    

def here_you_go():
    print ("\Here you go")
    print(dn_table)

def send_thank_you_note():
    print ("---Thank You Note ---")
    ans = input("\tEnter anthing except quit : ")
    #print( f"1{ans.lower()}1")
    #ans = ans.split()
    ans = ans.lower()
    print ( ans) 

    while( ans.lower() != 'quit' ):

        #print( f"1{ans.lower()}1")
        #here_you_go()   
    

        ans = input("\tEnter anthing except quit {}: ")
        ans = ans.strip()
        ans = ans.lower()
        print( f"2{ans.lower()}2")


# Note to myself
# In [44]: dnlist
# Out[44]: 
# [['one', [1, 11, 1111, 200]],
#  ['two', [2, 22, 22345]],
#  ['three', [5000]],

# In [45]: dn1[0]
# Out[45]: 'one'
# 
# In [46]: dnlist[0]
# Out[46]: ['one', [1, 11, 1111, 200]]
# 
# In [47]: dnlist[0][0]
# Out[47]: 'one'
# 
# In [48]: dnlist[0][1]
# Out[48]: [1, 11, 1111, 200]



def create_report():
    print("Create report")
    print("{:<40}|{:>14} | {:>12} | {:>14}".format("Donor Name", "Total Give", "Num Gifts", "Average Gift"))
    print("_"*40 + " " + "_"*14 + "   " + "_"*12 +"   " + "_"*14 +"\n")
    for donor in dn_table:
        gift_val = 0
        for val in donor[1]:
            gift_val += val
        gift_avg = gift_val / len(donor[1])
        print("{:<40}   ${:>14} {:>12}   ${:>14}".format(donor[0], gift_val, len(donor[1]), gift_avg))
        
if __name__ == "__main__":
    print ("MAIN FUNCTION")
    print ("Original table")
    print (dn_table)
    ans = 0
    while ( ans != 3):
        print("Select what to do")
        print("--" * 15)
        print(" 1: Send a Thank you" )
        print(" 2: Create a Report")
        print(" 3: quit ")
        print("--" * 15)
        ans = int(input("\nEnter your number : "))

        if ans == 1:
            send_thank_you_note()
        if ans == 2:
            create_report()




# It should have a data structure that holds a list of your donors and a history of the amounts they have donated. This structure should be populated at first with at least five donors, with between 1 and 3 donations each.
# 
# You can store that data structure in the global namespace.
# 

# The script should prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”)
# 











# Creating a Report
# 
# If the user (you) selected “Create a Report”, print a list of your donors, sorted by total historical donation amount.
# Include Donor Name, total donated, number of donations and average donation amount as values in each row. You do not need to print out all their donations, just the summary info.
# Using string formatting, format the output rows as nicely as possible. The end result should be tabular (values in each column should align with those above and below)
# After printing this report, return to the original prompt.



# First, factor your script into separate functions. Each of the above tasks can be accomplished by a series of steps. Write discreet functions that accomplish individual steps and call them.
# 
# Second, use loops to control the logical flow of your program. Interactive programs are a classic use-case for the while loop.
# 
# Of course, input() will be useful here.
# 
# Put the functions you write into the script at the top.
# 
# Put your main interaction into an if __name__ == '__main__' block.
# 
# Finally, use only functions and the basic Python data types you’ve learned about so far. There is no need to go any farther than that for this assignment.
# 
# Submitting Your Work
# 
# Put the file(s) (ex: a_new_file.py) in your student directory in a new subdirectory named for this lesson, and add it to your clone early (git add a_new_file.py). Make frequent commits with good, clear messages about what you're doing and why.
# 
# When you're done and ready for the instructors to review your work, push your changes to your GitHub fork (git push) and then go to the GitHub website and make a pull request. Copy the link to the pull request.
# 
# You will then submit the pull request link and the .py file (or .zip if there are multiple files).
# 
# 
