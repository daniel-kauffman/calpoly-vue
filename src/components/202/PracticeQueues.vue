<template>
  <Assignment :name="name" :title="title" :files="files">
    <template v-slot:description>
      <p>Standard queues are a simple First In First Out (FIFO) abstract data type that support the enqueueing of items and dequeueing them in the order they entered. The front of a queue is typically referred to its head, and the end the queue its tail; items can only be added at the tail and removed at the head. These queues are thus similar to stacks in that the point of entry and exit is fixed.</p>
      <p>Variations of queues exist that differ in how and which items dequeue first. In a double-ended queue, or deque (pronounced "deck"), items can be enqueued or dequeued from the head or the tail (but not from the middle). This modification offers additional flexibility when such is desired, but in many cases (like file access or <a target="_blank" href="https://en.wikipedia.org/wiki/Inter-process_communication">inter-process communication</a>), it may not be.</p>
      <p>Another common queue type is a priority queue, in which items are dequeued in order based on some measure of priority that is determined in advance. Uses for priority queues include building <a target="_blank" href="https://en.wikipedia.org/wiki/Huffman_coding">Huffman trees</a>, <a target="_blank" href="https://en.wikipedia.org/wiki/Scheduling_(computing)">process scheduling</a>, as well as many kinds of <a target="_blank" href="https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)">graph</a> problems. Priority queues are often implemented using a heap data structure, which efficiently restructures itself whenever an item is added or removed.</p>
      <h4>Heaps</h4>
      <p>A heap is a (typically binary) tree data structure in which two properties must always hold. The Shape Property requires that every level be complete - meaning every parent has exactly two children - before another level can be added to the tree. The requirements for the Heap Property depend on the type of heap; in a max heap, the value stored in every parent node must be greater than the values stored in its child nodes (with the opposite being true for a min heap). Thus, a max heap may look like the following:</p>
      <pre>
     6
   /   \
  3     5
 / \   /
1   2 4</pre>
      <p>Because heaps are complete binary trees, they may also be represented using a 1D list of values, which is much more memory-efficient than using a node-like data structure, and allows constant-time access of any value by simply indexing on the list.</p>
      <table>
        <tr>
          <td>Value</td>
          <td>6</td>
          <td>3</td>
          <td>5</td>
          <td>1</td>
          <td>2</td>
          <td>4</td>
        </tr>
        <tr>
          <td>Index</td>
          <td>0</td>
          <td>1</td>
          <td>2</td>
          <td>3</td>
          <td>4</td>
          <td>5</td>
        </tr>
      </table>
      <p>In this representation, the parent of any (non-root) node can be found by taking the floor of half of one less its index: <code>&#x230A;(i - 1) / 2&#x230B;</code>. For example, the value at index <code>5</code> would have its parent value at index <code>2</code>. Furthermore, the left and right children of a node can be found at indices <code>2i + 1</code> and <code>2i + 2</code>, respectively.</p>

    </template>

    <template v-slot:implementation>
      <p>Only use Python lists for the heap functions.</p>
      <ClassDefinition name="Queue">
        <p>Only methods of the <code>Queue</code> class (not functions defined outside the class) may access a ListNode's <code>ref</code> attribute.</p>

        <FunctionSignature name="__init__" :params="[['self'], ['head', 'Optional[ListNode]']]"/>
        <p>An instance of Queue has two attributes.</p>
        <ul>
          <li><code>head</code>: A reference to the first <code>ListNode</code> in the queue.</li>
          <li><code>tail</code>: A reference to the final <code>ListNode</code> in the queue.</li>
        </ul>
        <pre>
queue = Queue(ListNode(1, ListNode(2, ListNode(3, None))))
queue.head -&gt; ListNode(1, ListNode(2, ListNode(3, None)))
queue.tail -&gt; ListNode(3, None)</pre>

        <FunctionSignature name="__eq__" :params="[['self'], ['other', 'Optional[\'Queue\']']]" type="bool"/>
        <p>Return True if both Queue objects maintain references to the same sequence of <code>ListNode</code> objects and False otherwise.</p>
        <pre>
qx = Queue(ListNode(1, ListNode(2, ListNode(3, None))))
qy = Queue(ListNode(1, ListNode(2, ListNode(3, None))))
qz = Queue(ListNode(3, ListNode(2, ListNode(1, None))))
qx == qy -&gt; True
qx == qz -&gt; False</pre>

        <FunctionSignature name="enqueue" :params="[['self'], ['val', 'int']]"/>
        <p>Add the given integer as a <code>ListNode</code> to the tail of the queue. This function mutates the calling Queue object in-place and does not return a value.</p>

        <pre>
queue = Queue(ListNode(1, ListNode(2, None)))
queue.enqueue(3)
queue.head -&gt; ListNode(1, ListNode(2, ListNode(3, None)))
queue.tail -&gt; ListNode(3, None)</pre>

        <FunctionSignature name="dequeue" :params="[['self']]" type="ListNode"/>
        <p>Remove the <code>ListNode</code> at the head of the queue and return it with its reference set to None. If the queue is empty, raise a <code>ValueError</code>. This function mutates the calling Queue object.</p>
        <pre>
