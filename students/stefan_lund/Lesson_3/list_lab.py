# /usr/bin/env python3

# list_lab.py
# ['Pineapple', 'Plum', 'Apples', 'Pears', 'Oranges', 'Peaches', 'Banana']


def user_input(q):
    """
        generates a request for user input
    """
    prompt = q + " : "
    response = input(prompt)
    return response


def series_1():
    """

    """

    fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
    questions_str = "{0}/{1}/{0}/{0}".\
        format("Enter another fruit", "Enter a number, 1 to 4")
    questions = questions_str.split("/")
    io = ''
    print()
    for question in questions:
        if io.isdigit():
            print("{}   {}\n".format(int(io), fruit_list[int(io) - 1]))
        else:
            print(fruit_list, "\n")
        io = user_input(question)
        if not io.isdigit():
            if len(fruit_list) == 4:
                fruit_list.append(io)
            elif len(fruit_list) == 5:
                fruit_list = [io] + fruit_list
            elif len(fruit_list) == 6:
                fruit_list.insert(0, io)

    print(fruit_list, "\n")
    for fruit in fruit_list:
        if fruit[0] == 'P':
            print(fruit)

    return fruit_list


def series_2(fruit_list):
    """
    fruit_list: expects a list type, the list produced by series_1
    """
    f_l = fruit_list[:]
    print("\n\n", f_l)

    f_l.pop()
    print("\n", f_l)

    fruit_to_delete = input("\nWhat fruit should be removed? ")
    f_l.remove(fruit_to_delete)
    print("\n", f_l)

    # Bonus Round

    f_l = fruit_list * 2
    print("\n\n", f_l)

    fruit_to_delete_in_fruit_list = False
    while not fruit_to_delete_in_fruit_list:
        fruit_to_delete = input("\nWhat fruit should be removed? ")
        fruit_to_delete = fruit_to_delete.title()
        fruit_to_delete_in_fruit_list = fruit_to_delete in f_l

    while fruit_to_delete in f_l:
        f_l.remove(fruit_to_delete)
    print("\n", f_l)


def series_3(fruit_list):
    """
    fruit_list: expects a list type, the list produced by series_1
    """
    f_l = fruit_list[:]
    print("\n\n", f_l)

    for fruit in fruit_list:

        question = "\nDo you like {}? ".format(fruit)
        reply = input(question)
        reply = reply.lower()

        yes_or_no = reply in ("yes", "no")

        while not yes_or_no:
            reply = input("You have to answer with YES or NO! ")
            reply = reply.lower()
            yes_or_no = reply in ("yes", "no")

        if reply == "yes":
            f_l[f_l.index(fruit)] = fruit.lower()
        else:
            f_l.remove(fruit)

    print("\n{}".format(f_l))


def series_4(fruit_list):
    """
    fruit_list: expects a list type, the list produced by series_1
    """

    f_l = fruit_list[:]

    for i in range(len(fruit_list)):
        f_l[i] = fruit_list[i][::-1]

    del fruit_list[-1]

    print("\noriginal list: {}\ncopy:          {}".format(fruit_list, f_l))


if __name__ == '__main__':
    fruit_list = series_1()
    series_2(fruit_list)
    series_3(fruit_list)
    series_4(fruit_list)
