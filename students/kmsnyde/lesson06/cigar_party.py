# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 17:51:38 2018

@author: Karl M. Snyder
"""

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
    return ((cigars >= 40) & is_weekend) or (((cigars >= 40) &
            (cigars <= 60)) and not is_weekend)