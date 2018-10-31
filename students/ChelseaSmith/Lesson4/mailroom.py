# define variables
record = {"James Smith": [85, 100, 75],  # dictionary with key as donor name and value as list of previous donations
          "Alex Jones": [25, 25, 25],
          "Kate Smith": [100],
          "Kate Jones": [175, 50],
          "Alex Smith": [200, 200, 200]}

choice = 1  # variable used to choose main menu options

# functions


def report(dictin):  # this prints a report given database dictin
    print(f"Donor name" + " " * 17 + " | Total Given | Num Gifts | Average Gift\n")
    for k in dictin:
        sum = 0
        num = 0
        for item in dictin[k]:
            sum = sum + int(item)
            num = num + 1
        print(f"{k:<28}${sum:12.2f}{num:10}   ${(sum / num):13.2f}")


def getname(dictin):  # ask for name or to list names if user asks to write letter
    name = input("Please enter the donor's full name or list for a list of donors.")
    if name == "list":
        for x in dictin:
            print(x)
        name = input("Please enter the donor's full name")
    return name


def checknew(dictin, name):  # returns true if name is not already in list input
    new = True
    for x in dictin:
        if name == x:
            new = False
    return new


# get donation amount and save in records, uses new name check.
def getdonation(dictin, name):
    donation = float(input("Please enter the donation amount:"))
    if checknew(dictin, name) == True:
        dictin[name] = [donation]
    else:
        dictin[name].append(donation)
    return dictin


# write letter function. I don't think I structured my dictionary right to use .format(**dict)
def writenote(name, donation):
    letter = "Dear {},\nThank you for your generous donation of ${}.\nSincerely,\n Generic Charities".format(name, donation)
    return letter


def thankyou(dictin):  # collects all actions for sending a thank you
    name = getname(dictin)
    dictin = getdonation(dictin, name)
    print(writenote(name, dictin[name][-1]))


def saveletter(filename, message):  # saves message to file named filename
    f = open(filename, 'w')
    f.write(message)


def letters(dictin):
    for k in dictin:
        letter = writenote(k, dictin[k][-1])  # name is keyword, donation value is last entry in list that is value tied to keyword
        filename = k + ".txt"
        saveletter(filename, letter)


choose = {1: thankyou,
          2: report,
          3: letters}  # dictionary used as switch

# main function
if __name__ == "__main__":
    while choice != 0:
        choice = int(input("Please enter 1 to send a thank you, 2 to generate a report, 3 to generate letters for all donors, or 0 to quit"))
        if choice != 0:
            choose.get(choice)(record)
