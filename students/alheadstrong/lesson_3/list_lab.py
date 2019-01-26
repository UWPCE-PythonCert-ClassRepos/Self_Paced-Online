def series1(fruit):
    """Display and add to a list of fruit based on user input"""
    series_header("Series 1")
    print(fruit)
    new_fruit = input('Enter the name of a fruit to be added:')
    fruit.append(new_fruit)  # Add item to end of list, creates new global list
    print(fruit)
    num = int(input('Enter a number:'))-1
    print('The fruit at number {} is {}.'.format(num+1, fruit[num]))

    new_fruit = input('Add a fruit to the beginning of the list:')
    new_fruit_list = [new_fruit]  # Seeing an type error when on one line.
    fruit = new_fruit_list + fruit
    print(fruit)

    new_fruit = input('Add another fruit to the beginning of the list:')
    fruit.insert(0, new_fruit)
    print(fruit)

    print("These are all of the fruit that begin with 'P':")
    for i in fruit:
        if i[0].lower() == 'p':
            print(i)


def series2(fruit):
    """Display and remove items from list based on user input."""
    series_header("Series 2")
    print(fruit)
    fruit.pop()  # Removes last item
    print(fruit)
    d_fruit = input("Select a fruit to remove:")
    fruit.remove(d_fruit)  # No exception handling, see below
    fruit = fruit*2
    length = len(fruit)
    while length == len(fruit):
        d_fruit = input("Select a fruit to remove:")
        for f in fruit:
            if f == d_fruit:
                fruit.remove(dfruit)
        if length == len(fruit):
            print("Fruit not found!")
            print("Current fruit: {}".format(fruit))
    print(fruit)


def series3(fruit):
    """Copy list, reverse letters in each item. Remove last item of original list, and display both lists"""
    series_header("Series 3")
    for f in fruit[:]:
        ans = input("Do you like {}? (yes or no)".format(f.lower()))
        while ans != 'yes' and ans != 'no':
            ans = input("Do you like {}? (yes or no)".format(f.lower()))
            if ans != "yes" and ans != "no":
                print("Please respond with 'yes' or 'no'.")
        if ans == "no":
            fruit.remove(f)
    print("Some fruits you like: {}".format(fruit))


def series4(fruit):
    """Take list and display without last item. Display copy of list with items reversed."""
    series_header("Series 4")
    fruit_copy = []
    for f in fruit:
        fruit_copy.append(f[::-1])
    fruit = fruit[:-1]

    print("Original list, minus last item: {}".format(fruit))
    print("Modified list with reversed letters: {}".format(fruit_copy))


def series_header(series_name):
    """Print some text to indicate new series to user."""
    print('\n{}{}{}\n'.format('*'*10, series_name, '*'*10))


if __name__ == '__main__':
    fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
    series1(fruit_list[:])
    series2(fruit_list[:])
    series3(fruit_list[:])
    series4(fruit_list[:])