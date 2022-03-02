import unittest
import random
import math
import sys
sys.setrecursionlimit(500000)

from assign02 import *


class TestAssign2Functions(unittest.TestCase):
    """ A class derived from unittest.TestCase to test assign02.py functions """

    def setUp(self):
        self.list_sorted = list(range(1, 5001))
        self.list_reversed = self.list_sorted.copy()
        self.list_reversed.reverse()
        self.list_shuffled = self.list_sorted.copy()
        random.seed(1)
        random.shuffle(self.list_shuffled)
        self.shuf_bubbleRes = bubbleSort(list(self.list_shuffled))
        self.shuf_mergeRes2 = mergeSort(list(self.list_shuffled), split_by_3=False)
        self.shuf_mergeRes3 = mergeSort(list(self.list_shuffled), split_by_3=True)
        self.shuf_quickResA = quickSort(list(self.list_shuffled), pivot_to_use='first')
        self.shuf_quickResB = quickSort(list(self.list_shuffled), pivot_to_use='middle')
        self.shuf_radixRes = radixSort(list(self.list_shuffled), math.ceil(math.log10(max(self.list_sorted))))
        self.rev_bubbleRes = bubbleSort(list(self.list_reversed))
        self.rev_mergeRes2 = mergeSort(list(self.list_reversed), split_by_3=False)
        self.rev_mergeRes3 = mergeSort(list(self.list_reversed), split_by_3=True)
        self.rev_quickResA = quickSort(list(self.list_reversed), pivot_to_use='first')
        self.rev_quickResB = quickSort(list(self.list_reversed), pivot_to_use='middle')
        self.rev_radixRes = radixSort(list(self.list_reversed), math.ceil(math.log10(max(self.list_sorted))))
        self.m2 = 0
        self.m3 = 0
        for i in range(10):
            tmp = self.list_sorted.copy()
            random.shuffle(tmp)
            self.m2 += mergeSort(tmp, split_by_3=False)[1]
            self.m3 += mergeSort(tmp, split_by_3=True)[1]
        self.m2 /= 10
        self.m3 /= 10

    def testSorting(self):
        """ Confirm that functions sort as expected """
        self.assertEqual(self.list_sorted, self.shuf_bubbleRes[0])
        self.assertEqual(self.list_sorted, self.shuf_mergeRes2[0])
        self.assertEqual(self.list_sorted, self.shuf_mergeRes3[0])
        self.assertEqual(self.list_sorted, self.shuf_quickResA[0])
        self.assertEqual(self.list_sorted, self.shuf_quickResB[0])
        self.assertEqual(self.list_sorted, self.shuf_radixRes[0])
        self.assertEqual(self.list_sorted, self.rev_bubbleRes[0])
        self.assertEqual(self.list_sorted, self.rev_mergeRes2[0])
        self.assertEqual(self.list_sorted, self.rev_mergeRes3[0])
        self.assertEqual(self.list_sorted, self.rev_quickResA[0])
        self.assertEqual(self.list_sorted, self.rev_quickResB[0])
        self.assertEqual(self.list_sorted, self.rev_radixRes[0])

    def testTimings(self):
        """ Confirm that sorting functions run in expected times """
        self.assertGreater(self.shuf_bubbleRes[1]/2, self.shuf_mergeRes2[1])
        self.assertGreater(self.shuf_bubbleRes[1]/2, self.shuf_mergeRes3[1])
        self.assertGreater(self.shuf_bubbleRes[1]/10, self.shuf_quickResA[1])
        self.assertGreater(self.shuf_bubbleRes[1]/10, self.shuf_quickResB[1])
        self.assertGreater(self.shuf_bubbleRes[1]/10, self.shuf_radixRes[1])
        self.assertGreater(self.shuf_mergeRes3[1]*1.5, self.shuf_mergeRes2[1])
        self.assertGreater(self.rev_quickResA[1]/10, self.rev_quickResB[1])
        self.assertGreater(self.m3 * 2, self.m2)
        self.assertGreater(self.m2 * 2, self.m3)

