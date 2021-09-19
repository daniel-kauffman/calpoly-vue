# Name:         
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set V
# Term:         Spring 2021

from typing import List, Optional, Tuple


class ListNode:

    def __init__(self, val: int, ref: Optional["ListNode"]) -> None:
        self.val = val
        self.ref = ref

    def __eq__(self, other: Optional["ListNode"]) -> bool:
        if other is None:
            return False
        return self.val == other.val and self.ref == other.ref

    def __repr__(self) -> str:
        if self.ref is None:
            return str(self.val)
        return str(self.val) + " " + str(self.ref)




class Queue:

    def __init__(self, head: Optional[ListNode]) -> None:
        """
        An instance of Queue has two attributes.

            head: A reference to the first ListNode in the queue.
            tail: A reference to the final ListNode in the queue.

        >>> queue = Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        >>> queue.head
        ListNode(1, ListNode(2, ListNode(3, None)))
        >>> queue.tail
        ListNode(3, None)
        """


    def __eq__(self, other: "Queue") -> bool:
        """
        Return True if both Queue objects maintain references to the same
        sequence of ListNode objects and False otherwise.

        >>> qx = Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        >>> qy = Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        >>> qz = Queue(ListNode(3, ListNode(2, ListNode(1, None))))
        >>> qx == qy
        True
        >>> qx == qz
        False
        """


    def enqueue(self, val: int) -> None:
        """
        Add the given integer as a ListNode to the tail of the queue. This
        function mutates the calling Queue object in-place and does not return
        a value.

        >>> queue = Queue(ListNode(1, ListNode(2, None)))
        >>> queue.enqueue(3)
        >>> queue.head
        ListNode(1, ListNode(2, ListNode(3, None)))
        >>> queue.tail
        ListNode(3, None)
        """


    def dequeue(self) -> ListNode:
        """
        Remove the ListNode at the head of the queue and return it with its
        reference set to None. If the queue is empty, raise a ValueError. This
        function mutates the calling Queue object.

        >>> queue = Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        >>> queue.dequeue()
        ListNode(1, None)
        >>> queue.head
        ListNode(2, ListNode(3, None))
        >>> queue.tail
        ListNode(3, None)
        """




def size(queue: Queue) -> int:
    """
    Return the number of ListNodes in the given queue. The queue must contain
    its original ListNodes in the same order at the end of the procedure.

    >>> queue = Queue(ListNode(1, ListNode(2, ListNode(3, None))))
    >>> size(queue)
    3
    """




def dequeue_all(queue: Queue, val: int) -> int:
    """
    Using dequeue and enqueue operations, remove all ListNodes from the queue
    that contain the given integer value and return the number of nodes removed.
    All other ListNodes must be in the queue in their original order at the end
    of the procedure.

    >>> queue = Queue(ListNode(1, ListNode(2, ListNode(1, ListNode(3, None)))))
    >>> dequeue_all(queue, 1)
    2
    >>> queue.head
    ListNode(2, ListNode(3, None))
    """




def flip(queue: Queue) -> None:
    """
    Reverse the ListNodes of the given queue such that the original tail node
    becomes the head and vice versa. This function mutates the queue.

    >>> queue = Queue(ListNode(1, ListNode(2, ListNode(3, None))))
    >>> flip(queue)
    >>> queue.head
    ListNode(3, ListNode(2, ListNode(1, None)))
    >>> queue.tail
    ListNode(1, None)
    """




def sift_up(heap: List[int], index: int) -> List[int]:
    """
    Return a max-heap that has undergone a sift-up operation for the value at
    the given index.

    >>> sift_up([7, 6, 5, 4, 3, 2, 8], 6)
    [8, 6, 7, 4, 3, 2, 5]
    """




def sift_down(heap: List[int], index: int) -> List[int]:
    """
    Return a max-heap in which the root of a subtree at the given index has
    been sifted down (if necessary) to maintain the Heap Property.

    >>> sift_down([1, 7, 6, 5, 4, 3, 2], 0)
    [7, 5, 6, 1, 4, 3, 2]
    """




def heapify(ints: List[int]) -> List[int]:
    """
    Return a max-heap (represented as a list of integers) created using the
    given integers. This function must using sifting instead of insert to run
    in linear (instead of log-linear) time.

    >>> heapify([1, 2, 3, 4, 5, 6, 7])
    [7, 5, 6, 4, 2, 1, 3]
    """




def insert(heap: List[int], val: int) -> List[int]:
    """
    Return a max-heap with the given value added, using the sift-up operation
    to restore the Heap Property as necessary.

    >>> insert([6, 5, 4, 3, 2, 1], 7)
    [7, 5, 6, 3, 2, 1, 4]
    """




def remove(heap: List[int]) -> Tuple[int, List[int]]:
    """
    Return a tuple containing the removed value (previously at the root of the
    max-heap) along with the updated max-heap, using the sift-down operation to
    restore the Heap Property as necessary. If the heap is empty, raise a
    ValueError.

    >>> remove([7, 6, 5, 4, 3, 2, 1])
    (7, [6, 4, 5, 1, 3, 2])
    """

