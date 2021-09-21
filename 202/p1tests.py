# Name:         
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set I
# Term:         Spring 2021

import unittest

import pset1
from pset1 import ListNode  # only allowed use of from ... import


class TestInsert(unittest.TestCase):

    def test_insert_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset1.insert(head, 4, 0),
                    ListNode(4, ListNode(1, ListNode(2, ListNode(3, None)))))

    def test_insert_2(self):
        pass

    def test_insert_3(self):
        pass

    def test_insert_4(self):
        pass

    def test_insert_5(self):
        pass




class TestRemove(unittest.TestCase):

    def test_remove_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset1.remove(head, 0),
                         ListNode(2, ListNode(3, None)))




class TestIndex(unittest.TestCase):

    def test_index_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset1.index(head, 3), 2)




class TestConcat(unittest.TestCase):

    def test_concat_1(self):
        xs = ListNode(1, ListNode(2, ListNode(3, None)))
        ys = ListNode(4, ListNode(5, None))
        self.assertEqual(pset1.concat(xs, ys),
                         ListNode(1, ListNode(2, ListNode(3, ListNode(4,
                                  ListNode(5, None))))))




class TestSumList(unittest.TestCase):

    def test_sum_list_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset1.sum_list(head), 6)




class TestExpList(unittest.TestCase):

    def test_exp_list_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset1.exp_list(head, 3),
                         ListNode(1, ListNode(8, ListNode(27, None))))




class TestFibonacci(unittest.TestCase):

    def test_fibonacci_1(self):
        head = ListNode(0, ListNode(1, ListNode(1, ListNode(2,
                        ListNode(3, None)))))
        self.assertEqual(pset1.fibonacci(5), head)




class TestZipLists(unittest.TestCase):

    def test_zip_lists_1(self):
        xs = ListNode(1, ListNode(2, ListNode(3, None)))
        ys = ListNode(4, None)
        self.assertEqual(pset1.zip_lists(xs, ys),
                         ListNode(1, ListNode(4, ListNode(2,
                                  ListNode(3, None)))))




class TestUnzipList(unittest.TestCase):

    def test_unzip_list_1(self):
        head = ListNode(1, ListNode(4, ListNode(2, ListNode(5,
                        ListNode(3, None)))))
        unzipped = (ListNode(1, ListNode(2, ListNode(3, None))),
                    ListNode(4, ListNode(5, None)))
        self.assertEqual(pset1.unzip_list(head), unzipped)


if __name__ == "__main__":
    unittest.main()
