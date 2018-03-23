#!/usr/bin/env python3
#Series 1
list_ = ["Apples","Pears","Oranges","Peaches"]
print(list_)
print("Please add one more fruit to the list")
response = input()
list_.append(response)
print(list_)
print("Please enter a number")
response_num = input()
print(response_num," ",list_[int(response_num)+1])
list_=["Bananas"]+list_
print(list_)
list_.insert(0,"Grapes")
print(list_)
for i in list_:
	if i[0] == 'P':
		print(i)


#Series 2
print(list_)
list_=list_[:-1]
print(list_)
print("What fruit would you like to remove")
response = input()
if response in list_:
	list_.remove(response)
print(list_)

#Series 3
bool = False
for item in list_:
	print("Do you like "+item.lower())
	response = input()
	if response == "no":
		list_.remove(item)
	elif response != "yes":
		while bool == False:
			print("Please enter either yes or no")
			response = input()
			if response == "yes" or response == "no":
				bool = True
print(list_)

#Series 4
list_copy = []
str_ = ''
for item in list_:
	for i in range(len(item)-1,-1,-1):
			# print(i)
			if i == 0:
				str_+=item[i]
			else:
				str_+=item[i]
	list_copy.append(str_)
	str_=''
list_copy= list_copy[:-1]
print(list_copy)








