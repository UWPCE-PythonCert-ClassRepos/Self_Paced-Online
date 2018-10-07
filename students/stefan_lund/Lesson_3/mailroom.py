# python3

# The Mailroom Automation
# mailroom.py


def user_input(options, data):
    """
    options: type - list, [option0, option1, ..., option'n'] of str type
    options[0] = option1 are "Send Thank You", "Create a Report", "quit" or "amount"
    thank you: options are ["list", "New Name not in the list", "Name in the list"]
        if Name prompt for amount

    """
    # process tells if it's a start, thank you, amount or report
    process = options[0]

    if process == "start":
        # start_options = ["start", "Send a Thank You", "Create a Report", "quit"]
        start_form = "\nYour options are:\na.) {}\nb.) {}\nc.) {}".format(options[1], options[2], options[3])
        print(start_form)
        answer = input("\nEnter letter a, b or c according to your choice.: ")
        return answer

    elif process == "thank_you":
        # thank_you_options = ["thank_you", "list", "Name", "quit"]
        options_choice = options[1], options[2], options[3]
        start_form = "\n  Your options are:\n  {}\n  {}\n  {}".format(*options_choice)
        print(start_form)
        input_prompt = "\nEnter option:   {}, {} of donor or {}: ".format(*options_choice)
        answer = input(input_prompt)
        return answer

    elif process == "amount":
        # amount_options = ["amount", "dollars or dollars.cents"]
        print("\nEnter the amount.")
        donation = input(options[1])
        return donation

    elif process == "report":
        report(data)


def thank_you(data):

    thank_you_options = ["thank_you", "list", "Name", "quit"]

    wrong_answer = True
    question = user_input
    while wrong_answer:
        answer = question(thank_you_options, data)
        accept = ["thank_you", "list", "quit"]
        answer_list_or_quit = accept_user_input(answer, accept)
        if answer_list_or_quit[1]:
            answer = answer_list_or_quit[1]
            if answer == "list":
                report(data)
            elif answer == "quit":
                return False
            else:
                # assuming this must be a name and the program can continue
                answer_list_or_quit = answer, False
                wrong_answer = False

    #  answer is a New Name or a Name already in data
    name = answer
    names = []
    for old_name in data[::3]:
        names.append(old_name)
    if name not in names:
        data.append(name)
        data.append(0.00)
        data.append(0)

    name_ind = data.index(name)
    wrong_answer = True
    amount_options = ["amount", "dollars or dollars.cents: "]
    accept = ["amount"]
    while wrong_answer:
        answer = user_input(amount_options, data)
        if accept_user_input(answer, accept):
            wrong_answer = False
            amount = answer
            if "." not in amount:
                amount += '.00'
            amount = round(float(amount), 2)
            data[name_ind + 1] += amount
            data[name_ind + 2] += 1

    # print thank you note after accounting for the gift
    thank_you_form = "\n\nDear {name},\n\nThank you for the very generous donation of ${amount}\n\nYours Truly,\n"
    print(thank_you_form.format(name = name, amount = amount))


def accept_user_input(answer, accept):
    """
    "start" : "a", "b", "c"
    "thank_you" : "list", "quit", anything else is interpreted to be a Name
    "amount" : string of digits with or without decimals
    """
    if accept[0] == "start":
        if len(answer) == 1 and answer.isalpha():
            answer = answer.lower()
            if answer in accept[1]:
                return True
        return False

    if accept[0] == "thank_you":
        if len(answer) == 4 and answer.isalpha():
            answer = answer.lower()
            if answer == accept[1] or answer == accept[2]:
                return True, answer
        return True, answer

    if accept[0] == "amount":
        if float(answer) <= 0:
            return False
        else:
            if "." not in answer:
                return answer.isdecimal()
            elif "." in answer:
                if answer.count('.') == 1:
                    temp_answer = answer[:answer.index(".")] + answer[answer.index(".") + 1:]
                    return temp_answer.isdecimal()


def report(data):

    name_len = 0
    amount_len = 0
    for i in range(0, len(data), 3):
        name_i = i
        amount_i = name_i + 1
        if len(data[name_i]) > name_len:
            name_len = len(data[name_i]) + 3
        if len(str(data[amount_i])) > amount_len:
            amount_len = len(str(data[amount_i])) + 3

    temp_str = "Donor Name", "Total Given", "Num Gifts", "Average Gift"
    temp_form = "\n{:<{nl}}|{:>{al}}|{:>{al}}|{:>{al}}"
    header = temp_form.format(*temp_str, nl = name_len, al = amount_len)
    print(header)
    print("-" * (name_len + 3 * amount_len + 3))

    for i in range(0, len(data), 3):
        temp_form = "{:<{nl}} ${:>{al}.2f}  {:>{al}} ${:>{al}.2f}"
        d0 = data[i]
        d1 = data[i + 1]
        d2 = data[i + 2]
        if d2 == 0:
            d3 = 0
        else:
            d3 = data[i + 1] / data[i + 2]
        line = temp_form.format(d0, d1, d2, d3, nl = name_len, al = amount_len - 1)
        print(line)


def run_mailroom(data):
    """
    data: list with name, total of donations - dddd.cc, number of gift occations
    """
    # data = []
    start_options = ["start", "Send a Thank You", "Create a Report", "quit"]
    question = user_input
    not_finished = True
    while not_finished:
        wrong_answer = True
        while wrong_answer:
            answer = question(start_options, data)
            accept = ["start", ["a", "b", "c"]]
            if accept_user_input(answer, accept):
                answer = answer.lower()
                wrong_answer = False

        if answer == "a":
            thank_you(data)
        elif answer == "b":
            report(data)
        elif answer == "c":
            not_finished = False
        else:
            print("We have a bug!")
            not_finished = False
    print("Leaving the Mailroom.")


data = ["William Gates, III", 653784.49, 2, "Mark Zuckerberg", 16396.10, 3, "Jeff Bezos", 877.33, 1, "Paul Allen", 708.42, 3]

if __name__ == '__main__':
    run_mailroom(data)
