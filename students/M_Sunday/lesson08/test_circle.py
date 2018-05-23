#!/usr/bin/python
import circle as cir
import unittest


class TestCircle(unittest.TestCase):

    def test_instance(self):
        c = cir.Circle(4)
        self.assertEqual(c.radius, 4)

        c.radius = 6
        self.assertEqual(c.radius, 6)

        c.radius = 13.543534
        self.assertEqual(c.radius, 13.543534)

        with self.assertRaises(ValueError):
            c.radius = -24.67

        with self.assertRaises(TypeError):
            c.radius = "4"

        with self.assertRaises(TypeError):
            c.radius = [6]

        with self.assertRaises(TypeError):
            c.radius = [6, 9]

        with self.assertRaises(TypeError):
            c.radius = (5, 10)

        with self.assertRaises(TypeError):
            c.radius = {'radius': 5}

        with self.assertRaises(TypeError):
            cir.Circle()

        with self.assertRaises(ValueError):
            c = cir.Circle(-24.67)

        with self.assertRaises(TypeError):
            c = cir.Circle("4")

        with self.assertRaises(TypeError):
            c = cir.Circle([6])

        with self.assertRaises(TypeError):
            c = cir.Circle([6, 9])

        with self.assertRaises(TypeError):
            c = cir.Circle((5, 10))

        with self.assertRaises(TypeError):
            c = cir.Circle({'radius': 5})

    

