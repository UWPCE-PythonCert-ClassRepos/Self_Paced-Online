#!/usr/bin/env python3
print ("Today we formatstrings. We start with the tuple:")
#setup...
seq_1 = (2, 123.4567, 10000, 12345.67)
print(seq_1, "\n")
print(seq_1[0])
print(seq_1[1])
print(seq_1[2])
print(seq_1[3])


print("---Task 1--Prescribed format---------------------------------")
#format to produce: 'file_002 :   123.46, 1.00e+04, 1.23e+04'
form_logic = 'file_{:03d}: {:05.2f}, {:0.2e}, {:0.2e}'
print(form_logic.format(*seq_1),"\n")


print("---Task 2--reformat - using f'-string format--------------")
#format usingf-string formatting: 'file_002 :   123.46, 1.00e+04, 1.23e+04'
out_2 = f'file_{seq_1[0]:03d}: {seq_1[1]:5.2f}, {seq_1[2]:.2e}, {seq_1[2]:.2e}'
print(out_2,"\n")


print("---Task 3--Dynamc Buildup of strings-------------------")
print("The 3 numbers are {:d}, {:d}, {:d} ".format (1,2,3))
dyn_tup=[]
ent = input("Enter a series of numbers to start a tuple:")
set_in = ent.split()
for i in set_in:
    dyn_tup.append(int(i))              
def formatter(in_tup):
    c = len(in_tup)
    return (('The {} numbers in the tuple are: \n' + ", ".join(['{}']*c)).format(c, *in_tup))
print(formatter(dyn_tup), "\n")
    
print("---Task 4-- tupple, re-aligned-------------------")
seq_4 = 4, 30, 2017, 2, 27
print(f'We start with te tuple: {seq_4}' "\n")
print('format the tuple to get the string: 02 27 2017 04 30')

print(f'{seq_4[3]:02d} {seq_4[4]:2d} {seq_4[2]:4d} {seq_4[0]:02d} {seq_4[1]:2d} \n')


print("---Task 5--f-strings-------------------")
name= input("For fun... Enter the name of your 'Alter-Ego:' ")
print("\n" f'Ya-your alter ego is {name}?   No kidding?  The great {name.upper()}! \n  Well, welcome.')
seq_5 = 'oranges', 1.3, 'lemons', 1.1
print("\n"f'Now, on with the assignment....  We will be formatting thetuple: {seq_5}')
#format to print "The weight of an orange is 1.3 and the weight of a lemon is 1.1"
print(f'The weight of an {seq_5[0][:-1]} is {seq_5[1]} and the weight of a {seq_5[2][:-1]} is {seq_5[3]}. \n')  


print("---Task 6--strings in collumns-------------------\n")
seq_6_1 = ("Tom", 67, 5863.90), ("Vic", 43, 63.90), ("John", 32, 677), ("Lucy", 58, 1200), ("Jack", 37, 234.5)
print(seq_6_1)
for entry in seq_6_1:
    print("Name: {:>8}, age {:3}  owes ${:>6,.02f}".format(*entry))
 
 
print("\n Task six part 2 output: print sequence in columns of 5... no 5 with 2 decimal places")
seg_6_2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(("{:7.2f}"*len(seg_6_2)).format(*seg_6_2))