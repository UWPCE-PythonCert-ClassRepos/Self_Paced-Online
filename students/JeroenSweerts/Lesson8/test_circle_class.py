import unittest
import circle_class as cc


class TestCircleClass(unittest.TestCase):

    def test_Step1(self):
        circle = cc.Circle(4)
        self.assertEqual(4, circle.radius)
        


if __name__ == '__main__':
    unittest.main()
