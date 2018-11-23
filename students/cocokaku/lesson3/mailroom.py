donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ("Colleen Kaku", [1000000,1000000,1000000])
            ]

def send_thank_you():
    while(True):
        name = input("\nDonor Full Name (type 'list' for donor list or 'q' to quit): ")
        if name=='q': return
        if name!='list': break
        list_donors()
    amount = input("Donation amount: ")
    if amount=='q': return
    if name.title() not in donor_names():
        donor_db.append((name,[]))
    for donor_name,amounts in donor_db:
        if donor_name==name:
            amounts.append(float(amount))
    print()
    print(thank_you_letter(name,float(amount)))

def donor_names():
    return [name for (name,amounts) in donor_db]

def list_donors():
    for donor_name,amounts in donor_db:
        print('   '+donor_name)

def thank_you_letter(name,amount):
    return f"Dear Mr(s) {name},\n" \
           f"Thank you very much for your generous donation of ${amount:,.2f}.\n" \
           f"Sincerely,\n" \
           f"Python 210 Classs of 2018"

def create_a_report():
    summary_list = [(name,sum(amounts),len(amounts),sum(amounts)/len(amounts)) for (name,amounts) in donor_db]
    summary_list.sort(key=get_second,reverse=True)
    print("\nDONOR NAME             TOTAL DONATED   NUM DONATIONS   AVG DONATION AMT")
    for (name,total,num,avg) in summary_list:
        print(f"{name:20s}   ${total:12,.2f} {num:3d}               ${avg:12,.2f}")

def get_second(elem):
    return elem[1]

def main():
    while(True):
        print("\nMAIN MENU")
        print("   1 = Send a Thank You")
        print("   2 = Create a Report")
        print("   q = Quit")
        choice = input("   ? ")
        if choice=='1':
            send_thank_you()
            continue
        if choice=='2':
            create_a_report()
            continue
        if choice=='q':
            break
        print("Invalid choice, try again")
        continue

if __name__=='__main__':
    main()