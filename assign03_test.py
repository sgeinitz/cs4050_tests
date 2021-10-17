import unittest

from assign03 import *

class TestAssign3Functions(unittest.TestCase):
    """ A class derived from unittest.TestCase to test assign03.py functions """

    def setUp(self):
        self.g10 = adjMatFromFile("graph_10verts.txt")
        self.g20 = adjMatFromFile("graph_20verts.txt")
        self.g100 = adjMatFromFile("graph_100verts.txt")
        self.g100_alt1 = adjMatFromFile("graph_100verts.txt")
        self.g100_alt2 = adjMatFromFile("graph_100verts.txt")
        self.g10alt = [list(row) for row in self.g10]
        self.g10alt[6][1], self.g10alt[6][8] = self.g10alt[6][8], self.g10alt[6][1]
        self.g10alt[2][8] = 4
        self.dijkstra_start = 2
        self.res_dijkstra10 = dijkstra(self.g10, self.dijkstra_start)
        self.res_dijkstra10alt = dijkstra(self.g10alt, self.dijkstra_start)
        self.res_dijkstra20 = dijkstra(self.g20, self.dijkstra_start)
        self.res_dijkstra100 = dijkstra(self.g100, self.dijkstra_start)

        self.res_dijkstra100 = [[None]*len(self.g100) for i in range(len(self.g100))]
        start_time = time.time()
        for sv in range(len(self.g100_alt1)):
            self.res_dijkstra100[sv] = dijkstra(self.g100, sv)
        self.elapsed_time_dijkstra = time.time() - start_time
        self.res_dijkstra100

        start_time = time.time()
        self.res_floyd100 = floyd(self.g100_alt2)
        self.elapsed_time_floyd = time.time() - start_time

    def testFloydAndDijkstra(self):
        """ Confirm that both produce same results """
        self.assertGreater(self.elapsed_time_dijkstra * 2.0, self.elapsed_time_floyd)
        self.assertEqual(self.res_dijkstra100, self.res_floyd100)

    def testDijkstra10(self):
        """ Confirm that functions run as expected """
        expected10 = [46, 52, 0, 19, 8, 2, 37, 9, 30, 25]
        self.assertEqual(self.res_dijkstra10, expected10)
        expected_10alt = [20, 16, 0, 14, 8, 2, 11, 9, 4, 8]
        self.assertEqual(self.res_dijkstra10alt, expected_10alt)

    def testDijkstra20(self):
        """ Confirm that functions run as expected """
        expected20 = [24, 8, 0, 31, 8, 19, 16, 8, 20, 15, 21, 14, 34, 18, 24, 29, 21, 26, 17, 7]
        self.assertEqual(self.res_dijkstra20, expected20)
