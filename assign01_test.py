import unittest
import random
import math
from assign01 import *


class TestAssign1Functions(unittest.TestCase):
    """ A class derived from unittest.TestCase to test activity01.py functions """

    def setUp(self):
        self.list_testA = [3, 5, 6, 13, 22, 27, 34]
        self.item_testA = 13
        self.list_testB = list(range(1, 1001))
        self.item_testB = 500
        self.list_testC = list(range(1, 100001))
        self.item_testC = 50000
        self.testC_linear_runtime = linearSearch(self.list_testC, self.item_testC)[2]
        self.testC_binary_runtime = binarySearch(self.list_testC, self.item_testC)[2]

    def testLinearSearchA(self):
        """ Confirm that linearSearch can find an item """
        ls_res = linearSearch(self.list_testA, self.item_testA)
        print(f"testLinearSearchA runtime = {ls_res[2]:.6f}")
        self.assertTrue(ls_res[0])
        self.assertEqual(ls_res[1], 4)

    def testBinarySearchA(self):
        """ Confirm that binarySearch can find an item """
        bs_res = binarySearch(self.list_testA, self.item_testA)
        print(f"testBinarySearchA runtime = {bs_res[2]:.6f}")
        self.assertTrue(bs_res[0])
        self.assertEqual(bs_res[1], 1)

    def testLinearSearchB(self):
        """ Confirm that linearSearch can find an item """
        ls_res = linearSearch(self.list_testB, self.item_testB)
        print(f"testLinearSearchB runtime = {ls_res[2]:.6f}")
        self.assertTrue(ls_res[0])
        self.assertEqual(ls_res[1], self.item_testB)

    def testBinarySearchB(self):
        """ Confirm that binarySearch can find an item """
        bs_res = binarySearch(self.list_testB, self.item_testB)
        print(f"testBinarySearchB runtime = {bs_res[2]:.6f}")
        self.assertTrue(bs_res[0])
        self.assertLessEqual(bs_res[1], int(math.log2(len(self.list_testB))) + 1)

    def testLinearSearchC(self):
        """ Confirm that linearSearch can find an item """
        ls_res = linearSearch(self.list_testC, self.item_testC)
        print(f"testLinearSearchC runtime = {ls_res[2]:.6f}")
        self.assertTrue(ls_res[0])
        self.assertEqual(ls_res[1], self.item_testC)

    def testBinarySearchC(self):
        """ Confirm that binarySearch can find an item """
        bs_res = binarySearch(self.list_testC, self.item_testC)
        print(f"testBinarySearchC runtime = {bs_res[2]:.6f}")
        self.assertTrue(bs_res[0])
        self.assertLessEqual(bs_res[1], int(math.log2(len(self.list_testC))) + 1)

    def testCompareRuntimes(self):
        self.assertLess(self.testC_binary_runtime, self.testC_linear_runtime/5.0)
