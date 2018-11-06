list_col = ['Donor Name','Total Given','Num Gifts','Average Gift']
list_donor_name = ['Fred','Alex','Henry','Alyssa','Leo']
list_total_given = [7000, 30000, 5000, 120000, 107000]
list_num_gifts = [2, 3, 1, 3, 2]
list_avg_gift = [4500, 10000, 5000, 40000, 53500]

def send_thanks():
    user_input = input("Do you want to see the list of donor? Please type 'list'--> ")
    if user_input == "list":
        print('{:^15}'.format("==Donor Name=="))
        for donor_name in list_donor_name:
            print('{:^15}'.format(donor_name))
        donor_name = input("Type the donor's name: ")
        new_gift = int(input("Type your donations: "))

        if donor_name in list_donor_name:
            i = list_donor_name.index(donor_name)
            print(donor_name, list_donor_name[i])
            if list_donor_name[i] in list_donor_name:
                list_total_given[i] = list_total_given[i] + new_gift
                print(list_total_given[i])
                list_num_gifts[i]  = list_num_gifts[i] + 1
                print(list_num_gifts[i])
                list_avg_gift[i] = list_total_given[i]/list_num_gifts[i]
        else:
            list_donor_name.append(donor_name)
            list_total_given.append(new_gift)
            list_num_gifts.append(1)
            list_avg_gift.append(new_gift)
        #print the email
        print('Dear {:s}, thank you for your ${:.2f} donation!'.format(donor_name,new_gift))
        #return to the original prompt
        print('{:<20} | {:^10} | {:^10} | {:^10}'.format(*list_col))
        print('{}'.format("-"*63))
        for i in range(len(list_donor_name)):
            print('{:<20}   ${:>10,.2f}   {:>10}   ${:>10,.2f}'.format\
            (list_donor_name[i],list_total_given[i],list_num_gifts[i],list_avg_gift[i]))


def create_report():
    print('{:<20} | {:^10} | {:^10} | {:^10}'.format(*list_col))
    print('{}'.format("-"*63))
    for i in range(len(list_donor_name)):
        print('{:<20}   ${:>10,.2f}   {:>10}   ${:>10,.2f}'.format\
             (list_donor_name[i],list_total_given[i],list_num_gifts[i],list_avg_gift[i]))
    print('{}'.format("-"*63))


def quit():
    print("Quit current task!")


def main():
    while True:
        print("Choose the number(1,2,3) from a menu:(1)Send a Thank you (2)Create a Report (3)quit")
        choice_action = int(input())
        if choice_action == 1:
            send_thanks()
        elif choice_action == 2:
            create_report()
        elif choice_action == 3:
            quit()
            break

if __name__ == '__main__':
    main()
