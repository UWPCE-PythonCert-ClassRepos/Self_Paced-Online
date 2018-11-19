# in filesystem copy Lesson3_Ex2_Lists.py into new folder C:\Users\v-micmcd.Redmond\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson3
# wk: cd C:\Users\v-micmcd.Redmond\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson3
# mo: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson3
# hm: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson3
# git status
# git add Lesson3_Ex2_Lists.py
# git commit Lesson3_Ex2_Lists.py
# git push
# goto https://github.com/geekwriter2/Self_Paced-Online/tree/master/students/MichaelM/lesson3/
# click Pull request > new pull request
# go back to assignment webpage and fill in submission comments

my_fruit_cart_tuple = ("Apples", "Pears", "Oranges", "Peaches")
their_fruit_basket = []
discarded_fruit = []


def my_p_fruit_selection(letter, fruit_cart):
    """
        Returns a list of terms beginning with a specific letter given a list of assorted terms

        {Extended description}

        Parameters:
        letter(str): the beginning letter of the terms to be returned
        fruit_cart (list): a list of terms

        Returns:
        list: All terms which begin with the letter provided

        """
    result = []
    for i in fruit_cart:
        if i.startswith(letter):
            result.append(i)
    return result


def my_fruit_remove_selection(my_fruit, fruit_cart):
    """
        removes a specific term from a list

        {Extended description}

        Parameters:
        my_fruit (string): term to be deleted from the list
        fruit_cart (list): a list of terms

        Returns:
        list: a list of terms minus the term provided

        """
    result = []
    for i in fruit_cart:
        if i != my_fruit:
            result.append(i)
    return result


if __name__ == "__main__":
    my_fruit_cart = list(my_fruit_cart_tuple)
    start_seq = list(my_fruit_cart)
    print("Series 1:")
    start_result = "A well-stocked fruit cart: {0:<2}{1:}".format(" ", start_seq)
    print(start_result)
    response_1 = input("If you throw in another fruit you may win a surprise > ")
    my_fruit_cart.append(response_1)
    response_2 = input("Now pick a number between 1 and {} > ".format(len(my_fruit_cart)))
    my_pick = my_fruit_cart[int(response_2) - 1]
    print("Congratulations! You picked {} ({})".format(my_pick, response_2))
    response_3 = input("Now, toss in another > ")
    my_fruit_cart = [response_3] + my_fruit_cart
    print("Wonderful, here's a look at our new fruit cart {})".format(my_fruit_cart))
    response_4 = input("Add one in more fruit to the pile... > ")
    my_fruit_cart.insert(len(my_fruit_cart), response_4)
    print("And another look: {}".format(my_fruit_cart))
    print("You won! I hope you like fruits that begin with 'P': {}".format(
        my_p_fruit_selection('P', my_fruit_cart)))
    print()
    print("Series 2:")
    print("Of course there's more. For reference, the new fruit cart: {}".format(my_fruit_cart))
    print("Let's remove the last fruit ({}) from our fruit cart)".format(my_fruit_cart[-1]))
    my_fruit_cart = my_fruit_cart[:-1]
    print("Leaving us with: {}".format(my_fruit_cart))
    response_5 = input("You've been patient. TY! Go ahead and pick a fruit to take with you > ")
    my_fruit_cart = my_fruit_remove_selection(str(response_5), my_fruit_cart)
    print("This is all we have left: {}".format(my_fruit_cart))
    print()
    print("Series 3:")
    print("Of course there's more. For reference, our new fruit cart: {} ".format(my_fruit_cart))
    for fruit in reversed(my_fruit_cart):
        response_6 = input("Would you like to take some {} with you? > ".format(fruit.lower()))
        while response_6.lower() not in ("yes", "no"):
            response_6 = input(
                "Please answer yes or no. Would you like to take some {} with you? > ".format(fruit.lower()))
        if response_6 == "no":
            my_fruit_cart.remove(fruit)
            discarded_fruit.append(fruit)
        elif response_6 == "yes":
            their_fruit_basket.append(fruit)
            my_fruit_cart.remove(fruit)
    print(
        "{} Congratulations, a well chosen fruit basket. For a delicious fruit salad consider adding {} next time.".format(
            their_fruit_basket,
            discarded_fruit))
    print()
    print("Series 4:")
    my_fruit_cart_reversed = list(my_fruit_cart_tuple)
    for fruit in reversed(my_fruit_cart_reversed):
        rev_fruit = fruit[::-1]
        my_fruit_cart_reversed.remove(fruit)
        my_fruit_cart_reversed.append(rev_fruit)
    print("Or even better, next time try some bizzaro fruit: {}".format(my_fruit_cart_reversed))
    print("... or stick with some of the normal stuff: {}".format(my_fruit_cart_tuple[0:len(my_fruit_cart_tuple) - 1]))
