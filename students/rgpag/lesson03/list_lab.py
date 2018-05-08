#!/usr/bin/env

#series1
series1 = ["Apples","Pears","Oranges","Peaches"]
def series_1():
	print(series1)
	response = [input("Please enter another fruit > ")]
	series1=series1+response
	print(series1)
	response = int(input("Please pick a number "))
	print(response, series1[response-1])
	series1= ["Tomato"]+series1
	print(series1)
	series1.insert(0,"Durian")
	print(series1)
	for i in range(len(series1)):
		x=series1[i]
		if x[0]=="P":
			print(x)

#series2
def series_2():
	series2=series1
	print(series2)
	del series2[len(series2)-1]
	print(series2)
	response = input("Please enter fruit to del ")
	while response not in series2:
		response = input("Please enter fruit to del ")
	series2.remove(response)
	print(series2)

#series2 bonus
	series22=series2*2
	print(series22)
	response2=input("Please enter fruit to del ")
	while response2 not in series22:
		response2 = input("Come on, please select fruit from list to del ")
	while response2 in series22:
		series22.remove(response2)
	print(series22)

#series3
def series_3():
	series3=series1
	print(series3)
	responsei=list(range(len(series3)))
	for i in range(len(series3)):
		response3=input("Do you like " + series3[i].lower() + "? ")
		while response3 not in ("yes","no"):
			response3=input("Please respond 'yes' or 'no', do you like "+ series3[i].lower()+"? ")
		responsei[i]=response3
	print(responsei)
	for j in range(len(series3)):
		if responsei[j]=="no":
			del series3[j]
	print(series3)

#series4
def series_4():
	series4 = series1[:]
	for i in range(len(series4)):
		temp = series4[i]
		temp2=temp[::-1]
		series4[i]=temp2
		print(temp2)
	print(series4)
	del series4[-1]
	print(series4)
	print(series1)







