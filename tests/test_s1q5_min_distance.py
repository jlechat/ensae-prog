#bonus
import sys 
sys.path.append("delivery_network")

from graph import Graph, graph_from_file

import unittest   # The test framework

class Test_Reachability(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file("input/network.00.in")
        self.assertEqual(g.get_path_with_power(1, 4, 11), "path : [1, 2, 3, 4], distance : 3")
        self.assertEqual(g.get_path_with_power(1, 4, 10), None)

    def test_network2(self):
        g = graph_from_file("input/network.02.in")
        self.assertEqual(g.get_path_with_power(1, 2, 11), "path : [1, 2], distance : 1")
        self.assertEqual(g.get_path_with_power(1, 2, 5), "path : [1, 4, 3, 2], distance : 3")

    def test_network4(self):
        g = graph_from_file("input/network.04.in")
        self.assertEqual(g.get_path_with_power(1, 3, 11), "path : [1, 4, 3], distance : 8")
        self.assertEqual(g.get_path_with_power(2, 4, 5), "path : [2, 3, 4], distance : 5")

if __name__ == '__main__':
    unittest.main()
