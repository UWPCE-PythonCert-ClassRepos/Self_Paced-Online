import unittest
import circle_class as cc
import io
import sys



class TestCircleClass(unittest.TestCase):

    def test_Step1a(self):
        circle = cc.Circle(4)
        self.assertEqual(4, circle.radius)

    def test_Step1b(self):
        circle = cc.Circle()
        with self.assertRaises(ValueError):
            circle.radius = -4

    def test_Step1c(self):
        with self.assertRaises(ValueError):
            circle = cc.Circle(-4)

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

    def test_Step3b(self):
        circle = cc.Circle(4)
        with self.assertRaises(ValueError):
            circle.diameter = -2

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

    def test_Step5b(self):
        with self.assertRaises(ValueError):
            circle = cc.Circle.from_diameter(-8)

    def test_Step6a(self):
        circle = cc.Circle(4)
        self.capturedOutput = io.StringIO()
        sys.stdout = self.capturedOutput
        print(circle)
        sys.stdout = sys.__stdout__
        self.assertEqual(self.capturedOutput.getvalue(), "Circle with radius: 4\n")

    def test_Step6b(self):
        circle = cc.Circle(4)
        d = repr(circle)
        self.assertEqual(d, "Circle(4)")

    def test_Step7a(self):
        circle1 = cc.Circle(4)
        circle2 = cc.Circle(3)
        d = repr(circle1+circle2)
        self.assertEqual(d, "Circle(7)")

    def test_Step7b(self):
        circle = cc.Circle(4)
        d = repr(circle * 3)
        self.assertEqual(d, "Circle(12)")

    def test_Step7c(self):
        circle = cc.Circle(4)
        d = repr(3 * circle)
        self.assertEqual(d, "Circle(12)")

    def test_Step8a(self):
        circle1 = cc.Circle(4)
        circle2 = cc.Circle(3)
        self.assertTrue(circle1 > circle2)

    def test_Step8b(self):
        circle1 = cc.Circle(4)
        circle2 = cc.Circle(4)
        self.assertTrue(circle1 == circle2)

    def test_Step8c(self):
        circle1 = cc.Circle(4)
        circle2 = cc.Circle(3)
        self.assertTrue(circle2 < circle1)

    def test_Step8d(self):
        circle1 = cc.Circle(4)
        circle2 = cc.Circle(4)
        self.assertTrue(circle1 <= circle2)

    def test_Step8e(self):
        circle1 = cc.Circle(4)
        circle2 = cc.Circle(4)
        self.assertTrue(circle1 >= circle2)

    def test_Step8f(self):
        circle1 = cc.Circle(4)
        circle2 = cc.Circle(5)
        self.assertTrue(circle1 != circle2)

    def test_Step8g(self):
        circles = [cc.Circle(6), cc.Circle(7), cc.Circle(8), cc.Circle(4), \
            cc.Circle(0), cc.Circle(2), cc.Circle(3), cc.Circle(5), cc.Circle(9), cc.Circle(1)]
        circles.sort()
        self.assertEqual(circles, [cc.Circle(0), cc.Circle(1), cc.Circle(2), \
            cc.Circle(3), cc.Circle(4), cc.Circle(5), cc.Circle(6), cc.Circle(7), \
            cc.Circle(8), cc.Circle(9)])

    def test_Step8h(self):
        a_circle = cc.Circle(4)
        self.assertTrue(a_circle * 3 == 3 * a_circle)


if __name__ == '__main__':
    unittest.main()
