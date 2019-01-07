#!/usr/bin/env python3

import os, json

data_file = None
data = {}

def get_data_from(file_name):
    """
    uses the json module to retrieve data from file as a dictionary
    file_name:  file name where the data of the donors etc. can be found.
                must be in the cwd,
    data:       expected to be in a dictionary
                {name:(amount, times donating), etc}
    """

    source = os.path.join(os.getcwd(), file_name)
    try:
        with open(source, 'r') as infile:
            # data_dict = json.load(infile)
            data = json.load(infile)

            return data
    except FileNotFoundError as e:
        stringerror = e.args  #  stringerror will have unintended info with it
        # errno, stringerror = e.args  -  this upsets the linter

        # file searched for:
        file = str(e).split(":")[-1].split("\\")[-1]

        message = "FileNotFoundError was caused by function: 'get_data_from()' \n"
        error_encountered = "Following problem was encountred: "
        looking_for = "\nFile searched for: "
        print(message, error_encountered, stringerror, looking_for, file)


def store_data():
    """
    writes data to data_file
    file_path:  abspath including file-name
    data:       dictionary
    """
    global data_file, data
    destination = os.path.join(os.getcwd(), data_file)

    try:
        with open(destination, 'w') as outfile:
            json.dump(data, outfile)
            print("\nstored data in: ", data_file)
    except FileNotFoundError as e:
        stringerror = e.args  #  stringerror will have unintended info with it
        # errno, stringerror = e.args  -  this upsets the linter

        # file searched for:
        file = str(e).split(":")[-1].split("\\")[-1]

        message = "FileNotFoundError was caused by function: 'store_data()' \n"
        error_encountered = "Following problem was encountred: "
        looking_for = "\nFile searched for: "
        print(message, error_encountered, stringerror, looking_for, file)
