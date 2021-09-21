# Name:         
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set VI
# Term:         Spring 2021

import unittest

import pset6
from pset6 import Entry, TreeNode  # only allowed use of from ... import


class TestHashKey(unittest.TestCase):

    def test_hash_key_1(self):
        self.assertEqual(pset6.hash_key(3, 3), 0)

    def test_hash_key_2(self):
        self.assertEqual(pset6.hash_key(6, 5), 1)

    def test_hash_key_3(self):
        self.assertEqual(pset6.hash_key(10, 7), 3)

    def test_hash_key_4(self):
        self.assertEqual(pset6.hash_key(0, 1), 0)

    def test_hash_key_5(self):
        with self.assertRaises(ZeroDivisionError):
            pset6.hash_key(1, 0)




class TestGetLoadFactor(unittest.TestCase):

    def test_get_load_factor_1(self):
        table = [None, Entry(1, "A", Entry(5, "B", None)), None, None]
        self.assertEqual(pset6.get_load_factor(table), 0.5)

    def test_get_load_factor_2(self):
        table = [Entry(0, "A", None), Entry(5, "B", None), None, None, None]
        self.assertEqual(pset6.get_load_factor(table), 0.4)




class TestResize(unittest.TestCase):

    def test_resize_1(self):
        table = [Entry(0, "A", Entry(3, "B", Entry(6, "C", None))),
                 Entry(7, "D", Entry(1, "E", None)), None]
        resized = [Entry(7, "D", Entry(0, "A", None)), Entry(1, "E", None),
                   None, Entry(3, "B", None), None, None, Entry(6, "C", None)]
        self.assertEqual(pset6.resize(table, "chain"), resized)

    def test_resize_2(self):
        table = [Entry(0, "A", None), Entry(3, "B", None), Entry(8, "C", None)]
        resized = [Entry(0, "A", None), Entry(8, "C", None), None,
                   Entry(3, "B", None), None, None, None]
        self.assertEqual(pset6.resize(table, "probe"), resized)




class TestChainGet(unittest.TestCase):

    def test_chain_get_1(self):
        table = [Entry(3, "B", Entry(0, "A", None)), None, None]
        self.assertEqual(pset6.chain_get(table, 0), "A")




class TestChainInsert(unittest.TestCase):

    def test_chain_insert_1(self):
        table = [Entry(3, "C", Entry(0, "A", None)), 
                 Entry(4, "D", Entry(1, "B", None)), None]
        inserted = [Entry(0, "A", None), Entry(8, "E", Entry(1, "B", None)),
                    None, Entry(3, "C", None), Entry(4, "D", None), None, None]
        self.assertEqual(pset6.chain_insert(table, 8, "E"), inserted)




class TestChainRemove(unittest.TestCase):

    def test_chain_remove_1(self):
        table = [Entry(6, "C", Entry(3, "B", Entry(0, "A", None))), None, None]
        self.assertEqual(pset6.chain_remove(table, 3),
                         [Entry(6, "C", Entry(0, "A", None)), None, None])




class TestProbeGet(unittest.TestCase):

    def test_probe_get_1(self):
        table = [Entry(0, "A", None), Entry(3, "B", None), None]
        self.assertEqual(pset6.probe_get(table, 3), "B")




class TestProbeInsert(unittest.TestCase):

    def test_probe_insert_1(self):
        table = [Entry(0, "A", None), Entry(1, "B", None), None]
        inserted = [Entry(0, "A", None), Entry(1, "B", None),
                    Entry(2, "C", None), None, None, None, None]
        self.assertEqual(pset6.probe_insert(table, 2, "C"), inserted)




class TestProbeRemove(unittest.TestCase):

    def test_probe_remove_1(self):
        table = [Entry(0, "A", None), Entry(1, "B", None), None]
        self.assertEqual(pset6.probe_remove(table, 0),
                         [Entry(None, None, None), Entry(1, "B", None), None])




class TestGetHeight(unittest.TestCase):

    def test_get_height_1(self):
        root = TreeNode(3, TreeNode(2, TreeNode(1, None, None), None),
                           TreeNode(4, None, None))
        self.assertEqual(pset6.get_height(root), 2)




class TestBalanceTree(unittest.TestCase):

    def test_balance_tree_1(self):
        root = TreeNode(3, TreeNode(2, TreeNode(1, None, None), None), None)
        self.assertEqual(pset6.balance_tree(root),
                         TreeNode(2, TreeNode(1, None, None),
                                     TreeNode(3, None, None)))


if __name__ == "__main__":
    unittest.main()
