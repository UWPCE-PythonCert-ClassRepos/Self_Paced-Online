# in filesystem copy Lesson3_Ex3_strformat_lab.py into new folder:
#        C:\Users\v-micmcd.Redmond\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson3
# wk: cd C:\Users\v-micmcd.Redmond\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson3
# mo: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson3
# hm: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson3
# git status
# git add Lesson3_Ex3_strformat_lab.py
# git commit Lesson3_Ex3_strformat_lab.py
# git push
# goto https://github.com/geekwriter2/Self_Paced-Online/tree/master/students/MichaelM/lesson3/
# click Pull request > new pull request
# go back to assignment webpage and fill in submission comments

my_four_element_tuple = (2, 123.4567, 10000, 12345.67)
my_headers = ["Name", "Age", "Cost"]
wizarding_clothes = (["Gandalf (cloak grey, heavily traveled)", 2019, 100000],
                     ["Potter (Yule Ball cape, black, size sm)", 16, 10000],
                     ["Ged (cloak, fine Gontish wool)", 99, 500],
                     ["Maleficent (cloak w/hood, black, victorian collar)", 90, 10000],
                     ["Jadis, 'The White Witch' (cloak snow leopard leatherette)", 1000, 10000],
                     ["Glinda (gown, glitter organza)", 54, 50000])


def pad_to_three_digits(my_int):
    """
    pads a number out to 3 digits

    {Extended description}

    Parameters:
    my_int (int): integer to be padded

    Returns:
    result (string): a padded number

    """
    my_int_length = len(str(my_int))
    result = ""
    if my_int_length == 3:
        result = str(my_int)
    elif my_int_length == 2:
        result = "{:0>2d}".format(my_int)
    elif my_int_length == 1:
        result = "{:0>3d}".format(my_int)
    return result


def my_formatter(numbers):
    """
        formats a list of integers

        {Extended description}

        Parameters:
        numbers (list): list to be formatted

        Returns:
        results (string): the formatted list of numbers

        """
    my_list_of_numbers = ", ".join("{:d}".format(my_num) for (my_num) in numbers)
    results = f"My list of numbers is: {my_list_of_numbers}."
    return results


if __name__ == "__main__":
    my_filename = "file_{}".format(pad_to_three_digits(my_four_element_tuple[0]))
    my_padded_number = pad_to_three_digits(my_four_element_tuple[0])
    my_filename = "file_{}".format(pad_to_three_digits(my_four_element_tuple[0]))
    my_float_to_two_dec = my_four_element_tuple[1]
    my_sci_sample_number = my_four_element_tuple[2]
    my_sci_sample_number_to_three_digits = my_four_element_tuple[3]
    print()
    print("Task 1:")
    print("The filename for correct alphabetation is: {}".format(my_filename))
    print("{} to 2 decimal places is: {:.2f}".format(my_float_to_two_dec, my_float_to_two_dec))
    print("{} in scientific notation is: {:.2e}".format(my_sci_sample_number, my_sci_sample_number))
    print("{} in scientific notation with 3 significant digits is: {:0.3e}".format(my_sci_sample_number_to_three_digits,
                                                                                   my_sci_sample_number_to_three_digits))
    print()
    print("Task 2 (Task 1 in 'f' strings):")
    print(f"The filename for correct alphabetation is: {my_filename}")
    print(f"{my_float_to_two_dec} to 2 decimal places is: {my_float_to_two_dec:.2f}")
    print(f"{my_sci_sample_number} in scientific notation is: {my_sci_sample_number:.2e}")
    print(
        f"{my_sci_sample_number_to_three_digits} in scientific notation with "
        f"3 significant digits is: {my_sci_sample_number_to_three_digits:0.3e}")
    print()
    print("Task 3:")
    my_number_list = (1, 2, 3)
    print(my_formatter(my_number_list))
    print()
    print("Task 4:")
    my_tuple = (4, 30, 2017, 2, 27)
    my_string = "My new string {month} {day} {year} {hour} {minute}".format(month=my_tuple[0] - 2,
                                                                            day=my_tuple[1] - 3,
                                                                            year=my_tuple[2],
                                                                            hour=my_tuple[3] + 2,
                                                                            minute=my_tuple[4] + 4
                                                                            )
    print(my_string)
    print()
    print("Task 5:")
    my_list = ['orange', 1.3, 'lemon', 1.1]
    print(f"The weight of an {my_list[0]} is {my_list[1]} and the weight of a {my_list[2]} is {my_list[3]}")
    print()
    print("Task 6: my wizarding clothing sale")
    print("{name:<70}{age:<10}{cost:}".format(name=my_headers[0], age=my_headers[1], cost=my_headers[2]))
    for row in wizarding_clothes:
        print("{name:{width}}{age:<10,}{cost:,}".format(width=70, name=row[0], age=row[1], cost=row[2]))
    my_ten_char_tuple = tuple(range(10))
    my_evenly_spaced_tuples = ""
    for t in my_ten_char_tuple:
        my_evenly_spaced_tuples = my_evenly_spaced_tuples + "{0:>5}".format(str(t))
    print()
    print("My evenly spaced tuple: {0:>50}".format(str(my_evenly_spaced_tuples)))
    print("end")

