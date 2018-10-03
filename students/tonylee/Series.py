fruitList = ["Apples", "Pears", "Oranges", "Peaches"]

def add_fruit_at_end():
    newFruit = get_new_fruit()
    fruitList.append(newFruit)

def print_fruit_list(fruitList):
    print(fruitList)

def get_fruit_name(index):
    print("Fruit[" + str(index) + "] = " + fruitList[index-1])

def get_fruit_number():
	  prompt = "Enter the fruit's number in the fruit list: "
	  fruitIndex = int(input(prompt))
	  return fruitIndex

def add_fruit_at_front():
    newFruit = get_new_fruit()
    global fruitList
    fruitList = [newFruit] + fruitList
    print_fruit_list(fruitList)

def add_fruit_at_front_with_insert():
    newFruit = get_new_fruit()
    fruitList.insert(0, newFruit)
    print_fruit_list(fruitList)

def display_all_fruits_begin_with_p():
    print("List of all fruits that begin with \"P\": ", end= " ")
    for fruit in fruitList:
        if fruit[:1] == 'P':
            print(fruit, end=" ")
    print()

def get_new_fruit():
    prompt = "Enter a fruit for adding to the list: "
    newFruit = input(prompt)
    return newFruit

def get_answer(fruitName):
      prompt = "Do you like " + fruitName.lower() + " ?"
      answer = input(prompt)
      return answer

def isValidAnswer(answer):
      validAnswer = ["yes", "no"]
      if answer in validAnswer:
          return True
      else:
          return False

def series1():
    print_fruit_list(fruitList)
    add_fruit_at_end()
    print_fruit_list(fruitList)
    get_fruit_name(get_fruit_number())
    add_fruit_at_front()
    add_fruit_at_front_with_insert()
    display_all_fruits_begin_with_p()

def remove_last_fruit():
    print("Remove the last fruit in the list")
    fruitList.pop()

def remove_fruit():
    prompt = "Enter a fruit you want to delete from the list: "
    deleteFruit = input(prompt)
    for fruit in fruitList:
        if fruit == deleteFruit:
            fruitList.remove(deleteFruit)

def series2():
    print_fruit_list(fruitList)
    remove_last_fruit()
    print_fruit_list(fruitList)
    remove_fruit()
    print_fruit_list(fruitList)

def series3():
    global fruitList
    fruits = fruitList.copy()
    for fruit in fruitList:
        answer = get_answer(fruit)
        while not isValidAnswer(answer):
            print("Please answer with yes or no.")
            answer = get_answer(fruit)
        if answer == "no":
            fruits.remove(fruit)
    fruitList = fruits.copy()
    print_fruit_list(fruitList)

def copy_and_reverse_fruit_list():
    fruits = fruitList.copy()
    newFruitList = []
    for fruit in fruits:
        newFruitList.append(reverse_fruit_name(fruit))
    return newFruitList

def reverse_fruit_name(fruit):
    return fruit[::-1]

def series4():
    print_fruit_list(copy_and_reverse_fruit_list())
    remove_last_fruit()
    print_fruit_list(fruitList)

series1()
series2()
series3()
series4()
