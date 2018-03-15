

"""
Thomas Horn
mailroom.py
Tracks donor information and automates the sending of thank you notes.
"""

# Global that holds donor history and the amounts donated.
DONOR_HISTORY = [
    ['Tom Horn',        599.23, 1000.00],
    ['Theo Hartwell',   0.01, 0.01, 0.1],
    ['Bailey Kimmitt',  8723.22, 27167.22, 91817.66],
    ['Paul Hubbell',    90012.32, 2312.24],
    ['David Beckham',   1817266.11, 123123.66, 111335.112]
]

def send_thanks():
    """
    Prompts user for a full name and performs an action based on the input.
    - 'list' -> shows a list of donor names and re-prompts
    - Name not in list -> adds the name to the data structure and uses it
    - Name in list -> use it
    After name is used -> prompt for donation amount and turn into a number.
    - Add that amount to donation history of selected user
    - Print thank you note
    - Returns to original prompt or quit to prompt
    """
    name_request = input("Please enter a donor's full name, or 'list' for a full list of donors.  'Quit' or 'Return' valid commands. ")

    # Return or Quit.
    if name_request.lower() == "quit":
        quit()

    if name_request.lower() == "return":
        return

    # List request.
    if name_request.lower() == 'list':
        for donors in DONOR_HISTORY:
            print(donors[0])

    name_request = name_request.title()
    donation_amount = float("Please enter a donation amount for {}".format(name_request))

    # Add to existing donor.

    # Create new donor and add amount.

    # Print thank you note.
        
        
        

def create_report():
    """
    Prints a list of donors sorted by total historical donation amount.
    - Includes donor name, total donated, number of donations, average donation
      amount.
    - Returns to original prompt or quit to prompt
    """
    pass

if __name__ == "__main__":
    # Select from options.  No checks to sanatize input.
    while True:
        choice = input(
        "Please select an option:\n\
        1 - Send Thanks\n\
        2 - Create Donor Report\n\
        3 - Quit\n")
        if choice == "1":
            send_thanks()
        if choice == "2":
            create_report()
        if choice == "3":
            print("Quitting.")
            break

    

"""
    - Ex:
Donor Name                | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------
William Gates, III         $  653784.49           2  $   326892.24
Mark Zuckerberg            $   16396.10           3  $     5465.37
Jeff Bezos                 $     877.33           1  $      877.33
Paul Allen                 $     708.42           3  $      236.14
    """


"""First, factor your script into separate functions. Each of the above tasks can be accomplished by a series of steps. Write discreet functions that accomplish individual steps and call them.

Second, use loops to control the logical flow of your program. Interactive programs are a classic use-case for the while loop.

Of course, input() will be useful here.

Put the functions you write into the script at the top.

Put your main interaction into an if __name__ == '__main__' block.

Finally, use only functions and the basic Python data types you’ve learned about so far. There is no need to go any farther than that for this assignment."""