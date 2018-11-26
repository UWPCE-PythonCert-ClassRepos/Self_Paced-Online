fruit = ["apples","oranges","Pear","peaches","lemon"]

print("\n")
print(fruit)

print("\nSeries 3")

for item in fruit:
    answer = input("\ndo you like " + item.lower() + " > ")
    answer = str(answer)
    while answer not in ["yes","no"]:
        answer = input("\nthis is a yes/no question. Do you like " + item.lower() + " > ")
        answer = str(answer)
    else:
        if answer.lower() == "no":
            fruit.remove(item)
            print("remaining fruit: ") 
            print(fruit)
        else:
            print("remaining fruit: ") 
            print(fruit)


"""
Once more, using the list from series 1:

Make a copy of the list and reverse the letters in each fruit in the copy.
Delete the last item of the original list. Display the original list and the copy.
"""

fruit = ["apples","pears","oranges","peaches"]

fruit_r = fruit[:]

fruit_r = [item[::-1] for item in fruit_r]

fruit.pop(3)

print("\nComparing fruit list to copied fruit list\n")
print(fruit)
print("\n")
print(fruit_r)
