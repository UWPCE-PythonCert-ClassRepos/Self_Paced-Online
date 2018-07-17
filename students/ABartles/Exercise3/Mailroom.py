def Send_Thanks(dnrslst):
    response = "Not a donor or the word list"

    while response not in dnrslst:
        print("----------------------------------------")
        response = input("Who would you like to thank ('first last', 'list', or 'exit'? ")
        response = response.title()

        if response == "Exit":
            break
        elif response == "List":
            print("----------------------------------------")
            print("Below is the list of Donors:")
            print(List_Donors(dnrslst))
        elif response != "List":
            print("----------------------------------------")
            amount = input("How much was dontated by {}? ".format(response))
            dnrslst = Rec_Donation(dnrslst, response, amount)
            print("----------------------------------------")
            Thanks_Email(response, dnrslst)

def List_Donors(dnrslst):
    name_lst = []
    for i in dnrslst:
        if i[0] not in name_lst:
            name_lst.append(i[0])
    return name_lst

def Rec_Donation(dnrslst, donor, money):
    donor_tpl = (donor, money)
    dnrslst.append(donor_tpl)
    return dnrslst

def Thanks_Email(donor, dnrslst):
    money = Sum_Gift(donor, dnrslst)
    print("Dear {},".format(donor))
    print("Thank you for your generous gift of {}.".format(money))

def Sum_Gift(donor, dnrslst):
    total = 0
    for i in dnrslst:
        if i[0] == donor:
            total = total + int(i[1])
    return total

def donation_count(donor, dnrslst):
    count = 0
    for i in dnrslst:
        if i[0] == donor:
            count = count + 1
    return count

def Create_Report(dnrslst):
    dnrNames = List_Donors(dnrslst)
    print(f'{"Donor Name":<20}{"|":<1}{"Total Given":^15}{"|":<1}{"Num Gifts":^15}{"|":<1}{"Average Gift":>15}')
    print("-" * 68)
    iCount = 1
    for i in dnrNames:
        iTotalGift = Sum_Gift(i, dnrslst)
        iCount = donation_count(i, dnrslst)
        iAveGift = iTotalGift / iCount
        s = f'{i:<20}{" ":<1}{"$":<1}{iTotalGift:>14}{" ":<1}{iCount:>15}{" ":<1}{"$":<1}{iAveGift:>14}'
        print(s)

if __name__ == '__main__':
    donors = [("Anita Bath", 200),("Isabelle Ringing", 101), ("John Smith", 100), ("Seymour Butz", 95), ("Anita Bath", 150)]
    response = 123456

    while True:
        print("Would you like to;")
        print("1: Send a 'Thank You'")
        print("2: Create a 'Report'")
        print("3: 'Quit'")
        response = input("Please select option: ")

        if response.title() == "Thank You":
            Send_Thanks(donors)
        elif response.title() == "Report":
            Create_Report(donors)
        elif response.title() == "Quit":
            break
        print()