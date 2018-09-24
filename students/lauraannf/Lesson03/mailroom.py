# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 13:06:38 2018

@author: Laura.Fiorentino
"""
DonorList = [
        'Frank Reynolds', [10, 20, 50], 
        'Dee Reynolds', [25, 100], 
        'Dennis Reynolds', [10, 50], 
        'Mac McDonald', [25, 35, 20], 
        'Charlie Kelly', [0.25]
        ]

def namefunc(Name):
    while Name == 'list' or Name == 'List':
                print(DonorList[0::2])
                Name = input("Type full donor name, or ''list'' for choices?>")
    if Name not in DonorList:
        DonorList.append(Name)
        Donation = input("Donation Amount?>")
        Donation = float(Donation)
        DonorList.append([Donation])      
    else:
        indx =  DonorList.index(Name)
        Donation = input("Donation Amount?>")
        Donation = float(Donation)
        DonorList[indx+1].append(Donation)
    print('Email Creation:')
    print('Dear {}, \n'
          'Thank you so much for your generous donation of ${:.2f} \n'
          'Sincerely, \n'
          'Laura F'.format(Name,Donation))
def reportfunc():
    print('-------List of Donors-------')
    print('{:<20}{:<20}{:<20}{:<20}'.format('Donor Name', 'Total Donated', '# of Donations', 'Average Donation'))
    print('-----------------   '*4)
    for it in range(0,len(DonorList),2):
        print('{:<20}${:<20.2f}{:<20d}${:<20.2f}'.format(DonorList[it], sum(DonorList[it+1]), len(DonorList[it+1]),  sum(DonorList[it+1])/len(DonorList[it+1])))              
    
def main():
    print('----------Mailroom------------')
    Task = input("Choose an action: [1] Send a Thank You; [2] Create a Report; [3] Quit)>")
    while Task not in ('1','2','3'):
        Task = input("Choose an action: [1] Send a Thank You; [2] Create a Report; [3] Quit)>")
    while Task !='3':  
        if Task == '1':
            Name = input("Type full donor name, or ''list'' for choices?>")
            namefunc(Name)
            Task = input("Choose an action: [1] Send a Thank You; [2] Create a Report; [3] Quit)>")
        elif Task == '2':
            reportfunc()
            Task = input("Choose an action: [1] Send a Thank You; [2] Create a Report; [3] Quit)>")

if __name__ == '__main__':
    main()