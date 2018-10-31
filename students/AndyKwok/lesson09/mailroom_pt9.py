# Description: Mailroom Program - OOP
# Author: Andy Kwok
# Last Updated: 9/18/18
# ChangeLog: 
# v1.0 - Initialization

#!/usr/bin/env python3
 

class Donor():
    ''' Class to hold donor name and donation information'''
    def __init__(self, First = None, Last = None):
        self.__First = First
        self.__Last = Last
        self.Donation_Record = []
        self.__Fullname = None
        
    @property
    def First(self):
        return self.__First

    @First.setter
    def First(self, name):
        self.__First = name
        
    @property
    def Last(self):
        return self.__Last       
    
    @Last.setter
    def Last(self, name):
        self.__Last = name
    
    @property
    def Fullname(self):
        self.__Fullname = self.__First + ' ' + self.__Last
        return self.__Fullname
        
    def __lt__(self, other):
        return self.First < other.First
    
    def AddDonation(self, Amount):  
        self.Donation_Record.append(Amount)
        
class DonorInfo(object):
    ''' Class to hold all methods and data for a list of donors'''
    Donor_List = []
    
    def AddDonor(Donor):
        DonorInfo.Donor_List.append(Donor)     
    
    def Display():
        print('Donor Name' + ' '*10 + '| Total Given' + ' '*5 + '| Num Gifts' + ' '*5 + '| Average Gift')
        print('-'*75)
        for i in DonorInfo.Donor_List:
            print('{:20}'.format(i.First + ' ' + i.Last) + '$ {:>10.2f} {:7}'.format(sum(i.Donation_Record), len(i.Donation_Record)) + ' '*14 + '$ {:>10.2f}'.format(sum(i.Donation_Record)/len(i.Donation_Record))) 
          
    def SentLetters(Donor):
        printout = 'To {} {},'.format(Donor.First, Donor.Last) + '\n' + 'Thank you for your donation of ${:.2f}.'.format(sum(Donor.Donation_Record)) + '\n'*2 + '\t'*5 + '-System Generated Email'
        return printout
    
    def SortList():
        # Sort per first name
        DonorInfo.Donor_List.sort()

# Initial value for verification
def Tester():
    one = Donor()
    one.First = 'C'
    one.Last = 'Character'
    one.AddDonation(5)
    one.AddDonation(10)
    DonorInfo.AddDonor(one)

    two = Donor()
    two.First = 'B'
    two.Last = 'Character'
    two.AddDonation(15)
    two.AddDonation(153)
    two.AddDonation(20)
    DonorInfo.AddDonor(two)

    three = Donor()
    three.First = 'A'
    three.Last = 'Character'
    three.AddDonation(1200)
    DonorInfo.AddDonor(three)

        
if __name__ == '__main__':
    option = 'start'
    Tester()
    while option.lower() != 'quit':
        print(
            '''    
            1 - Sent a Thank you
            2 - Create a Report
            3 - Send Letters to Everyone
            4 - Quit
            '''
            )
        try:
            option = input('Please select an option> ')
        except KeyError:
            print('Option does not exist...Please try again')
        if option == '1':
            # Modify list
            Entry = input('Enter donor\'s name to search or \'list\' to show all donors> ')
            Name = Entry.split(' ')
            if Entry.lower() == 'list':
                DonorInfo.Display()
            else:
                stop = False
                new = True
                while stop is False:
                    try:
                        Donation = float(input('How much does {} want to donate? '.format(Entry)))
                    except ValueError:
                        print("Please enter a real donation amount.")
                    else:
                        # Scan for existing donor
                        for count, item in enumerate(DonorInfo.Donor_List):
                            if item.Fullname.lower() == Entry.lower():
                                DonorInfo.Donor_List[count].AddDonation(Donation)
                                new = False
                                stop = True
                        # Add new donor if non exist
                        if new is True:
                            Newdonor = Donor()
                            Newdonor.First = Name[0]
                            Newdonor.Last = Name[1]
                            Newdonor.AddDonation(Donation)
                            DonorInfo.AddDonor(Newdonor)
                            stop = True 
        elif option == '2':
            # Report out
            DonorInfo.SortList()
            DonorInfo.Display()
        elif option == '3':
            # Send letters to everyone
            for item in DonorInfo.Donor_List:
                with open(item.First + ' ' + item.Last + '.txt', 'w') as doc:
                    doc.write(DonorInfo.SentLetters(item))
        elif option == '4':
            # Quit
            option = 'quit'
            
   