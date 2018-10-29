# python3

# Lesson 4
#
# run_mailroom_part2(file)
# script needs the abspath where the information:
#
# William Gates, III/653784.49/2\n
# Mark Zuckerberg/16396.10/3\n
# Jeff Bezos/877.33/1\n
# Paul Allen/708.42/3\n
# ""
#
# is stored


import os, sys, datetime

def run_mailroom_part2(file):

    """
        d_actions: dictionary form, key - action, value - functions to perform
        d_lables: lables for info stored or that will be stored in info_file
        info_file: path and filename to text file where info is or will be stored.
            info is '/' separated
    """

    finished = False
    while not finished:
        mrl = MailroomPart2(file)
        select = mrl.act
        if select == "Quit":
            finished = True



class ValidDigit:
    # is a number, int or float, with or without $ sign
    def __init__(self, answer, valid):
        self.answer = answer
        self.valid = valid

    def validate_digit(self):
        # menu choice 1, 2, 3, etc
        # amount, always includes $ and maybe decimals

        temp_answer = str(self.answer)
        temp_dec = temp_answer.replace("$", "")
        temp = temp_dec.replace(".", "")
        temp_count_dot = temp_answer.count('.')
        temp_count_currency = temp_answer.count('$')

        if temp.isdigit() and temp_count_dot < 2 and temp_count_currency < 2:
            if float(temp_dec) <= 0:
                return False
            else:
                if temp_count_currency == 1:
                    # amount
                    return True
                else:
                    # menu choice, 1, 2, 3, etc
                    valid_answer = int(self.answer) in self.valid
                    if valid_answer:
                        return True
                    else:
                        return False
        else:
            return False


class ValidAlpha:

    def __init__(self, answer, valid):
        self.answer = answer
        self.valid = valid

    def validate_alpha(self):
    # valid: list of accepted  strings, "list", "quit" or a name,
    # name is also checked to be of alpha numeric and white space
    # any name will return True as will "list" or "quit"
    # return value(s) in list form so check for name in list can be identified

        # consecutive digits discualifies the entry as a valid name
        for i in range(len(self.answer)):
            if self.answer[i].isdigit():
                if self.answer[i + 1].isdigit():
                    return False

        if all(x.isalpha() or x.isspace() or x.isdigit() or x  == "." for x in self.answer):
            temp = self.answer.lower()
            # see if answer is in the valid list
            for string in self.valid:
                if temp == string.lower():
                    return True
            # otherwise assume it's a new name
                else:
                    return True
        # answer does not make sense
        else:
            return False


