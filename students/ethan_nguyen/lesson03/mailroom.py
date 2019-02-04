
import operator
'''
Class to store Donor object and its attributes
'''
class Donor:
    def __init__(self, name, amount=0, num=0):
        self.name = name
        self.amount_gift = amount
        self.num_gift = num
    '''function to calculate average donation'''
    def getAverge(self):
        return (self.amount_gift/self.num_gift)
    '''function to return number of donations'''
    def getCount(self):
        return self.num_gift
    '''function to return historical amount'''
    def getAmount(self):
        return self.amount_gift
    def getName(self):
        return self.name
    '''function to add new donation amount to historical'''
    def addAmount(self, addition):
        self.amount_gift += addition
        self.num_gift += 1

if __name__ == "__main__":
    #create a dict object to store donors
    DonorDict = {}
    D1 = Donor("William Gates, III", 100.2, 2)
    DonorDict['William Gates, III'] = D1
    D2 = Donor("Mark Zuckerberg", 3000.2, 3)
    DonorDict['Mark Zuckerberg'] = D2
    D3 = Donor("Jeff Bezos", 100000.2, 3)
    DonorDict['Jeff Bezos'] = D3
    D4 = Donor("Paul Allen", 5000.24, 1)
    DonorDict['Paul Allen'] = D4
    D5 = Donor("Donald Trump", 50000.24, 1)
    DonorDict['Donald Trump'] = D5
    
    #sort = sorted(DonorDict.items(), key=operator.itemgetter(1).getAmount(), reverse = True)

    response = input("Please select S for \"Send a Thank You\" C for \"Create a Report\" or Q to quit >")
    while ("S" or "C" in response.upper()):
        if 'S' in response.upper():
            print("Do Thank you")
            inputName = input("Please enter a name > ")
            while("list" in inputName):
                for k,v in DonorDict.items():
                    print(k)
                inputName = input("Please enter a name > ")
            if inputName in DonorDict:
                selectDonor = DonorDict[inputName]
            else:
                selectDonor = Donor(inputName)
            
            inputAmount = input(f"{inputName} please input amount > ")
            selectDonor.addAmount(float(inputAmount))

            print(f'Thank you {selectDonor.getName()} for your generous donation of ${float(inputAmount):,.2f}')

            #add Donor if he/she is not in DonorDict
            if inputName not in DonorDict:
                DonorDict[selectDonor.getName()] = selectDonor

            response = input("Please select S for \"Send a Thank You\" C for \"Create a Report\" or Q to quit >")
            
        elif 'C' in response.upper():
            #print(f"Donor Name                | Total Given | Num Gifts | Average Gift")
            space=''
            print(f'Donor Name {space:<15}| Total Given {space:<10}| Num Gifts {space:<9}| Average Gift {space:<19}')
            print("-"*85)

            #Have to use lambda to sort the historical amount donated
            sortDonor = sorted(DonorDict.items(), key=lambda x: x[1].getAmount(), reverse = True)
            for d in sortDonor:
                #print("{:>25} ${}{:,.2f}{:>18}{:,.2f}{:>5}${:>15}{:.2f}".format(v.getName(), '  ', 
                #        v.getAmount(),space, v.getCount(),space,space, v.getAverge()))
                print("{:<25} ${:>12,.2f}{:>22}{:<10}${:>12,.2f}".format(d[1].getName(), d[1].getAmount(), d[1].getCount(), space,d[1].getAverge()))

            response = input("Please select S for \"Send a Thank You\" C for \"Create a Report\" or Q to quit >")

        else: 
            print("Thank you")
            exit() 

       