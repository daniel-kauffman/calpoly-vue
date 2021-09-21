# Name:         
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set II
# Term:         Spring 2021

import unittest

import pset2
from pset2 import StackNode  # only allowed use of from ... import


class TestPush(unittest.TestCase):

    def test_push_1(self):
        top = StackNode(2, StackNode(3, None))
        top = pset2.push(top, StackNode(1, None))
        self.assertEqual(top, StackNode(1, StackNode(2, StackNode(3, None))))

    def test_push_2(self):
        pass

    def test_push_3(self):
        pass

    def test_push_4(self):
        pass

    def test_push_5(self):
        pass




class TestPop(unittest.TestCase):

    def test_pop_1(self):
        top = StackNode(1, StackNode(2, StackNode(3, None)))
        node, top = pset2.pop(top)
        self.assertEqual(node.val, 1)
        self.assertEqual(node.ref, None)
        self.assertEqual(top, StackNode(2, StackNode(3, None)))




class TestMove(unittest.TestCase):

    def test_move_1(self):
        top = StackNode(1, StackNode(2, StackNode(3, None)))
        self.assertEqual(pset2.move(top, None),
                         (StackNode(2, StackNode(3, None)), StackNode(1, None)))




class TestFlipStack(unittest.TestCase):

    def test_flip_stack_1(self):
        top = StackNode(1, StackNode(2, StackNode(3, None)))
        self.assertEqual(pset2.flip_stack(top),
                         StackNode(3, StackNode(2, StackNode(1, None))))




class TestConcat(unittest.TestCase):

    def test_concat_1(self):
        xs = StackNode(1, StackNode(2, StackNode(3, None)))
        ys = StackNode(4, StackNode(5, None))
        self.assertEqual(pset2.concat(xs, ys),
                         StackNode(1, StackNode(2, StackNode(3, \
                                      StackNode(4, StackNode(5, None))))))



class TestPopAll(unittest.TestCase):

    def test_pop_all_1(self):
        top = StackNode(1, StackNode(2, StackNode(1, StackNode(3, None))))
        self.assertEqual(pset2.pop_all(top, 1),
                         StackNode(2, StackNode(3, None)))




class TestZipStacks(unittest.TestCase):

    def test_zip_stacks_1(self):
        xs = StackNode(1, StackNode(2, StackNode(3, None)))
        ys = StackNode(4, None)
        self.assertEqual(pset2.zip_stacks(xs, ys),
                         StackNode(1, StackNode(4, StackNode(2, \
                                      StackNode(3, None)))))




class TestUnzipStack(unittest.TestCase):

    def test_unzip_stack_1(self):
        top = StackNode(1, StackNode(4, StackNode(2, \
                                        StackNode(5, StackNode(3, None)))))
        self.assertEqual(pset2.unzip_stack(top),
                         (StackNode(1, StackNode(2, StackNode(3, None))),
                          StackNode(4, StackNode(5, None))))




class TestSortStack(unittest.TestCase):

    def test_sort_stack_1(self):
        top = StackNode(5, StackNode(2, StackNode(8, None)))
        self.assertEqual(pset2.sort_stack(top),
                         StackNode(2, StackNode(5, StackNode(8, None))))


if __name__ == "__main__":
    unittest.main()