class MailroomPart2:


    def __init__(self, tryfile):
        self.file = tryfile
        self.act = self.action()

    def action(self):

        act_menu1 = {"Send a Thank You": self.send_a_thank_you,
                    "Create a Report": self.create_a_report,
                    "Send Letter to Everyone": self.send_letters_to_everyone,
                    "Quit": self.__quit_}

        selection = self.__choice(act_menu1)
        select = act_menu1[selection]
        v = select()

        if v == "Quit":
            return v



    def __choice(self, menu_dict):
        """
        returns the 'Send a Thank You' etc from menu,
        """
        local_menu = self.__menu(menu_dict)
        max_opt = str(len(local_menu))
        choice_str = "\nEnter the number of your choice, 1 - " + max_opt + ": "
        selection = input(choice_str)

        answer = selection
        valid = local_menu.keys()
        choice = ValidDigit(answer, valid)
        valid_choice = choice.validate_digit()
        if valid_choice:
            return local_menu[int(selection)]
        else:
            print("Choice not valid.")
            self.action()

    def __menudict(self, menu_dict):
        m_dict = {}
        for n, choice in enumerate(menu_dict.keys()):
            m_dict[n + 1] = choice
        return m_dict

    def __menu(self, menu_dict):
        print("\nMain Menu\n")
        menu = self.__menudict(menu_dict)
        for choice in sorted(menu):
            print("{} - {}".format(str(choice), menu[choice]))
        return menu


    def create_a_list(self):
        # expects an existing path
        # file name may exist or not but has to be a txt file
        info = ReadWriteFile(self.file)
        report_dict = info.read_line()

        name_len = 0
        for key in report_dict.keys():
            if len(key) > name_len:
                name_len = len(key) + 3

        temp_str = "Name"
        temp_form = "\n{:<{nl}}|"
        header = temp_form.format(temp_str, nl = name_len)
        print(header)
        print("-" * (name_len + 3 ))

        for key in report_dict.keys():
            temp_form = "{:<{nl}}"
            d0 = key
            line = temp_form.format(d0, nl = name_len)
            print(line)

    def create_a_report(self):
        # expects an existing path
        # file name may exist or not but has to be a txt file
        info = ReadWriteFile(self.file)
        report_dict = info.read_line()

        name_len = 0
        amount_len = 0
        for key in report_dict.keys():
            if len(key) > name_len:
                name_len = len(key) + 3
            if len(str(report_dict[key][0])) > amount_len:
                amount_len = len(str(report_dict[key][0])) + 3

        temp_str = "Name", "Total Given", "Num Gifts", "Average Gift"
        temp_form = "\n{:<{nl}}|{:>{al}}|{:>{al}}|{:>{al}}"
        header = temp_form.format(*temp_str, nl = name_len, al = amount_len)
        print(header)
        print("-" * (name_len + 3 * amount_len + 3))

        for key in report_dict.keys():
            temp_form = "{:<{nl}} ${:>{al}.2f}  {:>{al}} ${:>{al}.2f}"
            d0 = key
            d1 = float(report_dict[key][0])
            d2 = int(report_dict[key][1])
            if d2 == 0:
                d3 = 0
            else:
                d3 = d1 / d2
            line = temp_form.format(d0, d1, d2, d3, nl = name_len, al = amount_len - 1)
            print(line)


    def send_a_thank_you(self):

        act_menu2 = ["Options are to enter a \nName or \nCreate List of Names or \nMain Menu",
                    {"Name": "",
                     "List": self.create_a_list,
                     "Main": self.action}]

        print("\n" * 2 + act_menu2[0])
        choice_str = "\nEnter a Name, List or Main: "
        selection = input(choice_str)

        answer = selection
        valid = ["list", "main"]
        choice = ValidAlpha(answer, valid)
        valid_choice = choice.validate_alpha()
        if valid_choice:
            if selection.lower() == valid[0]:
                act_menu2[1][selection]()
                self.send_a_thank_you()
            elif selection.lower() == valid[1]:
                act_menu2[1][selection]
            else:
                # update will have the name, total amount, number of times

                name = selection
                amount = input("\nEnter amount donated: ")
                update = ReadWriteFile(self.file, name, amount)
                existing_name = update.writefile()
                self.__send_thank_you(existing_name, amount)

        else:
            print("Choice not valid.")
            self.__choice()


    def send_letters_to_everyone(self):
        """
        report_dict: {'name': ['total amount donated', 'number of times donating']}
        """

        info = ReadWriteFile(self.file)
        report_dict = info.read_line()
        today = self.__date()
        letter_template = self.__letter("2")

        for key in report_dict.keys():
            letter = letter_template.format(name=key,
                                            amount=report_dict[key][0],
                                            date = today[1] + "/" + today[2] + "/" + today[0])
            print("\n", letter)

            donor = "_".join(key.split())
            letter_file = donor + "__" + today[0] + "_" + today[1] + "_" + today[2]

            fp = ReadWriteFile(self.file)
            fpath = fp.create_path(letter_file, False)
            fp.writenewfile(letter, fpath)


    def __send_thank_you(self, name, amount):

        letter1 = self.__letter("1")
        letter11 = letter1.format(name=name, amount=amount)
        print("\n", letter11)

        today = self.__date()
        donor = "_".join(name.split())
        letter_file = donor + "__" + today[0] + "_" + today[1] + "_" + today[2]

        fp = ReadWriteFile(self.file)
        fpath = fp.create_path(letter_file, False)
        fp.writenewfile(letter11, fpath)

    def __date(self):
        today = datetime.date.today()
        year, month, day = str(today.year), str(today.month), str(today.day)
        return [year, month, day]

    def __letter(self, ltr):

        n = "\n"
        t = "\t"
        s = " "

        # letter 1
        l1 = "Dear {name}," + n * 2
        l2 = (t + s) * 1 + "Thank you for your very kind donation of ${amount}." + n * 2
        l3 = (t + s) * 1 + "It will be put to very good use." + n * 2
        l4 = (t + s) * 5 + "Sincerely," + n * 2
        l5 = (t + s) * 6 + "-The Team"
        letter1 = l1 + l2 +l3 +l4 + l5

        # letter 2
        day = (t + s) * 8 + "{date}" + n * 6
        l1 = "Dear {name}," + n * 2
        l2 = (t + s) * 1 + "Your very generous donation of ${amount} this year is very much appreciated." + n * 2
        l3 = (t + s) * 1 + "It will be put to very good use." + n * 2
        l4 = (t + s) * 5 + "Sincerely," + n * 2
        l5 = (t + s) * 6 + "-The Team"
        letter2 = day + l1 + l2 +l3 +l4 + l5

        if ltr == "1":
            return letter1
        elif ltr == "2":
            return letter2


    def __quit_(self):
            return "Quit"



