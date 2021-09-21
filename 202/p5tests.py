# Name:         
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set V
# Term:         Spring 2021

import unittest

import pset5
from pset5 import ListNode  # only allowed uses of from ... import


class TestQueueConstructor(unittest.TestCase):

    def test_queue_constructor_1(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        self.assertEqual(queue.head,
                         ListNode(1, ListNode(2, ListNode(3, None))))
        self.assertEqual(queue.tail, ListNode(3, None))




class TestQueueEquals(unittest.TestCase):

    def test_queue_equals_1(self):
        qx = pset5.Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        qy = pset5.Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        self.assertEqual(qx, qy)

    def test_queue_equals_2(self):
        qx = pset5.Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        qy = pset5.Queue(ListNode(3, ListNode(2, ListNode(1, None))))
        self.assertNotEqual(qx, qy)




class TestQueueEnqueue(unittest.TestCase):

    def test_queue_enqueue_1(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, None)))
        queue.enqueue(3)
        self.assertEqual(queue.head,
                         ListNode(1, ListNode(2, ListNode(3, None))))
        self.assertEqual(queue.tail, ListNode(3, None))




class TestQueueDequeue(unittest.TestCase):

    def test_queue_dequeue_1(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        self.assertEqual(queue.dequeue(), ListNode(1, None))
        self.assertEqual(queue.head, ListNode(2, ListNode(3, None)))
        self.assertEqual(queue.tail, ListNode(3, None))




class TestSize(unittest.TestCase):

    def test_size_1(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        self.assertEqual(pset5.size(queue), 3)




class TestDequeueAll(unittest.TestCase):

    def test_dequeue_all_1(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, ListNode(1,
                                                    ListNode(3, None)))))
        self.assertEqual(pset5.dequeue_all(queue, 1), 2)
        self.assertEqual(queue.head, ListNode(2, ListNode(3, None)))




class TestQueueFlip(unittest.TestCase):

    def test_flip_1(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        pset5.flip(queue)
        self.assertEqual(queue.head,
                         ListNode(3, ListNode(2, ListNode(1, None))))
        self.assertEqual(queue.tail, ListNode(1, None))




class TestSiftUp(unittest.TestCase):

    def test_sift_up_1(self):
        self.assertEqual(pset5.sift_up([7, 6, 5, 4, 3, 2, 8], 6),
                         [8, 6, 7, 4, 3, 2, 5])




class TestSiftDown(unittest.TestCase):

    def test_sift_down_1(self):
        self.assertEqual(pset5.sift_down([1, 7, 6, 5, 4, 3, 2], 0),
                         [7, 5, 6, 1, 4, 3, 2])




class TestHeapify(unittest.TestCase):

    def test_heapify_1(self):
        self.assertEqual(pset5.heapify([1, 2, 3, 4, 5, 6, 7]),
                         [7, 5, 6, 4, 2, 1, 3])




class TestInsert(unittest.TestCase):

    def test_insert_1(self):
        self.assertEqual(pset5.insert([6, 5, 4, 3, 2, 1], 7),
                         [7, 5, 6, 3, 2, 1, 4])




class TestRemove(unittest.TestCase):

    def test_remove_1(self):
        self.assertEqual(pset5.remove([7, 6, 5, 4, 3, 2, 1]),
                         (7, [6, 4, 5, 1, 3, 2]))


if __name__ == "__main__":
    unittest.main()
