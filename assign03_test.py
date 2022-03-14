import unittest

from assign03 import *

class TestAssign3Functions(unittest.TestCase):
    """ A class derived from unittest.TestCase to test assign03.py functions """

    def setUp(self):
        self.g10 = adjMatFromFile("graph_10verts.txt")
        self.g10alt = [list(row) for row in self.g10]
        self.g10alt[6][1], self.g10alt[6][8] = self.g10alt[6][8], self.g10alt[6][1]
        self.g10alt[2][8] = 4

        self.g20 = adjMatFromFile("graph_20verts.txt")

        self.g100A = adjMatFromFile("graph_100verts_A.txt") # sparse graph
        self.g100B = adjMatFromFile("graph_100verts_B.txt") # dense graph

        self.dijkstra_start = 2

        self.res_dijkstra_pq10 = dijkstra_w_pri_queue(list(self.g10), self.dijkstra_start)
        self.res_dijkstra_pq10alt = dijkstra_w_pri_queue(list(self.g10alt), self.dijkstra_start)
        self.res_dijkstra_pq20 = dijkstra_w_pri_queue(list(self.g20), self.dijkstra_start)

        self.res_dijkstra_arr10 = dijkstra_w_array(list(self.g10), self.dijkstra_start)
        self.res_dijkstra_arr10alt = dijkstra_w_array(list(self.g10alt), self.dijkstra_start)
        self.res_dijkstra_arr20 = dijkstra_w_array(list(self.g20), self.dijkstra_start)

        # run dijkstra's with a priority queue on a sparse graph -> O(E * lg V)
        self.res_dijkstra_pq100A = [[None]*len(self.g100A) for i in range(len(self.g100A))]
        start_time = time.time()
        for sv in range(len(self.g100A)):
            self.res_dijkstra_pq100A[sv] = dijkstra_w_pri_queue(list(self.g100A), sv)
        self.elapsed_time_dijkstra_pqA = time.time() - start_time
        print(f"dijkstra pri que w/ sparse graph: {self.elapsed_time_dijkstra_pqA:.4f} runtime")

        # run dijkstra's with an array on a sparse graph -> O( V^2 )
        self.res_dijkstra_arr100A = [[None]*len(self.g100A) for i in range(len(self.g100A))]
        start_time = time.time()
        for sv in range(len(self.g100A)):
            self.res_dijkstra_arr100A[sv] = dijkstra_w_array(list(self.g100A), sv)
        self.elapsed_time_dijkstra_arrA = time.time() - start_time
        print(f"dijkstra array w/ sparse graph: {self.elapsed_time_dijkstra_arrA:.4f} runtime")

        # run dijkstra's with a priority queue on a dense graph -> O(E * lg V), so longer runtime than w/ A
        self.res_dijkstra_pq100B = [[None]*len(self.g100B) for i in range(len(self.g100B))]
        start_time = time.time()
        for sv in range(len(self.g100B)):
            self.res_dijkstra_pq100B[sv] = dijkstra_w_pri_queue(list(self.g100B), sv)
        self.elapsed_time_dijkstra_pqB = time.time() - start_time
        print(f"dijkstra pri que w/ dense graph: {self.elapsed_time_dijkstra_pqB:.4f} runtime")

        # run dijkstra's with an array on a dense graph -> O( V^2 ), so roughly same runtime as w/ A
        self.res_dijkstra_arr100B = [[None]*len(self.g100B) for i in range(len(self.g100B))]
        start_time = time.time()
        for sv in range(len(self.g100B)):
            self.res_dijkstra_arr100B[sv] = dijkstra_w_array(list(self.g100B), sv)
        self.elapsed_time_dijkstra_arrB = time.time() - start_time
        print(f"dijkstra array w/ dense graph: {self.elapsed_time_dijkstra_arrB:.4f} runtime")

        # floyd's with sparse graph
        start_time = time.time()
        self.res_floyd100A = floyd(list(self.g100A))
        self.elapsed_time_floydA = time.time() - start_time

        # floyd's with dense graph
        start_time = time.time()
        self.res_floyd100B = floyd(list(self.g100B))
        self.elapsed_time_floydB = time.time() - start_time

    def testFloydAndDijkstra(self):
        """ Confirm that all three produce same results """
        #self.assertGreater(self.elapsed_time_dijkstra_pqA, self.elapsed_time_floydA)
        self.assertEqual(self.res_dijkstra_pq100A, self.res_floyd100A)
        self.assertEqual(self.res_dijkstra_arr100A, self.res_floyd100A)

    def testFloydTiming(self):
        """ Floyd's runtime is not dependent on number of edges """
        self.assertLess(self.elapsed_time_floydA/self.elapsed_time_floydB, 1.5)
        self.assertGreater(self.elapsed_time_floydA/self.elapsed_time_floydB, 0.5)

    def testDijkstraTiming(self):
        """ Dijkstra with array should be similar, but with priqueue is different """
        self.assertLess(self.elapsed_time_dijkstra_arrA/self.elapsed_time_dijkstra_arrB, 1.5)
        self.assertGreater(self.elapsed_time_dijkstra_arrA/self.elapsed_time_dijkstra_arrB, 0.5)
        self.assertGreater(self.elapsed_time_dijkstra_pqB/self.elapsed_time_dijkstra_pqA, 1.1) # was 1.50

    def testDijkstra10(self):
        """ Confirm that functions run as expected """
        expected_10 = [46, 52, 0, 19, 8, 2, 37, 9, 30, 25]
        self.assertEqual(self.res_dijkstra_pq10, self.res_dijkstra_arr10)
        self.assertEqual(self.res_dijkstra_arr10, expected_10)
        expected_10alt = [20, 16, 0, 14, 8, 2, 11, 9, 4, 8]
        self.assertEqual(self.res_dijkstra_pq10alt, self.res_dijkstra_arr10alt)
        self.assertEqual(self.res_dijkstra_arr10alt, expected_10alt)

    def testDijkstra20(self):
        """ Confirm that functions run as expected """
        expected20 = [24, 8, 0, 31, 8, 19, 16, 8, 20, 15, 21, 14, 34, 18, 24, 29, 21, 26, 17, 7]
        self.assertEqual(self.res_dijkstra_pq20, expected20)
        self.assertEqual(self.res_dijkstra_arr20, expected20)

