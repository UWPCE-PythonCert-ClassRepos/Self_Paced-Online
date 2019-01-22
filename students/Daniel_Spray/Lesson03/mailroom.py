import sys

donation_data = [["William Gates, III","Mark Zuckerberg","Jeff Bezos","Paul Allen"],[653784.49,16396.10,877.33,708.42], [2,3,1,3]]

def main(donation_data=donation_data):
    while True:
        print("""This program will hopefully help you send some meaningful messages
Type the corresponding number to select from the following list:

1: Send a Thank You
2: Create a Report
3: Quit""")
        response=input(">")
	
        if response == "1":
            send_thank_you()
        elif response == "2":
            create_report(donation_data)
        elif response == "3":
            sys.exit()
        else:
            print("Sorry, I didn't recognize that command")

def send_thank_you(donation_data = donation_data):
    
    donors = donation_data[0]
    
    total_given = donation_data[1]
	
    num_gifts = donation_data[2]

    name = input("Please enter a full name > ")
    donor_index = "None"
	
    while name == "list":
        list_of_donors = "{}, "*(len(donors)-1)+"{}"
        print(list_of_donors.format(*donors))
        name = input("Please enter a full name > ")

    if name.lower() == "quit":
        sys.exit()

    if name not in donors:
        donation = input("Donation Amount? > ")
        if donation.lower() == "quit":
            sys.exit()
        else:
            donors.append(name)
            total_given.append(float(donation))
            num_gifts.append(int(1))
            print("Donor has been added to the list")
            letter(name,donation)

            main([donors, total_given, num_gifts])

    else:
        donor_index = donors.index(name)
        donation = input("Donation Amount? > ")
        if donation.lower() == "quit":
            sys.exit()
        else:
            total_given[donor_index] += float(donation)
            num_gifts[donor_index] += 1
            letter(name,donation)
            main([donors, total_given, num_gifts])
	
def letter(name,donation):		
    donation=round(float(donation),2)   
    print("""
Dear {},

Thank you for your generous donation of ${:.2f}

Sincerely,
The Charity
""".format(name,donation))

	
def create_report(donation_data):
    result = calculation(donation_data[0],donation_data[1],donation_data[2])
    table(result)
    main()

def table(result):
    print(" ")
    print("{:<24}{:<1}{:^13}{:<1}{:^13}{:<1}{:^17}".format('Donor Name','|','Total Given','|','Num Gifts','|','Average Gift'))
    print("-"*67)
    for row in result:
        print("{:<25}{:<1}{:>12.2f}{:>14}{:>2}{:>13.2f}".format(*row))
    print(" ")

def useTotal(amounts):
    return amounts[2]

def calculation(donors, total_given, num_gifts):
    donors = donation_data[0]
    total_given = donation_data[1]
    num_gifts = donation_data[2]
    averages = []
    data = []

    for index_averages in range(0,len(donors)):
        averages.append(float(total_given[index_averages])/float(num_gifts[index_averages]))

    for index_data in range(0,len(donors)):
        compiled_data = [donors[index_data],"$",round(total_given[index_data],2),num_gifts[index_data],"$",round(averages[index_data],2)]
        data.append(compiled_data)
    
    sortedData = sorted(data,key=useTotal,reverse=True)
    return sortedData

if __name__ == '__main__':
    main()