class ReadWriteFile:
    """
    file_path: raw string of full file path including file name
        expects lines
    file line is '/' delimited, lines are '\n' delimited
    """

    def __init__(self, file_path, name=None, amount=None):
        self.file = file_path
        self.name = name
        self.amount = amount

    def create_path(self, f_name, add=True):
        source = self.file
        folder, file = os.path.split(self.file)
        filename, ext = file.split(".")
        if add:
            new_destination = folder + "\\" + filename + f_name + "." + ext
        else:
            new_destination = folder + "\\" + f_name + "." + ext
        return new_destination

    def writenewfile(self, letter, new_file_path):
        try:
            # copy entire file to a temp file
            with open(new_file_path, 'w') as outfile:
                outfile.write(letter)
        except: # catch all - not good but the best I can come up with for the moment.
            e = sys.exc_info()
            print("<p>Error: {}</p>".format(e)[0])


    def writefile(self):
        """
        windows ==> path entered with prefix r, raw string, alt. duplicate all \
                    works as long as the path doesn't end with \.
        source: abspath
        to_destination: abspath
        # file: name of file to be copied
        """
        source = self.file
        folder, file = os.path.split(self.file)
        filename, ext = file.split(".")
        temp_destination = self.create_path("_temp")

        line_form = "{name}/{amount}/{times}\n"#{}.format(name = self.name, amount = updated_amount, times = updated_times)

        try:
            # copy entire file to a temp file
            with open(source, 'r') as infile, open(temp_destination, 'w') as outfile:
                for line in infile:
                    outfile.write(line)
        except: # catch all - not good but the best I can come up with for the moment.
            e = sys.exc_info()[0]
            print("<p>Error: {}</p>".format(e))

        source = temp_destination
        destination = self.file
        found_name = False
        end_of_file = False

        try:
            with open(source, 'r') as infile, open(destination, 'w') as outfile:
                while not end_of_file:
                    line = infile.readline()
                    end_of_file = True == line.count("")
                    if not found_name:

                        if not end_of_file:
                            if self.name in line:
                                line = line.replace("\n", "")
                                line  = line.split('/')

                                existing_name, current_amount, times = line[0], line[1], line[2]
                                updated_amount = str(float(current_amount) + float(self.amount))
                                updated_times = str(int(times) + 1)
                                new_line = line_form.format(name = existing_name,
                                                            amount = updated_amount,
                                                            times = updated_times)
                                outfile.write(new_line)
                                found_name = True
                            else:
                                outfile.write(line)

                    else:
                        outfile.write(line)

        except: # catch all - not good but the best I can come up with for the moment.
            e = sys.exc_info()
            print("<p>Error: {}</p>".format(e[0]))
            print(e[1], "\n", e[2])

        try:
            os.remove(temp_destination)
        except OSError as e: # this would be "except OSError, e:" before Python 2.6
            if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
                raise # re-raise exception if a different error occurred

        return existing_name


    def read_line(self):  #(fle, nme=None):
        """
        if name is None, a report is being produced
        if name is a name, check if name is in the file or not
        line is a list, ['name', 'total amount donated', 'number of times donating']
        """

        file_dict = {}
        with open(self.file, "r") as f:
            repeat = True
            while repeat:
                line  = f.readline()
                end_of_file = True == line.count("")

                if not end_of_file:
                    line = line.replace("\n", "")
                    line  = line.split('/')
                    # print("1.  line: {}".format(line))
                    # print("line: {}, position: {}, temp: {}, nme in line[0]: {}".format(line, position, temp, nme in line[0]))
                    # print(nme is not None, nme in line[0], repeat)
                    # if nme is not None, checking to see if the name is in the file or not
                if self.name is not None:
                    if nme in line[0]:
                        # position = temp
                        file_dict[line[0]] = [line[1], line[2]]
                        # print("{} is in the file, {}".format(self.name, line[0]))
                        # print("2.  line: {}".format(line))
                        repeat = False
                    else:
                        # print("3.  line: {}".format(line))
                        if end_of_file:
                            file_dict[self.name] = [0, 0]
                            # print("{} is not in the file".format(self.name))
                            repeat = False

                # nme is None and all info from the file is returned
                else:
                    if end_of_file:
                        repeat = False
                    else:
                        file_dict[line[0]] = [line[1], line[2]]
                        # print("4.  line: {}".format(line))
        return file_dict
