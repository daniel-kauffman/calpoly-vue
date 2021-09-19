<template>
  <Assignment :name="name" :title="title" :files="files">
    <template v-slot:description>
      <p>Stacks are a fundamental data structure that support the following two operations:</p>
      <ul>
        <li><code>push</code>: add an item to the top of the stack</li>
        <li><code>pop</code>: remove the top-most item from the stack</li>
      </ul>
      <p>Because only the top item is ever accessed, each operation runs in <code>O(1)</code> constant time, meaning that the time it takes to perform the operation is independent of the size of the stack.</p>
      <p>Stacks have many applications in computer science, including the evaluation of arithmetic expressions and the management of function calls in memory.</p>
    </template>

    <template v-slot:implementation>
      <p>Only the <code>push</code> and <code>pop</code> functions may access the <code>ref</code> attribute of a <code>StackNode</code>; all other functions must call <code>push</code> and <code>pop</code> to modify a stack.</p>

      <FunctionSignature name="push" :params="[['top', 'Optional[StackNode]'], ['new', 'StackNode']]" type="StackNode"/>
      <p>Add the given new <code>StackNode</code> to the top of the stack and return a reference to it. Assume the new <code>StackNode</code>'s ref attribute is <code>None</code>.</p>
      <pre>
top = StackNode(2, StackNode(3, None))
push(top, StackNode(1, None)) -&gt; StackNode(1, StackNode(2, StackNode(3, None)))</pre>

      <FunctionSignature name="pop" :params="[['top', 'Optional[StackNode]']]" type="Tuple[StackNode, Optional[StackNode]]"/>
      <p>Remove the <code>StackNode</code> at the top of the stack and return the popped <code>StackNode</code> (with its ref set to <code>None</code>) and the reference to the new top of the stack. If the stack is initially empty, raise a <code>ValueError</code>.</p>
      <pre>
top = StackNode(1, StackNode(2, StackNode(3, None)))
pop(top) -&gt; (StackNode(1, None), StackNode(2, StackNode(3, None)))</pre>

      <FunctionSignature name="move" :params="[['xs', 'Optional[StackNode]'], ['ys', 'Optional[StackNode]']]" type="Tuple[Optional[StackNode], StackNode]"/>
      <p>Pop the top <code>StackNode</code> from <code>xs</code> and push it to <code>ys</code>. Return references to the tops of both stacks.</p>
      <pre>
xs = StackNode(1, StackNode(2, StackNode(3, None)))
ys = None
move(xs, ys) -&gt; (StackNode(2, StackNode(3, None)), StackNode(1, None))</pre>

      <FunctionSignature name="flip_stack" :params="[['top', 'Optional[StackNode]']]" type="Optional[StackNode]"/>
      <p>Return the reversal of the given stack by creating an empty stack and moving StackNodes onto it.</p>
      <pre>
top = StackNode(1, StackNode(2, StackNode(3, None)))
flip_stack(top) -&gt; StackNode(3, StackNode(2, StackNode(1, None)))</pre>

      <FunctionSignature name="concat" :params="[['xs', 'Optional[StackNode]'], ['ys', 'Optional[StackNode]']]" type="Optional[StackNode]"/>
      <p>Return the top of a stack that represents the concatenation of the given stacks, such that <code>xs</code> comes before <code>ys</code>.</p>
      <pre>
xs = StackNode(1, StackNode(2, StackNode(3, None)))
ys = StackNode(4, StackNode(5, None))
concat(xs, ys) -&gt; StackNode(1, StackNode(2, StackNode(3, StackNode(4, StackNode(5, None)))))</pre>

      <FunctionSignature name="pop_all" :params="[['top', 'Optional[StackNode]'], ['val', 'int']]" type="Optional[StackNode]"/>
      <p>Return a stack with all StackNodes containing the given integer value removed from the given stack.</p>
      <pre>
top = StackNode(1, StackNode(2, StackNode(1, StackNode(3, None))))
pop_all(top, 1) -&gt; StackNode(2, StackNode(3, None))</pre>

      <FunctionSignature name="zip_stacks" :params="[['xs', 'Optional[StackNode]'], ['ys', 'Optional[StackNode]']]" type="Optional[StackNode]"/>
      <p>Return the top of a stack that represents the pair-wise combination of the given stacks. If one stack runs out of StackNodes, append the remainder of the other stack.</p>
      <pre>
xs = StackNode(1, StackNode(2, StackNode(3, None)))
ys = StackNode(4, None)
zip_stacks(xs, ys) -&gt; StackNode(1, StackNode(4, StackNode(2, StackNode(3, None))))</pre>

      <FunctionSignature name="unzip_stack" :params="[['top', 'Optional[StackNode]']]" type="Tuple[Optional[StackNode], Optional[StackNode]]"/>
      <p>Return a 2-tuple of tops of stacks that represents the pair-wise separation of the given stacks. This operation is the inverse of zip_stacks.</p>
      <pre>
top = StackNode(1, StackNode(4, StackNode(2, StackNode(5, StackNode(3, None)))))
unzip_stack(top) -&gt; (StackNode(1, StackNode(2, StackNode(3, None))), StackNode(4, StackNode(5, None)))</pre>

      <FunctionSignature name="sort_stack" :params="[['top', 'Optional[StackNode]']]" type="Optional[StackNode]"/>
      <p>Return a stack in with the StackNodes from the given stack are sorted in ascending order by their integer values.</p>
      <p>It is recommended to create two empty stacks: one to which StackNodes are temporarily moved, and another to store the sorted StackNodes.</p>
      <pre>
top = StackNode(5, StackNode(2, StackNode(8, None)))
sort_stack(top) -&gt; StackNode(2, StackNode(5, StackNode(8, None)))</pre>
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
        name: "pset2",
        title: "Problem Set II: Stacks",
        files: ["pset2.py", "p2tests.py"]
      };
    }
}
</script>
