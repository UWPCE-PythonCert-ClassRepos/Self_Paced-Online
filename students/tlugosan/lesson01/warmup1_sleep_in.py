# weekday is true if it is a weekday
# vacation is true if we are on vacation
# we sleep in if not a weekday or on vacation
# return true if we sleep in

import pdb

def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False