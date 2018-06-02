# ------------------------------------------------------------------------
# NAME: MICAH BRAUN
# PROJECT: Lesson 3
# PURPOSE: Format/manipulate sequences of data
# DATE: 05/06/2018
#
# DESCRIPTION:  Program incorporates 5 functions that accept sequences of
# input (string, int, list, etc.) and manipulate them. They are as follows:
#
#   Function I swaps the first and last character/item in a sequence
#   Function II prints every other item in the sequence
#   Function III removes the first and last 4 items from a sequence
#   Function IV displays the sequence in reverse
#   Function V divides the sequence into a beginning/middle/end and swaps
#   the order of the sequence to middle/end/beginning
# ------------------------------------------------------------------------


# Processing --------------------------------------------------------------

#  ---  USER NOTIFICATION: If entry is too low  ---  #
def few_items(i):
    l = len(i)                                                                   # get entry length to display
    print("The sequence you have entered contains {0} element(s).".format(l))    # display message to user
    print("It is too small to be re-formatted.")

#  ---  FUNCTION I: Swap first and last element  ---  #
def exchange_first_last(seq):
    l = len(seq)                        # Obtain length of input
    if l <= 1 or seq == "":             # if input is 1 or nothing, call function few_items, return input
        few_items(seq)                  # function prints message saying nothing has happened because
        print("You entered:", seq)      # input is too small
    #   return seq                      # return commented out, not using for now
    else:
        new_seq = seq[-1:] + seq[1:-1] + seq[:1]    # last index[-1] + indices from [1:-1], then first index [0:1]
        print(new_seq)                              # display new reordered seq
        #  return new_seq


#  ---  FUNCTION II: Remove every other item  ---  #
def every_other(seq):
    print(seq[::2])                # [start: stop: step]


#  ---  FUNCTION III: Remove first four items and last four items ---  #
def first4_last4_removed(seq):
    l = len(seq)                        # Obtain length of input
    if l < 8 or seq == "":              # if input too short, call function
        few_items(seq)                  # function prints message saying nothing has happened because
        print("You entered:", seq)      # input is too small
    #   return seq                      # return commented out, not using for now
    else:
        new_seq = seq[4:-4]             # starting index is after the 4th element which was index 3 [start at 4]
        print(new_seq)                  # and ending element is up to -4
        #  return new_seq               # print results


#  ---  FUNCTION IV: Reverse items  ---  #
def reverse_me(seq):
    print(seq[::-1])                    # [start: stop: step]


#  ---  FUNCTION V: Mix-up by thirds  ---  #
def div_thirds(seq):
    l = len(seq)                        # fetch and set the variable "l" to length of seq
    div = int(len(seq)/3)               # create variable to simplify slicing at next step -
                                        # - div is the quotient of len(seq) / 3

    if l % 3 == 0:                          # if seq length is evenly divided into thirds: do something
        beginning = seq[0:div:]             # beginning = first part of seq, start at 0, stop at div, no step
        middle = seq[div:(div + div):]      # middle, start at div, end at the result of div + div, no step
        ends = seq[(div + div): l:]         # ends, start where middle left off, end at the max value of seq, no step
        final = middle + ends + beginning     # re-arrange variables per instructions
        print(final)
    else:
        print("Not evenly divisible by 3")      # if seq length NOT evenly divided into thirds: do something
        print("-" * (l * 3 + 12))               # formatting
        beginning = seq[0:div:]                 # same as above
        middle = seq[div:(div + div):]
        ends = seq[(div + div): l:]
        final = middle + ends + beginning

        print("    ", final)                    # display

# ---------------------------------------------------------------------------

# Display -------------------------------------------------------------------

# Function I
print("1.  Result: ", end="")
exchange_first_last("Welcome to Westworld")
print()

# Function II
print("2.  Result: ", end="")
every_other([1,2,3,4,5,6,7,8])
print()

# Function III
print("3.  Result: ", end="")
first4_last4_removed("Hello darkness, my old friend.")
print()

# Function IV
print("4.  Result: ", end="")
reverse_me([(1,2,3),(4,5,6),(7,8,9)])
print()

# Function V
print("5.  Result: ", end="")
div_thirds("Just a flesh wound")
print()

