import unittest
from MailRoomPt4 import PrintEMail
from MailRoomPt4 import Generate_Letters

class MyTestCases(unittest.TestCase):

    def test_PrintEmail(self):
        #Expected
        expected='\nDear Jeff Bezos \nWe would like to thank you for continuing support for our organization!\nYour contribution of $1234 is received and very much appreciated!\nThank you\nKennan Yilmaz'

        #Actual output
        actual=PrintEMail('Jeff Bezos', 1234)
        #print (actual)
        #print(expected)

        #Compare
        self.assertEqual(expected, actual)

    def test_Generate_Letters(self):
        donationdata = {'Kelly Hirsch': [800]}
        expected=0
        actual=Generate_Letters(donationdata)
        self.assertEqual(expected,actual)

if __name__=='__main__':
    #Run the tests
    unittest.main()
