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

    def stCost(self, spantree):
        edge_weights = [e[2] for e in spantree]
        return sum(edge_weights)

    def testPrim(self):
        """ Confirm that Prim's produces correct results """
        self.assertEqual(self.stCost(self.res_prim10), 94)
        self.assertEqual(self.stCost(self.res_prim100A), 418)
        self.assertEqual(self.stCost(self.res_prim100B), 99)

    def testKruskal(self):
        """ Confirm that Kruskal's produces correct results """
        self.assertEqual(self.stCost(self.res_krus10), 94)
        self.assertEqual(self.stCost(self.res_krus100A), 418)
        self.assertEqual(self.stCost(self.res_krus100B), 99)
        #self.assertEqual(self.res_krus100A[17], (i, j, c))

    def testSameResults(self):
        """ Confirm each produces same results """
        self.assertEqual(self.stCost(self.res_prim10), self.stCost(self.res_krus10))
        self.assertEqual(self.stCost(self.res_prim100A), self.stCost(self.res_krus100A))
        self.assertEqual(self.stCost(self.res_prim100B), self.stCost(self.res_krus100B))

    def testTimings(self):
        """ Confirm each algo runs as quickly as expected (given the input) """
        self.assertGreater(self.time_prim100A, self.time_krus100A)
        self.assertGreater(self.time_krus100B, self.time_krus100A)
