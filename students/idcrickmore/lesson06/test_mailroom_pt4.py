import mailroom_pt4 as m
import unittest


#test mailroom functions

class mailroom_tests(unittest.TestCase):
    donors = {}
    donors[('Bat Man')] = [20,30]
    donors[('Wonder Woman')] = [100, 500]
    
def report():
    print("\n-------------------- REPORT --------------------\n")

    column = ["Donor Name", "| Total Given", "| Num Gifts", "| Average Gift"]
    donors_report = [[name, sum(donors[name]), len(donors[name]),
                     (sum(donors[name])/len(donors[name]))]
                     for name in donors]

    # and reverses the order from largest to smallest
    donors_report = sorted(donors_report, key=itemgetter(1), reverse=True)
    
    report_string = str()
    
    report_string = "{:<15}{:>17}{:>15}{:>10}\n".format(*column)
    report_string += "---------------------------------------------------------------\n"

    # loops through 'donors_report' and
    # dumps all values for 'name' into .format
    for name in donors_report:
        report_string += ('{:<20} ${:>13.2f}{:>12}  ${:>10.2f}\n'.format(*name))

    
        
    

if __name__=='__mainn__':
    unittest.main()