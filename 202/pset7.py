# Name:         
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set VII
# Term:         Spring 2021

from typing import List, Optional, Tuple


class ListNode:  # do not modify

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




def to_adj_matrix(adj_list: List[List[int]]) -> List[List[int]]:
    """
    Given an adjacency list, return its equivalent adjacency matrix, in which
    each inner list represents a row in the matrix, with a 0 or 1 in the row
    indicating whether a directed edge does not or does exist, respectively,
    between the row vertex to the column vertex.

    >>> to_adj_matrix([[1, 2], [0, 2], [0, 1]])
    [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    """




def to_adj_list(adj_matrix: List[List[int]]) -> List[List[int]]:
    """
    Given an adjacency matrix, return its equivalent adjacency list, in which
    each inner list represents all vertex labels for which the vertex at that
    index has a directed edge. For example, the first inner list contains all
    vertex labels for which Vertex 0 has a directed edge.

    >>> to_adj_list([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    [[1, 2], [0, 2], [0, 1]])
    """




def order_bfs(adj_list: List[List[int]], start: int) -> List[int]:
    """
    Return a list of unique vertex labels from the given graph representing a
    breadth-first traversal of the graph starting at the specified vertex (with
    lower-numbered vertices chosen before higher-numbered vertices).

    >>> order_bfs([[1, 2], [0, 3], [0, 3], [1, 2]], 3)
    [3, 1, 2, 0]
    """




def order_dfs(adj_list: List[List[int]], start: int,
              explored: List[int]) -> List[int]:
    """
    Return a list of unique vertex labels from the given adjacency list
    representing a depth-first traversal of the graph starting at the specified
    vertex (with lower-numbered vertices chosen over higher-numbered vertices).
    The explored argument may be used as an accumulator and will initially be
    an empty list.

    >>> order_dfs([[1, 2], [0, 3], [0, 3], [1, 2]], 2, [])
    [2, 0, 1, 3]
    """




def count_components(adj_list: List[List[int]]) -> int:
    """
    Return the number of components in the given graph (represented as an
    adjacency list). A component is defined as a subgraph of vertices in which
    no vertex in the subgraph has a path (a sequence of edges) to a vertex
    outside the subgraph.

    >>> count_components([[1], [0], [3], [2], [5], [4]])
    3
    """




def has_cycle(adj_list: List[List[int]], start: int, path: List[int]) -> bool:
    """
    Return True if the given graph (represented as an adjacency list) has a
    cycle and False otherwise. A graph has a cycle if there exists a path of
    unique edges that start and end at the same vertex.

    >>> has_cycle([[1, 2], [0, 3], [0, 3], [1, 2]], 0, [])  # square
    True
    >>> has_cycle([[1, 2], [], []], 0, [])  # tree
    False
    """




def has_triangle(graph: Tuple[ListNode, ...]) -> bool:
    """
    Return True if the given graph (represented as an adjacency list) contains
    a simple triangle and False otherwise. For this problem, a simple triangle
    is composed of exactly 3 vertices; in other words, do not count triangles
    that require considering more than 3 vertices to form.

    The graph below contains a simple triangle, 1-3-4. Note that a graph with
    a simple triangle may still have additional vertices outside the triangle.

             0
           /   \
          1     2
         /  \    \
        3 -- 4 -- 5

    >>> graph = (ListNode(1, ListNode(2, None)), \
                 ListNode(0, ListNode(3, ListNode(4, None))), \
                 ListNode(0, ListNode(5, None)), \
                 ListNode(1, ListNode(4, None)), \
                 ListNode(1, ListNode(3, ListNode(5, None))), \
                 ListNode(2, ListNode(4, None)))
    >>> has_triangle(graph)
    True

    The graph below does not contain a simple triangle.

             0
           /   \
          1     2
         /       \
        3 -- 4 -- 5

    >>> graph = (ListNode(1, ListNode(2, None)), \
                 ListNode(0, ListNode(3, None)), \
                 ListNode(0, ListNode(5, None)), \
                 ListNode(1, ListNode(4, None)), \
                 ListNode(3, ListNode(5, None)), \
                 ListNode(2, ListNode(4, None)))
    >>> has_triangle(graph)
    False
    """

