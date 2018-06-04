#!/usr/bin/env python3
import os
import datetime
import collections
import threading
import time
import random
import queue

"""
Lesson10 - Functional Mailroom
"""

cwd = os.getcwd()
date = datetime.datetime.now().strftime('%Y-%m-%d')
Patron = collections.namedtuple('Patrons', ['name', 'donations'])

_donors = (
    Patron(name='Jim Halpert', donations=[1.00]),
    Patron(name='Pam Beesley', donations=[1000.00, 2000.00, 3000.00, 5.00]),
    Patron(name='Dwight Shrute', donations=[2.00, 3.00]),
    Patron(name='Michael Scott', donations=[10.00, 20.00, 30.00]),
    Patron(name='Andy Bernard', donations=[500.00])
)


###############################################################################

_factor = None
_db = None
_min = None
_max = None


DELAY = True  # flip to run without delays  :)


def delay():
    if DELAY:
        time.sleep(random.random())


###############################################################################

filtered_db_queue = queue.Queue()


def filter_range(x):
    return x if _min <= x <= _max else 0


def filtered_db():
    f_db = []
    db = filtered_db_queue.get()
    print_queue.put([f'Collecting filtered rows...'])
    for d in db:
        delay()
        delay()
        fd = list(filter(lambda x: filter_range(x), d.donations))
        if len(fd) > 0:
            print_queue.put([f'    {d.name}: {fd}'])
            f_db.append({'name': d.name, 'donations': fd})
    print_queue.put(['Temp filtered DB created.'])
    filtered_db_queue.task_done()
    factors_queue.put(f_db)


###############################################################################

factors_queue = queue.Queue()


def factor_donations(donations):
    return list(map(lambda x: x * _factor, donations))


def factors_update_db():
    db = factors_queue.get()
    print_queue.put([f'Calculating factors...'])
    for d in db:
        f = factor_donations(d['donations'])
        d['donations'] = f
        print_queue.put([f"    {d['name']}: {f}"])
    print_queue.put(['Temp DB updated with factored donations.'])
    delay()
    factors_queue.task_done()
    totals_queue.put(db)


###############################################################################

totals_queue = queue.Queue()


def calc_totals():
    db = totals_queue.get()
    delay()
    total = sum([sum(x['donations']) for x in db])
    print_queue.put([f'\n\nNew grand total ({_factor}x factor): {total}'])
    totals_queue.task_done()


###############################################################################

print_queue = queue.Queue()


def print_manager():
    while True:
        delay()
        job = print_queue.get()
        for line in job:
            print(line, end='\n')
            delay()
            delay()
        print_queue.task_done()
        delay()


###############################################################################

def worker():
    filtered_db_queue.put(_db)
    delay()


def challenge(factor, donors, min_donation, max_donation):

    global _factor
    global _db
    global _min
    global _max
    global t1
    global t2
    global t3
    global t4

    _factor = factor
    _db = donors
    _min = min_donation
    _max = max_donation

    t1 = threading.Thread(target=filtered_db)
    t1.daemon = False
    t1.start()
    del t1

    t2 = threading.Thread(target=factors_update_db)
    t2.daemon = False
    t2.start()
    del t2

    t3 = threading.Thread(target=calc_totals)
    t3.daemon = False
    t3.start()
    del t3

    t4 = threading.Thread(target=print_manager)
    t4.daemon = True
    t4.start()
    del t4

    print_queue.put(['\n\nGenerating projections...'])
    delay()

    t = threading.Thread(target=worker)
    t.start()
    delay()
    delay()
    t.join()
    del t

    filtered_db_queue.join()
    delay()
    factors_queue.join()
    totals_queue.join()
    delay()
    print_queue.put(['All Done!\n\n'])
    print_queue.join()


###############################################################################


def format_currency_str(amount=None):
    return "${0:.2f}".format(float(amount))


def list_donors():
    print('\n'.join(sorted(d.name for d in _donors)))


def sort_donors():
    return sorted(_donors, key=lambda x: sum(x.donations), reverse=True)


def find_name_bool(name=None):
    return bool([d for d in _donors if d.name == name])


def print_pre_process(donors):
    """pre-process donors to simplify printing"""
    print_list = []
    for d in donors:
        name = d.name
        donations = d.donations
        total = float(sum(donations))
        number = len(donations)
        str_total = format_currency_str(total)
        str_number = str(len(donations))
        str_average = format_currency_str(total / max(number, 1))
        print_list.append([name, str_total, str_number, str_average])
    return print_list


