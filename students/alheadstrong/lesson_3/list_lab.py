'''Author: Alex Filson
Updated: 1.18.19
List Lab for Lesson 3
Py210, Online Self-Paced
'''

def series1(fruit):
    '''Display and add to a list of fruit based on user input'''
    seriesheader("Series 1")
    print(fruit)
    newfruit = input('Enter the name of a fruit to be added:')
    fruit.append(newfruit) #Add item to end of list, creates new global list
    print(fruit)
    num = int(input('Enter a number:'))-1
    print('The fruit at number {} is {}.'.format(num+1,fruit[num]))

    newfruit = input('Add a fruit to the beginning of the list:')
    newfruitlist = [newfruit] #Seeing an type error when on one line.
    fruit = newfruitlist + fruit
    print(fruit)

    newfruit = input('Add another fruit to the beginning of the list:')
    fruit.insert(0,newfruit)
    print(fruit)

    print("These are all of the fruit that begin with 'P':")
    for i in fruit:
        if i[0].lower() == 'p':
            print (i)

def series2(fruit):
    '''Display and remove items from list based on user input'''
    seriesheader("Series 2")
    print(fruit)
    fruit.pop() #Removes last item
    print(fruit)
    dfruit = input("Select a fruit to remove:")
    fruit.remove(dfruit) # No exception handling, see below
    fruit = fruit*2
    length = len(fruit)
    while length == len(fruit):
        dfruit = input("Select a fruit to remove:")
        for f in fruit:
            if f == dfruit:
                fruit.remove(dfruit)
        if length == len(fruit):
            print("Fruit not found!")
            print("Current fruit: {}".format(fruit))
    print(fruit)



def series3(fruit):
    '''Copy list, reverse letters in each item. Remove last item of
    original list, and displahy both lists'''
    seriesheader("Series 3")
    for f in fruit[:]:
        ans = input("Do you like {}? (yes or no)".format(f.lower()))
        while ans != 'yes' and  ans != 'no':
            ans = input("Do you like {}? (yes or no)".format(f.lower()))
            if ans is not "yes" and ans is not "no":
                print("Please respond with 'yes' or 'no'.")
        if ans == "no":
            fruit.remove(f)
    print("Some fruits you like: {}".format(fruit))

def series4(fruit):
    seriesheader("Series 4")
    fruitcopy = []
    for f in fruit:
        fruitcopy.append(f[::-1])
    fruit = fruit[:-1]

    print("Original list, minus last item: {}".format(fruit))
    print("Modified list with reversed letters: {}".format(fruitcopy))

def seriesheader(seriesname):
    '''Print some text to indicate new series to user.'''
    print()
    print('{}{}{}'.format('*'*10,seriesname,'*'*10))
    print()

if __name__ == '__main__':
    fruitlist = ['Apples','Pears','Oranges','Peaches']
    series1(fruitlist[:])
    series2(fruitlist[:])
    series3(fruitlist[:])
    series4(fruitlist[:])

