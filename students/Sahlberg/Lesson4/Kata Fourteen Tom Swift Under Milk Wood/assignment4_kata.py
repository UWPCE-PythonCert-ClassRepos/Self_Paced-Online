"""Assignment 4
Kata Fourteen: Tom Swift Under Milk Wood
1/6/2019
Python 210"""

with open('C:\\Users\Ian\Documents\GitHub\Self_Paced-Online\students\Sahlberg\Lesson4\Kata Fourteen Tom Swift Under Milk Wood\\test.txt', 'r') as file:
    kata = file.read().split()

print(kata)

kata_set = []

for i in range(len(kata)-2):
    kata_set.append((kata[i], kata[i+1], kata[i + 2]))

print(kata_set)