def print_report(rows):
    # table heading
    h = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    hs = ' | '
    hf = '{0:<25}{1}{2}{3}{4}{5}{6}'
    print(hf.format(h[0], hs, h[1], hs, h[2], hs, h[3]))
    # table rows
    for r in rows:
        name = "{}".format(r[0])
        f0 = '{0:<' + str(max(len(name), 25)) + '}'
        f2 = '{2:>' + str(max(len(r[1]), len(h[1]))) + '}'
        f4 = '{4:>' + str(max(len(r[2]), len(h[2]))) + '}'
        f6 = '{6:>' + str(max(len(r[3]), len(h[3]))) + '}'
        rf = f0 + '{1}' + f2 + '{3}' + f4 + '{5}' + f6
        args = [name, '  $', r[1], ' | ', r[2], '  $', r[3]]
        print(rf.format(*args))


def create_report():
    sorted_donors = sort_donors()
    rows = print_pre_process(sorted_donors)
    print_report(rows)


def email_all_donations(name, donations):
    donations = format_currency_str(donations)
    m = ('\n\nDear {},\n\n'
         '        Thank you for your very kind donations totalling {}.\n\n'
         '        It will be put to very good use.\n\n'
         '               Sincerely,\n'
         '                  -The Team\n\n')
    print(m.format(name, donations))


def print_donor_summary(name):
    summary = ('\n\n===========================\n'
               'Donor: {}\n'
               'Total Donations: {}.\n'
               'Donation Count: {}\n'
               'Donation Average: {}\n'
               '===========================\n\n')
    total = donations_total(name)
    count = donations_count(name)
    average = donations_average(name)
    print(summary.format(name, total, count, "{0:.2f}".format(average)))


def generate_letters():
    path = cwd + '/letters/'
    ext = '.txt'
    for d in _donors:
        total_donations = sum(d.donations)
        n = d.name.split(' ')
        file_path = "{}{}_{}_{}{}".format(path, date, n[0], n[1], ext)
        donations = format_currency_str(total_donations)
        with open(file_path, 'w') as letter:
            text = ('\n\nDear {} {},\n\n'
                    '        Thank you for your very kind '
                    'donation of {}.\n\n'
                    '        It will be put to very good use.\n\n'
                    '               Sincerely,\n'
                    '                  -The Team\n\n')
            body = text.format(n[0], n[1], donations)
            letter.write(body)
    print('\n\n========== Letters Created ==========\n\n')


def get_donations(name=None):
    found = find_name_bool(name)
    if found:
        return [d.donations for d in _donors if d.name == name][0]
    else:
        return []


def donations_total(name=None):
    return sum(get_donations(name))


def donations_count(name=None):
    return len(get_donations(name))


def donations_average(name=None):
    found = find_name_bool(name)
    if found:
        total = donations_total(name)
        count = donations_count(name)
        return total / count
    else:
        return 0


def find_name_index(db_copy, name):
    for index, d in enumerate(db_copy):
        if d.name == name:
            return index


def donors_save(name, amount):
    global _donors
    db_copy = list(d for d in _donors)

    if find_name_bool(name) is False:
        # new donor
        db_copy.append(Patron(name=name, donations=[amount]))
    else:
        # existing donor
        donations = get_donations(name)
        donations.append(amount)
        del db_copy[find_name_index(db_copy, name)]
        db_copy.append(Patron(name=name, donations=donations))

    # overwrite main data set
    _donors = tuple(db_copy)


def email_single_donation(name, donation):
    donation = format_currency_str(donation)
    m = ('\n\nDear {},\n\n'
         '        Thank you for your very kind donation of {}.\n\n'
         '        It will be put to very good use.\n\n'
         '               Sincerely,\n'
         '                  -The Team\n\n')
    print(m.format(name, donation))


###############################################################################

def prompt_name():
    while True:
        name = input('Type donor name: ')
        try:
            if name is None:
                raise ValueError()
        except ValueError:
            print('Name string required.')
            continue
        return name


def prompt_donation():
    while True:
        amount = input('Enter donation amount: ')
        try:
            amount = float(amount)
        except ValueError:
            print('Input must be an int/float, try again.')
            continue
        return amount


def prompt_min():
    while True:
        amount = input('Minimum donation (leave empty to ignore): ')
        if not amount:
            return 0
        else:
            try:
                amount = float(amount)
            except ValueError:
                print('Input must be an int/float, try again.')
                continue
            return amount


