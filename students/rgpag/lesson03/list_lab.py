#!/usr/bin/env python3

# series1
print("Series 1")
series1 = ["Apples", "Pears", "Oranges", "Peaches"]
print(series1)
response = [input("Please enter another fruit > ")]
series1 = series1 + response
print(series1)
response = int(input("Please pick a number "))
print("Fruit " + str(response) + ": " + series1[response-1])
series1 = ["Banana"]+series1
print(series1)
series1.insert(0, "Strawberries")
print(series1)
for i in range(len(series1)):
    x = series1[i]
    if x[0] == "P":
        print(x)


# series2
print('\nSeries 2')
series2 = series1[:]
print(series2)
del series2[-1]
print(series2)
response = input("Please enter fruit to del ")
while response not in series2:
    response = input("Please enter fruit to del ")
series2.remove(response)
print(series2)


# series2 bonus
print('\nSeries 2 bonus')
series22 = series2*2
print(series22)
response2 = input("Please enter fruit to del ")
while response2 not in series22:
    response2 = input("Please select fruit from list to del ")
while response2 in series22:
    series22.remove(response2)
print(series22)


# series3
print('\nSeries 3')
series3 = series1[:]
print(series3)
y_n_list = []
for i in range(len(series3)):
    response3 = input("Do you like " + series3[i].lower() + "? ")
    while response3 not in ("yes", "no"):
        response3 = input("Please respond 'yes' or 'no', do you like " +
                          series3[i].lower() + "? ")
    y_n_list.append(response3)
print(y_n_list)
j = 0
temp = []
for j in range(len(y_n_list)):
    if y_n_list[j] == "yes":
        temp.append(series3[j])
print(temp)


# series4
print('\nSeries 4')
series4 = series1[:]
reversed_fruits = []
for fruit in series4:
    reversed_fruits.append(fruit[::-1])
print(reversed_fruits)

del series4[-1]
print(series4)
print(series1)
