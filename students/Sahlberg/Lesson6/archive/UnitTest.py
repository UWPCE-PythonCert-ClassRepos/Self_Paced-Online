import unittest as u

import Mailroom3 as m


class tests(u.TestCase):


    def test_amount_append(self):
        dict = {'Roberto' : []}
        name = 'Roberto'
        amount = 23.00
        expected = {name : [amount]}
        m.mail.amount_append(name, dict, amount)
        self.assertDictEqual(expected, dict)



    def test_print_list(self):
        dict = {'Bob': 1, 'Mary': 2}
        expected = ['Bob', 'Mary']
        actual = m.mail.print_list(dict)
        self.assertEqual(expected, actual)

    def test_email(self):
        name = 'Bibs'
        amount = 666.00
        expected = 'Thank you {} for the generous donation of $ {:.2f}. We appreciate your generosity.\n\nSincerely, \n\nThe Helping R Us Team\n\n'.format(name.title(), amount)
        actual = m.mail.email(name, amount)
        self.assertEqual(expected, actual)

    def test_sort_stats(self):

        dict = {'bob johnson': [150.00],
         'susan skoosan': [2000.00, 550.00]}
        expected = [('susan skoosan', [2550.00, 2, 1275.00]), ('bob johnson', [150.00, 1, 150.00])]
        actual = m.mail.sort_and_stats_dict(dict)
        self.assertListEqual(expected, actual)
    """
    def test_print_report(self):

        dict = {'bob': [3], 'Sue': [220]}
        expected = Donor Name       |      Donor Total    |  Count of Donations    |  Average of Donations
----------------------------------------------------------------------------------------
jon jacob           $    5005.00                2                  $        2502
susan skoosan       $    2550.00                2                  $        1275
roxanne raffle      $    211.00                 3                  $          70
bob johnson         $    150.00                 1                  $         150
tim tam             $    10.50                  1                  $          10


        self.assertEqual(expected,m.mail.print_report(dict))
    """

    def test_email_file(self):
        dict = {'Haggus': 4.00}
        expected = ''
        with open('Haggus.txt', 'r') as file:
            expected = file.readline()
        actual = m.mail.email_file(dict)
        self.assertEqual(expected, actual)





if __name__ == '__main__':
    u.main()

""" 

         def email_file(dictionary):
            Generates a thank you letter and writes to disk for all donors.
            try:
                count = 0
                for name, donations in dictionary.items():
                    amount = sum(donations)
                    file_name = '{}_{}.txt'.format(name, dt.date.today())
                    count += 1
                    try:
                        with open(file_name, 'w+') as file:
                            e_text = email(name, amount)
                            file.write(e_text)

                    except IOError as err:
                        print('There was an error:', err)
                return print('Emails written to file.')
            except TypeError:
                print('wrong type of object. Did you use an int instead of a string somewhere?')
            except AttributeError as err:
                print('Wrong object attribute:', err)                     
def print_report(stats_dictionary):
    Print out a report of donors and amounts donated, including stats (total donated, number of times donated, average donation).
    try:
        print('Donor Name       |      Donor Total    |  Count of Donations    |  Average of Donations')
        print('----------------------------------------------------------------------------------------')
        # access indexed results in stats dictionary
        for name, donor in stats_dictionary:
            print(f'{name:<20}$    {donor[0]:<23.2f}{donor[1]:<15}    ${donor[2]:>12.0f}')
    except (IndexError, NameError) as err:
        print('Please try again there was an error - ', err)
"""