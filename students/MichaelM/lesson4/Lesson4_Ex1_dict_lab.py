# in filesystem copy Lesson4_Ex1_dict_lab.py into new folder:
#        C:\Users\v-micmcd.Redmond\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson4
# wk: cd C:\Users\v-micmcd.Redmond\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson4
# mo: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson4
# hm: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson4
# git status
# git add Lesson4_Ex1_dict_lab.py
# git commit Lesson4_Ex1_dict_lab.py
# git push
# goto https://github.com/geekwriter2/Self_Paced-Online/tree/master/students/MichaelM/lesson4/
# click Pull request > new pull request
# go back to assignment webpage and fill in submission comments


chris_profile_dict = {"name": "chris", "city": "Seattle", "cake": "chocolate"}


def edit_chris_profile(key_to_edit, action, value_edited=""):
    """
        edits a dictionary based on user choice

        {Extended description}

        Parameters:
        key_to_edit (string): key
        value_edited (string): key
        action (string): key

        Returns:
        {none}

        """
    if action == "delete":
        del chris_profile_dict[key_to_edit]
    elif action == "add":
        chris_profile_dict[key_to_edit] = value_edited


if __name__ == "__main__":
    print("")
    print("Dictionaries1...")
    print(f"Chris's: profile: {chris_profile_dict}")
    edit_chris_profile("cake", "delete")
    print(f"Since Chris no longer likes cake, here is his new profile: {chris_profile_dict}")
    edit_chris_profile("fruit", "add", "mango")
    print(f"Since Chris is eating healthier, here is his new profile: {chris_profile_dict}")
    tmp_list = list(chris_profile_dict.keys())
    print(f"Our profile of Chris contains these keys: {tmp_list}")
    tmp_list = list(chris_profile_dict.values())
    print(f"...and his profile contains these values: {tmp_list}")
    is_there_cake = "cake" in chris_profile_dict.keys()
    print(f"Is there cake in the profile's keys: {is_there_cake}")
    is_there_cake = "mango" in chris_profile_dict.values()
    print(f"Is there Mango in the profile's values: {is_there_cake}")
    print("")
    print("Dictionaries2...")
    print(f"For reference Chris' current profile: {chris_profile_dict}")
    tmp_dict_of_ts = {}
    for key, value in chris_profile_dict.items():
        number_of_ts = value.lower().count("t")
        tmp_dict_of_ts[key] = number_of_ts
    print(f"Chris's: profile now includes a dictionary counting t's: {tmp_dict_of_ts}")
    print("")
    print("Sets1...")
    s2 = set([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
    s3 = set([0, 3, 6, 9, 12, 15, 18])
    s4 = set([0, 4, 8, 12, 16, 20])
    print(f"Set 2: {s2}\nSet 3: {s3}\nSet 4: {s4}")
    print(f"true/false: s3 is a subset of s2: {s3.issubset(s2)}, true/false: s4is a subset of s2: {s4.issubset(s4)}")
    print("")
    print("Sets2...")
    python_set = set(['P', 'y', 't', 'h', 'o', 'n'])
    python_set.add('i')
    print(f"Adding 'i' to a set of Python letters: {python_set}")
    marathon_set = frozenset(('m', 'a', 'r', 'a', 't', 'h', 'o', 'n'))
    union_set = python_set.union(marathon_set)
    intersection_set = python_set.intersection(marathon_set)
    print(f"The union of python_set and marathon_set is {union_set}\nThe intersection is: {intersection_set}")

