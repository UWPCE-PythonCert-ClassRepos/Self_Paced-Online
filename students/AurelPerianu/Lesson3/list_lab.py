#!/usr/bin/env python3
#list exercise

list=["Apples","Pears","Oranges","Peaches"]

def series_1(lst):
    print ("series1_function")
    print (lst)
    response = input("add a fruit > ")
    lst.append(response)
    print (lst)
    nr = int(input("enter a fruit location > "))
    print (nr, lst[nr-1])
    #nrq = input("Enter a nr > ")
    lst=["Cherry"]+lst
    lst.insert(0,"Bananas")
    print(lst)
    for i in lst:
        if i[0]=='P':
            print (i)
    return(lst)

def series_2(lst):
    print ("series2_function")
    print('Original list:\n', lst)
    lst.remove(lst[-1])
    print ('List after last elem removal:\n', lst)
    lst=2*lst
    print ('List after multiplication:\n',lst)
    response = input(" fruit to remove > ")
    print (response)
    while response not in lst:
        print ('fruit not in the list-try again')
        response = input(" fruit to remove > ")
    for lx in lst:
        if lx==response:
            lst.remove(response)
    print ('List after deletion:\n',lst)

def series_3(lst):
    print ("series3_function")
    print ('Original list:\n',lst)
    #lst2=lst[:]
    for ls in lst[:]:
        response = str(input(" do you like "+ ls.lower() + "> ")).lower()
        while response not in ["yes", "no"]:
            response = str(input(" do you like "+ ls.lower() + "> ")).lower()
            print (response)
        if response=='no':
            lst.remove(ls)
    #print (response)
    print('List after yes/no responses:\n',lst)


def series_4(lst):
    print ("series4_function")
    print ('Original list:\n',lst)
    lst_copy=[]
    for ls in lst[:]:
        #lst_copy.remove(ls)
        ls=ls[::-1]
        lst_copy.append(ls)
        #lst.pop()
    print ('Reversed list:\n',lst_copy)

list2=series_1(list)
list3=list2[:]
#use the series_1 return
series_2(list3)
#use the series_1 return
list3=list2[:]
series_3(list3)
#use the series_1 return
list3=list2[:]
series_4(list3)
