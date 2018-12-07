#Dict implementation of the menu

def func_Send_Thankyou():
    print('Thank you')

def func_Create_Report():
    print('Create report')

def  func_Send_Letters():
    print('Send letters to everyone')

def func_Quit():
    print('Quiting ... DONE!')


#Display the menu
def showmenu ():
    """Displays the menu options"""
    select=True
    while select:
        print('\n')
        print('1. Send a Thank You')
        print('2. Create a Report')
        print ('3. Quit')
        response=input("Please select and option (1,2 or 3)")
        print(response)
        switch_func_dict = {
            1: func_Send_Thankyou,
            2: func_Create_Report,
            3: func_Send_Letters,
            4: func_Quit,
        }
        else:
select=True


if __name__ == '__main__':
showmenu()