def prompt_max():
    while True:
        amount = input('Maximum donation (leave empty to ignore): ')
        if not amount:
            return float("inf")
        else:
            try:
                amount = float(amount)
            except ValueError:
                print('Input must be an int/float, try again.')
                continue
            return amount


def prompt_factor():
    while True:
        factor = input('Enter factor: ')
        if factor == '1':
            print('Input must be an int greater than 1, try again.')
            continue
        try:
            factor = int(factor)
        except ValueError:
            print('Input must be an int greater than 1, try again.')
            continue
        return factor


def process_new_donor():
    while True:
        name = prompt_name()
        if find_name_bool(name) is False:
            break
        else:
            print('Donor already exists, use append.')

    donation = prompt_donation()
    email_single_donation(name, donation)
    donors_save(name, donation)


def process_donation():
    while True:
        name = prompt_name()
        if find_name_bool(name) is False:
            print('Type the exact donor name (see list): ', end='\n\n')
            list_donors()
            continue
        else:
            break

    donation = prompt_donation()
    email_single_donation(name, donation)
    donors_save(name, donation)


def prompt_summary():
    while True:
        name = prompt_name()
        if find_name_bool(name) is False:
            print('Type the exact donor name (see list): ', end='\n\n')
            list_donors()
            continue
        else:
            break
    print_donor_summary(name)


def prompt_thanks(name=None, amount=None):
    if name is not None:
        # called by method
        email_single_donation(name, amount)  # single donation
    else:
        # called by menu
        while True:
            name = prompt_name()
            if find_name_bool(name) is True:
                amount = [d.donations for d in _donors if d.name == name][0]
                print(amount)
                break
            else:
                print('Type the exact donor name (see list): ', end='\n\n')
                list_donors()
        email_all_donations(name, sum(amount))  # total donations


def prompt_projection():
    factor = prompt_factor()
    min_donation = prompt_min()
    max_donation = prompt_max()
    challenge(factor, _donors, min_donation, max_donation)


def menu_selection(prompt, dispatch):
    while True:
        r = input(prompt)
        if r not in dispatch:
            print('Please choose a valid menu option.')
            continue
        if dispatch[r]() == "break":
            break


def quit_menu():
    return 'break'


def main_menu():
    main_prompt = ("\n--- MAIN MENU ---\n"
                   "What do you want to do?\n"
                   "Type '1' - Donors Menu\n"
                   "Type '2' - Reports Menu\n"
                   "Type '3' - Gratitude Menu\n"
                   "Type 'q' - Quit >> "
                   )
    main_dispatch = {'1': donors_sub_menu,
                     '2': reports_sub_menu,
                     '3': gratitude_sub_menu,
                     'q': quit_menu,
                     }
    menu_selection(main_prompt, main_dispatch)


def donors_sub_menu():
    donors_prompt = ("\n--- DONOR SUB MENU ---\n"
                     "Type '1' - Add Donor\n"
                     "Type '2' - Append Donation\n"
                     "Type '3' - List Donors\n"
                     "Type 'q' - Quit >> "
                     )
    donors_dispatch = {'1': process_new_donor,
                       '2': process_donation,
                       '3': list_donors,
                       'q': quit_menu,
                       }
    menu_selection(donors_prompt, donors_dispatch)


def reports_sub_menu():
    reports_prompt = ("\n--- REPORTS SUB MENU ---\n"
                      "Type '1' - Donors Report\n"
                      "Type '2' - Donor Summary\n"
                      "Type '3' - Donations Projection\n"
                      "Type 'q' - Quit >> "
                      )
    reports_dispatch = {'1': create_report,
                        '2': prompt_summary,
                        '3': prompt_projection,
                        'q': quit_menu,
                        }
    menu_selection(reports_prompt, reports_dispatch)


def gratitude_sub_menu():
    gratitude_prompt = ("\n--- GRATITUDE SUB MENU ---\n"
                        "Type '1' - Print Individual Letter\n"
                        "Type '2' - Generate Letters for All Donors\n"
                        "Type 'q' - Quit >> "
                        )
    gratitude_dispatch = {'1': prompt_thanks,
                          '2': generate_letters,
                          'q': quit_menu,
                          }
    menu_selection(gratitude_prompt, gratitude_dispatch)


if __name__ == "__main__":
    main_menu()
