<template>
  <Assignment :name="name" :title="title" :files="files">
    <template v-slot:description>
    </template>

    <template v-slot:implementation>
      <p>For this assignment, vertex labels are integers. Adjacency matrices and adjacency lists are represented as 2D lists of integers.</p>

      <FunctionSignature name="to_adj_matrix" :params="[['adj_list', 'List[List[int]]']]" type="List[List[int]]"/>
      <p>Given an adjacency list, return its equivalent adjacency matrix, in which each inner list represents a row in the matrix, with a 0 or 1 in the row indicating whether a directed edge does not or does exist, respectively, between the row vertex to the column vertex.</p>
      <pre>to_adj_matrix([[1, 2], [0, 2], [0, 1]]) -&gt; [[0, 1, 1], [1, 0, 1], [1, 1, 0]]</pre>

      <FunctionSignature name="to_adj_list" :params="[['adj_matrix', 'List[List[int]]']]" type="List[List[int]]"/>
      <p>Given an adjacency matrix, return its equivalent adjacency list, in which each inner list represents all vertex labels for which the vertex at that index has a directed edge. For example, the first inner list contains all vertex labels for which Vertex 0 has a directed edge.</p>
      <pre>to_adj_list([[0, 1, 1], [1, 0, 1], [1, 1, 0]]) -&gt; [[1, 2], [0, 2], [0, 1]])</pre>

      <FunctionSignature name="order_bfs" :params="[['adj_list', 'List[List[int]]'], ['start', 'int']]" type="List[int]"/>
      <p>Return a list of unique vertex labels from the given graph representing a breadth-first traversal of the graph starting at the specified vertex (with lower-numbered vertices chosen before higher-numbered vertices).</p>
      <pre>order_bfs([[1, 2], [0, 3], [0, 3], [1, 2]], 3) -&gt; [3, 1, 2, 0]</pre>

      <FunctionSignature name="order_dfs" :params="[['adj_list', 'List[List[int]]'], ['start', 'int'], ['explored', 'List[int]']]" type="List[int]"/>
      <p>Return a list of unique vertex labels from the given adjacency list representing a depth-first traversal of the graph starting at the specified vertex (with lower-numbered vertices chosen over higher-numbered vertices).  The explored argument may be used as an accumulator and will initially be an empty list.</p>
      <pre>order_dfs([[1, 2], [0, 3], [0, 3], [1, 2]], 2, []) -&gt; [2, 0, 1, 3]</pre>

      <FunctionSignature name="count_components" :params="[['adj_list', 'List[List[int]]']]" type="int"/>
      <p>Return the number of components in the given graph (represented as an adjacency list). A component is defined as a subgraph of vertices in which no vertex in the subgraph has a path (a sequence of edges) to a vertex outside the subgraph.</p>
      <pre>count_components([[1], [0], [3], [2], [5], [4]]) -&gt; 3</pre>

      <FunctionSignature name="has_cycle" :params="[['adj_list', 'List[List[int]]'], ['start', 'int'], ['path', 'List[int]']]" type="bool"/>
      <p>Return True if the given graph (represented as an adjacency list) has a cycle and False otherwise. A graph has a cycle if there exists a path of unique edges that start and end at the same vertex.</p>
      <p>For example, the following graph is cyclic:</p>
      <pre>
A - B - E
|   |
C - D - F</pre>
      <p>A tree, however, is acyclic because there never exists an edge from any vertex in the tree that returns to a previous vertex or a vertex in a different subtree. In the example below, there is no single edge from, say, D to A or B to C, and thus the graph contains no cycles.</p>
      <pre>
     A
   /   \
  B     C
 / \   / \
D   E F   G</pre>
      <p>Note that a cycle cannot be formed on the same edge and the following graph is acyclic:</p>
      <pre>A - B</pre>
      <p>To determine whether a graph contains a cycle, you may use a depth-first search (DFS) to traverse the graph, using the provided path argument to keep track of which vertices have been encountered along a particular path.  If, from the current vertex, another vertex is adjacent but is already in the path, the graph has a cycle.</p>
      <pre>
# square
has_cycle([[1, 2], [0, 3], [0, 3], [1, 2]], 0, []) -&gt; True

# tree
has_cycle([[1, 2], [], []], 0, []) -&gt; False</pre>

      <FunctionSignature name="has_triangle" :params="[['graph', 'Tuple[ListNode, ...]']]" type="bool"/>
      <p>Return True if the given graph (represented as an adjacency list) contains a simple triangle and False otherwise. For this problem, a simple triangle is composed of exactly 3 vertices; in other words, do not count triangles that require considering more than 3 vertices to form.</p>
      <p>The graph below does contains a simple triangle, 1-3-4. Note that a graph with a simple triangle may still have additional vertices outside the triangle.</p>
      <pre>
     0
   /   \
  1     2
 /  \    \
3 -- 4 -- 5

graph = (ListNode(1, ListNode(2, None)),
         ListNode(0, ListNode(3, ListNode(4, None))),
         ListNode(0, ListNode(5, None)),
         ListNode(1, ListNode(4, None)),
         ListNode(1, ListNode(3, ListNode(5, None))),
         ListNode(2, ListNode(4, None)))
has_triangle(graph) -&gt; True</pre>

      <p>The graph below does not contain a simple triangle.</p>

      <pre>
     0
   /   \
  1     2
 /       \
3 -- 4 -- 5

graph = (ListNode(1, ListNode(2, None)),
         ListNode(0, ListNode(3, None)),
         ListNode(0, ListNode(5, None)),
         ListNode(1, ListNode(4, None)),
         ListNode(3, ListNode(5, None)),
         ListNode(2, ListNode(4, None)))
has_triangle(graph) -&gt; False</pre>
    </template>
  </Assignment>
</template>


<script>
import Assignment from "@/components/BaseAssignment.vue"
import FunctionSignature from "@/components/AssignmentFunctionSignature.vue"


export default {
  components: {
    Assignment,
    FunctionSignature
  },
  data:
    function () {
      return {
        name: "pset7",
        title: "Problem Set VII: Graphs",
        files: ["pset7.py", "p7tests.py"]
      };
    }
}
</script>
