<template>
  <Assignment :name="name" :title="title" :files="files">
    <template v-slot:description>
      <p>A tree is a recursively-defined data structure in which each node (sometimes called a vertex) of the tree maintains a reference to zero or more other nodes. This structure differs from a linked list in that a node may maintain more than one reference. However, trees may not contain cycles; that is, a node lower in the tree may not reference a node higher in the tree. This structure establishes a hierarchy for the data it maintains, which is useful for many computational problems, including structuring documents (e.g. <a target="_blank" href="https://en.wikipedia.org/wiki/HTML">HTML</a>), modeling <a target="_blank" href="https://en.wikipedia.org/wiki/Abstract_syntax_tree">programming</a> or <a target="_blank" href="https://en.wikipedia.org/wiki/Parse_tree">natural</a> languages, representing some <a target="_blank" href="https://en.wikipedia.org/wiki/Game_tree">games</a>, as well as countless other examples.</p>
      <p>A <strong>binary tree</strong> is a type of tree in which all nodes have no more than two references each (often called the left and right children). A <strong>Binary Search Tree</strong> (BST) is a type of binary tree in which nodes are inserted at specific locations to allow values to be found in <code>O(log n)</code> time. Like a binary search on an array, on each step the number of nodes to search can be reduced by roughly half because of the BST Property that requires all nodes less than a subtree's root to be in its left subtree and all nodes greater than a subtree's root to be in its right subtree.</p>
      <p>An example BST is shown below. Note that in many instances (including this assignment), duplicate values are not allowed or supported in BSTs.</p>
      <pre>
     4
   /   \
  2     6
 / \   /
1   3 5</pre>

      <p>Trees may be traversed in different ways, and the order with which each node's value is processed with respect to the traversal may differ as well. Common types of traversal include:</p>
      <ul>
        <li>Preorder: Process a value before traversing down subtrees</li>
        <li>Postorder: Process a value after traversing down subtrees</li>
        <li>Inorder: Process a value between traversing down the left and right subtrees (for a binary tree only)</li>
      </ul>
      <p>Simple examples of the need to differ processing order include evaluating a <a target="_blank" href="https://en.wikipedia.org/wiki/Polish_notation">prefix</a> versus a <a target="_blank" href="https://en.wikipedia.org/wiki/Reverse_Polish_notation">postfix</a> expression.</p>

    </template>

    <template v-slot:implementation>
      <p>All functions must use recursion; do not use any iteration (<code>while</code> or <code>for</code> loops). Do not use any Python lists.</p>

      <FunctionSignature name="binary_search" :params="[['ints', 'Tuple[int, ...]'], ['n', 'int'], ['start', 'int'], ['stop', 'int']]" type="int"/>
      <p>Using binary search, return the index of the given integer or -1 if it is not in the tuple. Assume the tuple is already sorted.</p>
      <pre>
binary_search((2, 4, 6, 8, 10), 8, 0, 5) -&gt; 3
binary_search((2, 4, 6, 8, 10), 7, 0, 5) -&gt; -1</pre>

      <FunctionSignature name="sum_tree" :params="[['root', 'Optional[TreeNode]']]" type="int"/>
      <p>Return the sum of all integers in each TreeNode in the tree. If the tree is empty, return 0.</p>
      <pre>sum_tree(TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))) -&gt; 6</pre>

      <FunctionSignature name="all_binary" :params="[['root', 'Optional[TreeNode]']]" type="bool"/>
      <p>Return True if every node in the given tree is either a leaf or an interior node with exactly two children (or if the tree is empty). Otherwise, return False if there is at least one node with only one child.</p>
      <pre>
root = TreeNode(1, TreeNode(2, TreeNode(3, None, None), None), TreeNode(4, None, None))
all_binary(root) -&gt; False</pre>

      <FunctionSignature name="find_range" :params="[['root', 'Optional[TreeNode]']]" type="Tuple[int, int]"/>
      <p>Return a 2-tuple containing the minimum and maximum integers (in that order) contained in the tree. Assume the tree is non-empty.</p>
      <pre>
root = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
find_range(root) -&gt; (1, 3)</pre>

      <FunctionSignature name="is_bst" :params="[['root', 'Optional[TreeNode]']]" type="bool"/>
      <p>Return True if the given binary tree has the BST property and False otherwise. Assume the tree has no duplicate values.</p>
      <p>A binary tree is a BST if, for any node, all nodes in its left subtree contain values lower than its value, and all nodes in its right subtree contain values greater than its value.</p>
      <pre>is_bst(TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))) -&gt; False</pre>

      <FunctionSignature name="to_bst" :params="[['head', 'Optional[ListNode]'], ['root', 'Optional[TreeNode]']]" type="Optional[TreeNode]"/>
      <p>Return a BST constructed from values in the given linked list, adding TreeNodes with values in the same order as the list. Use the root argument as an accumulator for the BST being constructed.</p>
      <pre>
head = ListNode(2, ListNode(3, ListNode(1, None)))
to_bst(head, None) -&gt; TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))</pre>

      <FunctionSignature name="insert" :params="[['root', 'Optional[TreeNode]'], ['val', 'int']]" type="TreeNode"/>
      <p>Return the root of a BST with a TreeNode containing val in its correctly sorted position. Assume val is not already in the tree.</p>
      <pre>
root = TreeNode(2, None, None)
insert(root, 1) -&gt; TreeNode(2, TreeNode(1, None, None), None)
insert(root, 3) -&gt; TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))</pre>

      <FunctionSignature name="remove" :params="[['root', 'Optional[TreeNode]'], ['val', 'int']]" type="Optional[TreeNode]"/>
      <p>Return the root of a BST with the TreeNode containing the given integer removed. If such a node does not exist, raise a ValueError. Assume no more than one node contains this integer.</p>
      <p>If the node to be removed has two children, replace its value with the maximum value of its left subtree and remove that node in the left subtree.</p>
      <pre>
root = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
remove(root, 1) -&gt; TreeNode(2, None, TreeNode(3, None, None))</pre>

      <FunctionSignature name="rake_leaves" :params="[['root', 'Optional[TreeNode]'], ['head', 'Optional[ListNode]']]" type="Optional[ListNode]"/>
      <p>Return a linked list of ListNode objects, matching the order of the leaves of the given tree, from left to right.</p>
      <p>Construct the linked list in reverse, starting with the right-most leaf and building the list backward, using the given head argument as an accumulator.</p>
      <pre>
root = TreeNode(1, TreeNode(2, TreeNode(4, None, None), TreeNode(5, None, None)), TreeNode(3, None, None))
rake_leaves(root, None) -&gt; ListNode(4, ListNode(5, ListNode(3, None)))</pre>

      <FunctionSignature name="order_list" :params="[['root', 'Optional[TreeNode]'], ['order', 'str'], ['head', 'Optional[ListNode]']]" type="Optional[ListNode]"/>
      <p>Return a linked list in which the integers in the list were retrieved from the tree according to the given order. Assume the order is one of "preorder", "inorder", or "postorder".</p>
      <pre>
root = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
order_list(root, "inorder", None) -&gt; ListNode(2, ListNode(1, ListNode(3, None)))</pre>
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
        name: "pset4",
        title: "Problem Set IV: Binary Trees",
        files: ["pset4.py", "p4tests.py"]
      };
    }
}
</script>