queue = Queue(ListNode(1, ListNode(2, ListNode(3, None))))
queue.dequeue() -&gt; ListNode(1, None)
queue.head -&gt; ListNode(2, ListNode(3, None))
queue.tail -&gt; ListNode(3, None)</pre>
      </ClassDefinition>

      <FunctionSignature name="size" :params="[['queue', 'Queue']]" type="int"/>
      <p>Return the number of <code>ListNodes</code> in the given queue. The queue must contain its original <code>ListNodes</code> in the same order at the end of the procedure.</p>
      <pre>
queue = Queue(ListNode(1, ListNode(2, ListNode(3, None))))
size(queue) -&gt; 3</pre>

      <FunctionSignature name="dequeue_all" :params="[['queue', 'Queue'], ['val', 'int']]" type="int"/>
      <p>Using dequeue and enqueue operations, remove all <code>ListNodes</code> from the queue that contain the given integer value and return the number of nodes removed.  All other <code>ListNodes</code> must be in the queue in their original order at the end of the procedure.</p>
      <pre>
queue = Queue(ListNode(1, ListNode(2, ListNode(1, ListNode(3, None)))))
dequeue_all(queue, 1) -&gt; 2
queue.head &gt; ListNode(2, ListNode(3, None))</pre>

      <FunctionSignature name="flip" :params="[['queue', 'Queue']]"/>
      <p>Reverse the <code>ListNodes</code> of the calling <code>Queue</code> such that the original tail node becomes the head and vice versa, using the enqueue and dequeue methods. This function mutates the calling <code>Queue</code> object.</p>
      <pre>
queue = Queue(ListNode(1, ListNode(2, ListNode(3, None))))
flip(queue)
queue.head -&gt; ListNode(3, ListNode(2, ListNode(1, None)))
queue.tail -&gt; ListNode(1, None)</pre>

      <h4>Heaps</h4>
      <p>The following functions use a Python list to represent a binary heap. As these heaps represent priority queues (not FIFO queues), the <code>Queue</code> class should not be used.</p>

      <FunctionSignature name="sift_up" :params="[['heap', 'List[int]'], ['index', 'int']]" type="List[int]"/>
      <p>Return a max-heap that has undergone a sift-up operation for the value at the given index.</p>
      <pre>sift_up([7, 6, 5, 4, 3, 2, 8], 6) -&gt; [8, 6, 7, 4, 3, 2, 5]</pre>

      <FunctionSignature name="sift_down" :params="[['heap', 'List[int]'], ['index', 'int']]" type="List[int]"/>
      <p>Return a max-heap in which the root of a subtree at the given index has been sifted down (if necessary) to maintain the Heap Property.</p>
      <pre>sift_down([1, 7, 6, 5, 4, 3, 2], 0) -&gt; [7, 5, 6, 1, 4, 3, 2]</pre>

      <FunctionSignature name="heapify" :params="[['ints', 'List[int]']]" type="List[int]"/>
      <p>Return a max-heap (represented as a list of integers) created using the given integers. This function must using sifting instead of insert to run in linear (instead of log-linear) time.</p>
      <pre>heapify([1, 2, 3, 4, 5, 6, 7]) -&gt; [7, 5, 6, 4, 2, 1, 3]</pre>

      <FunctionSignature name="insert" :params="[['heap', 'List[int]'], ['val', 'int']]" type="List[int]"/>
      <p>Return a max-heap with the given value added, using the sift-up operation to restore the Heap Property as necessary.</p>
      <pre>insert([6, 5, 4, 3, 2, 1], 7) -&gt; [7, 5, 6, 3, 2, 1, 4]</pre>

      <FunctionSignature name="remove" :params="[['heap', 'List[int]']]" type="Tuple[int, List[int]]"/>
      <p>Return a tuple containing the removed value (previously at the root of the max-heap) along with the updated max-heap, using the sift-down operation to restore the Heap Property as necessary. If the heap is empty, raise a <code>ValueError</code>.</p>
      <pre>remove([7, 6, 5, 4, 3, 2, 1]) -&gt; (7, [6, 4, 5, 1, 3, 2])</pre>

    </template>
  </Assignment>
</template>


<script>
import Assignment from "@/components/BaseAssignment.vue"
import FunctionSignature from "@/components/AssignmentFunctionSignature.vue"
import ClassDefinition from "@/components/AssignmentClassDefinition.vue"


export default {
  components: {
    Assignment,
    ClassDefinition,
    FunctionSignature
  },
  data:
    function () {
      return {
        name: "pset5",
        title: "Problem Set V: Queues",
        files: ["pset5.py", "p5tests.py"]
      };
    }
}
</script>


<style scoped>
table {
  margin: 1em 0em 1em 0em;
}
td:first-child {
  font-weight: bold;
}
</style>
