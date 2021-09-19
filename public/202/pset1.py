# Name:         
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set I
# Term:         Spring 2021

from typing import Optional, Tuple


# do not modify this class
class ListNode:

    def __init__(self, val: int, ref: Optional["ListNode"]) -> None:
        self.val = val
        self.ref = ref

    def __eq__(self, other: "ListNode") -> bool:
        """
        Return True if the two given lists have the same number of ListNodes and
        the same Node val at each respective position and False otherwise.

        >>> xs = ListNode(1, ListNode(2, ListNode(3, None)))
        >>> ys = ListNode(1, ListNode(2, ListNode(4, None)))
        >>> xs == ys
        False
        """
        while self is not None and other is not None:
            if self.val != other.val:
                return False
            self = self.ref
            other = other.ref
        return self is None and other is None

    def __repr__(self) -> str:
        """
        Return a string representation of the linked list. String
        representations of objects are useful for reading test suite errors.

        >>> xs = ListNode(1, ListNode(2, ListNode(3, None)))
        >>> str(xs)
        "1-2-3"
        """
        list_str = str(self.val)
        while True:
            self = self.ref
            if self is None:
                return list_str
            list_str += "-" + str(self.val)




def insert(head: Optional[ListNode], val: int, index: int) -> ListNode:
    """
    Return the head of a linked list with a ListNode containing val at position
    index in the list. If index is outside the bounds of the list (including if
    the initial list is empty), the new ListNode should be appended to the end.

    >>> head = ListNode(1, ListNode(2, ListNode(3, None)))
    >>> insert(head, 4, 0)
    ListNode(4, ListNode(1, ListNode(2, ListNode(3, None))))
    """




def remove(head: Optional[ListNode], index: int) -> Optional[ListNode]:
    """
    Return the head of a linked list with the ListNode at position index
    removed. If index is outside the bounds of the list, raise an IndexError.

    >>> head = ListNode(1, ListNode(2, ListNode(3, None)))
    >>> remove(head, 0)
    ListNode(2, ListNode(3, None))
    """




def index(head: Optional[ListNode], val: int) -> int:
    """
    Return the position of the ListNode containing val. If such a node does not
    exist, return -1.

    >>> head = ListNode(1, ListNode(2, ListNode(3, None)))
    >>> index(head, 3)
    2
    """




def concat(xs: Optional[ListNode],
           ys: Optional[ListNode]) -> Optional[ListNode]:
    """
    Return the head of a linked list that represents the concatenation of the
    given lists, such that xs comes before ys.

    >>> xs = ListNode(1, ListNode(2, ListNode(3, None)))
    >>> ys = ListNode(4, ListNode(5, None))
    >>> concat(xs, ys)
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    """




def sum_list(head: Optional[ListNode]) -> int:
    """
    Return the sum of all integers in each ListNode in the list. If the list is
    empty, return 0.

    >>> head = ListNode(1, ListNode(2, ListNode(3, None)))
    >>> sum_list(head)
    6
    """




def exp_list(head: Optional[ListNode], exp: int) -> Optional[ListNode]:
    """
    Return the head of a linked list in which the integer in each ListNode has
    been raised to the exp power.

    >>> head = ListNode(1, ListNode(2, ListNode(3, None)))
    >>> exp_list(head, 3)
    ListNode(1, ListNode(8, ListNode(27, None)))
    """




def fibonacci(n: int) -> ListNode:
    """
    Return a the head of a linked list representing the Fibonacci Sequence up
    to the given number of n places. Each integer in this sequence is the sum
    of the previous two integers (except for the first two integers, 0 and 1,
    which are base values not derived from adding other integers). Assume n is
    non-negative; if it is zero, return an empty list.

    >>> fibonacci(5)
    ListNode(0, ListNode(1, ListNode(1, ListNode(2, ListNode(3, None)))))
    """




def zip_lists(xs: Optional[ListNode],
              ys: Optional[ListNode]) -> Optional[ListNode]:
    """
    Return the head of a linked list that represents the pair-wise combination
    of the given linked lists. If one list runs out of ListNodes, append the
    remainder of the other list.

    >>> xs = ListNode(1, ListNode(2, ListNode(3, None)))
    >>> ys = ListNode(4, None)
    >>> zip_lists(xs, ys)
    ListNode(1, ListNode(4, ListNode(2, ListNode(3, None))))
    """




def unzip_list(head: Optional[ListNode]
) -> Tuple[Optional[ListNode], Optional[ListNode]]:
    """
    Return a 2-tuple of heads of linked lists that represents the pair-wise
    separation of the given linked lists. This operation is the inverse of
    zip_lists.

    >>> head = ListNode(1, ListNode(4, ListNode(2, \
                                       ListNode(5, ListNode(3, None)))))
    >>> unzip_list(head)
    (ListNode(1, ListNode(2, ListNode(3, None))), \
     ListNode(4, ListNode(5, None)))
    """

