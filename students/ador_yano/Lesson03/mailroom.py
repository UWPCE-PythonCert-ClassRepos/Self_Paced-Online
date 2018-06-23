#!/usr/bin/env python3
# mailroom.py implements the Lesson 3 - Mailroom Part 1 assignment from UWPCE Python Programming

intro = '''UWPCE Python Programming: Lesson 3 Assignment -- Mailroom Part 1
'''
print(intro)


'''
The Program
Write a small command-line script called mailroom.py. This script should be executable.

The script should accomplish the following goals:

It should have a data structure that holds a list of your donors and a history of the amounts they have donated.
This structure should be populated at first with at least five donors, with between 1 and 3 donations each.

You can store that data structure in the global namespace.

The script should prompt the user (you) to choose from a menu of 3 actions:
“Send a Thank You”, “Create a Report” or “quit”)

Sending a Thank You
If the user (you) selects ‘Send a Thank You’, prompt for a Full Name.
If the user types ‘list’, show them a list of the donor names and re-prompt
If the user types a name not in the list, add that name to the data structure and use it.
If the user types a name in the list, use it.

Once a name has been selected, prompt for a donation amount.
Turn the amount into a number – it is OK at this point for the program to crash if someone types a bogus amount.

Once an amount has been given, add that amount to the donation history of the selected user.

Finally, use string formatting to compose an email thanking the donor for their generous donation.
Print the email to the terminal and return to the original prompt.
It is fine (for now) to forget new donors once the script quits running.

Creating a Report
If the user (you) selected “Create a Report”, print a list of your donors, sorted by total historical donation amount.
Include Donor Name, total donated, number of donations and average donation amount as values in each row.
You do not need to print out all their donations, just the summary info.
Using string formatting, format the output rows as nicely as possible.
The end result should be tabular (values in each column should align with those above and below)
After printing this report, return to the original prompt.
At any point, the user should be able to quit their current task and return to the original prompt.
From the original prompt, the user should be able to quit the script cleanly.
Your report should look something like this:

Donor Name                | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------
William Gates, III         $  653784.49           2  $   326892.24
Mark Zuckerberg            $   16396.10           3  $     5465.37
Jeff Bezos                 $     877.33           1  $      877.33
Paul Allen                 $     708.42           3  $      236.14
Guidelines
First, factor your script into separate functions.
Each of the above tasks can be accomplished by a series of steps.
Write discreet functions that accomplish individual steps and call them.

Second, use loops to control the logical flow of your program.
Interactive programs are a classic use-case for the while loop.

Of course, input() will be useful here.

Put the functions you write into the script at the top.

Put your main interaction into an if __name__ == '__main__' block.

Finally, use only functions and the basic Python data types you’ve learned about so far.
There is no need to go any farther than that for this assignment.


'''
