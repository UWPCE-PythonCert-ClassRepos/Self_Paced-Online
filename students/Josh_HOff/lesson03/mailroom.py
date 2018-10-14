def email(donor, donation):
    print(f'Hello, {donor}! Thank you very much for your generous donation of ${donation}! Your contribution is essential and will be well utilized.')

def response1(donors_list):
    while True:
        x = 0
        response = input('Type a Full Name: ')
        if response == 'list':
            for i in donors_list:
                print(i[0])
        else:
            don_amt = float(input('What is the donation amount?: '))
            count = 0
            for i in donors_list:
                if i[0] == response:
                    donors_list[count].append(don_amt)
                    email(response, don_amt, donors_list)
                    x = 2
                    break
                count += 1
            if x != 2:
                donors_list += ([response],)
                donors_list[count].append(don_amt)
                email(response, don_amt)
        return(donors_list)

def response2(donors_list):
    y = '|'
    print(f'Donor Name{y:>15} Total Given {y} Num Gifts {y} Average Gift')
    print('-' * 64)
#    print(donors_list)
    for i in donors_list:
        total = sum(i[1:])
        gift = len(i[1:])
        average = (total / gift)
        print(f'{i[0]:>10} {total:>15} {gift:<5} {average:<15}')
    

def main1():
    donors_list = (['Ralph Anders', 5, 10], ['Andrei Hoff', 101, 151, 75], ['Stalk Holmes', 40], ['Traci Johnston', 20], ['James Hendrick', 60], ['Angelica Kisel', 45, 25, 55])
    while True:
        response = input('1: Send a Thank You \n2: Create a Report \n3: Quit \nChoose an Option: ')
        if response == '1':
            donors_list = response1(donors_list)
        if response == '2':
            response2(donors_list)
main1()
    
    
#if response == 2:

#if response == 3: