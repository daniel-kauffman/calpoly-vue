# Name:         
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set VII
# Term:         Spring 2021

import unittest

import pset7
from pset7 import ListNode  # only allowed use of from ... import


class TestToAdjMatrix(unittest.TestCase):

    def test_to_adj_matrix_1(self):
        self.assertEqual(pset7.to_adj_matrix([[1, 2], [0, 2], [0, 1]]),
                         [[0, 1, 1], [1, 0, 1], [1, 1, 0]])




class TestToAdjList(unittest.TestCase):

    def test_to_adj_list_1(self):
        matrix = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
        self.assertEqual(pset7.to_adj_list(matrix), [[1, 2], [0, 2], [0, 1]])




class TestOrderBFS(unittest.TestCase):

    def test_order_bfs_1(self):
        adj_list = [[1, 2], [0, 3], [0, 3], [1, 2]]
        self.assertEqual(pset7.order_bfs(adj_list, 3), [3, 1, 2, 0])




class TestOrderDFS(unittest.TestCase):

    def test_order_dfs_1(self):
        adj_list = [[1, 2], [0, 3], [0, 3], [1, 2]]
        self.assertEqual(pset7.order_dfs(adj_list, 2, []), [2, 0, 1, 3])




class TestCountComponents(unittest.TestCase):

    def test_count_components_1(self):
        adj_list = [[1], [0], [3], [2], [5], [4]]
        self.assertEqual(pset7.count_components(adj_list), 3)




class TestHasCycle(unittest.TestCase):

    def test_has_cycle_1(self):
        adj_list = [[1, 2], [0, 3], [0, 3], [1, 2]]
        self.assertEqual(pset7.has_cycle(adj_list, 0, []), True)

    def test_has_cycle_2(self):
        adj_list = [[1, 2], [], []]
        self.assertEqual(pset7.has_cycle(adj_list, 0, []), False)




class TestHasTriangle(unittest.TestCase):

    def test_has_triangle_1(self):
        graph = (ListNode(1, ListNode(2, None)),
                 ListNode(0, ListNode(3, ListNode(4, None))),
                 ListNode(0, ListNode(5, None)),
                 ListNode(1, ListNode(4, None)),
                 ListNode(1, ListNode(3, ListNode(5, None))),
                 ListNode(2, ListNode(4, None)))
        self.assertTrue(pset7.has_triangle(graph))

    def test_has_triangle_2(self):
        graph = (ListNode(1, ListNode(2, None)),
                 ListNode(0, ListNode(3, None)),
                 ListNode(0, ListNode(5, None)),
                 ListNode(1, ListNode(4, None)),
                 ListNode(3, ListNode(5, None)),
                 ListNode(2, ListNode(4, None)))
        self.assertFalse(pset7.has_triangle(graph))


if __name__ == "__main__":
    unittest.main()
