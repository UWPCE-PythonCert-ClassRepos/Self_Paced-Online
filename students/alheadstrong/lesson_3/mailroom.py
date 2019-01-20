'''Author: Alex Filson
Updated: 1.20.19
String Formatting Lab for Lesson 3
Py210, Online Self-Paced
'''
ddb = (('Archie Bunker',20,100),
       ('Beyonce Knowles',2000000, 50000000 ),
       ('Charlie Kauffman', 12345),
       ('David Sedaris', 23000,1200,2000),
       ('Edvard Munch', 1,2,3))

def menu():
    while 1:
        userinput = input('''\n\nMENU:
                    1 - Send a Thank You
                    2 - Create a Report
                    3 - Quit
                    Please enter 1-3>''')
        if userinput == '1':
            thankyou()
        elif userinput == '2':
            report()
        elif userinput == '3':
            print('Goodbye')
            break
        else:
            print('Option not found. Please enter the numeral 1,2 or 3')

def thankyou():
    print('thank you message')

def report():
    print('report')

def main():
    menu()

if __name__ == '__main__':
    main()
