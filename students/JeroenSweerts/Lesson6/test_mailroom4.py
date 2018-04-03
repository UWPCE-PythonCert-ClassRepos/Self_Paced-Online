import unittest
import mailroom4
import os.path
import io
import sys



class TestMailroom(unittest.TestCase):
    def setUp(self):
        self.donations = {}
        self.donations['papa'] = [100, 5, 15]
        self.donations['mama'] = [12, 200, 2, 66]
        self.donations['bompa'] = [1000]
        self.donations['bobonne'] = [500, 500]
        self.donations['onbekende'] = [1000000]

    def test_createfile1(self):
        name = 'papa'
        mailroom4.createfile(name)
        assert os.path.isfile(name+'.txt')
        print(os.path)

    def test_thankyoueveryone(self):
        mailroom4.thankyoueveryone()
        for name in self.donations.keys():
            assert os.path.isfile(name+'.txt')

    def test_report(self):
        text = f'{"Donor Name":20s} {"|  Total Given":20s} {"|  Num Gifts  |":20s} {"Average Gift":20s}\n'
        text = text + f'{"-"*76}\n'
        for name in self.donations.keys():
            text = text + f'{name:20s} ${sum(self.donations[name]):20.2f} {len(self.donations[name]):13d}${sum(self.donations[name])/len(self.donations[name]):20.2f}\n'
        print(text)
        self.capturedOutput1 = io.StringIO()
        mailroom4.report()
        self.capturedOutput2 = io.StringIO()
        self.assertEqual(self.capturedOutput1.getvalue(),self.capturedOutput2.getvalue())




if __name__ == '__main__':
    unittest.main()
