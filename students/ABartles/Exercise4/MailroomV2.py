

def menu():
    print("\n==========================================")
    print("Would you like to:")
    print("\t1 - Send a thank you letter.")
    print("\t2 - Send thank you letters to everyone.")
    print("\t3 - Add a donation.")
    print("\t4 - Create a report.")
    print("\t5 - Quit.")
    response = int(input(">>> "))
    return response

def send_thanks_one():
    lst = list_donors(donors)
    while True:
        print(lst)
        print("Who from the list above would you like to thank?")
        response = input(">>> ")
        response = response.title()
        if response in lst:
            thanks_letter(response, donors)
            break
        else:
            print("{} is not a donor, would you like to add them?".format(response))
            x = input("Y/N >>> ")
            if x.lower() == "y":
                rec_dontation(response)

def send_thanks_all():
    name_lst = list_donors(donors)
    for i in name_lst:
        thanks_letter(i, donors)

def list_donors(dnrlst):
    name_lst = []
    for i in dnrlst:
        if i[0] not in name_lst:
            name_lst.append(i[0])
    return name_lst

def rec_dontation():
    print("Who made the donation?")
    dnr = input(">>> ").title()
    print("How much was the donation?")
    donation = input(">>> ")
    dnrtpl = (dnr, donation)
    donors.append(dnrtpl)

def thanks_letter(donor, dnrlst):
    file_name = "{}.txt".format(donor.replace(" ", "_"))
    donation = sum_gifts(donor, dnrlst)

    header = "Dear {},".format(donor)
    body = "Thank you for your donation of {}.".format(donation)
    close = "\tSincerely,\n\t\t-The Team"

    letter = "{}\n{}\n\n{}".format(header, body, close)

    with open(file_name, 'w+') as f:
        f.write(letter)
    f.close()
    print("Thank you letter for {} created.".format(donor))

def create_report():
    dnrNames = list_donors(donors)
    print(f'{"Donor Name":<20}{"|":<1}{"Total Given":^15}{"|":<1}{"Num Gifts":^15}{"|":<1}{"Average Gift":>15}')
    print("-" * 68)
    iCount = 1
    for i in dnrNames:
        iTotalGift = sum_gifts(i, donors)
        iCount = count_gifts(i)
        iAveGift = iTotalGift / iCount
        s = f'{i:<20}{" ":<1}{"$":<1}{iTotalGift:>14}{" ":<1}{iCount:>15}{" ":<1}{"$":<1}{iAveGift:>14}'
        print(s)

def sum_gifts(donor, dnrlst):
    total = 0
    for i in dnrlst:
        if i[0] == donor:
            total = total + int(i[1])
    return total

def count_gifts(donor):
    count = 0
    for i in donors:
        if i[0] == donor:
            count = count + 1
    return count

def run_func(fun_dict):
    while True:
        response = menu()
        if response != 5:
            fun_dict[response]()
        else:
            break


global donors
donors = [
 ("Anita Bath", 200),
 ("Isabelle Ringing", 101),
 ("John Smith", 100),
 ("Seymour Butz", 95),
 ("Anita Bath", 150)
]

functions = {
 1 : send_thanks_one,
 2 : send_thanks_all,
 3 : rec_dontation,
 4 : create_report,
 5 : quit
}



if __name__=='__main__':
    try:
        run_func(functions)
    except Exception as e:
        print(e)
        x = input("main error")


