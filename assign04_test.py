import unittest

from assign04 import *

class TestAssign4Functions(unittest.TestCase):
    """ A class derived from unittest.TestCase to test assign04.py functions """

    def setUp(self):
        self.g10 = adjMatFromFile("graph_verts10.txt")
        self.g100A = adjMatFromFile("graph_verts100_A.txt")
        self.g100B = adjMatFromFile("graph_verts100_B.txt")

        self.res_prim10 = prim(self.g10)
        self.res_prim10.sort()
        self.res_krus10 = kruskal(self.g10)
        self.res_krus10.sort()

        start_time = time.time()
        self.res_prim100A = prim(self.g100A)
        self.time_prim100A = time.time() - start_time
        self.res_prim100A.sort()

        start_time = time.time()
        self.res_krus100A = kruskal(self.g100A)
        self.time_krus100A = time.time() - start_time
        self.res_krus100A.sort()

        start_time = time.time()
        self.res_prim100B = prim(self.g100B)
        self.time_prim100B = time.time() - start_time
        self.res_prim100B.sort()

        start_time = time.time()
        self.res_krus100B = kruskal(self.g100B)
        self.time_krus100B = time.time() - start_time
        self.res_krus100B.sort()

    def testPrim(self):
        """ Confirm that Prim's produces correct results """
        #self.assertEqual(self.res_prim10[7], (i, j, c))
        #self.assertEqual(self.res_prim100A[17], (i, j, c))
        #self.assertEqual(self.res_prim100B[71], (i, j, c))
        pass

    def testKruskal(self):
        """ Confirm that Kruskal's produces correct results """
        #self.assertEqual(self.res_krus10[7], (i, j, c))
        #self.assertEqual(self.res_krus100A[17], (i, j, c))
        #self.assertEqual(self.res_krus100B[71], (i, j, c))
        pass

    def testSameResults(self):
        """ Confirm each produces same results """
        #self.assertEqual(self.res_prim10, self.res_krus10)
        #self.assertEqual(self.res_prim100A, self.res_krus100A)
        #self.assertEqual(self.res_prim100B, self.res_krus100B)
        pass

    def testTimings(self):
        """ Confirm each algo runs as quickly as expected (given the input) """
        self.assertGreater(self.time_prim100A, self.time_krus100A)
        self.assertGreater(self.time_krus100B, self.time_prim100B)
