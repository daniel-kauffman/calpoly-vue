<template>
  <Assignment :name="name" :title="title" :files="files">
    <template v-slot:description>
      <p>A singly linked list is a elementary linear data structure composed of a sequence of nodes. Each of these nodes contains two values: some form of data (such as an integer or string), and a <strong>reference</strong> to the next node in the sequence. These references allow an algorithm to traverse from the beginning, or <strong>head</strong>, of the list to the end, or <strong>tail</strong>. The tail of a linear linked list has a null value for its node reference (such as Python's <code>None</code>).</p>

      <p>Each node in the list is simple in structure. The following ListNode class provides the representation of nodes for this and some future assignments. For simplicity, we will use integers for the data component of a node, but in general this value could be anything.</p>
      <pre>
class ListNode:

    def __init__(self, val: int, ref: Optional["ListNode"]) -&gt; None:
        self.val = val
        self.ref = ref</pre>
      <p>Note that the <code>Optional</code> type annotation indicates that <code>ref</code> may be a ListNode or <code>None</code> (see below).</p>
      <p>As an example, the list <code>1 2 3</code> could be formed one ListNode object at a time as:</p>
      <pre>
head = ListNode(3, None)
head = ListNode(2, head)
head = ListNode(1, head)</pre>
      <p>This example could also be done on a single line as:</p>
      <pre>head = ListNode(1, ListNode(2, ListNode(3, None)))</pre>
      <p>In all instances, the first value to the ListNode constructor (the data) is an integer, and the second value (the reference) is either another ListNode object or <code>None</code>. A linked list can thus be traversed by starting from the head node and continuing until a node's <code>ref</code> attribute is <code>None</code>, indicating that it is the tail.</p>

      <h4>Type Annotations</h4>
      <p>As of Python 3.5, function headers may also include parameter and return type annotations to make it clear what data types are input and output by the function. Python is a <a target="_blank" href="https://en.wikipedia.org/wiki/Type_system#Dynamic_type_checking_and_runtime_type_information">dynamically-typed</a> language, meaning that data types used in the program are not known to be correct until the program is already running (in contrast to a <a target="_blank" href="https://en.wikipedia.org/wiki/Type_system#Static_type_checking">statically-typed</a> language). The benefit of dynamic typing is less code and more flexibility, at the cost of less error checking by a compiler and the potential for more bugs.</p>
      <p>To aid your learning and help you detect bugs early, all functions headers in this and future assignments must have correct type annotations. With some exceptions, variables will not require type annotations. See the Code Style policy for a link to an external reference on Python type annotations.</p>
      <h4>The Optional Type Annotation</h4>
      <p>A type can be specified to be either something or <code>None</code> using the <code>Optional[Type]</code> annotation. For example, if a function sometimes returns a string and sometimes returns <code>None</code>, use <code>Optional[str]</code> for the return type.</p>
      <p>To gain access to the <code>Optional</code> annotation in your program, include the following line before your function definitions:</p>
      <pre>from typing import Optional</pre>
      <p>Note that <code>typing</code> is the only module for which you may use the <code>from</code> import notation in this course (unless otherwise stated).</p>

      <h4>Testing</h4>
      <p>In this and future assignments, all functions must have at least 5 test cases in the required tests file. We will be using Python's <code>unittest</code> module to write test cases. Some example test cases have been provided for you in the starter file (linked above); additional examples and documentation can be found at: <a target="_blank" href="https://docs.python.org/3/library/unittest.html">https://docs.python.org/3/library/unittest.html</a>.</p>
      <p>Much of the code necessary to write unit tests is boilerplate; the primary assertion functions that you will need are:</p>
      <ul>
        <li><code><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual">assertAlmostEqual</a></code> for comparing floats</li>
        <li><code><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual">assertEqual</a></code> for any other comparison</li>
        <li><code><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotEqual">assertNotEqual</a></code> sometimes useful (e.g. for testing <code>__eq__</code> False cases) but usually <code>assertEqual</code> is preferred</li>
        <li><code><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises">assertRaises</a></code> for test cases that should raise an error (use the <code>with</code> notation; see link for an example)</li>
      </ul>
    </template>

    <template v-slot:implementation>
      <p>See the provided <code>pset1.py</code> file for the <code>ListNode</code> class, which contains <code>__eq__</code> (equality) and <code>__repr__</code> (string representation) methods to facilitate testing and debugging.</p>

      <AssignmentFunctionSignature name="insert" :params="[['head', 'Optional[ListNode]'], ['val', 'int'], ['index', 'int']]" type="ListNode"/>
      <p>Return the head of a linked list with a ListNode containing <code>val</code> at position <code>index</code> in the list. If <code>index</code> is outside the bounds of the list (including if the initial list is empty), the new ListNode should be appended to the end.</p>
      <pre>
head = ListNode(1, ListNode(2, ListNode(3, None)))
insert(head, 4, 0) -&gt; ListNode(4, ListNode(1, ListNode(2, ListNode(3, None))))</pre>

      <AssignmentFunctionSignature name="remove" :params="[['head', 'Optional[ListNode]'], ['index', 'int']]" type="Optional[ListNode]"/>
      <p>Return the head of a linked list with the ListNode at position <code>index</code> removed. If <code>index</code> is outside the bounds of the list, raise an <code>IndexError</code>.</p>
      <pre>
head = ListNode(1, ListNode(2, ListNode(3, None)))
remove(head, 0) -&gt; ListNode(2, ListNode(3, None))</pre>

      <AssignmentFunctionSignature name="index" :params="[['head', 'Optional[ListNode]'], ['val', 'int']]" type="int"/>
      <p>Return the position of the ListNode containing <code>val</code>. If such a node does not exist, return <code>-1</code>.</p>
      <pre>
head = ListNode(1, ListNode(2, ListNode(3, None)))
index(head, 3) -&gt; 2</pre>

      <AssignmentFunctionSignature name="concat" :params="[['xs', 'Optional[ListNode]'], ['ys', 'Optional[ListNode]']]" type="Optional[ListNode]"/>
      <p>Return the head of a linked list that represents the concatenation of the given lists, such that <code>xs</code> comes before <code>ys</code>.</p>
      <pre>
xs = ListNode(1, ListNode(2, ListNode(3, None)))
ys = ListNode(4, ListNode(5, None))
concat(xs, ys) -&gt; ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))</pre>

      <AssignmentFunctionSignature name="sum_list" :params="[['head', 'Optional[ListNode]']]" type="int"/>
      <p>Return the sum of all integers in each ListNode in the list. If the list is empty, return <code>0</code>.</p>
      <pre>
