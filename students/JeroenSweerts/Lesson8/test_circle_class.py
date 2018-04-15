import unittest
import circle_class as cc


class TestCircleClass(unittest.TestCase):

    def test_Step1(self):
        circle = cc.Circle(4)
        self.assertEqual(4, circle.radius)

    def test_Step2a(self):
        circle = cc.Circle(4)
        self.assertEqual(8, circle.diameter)

    def test_Step2b(self):
        circle = cc.Circle(4)
        circle.radius = 8
        self.assertEqual(16, circle.diameter)

    def test_Step3a(self):
        circle = cc.Circle(4)
        circle.diameter = 2
        self.assertEqual(1, circle.radius)

    def test_Step4a(self):
        circle = cc.Circle(2)
        self.assertEqual(12, int(circle.area))

    def test_Step4b(self):
        circle = cc.Circle(2)
        with self.assertRaises(AttributeError):
            circle.area = 42

    def test_Step5a(self):
        circle = cc.Circle.from_diameter(8)
        self.assertEqual(8, circle.diameter)
        self.assertEqual(4, circle.radius)


if __name__ == '__main__':
    unittest.main()
