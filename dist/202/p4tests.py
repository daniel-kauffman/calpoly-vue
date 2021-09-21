# Name:         
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set IV
# Term:         Spring 2021

import unittest

import pset4
# only allowed uses of from ... import
from pset4 import ListNode
from pset4 import TreeNode


class TestBinarySearch(unittest.TestCase):

    def test_binary_search_1(self):
        self.assertEqual(pset4.binary_search((2, 4, 6, 8, 10), 8, 0, 5), 3)

    def test_binary_search_2(self):
        self.assertEqual(pset4.binary_search((2, 4, 6, 8, 10), 7, 0, 5), -1)




class TestSumTree(unittest.TestCase):

    def test_sum_tree_1(self):
        root = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
        self.assertEqual(pset4.sum_tree(root), 6)




class TestAllBinary(unittest.TestCase):

    def test_all_binary_1(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3, None, None), None),
                           TreeNode(4, None, None))
        self.assertFalse(pset4.all_binary(root))




class TestFindRange(unittest.TestCase):

    def test_find_range_1(self):
        root = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
        self.assertEqual(pset4.find_range(root), (1, 3))




class TestIsBST(unittest.TestCase):

    def test_is_bst_1(self):
        root = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
        self.assertFalse(pset4.is_bst(root))




class TestToBST(unittest.TestCase):

    def test_to_bst_1(self):
        head = ListNode(2, ListNode(3, ListNode(1, None)))
        self.assertEqual(pset4.to_bst(head, None),
                         TreeNode(2, TreeNode(1, None, None),
                                     TreeNode(3, None, None)))




class TestInsert(unittest.TestCase):

    def test_insert_1(self):
        root = TreeNode(2, None, None)
        self.assertEqual(pset4.insert(root, 1),
                         TreeNode(2, TreeNode(1, None, None), None))

    def test_insert_2(self):
        root = TreeNode(2, TreeNode(1, None, None), None)
        self.assertEqual(pset4.insert(root, 3),
                         TreeNode(2, TreeNode(1, None, None),
                                     TreeNode(3, None, None)))




class TestRemove(unittest.TestCase):

    def test_remove_1(self):
        root = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
        self.assertEqual(pset4.remove(root, 1),
                         TreeNode(2, None, TreeNode(3, None, None)))




class TestRakeLeaves(unittest.TestCase):

    def test_rake_leaves_1(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4, None, None),
                                       TreeNode(5, None, None)),
                           TreeNode(3, None, None))
        self.assertEqual(pset4.rake_leaves(root, None),
                         ListNode(4, ListNode(5, ListNode(3, None))))




class TestOrderList(unittest.TestCase):

    def test_order_list_1(self):
        root = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
        self.assertEqual(pset4.order_list(root, "inorder", None),
                         ListNode(2, ListNode(1, ListNode(3, None))))


if __name__ == "__main__":
    unittest.main()
