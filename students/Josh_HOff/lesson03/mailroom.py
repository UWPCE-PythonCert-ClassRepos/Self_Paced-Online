def email(donor, donation):
    print(f'Hello, {donor}! Thank you very much for your generous donation of ${donation}! Your contribution is essential and will be well utilized.')

donors = (['Ralph Anderson', 5, 10], ['Andrei Jackson', 101, 151, 75], ['Stalk Holmes', 40], ['Traci Johnston', 20], ['James Hendrick', 60], ['Angelica Kisel', 45, 25, 55])
x = 1
while x == 1:
    response = input('1: Send a Thank You \n2: Create a Report \n3: Quit \nChoose an Option:')
    if response == '1':
        while True:
            response = input('Type a Full Name: ')
            if response == 'list':
                for i in donors:
                    print(i[0])
            else:
                don_amt = int(input('What is the donation amount?'))
                count = 0
                for i in donors:
                    if i[0] == response:
                        donors[count].append(don_amt)
                        email(response, don_amt)
                        n = 0
                    count += 1
                if n == 1:
                    donors += ([response],)
                    donors[count].append(don_amt)
                    email(response, don_amt)
                    n = 0
        
    
    
    
#if response == 2:

#if response == 3: