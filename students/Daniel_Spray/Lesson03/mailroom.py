def main(b=(["William Gates, III","Mark Zuckerberg","Jeff Bezos","Paul Allen"],[653784.49,16396.10,877.33,708.42], [2,3,1,3], [], [])):
    print("This program will hopefully help you send some meaningful messages")
    print("Type the corresponding number to select from the following list:")
    print(" ")
    print("1: Send a Thank You")
    print("2: Create a Report")
    print("3: Quit")
    a=input(">")
	
    if str(a) == "1":
        saty()
    elif str(a) == "2":
        car(calculation(b[0],b[1],b[2],b[3],b[4]))
    elif str(a) == "3":
        something="nothing"
    else:
        print("Sorry, I didn't recognize that command")
        main()

def saty():
    
    Donors = ["William Gates, III","Mark Zuckerberg","Jeff Bezos","Paul Allen"]
    
    Total_Given = [653784.49,16396.10,877.33,708.42]
	
    Num_Gifts = [2,3,1,3]

    c = input("Please enter a full name > ")
    e = "None"
	
    if c == "list":
        donors = "{}, "*(len(Donors)-1)+"{}"
        print(donors.format(*Donors))
        saty()

    if c.lower() == "quit":
        something="nothing"
		
    else:

        for d in Donors:
            if str(c) == d:
                e = Donors.index(str(c))

        if e == "None":
            g = input("Donation Amount? > ")
            if g.lower() == "quit":
                something = "nothing"
            else:
                Donors.append(str(c))
                Total_Given.append(float(g))
                Num_Gifts.append(int(1))
                letter(c,g)
                main((Donors, Total_Given, Num_Gifts, [], []))

        else:
            g = input("Donation Amount? > ")
            if g.lower() == "quit":
                something = "nothing"
            else:
                Total_Given[e] += float(g)
                Num_Gifts[e] += 1
                letter(c,g)		
                main((Donors, Total_Given, Num_Gifts, [], []))
	
def letter(a,b):		
    b=round(float(b),2)   
    print("""
Dear {},

Thank you for your generous donation of ${}

Sincerely,
The Charity
""".format(a,b))

	
def car(a):
    table(a)
    main()

def table(a):
    print(" ")
    print("{:<24}{:<1}{:^13}{:<1}{:^13}{:<1}{:^17}".format('Donor Name','|','Total Given','|','Num Gifts','|','Average Gift'))
    print("-"*67)
    for row in a:
        print("{:<25}{:<1}{:>12}{:>14}{:>2}{:>13}".format(*row))
    print(" ")

def useTotal(amt):
    return amt[2]

def calculation(Donors, Total_Given, Num_Gifts, Averages, Data):
    for n in range(0,len(Donors)):
        Averages.append(float(Total_Given[n])/float(Num_Gifts[n]))
    

    for a in range(0,len(Donors)):
        b = [Donors[a],"$",round(Total_Given[a],2),Num_Gifts[a],"$",round(Averages[a],2)]
        Data.append(b)
    
    sortedData = sorted(Data,key=useTotal,reverse=True)
    return sortedData

if __name__ == '__main__':
    main()