head = ListNode(1, ListNode(2, ListNode(3, None)))
sum_list(head) -&gt; 6</pre>

      <AssignmentFunctionSignature name="exp_list" :params="[['head', 'Optional[ListNode]'], ['exp', 'int']]" type="Optional[ListNode]"/>
      <p>Return the head of a linked list in which the integer in each ListNode has been raised to the <code>exp</code> power.</p>
      <pre>
head = ListNode(1, ListNode(2, ListNode(3, None)))
exp_list(head, 3) -&gt; ListNode(1, ListNode(8, ListNode(27, None)))</pre>

      <AssignmentFunctionSignature name="fibonacci" :params="[['n', 'int']]" type="ListNode"/>
      <p>Return a the head of a linked list representing the Fibonacci Sequence up to the given number of <code>n</code> places. Each integer in this sequence is the sum of the previous two integers (except for the first two integers, 0 and 1, which are base values not derived from adding other integers). Assume <code>n</code> is non-negative; if it is zero, return an empty list.</p>
      <pre>fibonacci(5) -&gt; ListNode(0, ListNode(1, ListNode(1, ListNode(2, ListNode(3, None)))))</pre>

      <AssignmentFunctionSignature name="zip_lists" :params="[['xs', 'Optional[ListNode]'], ['ys', 'Optional[ListNode]']]" type="Optional[ListNode]"/>
      <p>Return the head of a linked list that represents the pair-wise combination of the given linked lists. If one list runs out of ListNodes, append the remainder of the other list.</p>
      <pre>
xs = ListNode(1, ListNode(2, ListNode(3, None)))
ys = ListNode(4, None)
zip_lists(xs, ys) -&gt; ListNode(1, ListNode(4, ListNode(2, ListNode(3, None))))</pre>

      <AssignmentFunctionSignature name="unzip_list" :params="[['head', 'Optional[ListNode]']]" type="Tuple[Optional[ListNode], Optional[ListNode]]"/>
      <p>Return a 2-tuple of heads of linked lists that represents the pair-wise separation of the given linked lists. This operation is the inverse of zip_lists.</p>
      <pre>
head = ListNode(1, ListNode(4, ListNode(2, ListNode(5, ListNode(3, None)))))
unzip_list(head) -&gt; (ListNode(1, ListNode(2, ListNode(3, None))), ListNode(4, ListNode(5, None)))</pre>
      <p>The return type annotation of this function indicates that the returned tuple will have exactly two values, either of which can be a ListNode or <code>None</code>.</p>
    </template>
  </Assignment>
</template>


<script>
export default {
  data:
    function () {
      return {
        name: "pset1",
        title: "Problem Set I: Linked Lists",
        files: ["pset1.py", "p1tests.py"]
      };
    }
}
</script>
