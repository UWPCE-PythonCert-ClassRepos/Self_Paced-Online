import unittest
import mailroom4

class TestMailbox(unittest.TestCase):
    def test_thankyou(self):
        self.assertEqual(mailroom4.thank_you(), None)


if __name__ == '__main__':
    unittest.main()