import unittest
from activity01 import *


class TestAssign1Functions(unittest.TestCase):
    """ A class derived from unittest.TestCase to test activity01.py functions """

    def testHelloWorldNormal(self):
        """ Confirm that helloWorldNormal() returns the correct string """
        self.assertEqual('hello world', helloWorldNormal())

    def testHelloWorldInReverse(self):
        """ Confirm that helloWorldInReverse() returns the correct string """
        self.assertEqual('hello world'[::-1], helloWorldInReverse())

    def testHelloWorldTimesX(self):
        """ Confirm helloWorldTimesX() returns correct string for given input """
        self.assertEqual('hello world' * 3, helloWorldTimesX(3))

    def testCircleCircumferenceR1(self):
        """ test that circumference for radius one is correct """
        r = 1.0
        expected_value = 2 * 3.14159 * r
        actual_value = circleCircumference(r)
        self.assertAlmostEqual(actual_value, expected_value, 2, \
                "incorrect circumference for r = 1")

    def testCircleCircumferenceR3(self):
        """ test that circumference for radius three is correct """
        r = 3.0
        expected_value = 2 * 3.14159 * r
        actual_value = circleCircumference(r)
        self.assertAlmostEqual(actual_value, expected_value, 2, \
                "incorrect circumference for r = 3")

    def testCircleAreaR1(self):
        """ test that area for radius one is correct """
        r = 1.0
        expected_value = 3.14159 * r**2
        actual_value = circleArea(r)
        self.assertAlmostEqual(actual_value, expected_value, 2, \
                "incorrect area for r = 1")

    def testCircleAreaR7(self):
        """ test that area for radius seven is correct """
        r = 7.0
        expected_value = 3.14159 * r**2
        actual_value = circleArea(r)
        self.assertAlmostEqual(actual_value, expected_value, 2, \
                "incorrect area for r = 7")

    def testCircleCircumferenceRneg1(self):
        """ check that appropriate exception is raised for r = -1 """
        r = -1.0
        self.assertRaises(ValueError, circleCircumference, r)

    def testCircleAreaRstr(self):
        """ check that appropriate exception is raised when r is a bool """
        r = True
        self.assertRaises(TypeError, circleArea, r)

