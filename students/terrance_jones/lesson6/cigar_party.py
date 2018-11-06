#!/usr/bin/env python

"""
When squirrels get together for a party, they like to have cigars.
A squirrel party is successful when the number of cigars is between
40 and 60, inclusive. Unless it is the weekend, in which case there
is no upper bound on the number of cigars.

Return True if the party with the given values is successful,
or False otherwise.
"""


def cigar_party(cigars, is_weekend):
    cigar_min = 40
    cigar_max =60

    while True:

        if cigars >= cigar_min and is_weekend is True:
            return True

        if cigars >= cigar_min and  cigars<= cigar_max and is_weekend is False:
            return True
        if cigars >= cigar_min and cigars <= cigar_max and is_weekend is True:
            return True
        else:
            return False