# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 11:51:56 2018

@author: Laura.Fiorentino
"""

from mailroom_oo import Donor, Donor_List

#donor_list = Donor('Frank Reynolds', [10, 20, 50])
#donor_list.new_donation('Dee Reynolds', [25, 100])
#donor_list.new_donation('Dennis Reynolds', [10, 50])
#donor_list.new_donation('Mac McDonald', [25, 35, 20])
#donor_list.new_donation('Charlie Kelly', 0.25)

#donor = Donor('Frank Reynolds', [10, 20, 50])

donor_list = Donor_List()
donor_list.add_donation('Frank Reynolds', [10, 20, 50])
donor_list.add_donation('Dee Reynolds', [25, 100])
donor_list.add_donation('Dennis Reynolds', [10, 50])
donor_list.add_donation('Mac McDonald', [25, 35, 20])
donor_list.add_donation('Charlie Kelly', 0.25)
