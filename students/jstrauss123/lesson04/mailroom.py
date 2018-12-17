#!/usr/bin/env python3

# function - send thank you
#def send_thankyou(donorl):
def send_thankyou():
    print("")
    # prompt for donor name
    full_name = input("Please provide full name of donor or enter list to see all donors: ")
    print("")
    while full_name == "list":
        # print donor names
        for donor_name in donor_dict.keys():
            print(donor_name)
        #prompt for donor name
        print("")
        full_name = input("Please provide full name of donor: ")
    #if full_name not in donor_name_list:
    if full_name not in donor_dict.keys():
        # add to dict
        donor_dict[full_name] = []
    # prompt for contribution amount and add to dict
    contrib_amt = float(input("Enter donation amount for donor: "))
    donor_dict[full_name].append(contrib_amt)
    # send thank you email
    print("Dear {}, Thank you so much for your generous contribution of ${}.".format(full_name, contrib_amt))
    print(donor_dict.items())
    print("")

# function - create thank_you_email - returns formatted message
def thank_you_email(dname, donation):
    print("thank_you_email function called")
    #email_message = ("\nDear {},\n\n".format(dname)
    #                 "Thank you for your very kind donation of {}.format(contrib_amt).\n\n"
    #                 "It will be put to very good use.\n\n"
    #                 "    Sincerely,\n"
    #                 "        -The Team\n"
    #                 )
    printout = '\nDear {},'.format(dname) + '\n\n' + 'Thank you for your very kind donation of ${:.2f}.\n\n'.format(donation) + 'It will be put to very good use. \n\n' + '\tSincerely,\n' + '\t    -The Team \n'
    return printout
    print("email message is: ", email_message)
    #return email_message
    return printout    
# function - create donor report
def create_report():
    print("")
    sum = 0
    report_detail = []
    count = 0
    #print(dict1.get('cake'))
    for donor_name,contrib_amts in donor_dict.items():
        totamt = 0
        num_of_contributions = len(contrib_amts)
        for amt in contrib_amts:
            totamt = totamt + amt
        avg_contribution_amt = totamt // num_of_contributions
        donor_detail = (donor_name, totamt, num_of_contributions, avg_contribution_amt)
        report_detail.append(donor_detail)
    # sort by donor with largest contribution    
    def sort_key(print_detail):
        return print_detail[1]
    report_detail = sorted(report_detail, key=sort_key, reverse=True)
    #print report header
    print("{:15} |{:>15} |{:>2} |{:>15}".format("Donor Name","Total Given","Num Gifts","Average Gifts" ))
    # loop through donors and print detail lines
    i = 0
    while i < len(report_detail):
        print("{:15} ${:>15.2f} {:>2} ${:>15.2f}".format(report_detail[i][0], report_detail[i][1], report_detail[i][2], report_detail[i][3]))
        i += 1
    print("")

def send_letters():
        # create letter to each donor and save to disk
        print("you selected send letters to all")
        
def quit():
    print("Quitting this menu")
    return "exit menu"
    
def menu_selection(prompt, dispatch_dict):
        while True:
            response = input(prompt)
            if dispatch_dict[response]() == "exit menu":
                break
    
main_prompt = ("\nMain Menu\n"
               "Please select from the following options:\n"
               "1 - Send a Thank You\n"
               "2 - Create a Report\n"
               "3 - Send letters to everyone\n"
               "4 - Quit >> "
               )
               
main_dispatch = {"1": send_thankyou,
                 "2": create_report,
                 "3": send_letters,
                 "4": quit,
                }
                
# main
if __name__ == "__main__":
    donor_dict = {'Mickey Mouse': [100.00, 150.00, 100.00], 'Minnie Mouse': [50.00, 50.00], 'Ron Jones': [100.00], 'Donald Duck': [25.00], 'Busy Bear': [250.00, 10.00, 10.00]}
    menu_selection(main_prompt, main_dispatch)
            

