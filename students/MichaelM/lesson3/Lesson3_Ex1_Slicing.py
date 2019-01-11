# in filesystem copy Lesson3_Ex1_Slicing.py into new folder
# C:\Users\v-micmcd.Redmond\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson3
# wk: cd C:\Users\v-micmcd.Redmond\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson3
# mo: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson3
# hm: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson3
# run Lesson3_Ex1_Slicing.py
# git status
# git add Lesson3_Ex1_Slicing.py
# git commit Lesson3_Ex1_Slicing.py
# git push
# goto https://github.com/geekwriter2/Self_Paced-Online/tree/master/students/MichaelM/lesson3/
# click Pull request > new pull request
# go back to assignment webpage and fill in subumission comments

my_animal_parade = ("aardvark", "beetle", "caribou", "dingo", "emu", "fossa",
                    "goatfish", "hornbill", "iguana", "jackrabbit", "koala", "llama",
                    "mouse", "narhwal", "ostrich", "penguin", "quail", "reindeer")


def my_new_animal_leader(sequence):
    """
        for a given list returns a list with the first and last items reversed.

        {Extended description}

        Parameters:
        sequence (list):

        Returns:
        list

    """
    new_sequence = sequence
    last_element = len(new_sequence) - 1
    new_lead = new_sequence[last_element]
    new_last = new_sequence[0]
    del new_sequence[last_element]
    del new_sequence[0]
    new_sequence.insert(0, new_lead)
    new_sequence.insert(last_element, new_last)
    return new_sequence


def reverse_my_animals(sequence):
    """
    reverses a list.

    {Extended description}

    Parameters:
    sequence (list):

    Returns:
    list

    """
    rev_sequence = sequence[::-1]
    return rev_sequence


def my_odd_animals(sequence):
    """
    for a given list returns every other item.

    {Extended description}

    Parameters:
    sequence (list):

    Returns:
    list

    """
    odds = sequence[::2]
    return odds


def my_leftover_animals(sequence):
    """
    For a given list removes the first four items and the last four. Each remaining even item is removed

    {Extended description}

    Parameters:
    sequence (list):

    Returns:
    list

    """
    remove_last_four = sequence[:-4]
    remove_first_four = remove_last_four[4:]
    minus_fours = remove_first_four[::2]
    return minus_fours


def animals_in_thirds(sequence):
    """
    Returns a copy of a list with the middle third, then last third, then the first third in the new order..

    {Extended description}

    Parameters:
    sequence (list):

    Returns:
    list

    """
    first = 0
    last = len(sequence)
    first_third_end = (len(sequence) // 3)
    second_third_end = last - first_third_end
    first_third_seq = sequence[first:first_third_end]
    second_third_seq = sequence[first_third_end:second_third_end]
    third_third_seq = sequence[second_third_end:last]
    new_thirds = second_third_seq + third_third_seq + first_third_seq
    return new_thirds


"""
done with the first and last items exchanged.
done with every other item removed.
done with the first 4 and the last 4 items removed, and then every other item in between.
done with the elements reversed (just with slicing).
middle third > last third > first third in a new order.
"""

if __name__ == "__main__":
    start_seq = list(my_animal_parade)
    new_leader_seq = my_new_animal_leader(list(my_animal_parade))
    odd_seq = my_odd_animals(list(my_animal_parade))
    leftover_seq = my_leftover_animals(list(my_animal_parade))
    rev_seq = reverse_my_animals(list(my_animal_parade))
    new_thirds_seq = animals_in_thirds(list(my_animal_parade))
    start_result = "My animal parade: {0:<27}{1:}".format(" ", start_seq)
    new_leader_result = "Let's exchange the first and last animals: {0:<2}{1:}".format(" ", new_leader_seq)
    odd_result = "The odd but not really unusual animals: {0:<5}{1:}".format(" ", odd_seq)
    leftover_result = "The leftover animal(s): {0:<21}{1:}".format(" ", leftover_seq)
    rev_result = "Let's start with the last animal first: {0:<5}{1:}".format(" ", rev_seq)
    thirds_result = "The new animal order by thirds: {0:<13}{1:}".format(" ", new_thirds_seq)

    print(start_result)
    print(new_leader_result)
    print(odd_result)
    print(leftover_result)
    print(rev_result)
    print(thirds_result)
