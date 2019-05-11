#! /usr/bin/env python


def get_donor_db():
    return {
        "william gates, iii": ("William Gates, III", [653772.32, 12.17]),
        "jeff bezos": ("Jeff Bezos", [877.33]),
        "paul allen": ("Paul Allen", [663.23, 43.87, 1.32]),
        "mark zuckerberg": ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0])
    }


def thank_you():
    return None


def create_report():
    return None


def quit():
    return "exit menu"


def sort_key(donor):
    return sum(donor[1])


def menu_selection(prompt, dispatch_dict):
    while True:
        response = input(prompt)
        if dispatch_dict[response]() == "exit menu":
            break


if __name__ == "__main__":
    donor_db = get_donor_db()
    prompt = "\n".join(("Welcome to the mailroom!",
                        "Please choose from below options:",
                        "1 - Send a thank you",
                        "2 - Create a report",
                        "3 - Exit",
                        ">>> "))
    main_dispatch = {
        "1": thank_you,
        "2": create_report,
        "3": quit
    }
    menu_selection(prompt, main_dispatch)
