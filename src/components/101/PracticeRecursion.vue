<template>
  <Assignment :name="name" :title="title" :files="files">
    <template v-slot:description>
      <p>What is recursion? Recursion is defined by the definition of recursion. While somewhat unsatisfying, this definition illustrates the basic idea: a recursive function definition is one that calls the function it defines.</p>
      <p>A concept this abstract is best understood with an example (test cases in <span style="color: green;">green</span>):</p>

      <pre>
      def reverse(ints):<span style="color: red;">
          if len(ints) == 0:
              return []</span>
          <span style="color: blue;">return reverse(ints[1:]) + ints[:1]</span>
      <span style="color: green;">
      reverse([])         # returns []
      reverse([1])        # returns [1]
      reverse([1, 2, 3])  # returns [3, 2, 1]</span></pre>

      <p>Although this function definition is only 4 lines, there is a deep and fascinating process embedded in this code. The input argument <code>ints</code> is a list of integers that are to be reversed. However, what if this list was empty? What should the function return in this case? An empty list seems most appropriate, so the first two lines of the function body (highlighted in <span style="color: red;">red</span>) check for this condition; this branch is called the <strong>base case</strong>.</p>
      <p>The final line of the function is the most dense but notice that there are no new language features. The + operator is being used for list concatenation, rather than addition. The right operand is a slice of the <code>ints</code> list which is equivalent to <code>[ints[0]]</code> (recall that slicing a list always results in a list, even if that list only has zero or one elements). The left operand is the recursive call, which is passed a list of all but the first element of the original list. This line (highlighted in <span style="color: blue;">blue</span>) is the <strong>recursive case</strong>.</p>
      <p>To further illustrate the process, the following lines go through the recursive steps, starting with the top-most function call in <span style="color: red;">red</span>. Since the base case is not used until the last recursive call, it is de-emphasized in <span style="color: gray;">gray</span>. It is perhaps easiest to trace the recursion from the bottom, starting with the function call in <span style="color: purple;">purple</span>. In this case, the input argument is the empty list and the base condition is true, resulting in an empty list. Since the <span style="color: purple;">purple</span> call returned <code>[]</code>, the <span style="color: blue;">blue</span> recursive call will return <code>[] + [3]</code> which simply equals <code>[3]</code>. This process continues back to the top-most function call returning <code>[3, 2, 1]</code>.</p>

      <pre><span style="color: red;">
      reverse([1, 2, 3])</span><span style="color: gray;">
          if len([1, 2, 3]) == 0:
              return []</span>
          return <span style="color: green;">reverse([2, 3])</span> + [1]   # return [3, 2] + [1]
      <span style="color: green;">
      reverse([2, 3])</span><span style="color: gray;">
          if len([2, 3]) == 0:
              return []</span>
          return <span style="color: blue;">reverse([3])</span> + [2]      # return [3] + [2]
      <span style="color: blue;">
      reverse([3])</span><span style="color: gray;">
          if len([3]) == 0:
              return []</span>
          return <span style="color: purple;">reverse([])</span> + [3]       # return [] + [3]
      <span style="color: purple;">
      reverse([])</span>
          if len([]) == 0:
              return []<span style="color: gray;">
          return reverse([]) + []</span></pre>

      <p>Importantly, notice that the base case does not make a recursive call. What would happen had there been no base case? Each recursive call would continue to make a subsequent call to reverse indefinitely; this bug is referred to as <strong>infinite recursion</strong>. Like an infinite loop, infinite recursion stems from a lack of sufficient checks to halt the endless repetition of code execution. Unlike an infinite loop, however, there is a limit to the number of recursive calls a computer can make and thus the program will usually halt without requiring user intervention.</p>
    </template>

    <template v-slot:implementation>
      <p>All functions must use recursion. Do not use any iteration or slicing.</p>

      <FunctionSignature name="reverse_string" :params="[['chars', 'str'], ['index', 'int']]" type="str"/>
      <p>Return the reverse of the given string. Use the <code>index</code> argument to keep track of position, which starts at zero.</p>

      <FunctionSignature name="is_palindrome" :params="[['chars', 'str'], ['index', 'int']]" type="bool"/>
      <p>Return True if the given string is a palindrome and False otherwise. A palindrome is a symmetric sequence of characters, reading the same forward and backward. Use the <code>index</code> argument to keep track of position, which starts at zero. Do not call reverse_string.</p>

      <FunctionSignature name="find_max" :params="[['ints', 'List[int]'], ['index', 'int']]" type="int"/>
      <p>Return the highest number in the list of integers. Use the <code>index</code> argument to keep track of position, which starts at zero.</p>

      <FunctionSignature name="mul" :params="[['x', 'int'], ['y', 'int']]" type="int"/>
      <p>Return the product of <code>x</code> multiplied by <code>y</code> without using the multiplication operator. Assume both operands are non-negative.</p>

      <FunctionSignature name="exp" :params="[['x', 'int'], ['y', 'int']]" type="int"/>
      <p>Return <code>x<sup>y</sup></code> without using the multiplication or exponentiation operators, instead making calls to the <code>mul</code> function. Assume both operands are non-negative.</p>

      <FunctionSignature name="factorial" :params="[['n', 'int']]" type="int"/>
      <p>Return <code>n!</code> without using the multiplication operator, instead making calls to the <code>mul</code> function. Assume the argument is non-negative. This function should be able to handle arguments as high as 20 within one second.</p>

      <FunctionSignature name="fibonacci" :params="[['n', 'int'], ['acc', 'Tuple[int]']]" type="int"/>
      <p>Return the Fibonacci value at the position of the given argument. Use the <code>acc</code> argument to keep track of previous Fibonacci values, which starts with (0, 1). This function should be able to handle arguments as high as 90 within one second. Do not use more than one recursive call in the same recursive case, as doing so will be very inefficient. Note that the Fibonacci value at position zero is zero.</p>

      <FunctionSignature name="binary_search" :params="[['ints', 'List[int]'], ['n', 'int'], ['start', 'int'], ['end', 'int']]" type="int"/>
      <p>Using binary search, return the index of the given integer or -1 if it is not in the list. Use the <code>start</code> and <code>end</code> arguments to keep track of the region of the list to consider, which start at zero and <code>len(ints)</code>, respectively.</p>

      <ClassDefinition name="NestingDoll">
        <FunctionSignature name="__init__" :params="[['self', 'NestingDoll'], ['count', 'int']]"/>
        <p>Representation of a nesting (Matryoshka) doll, with <code>count</code> specifying how many dolls are nested inside. Each <code>NestingDoll</code> should have exactly one attribute, <code>inner</code>, which is either a <code>NestingDoll</code> or, if it is the innermost doll, <code>None</code>. Do not add an attribute for the <code>count</code> parameter.</p>

        <FunctionSignature name="__eq__" :params="[['self', 'NestingDoll'], ['other', 'NestingDoll']]" type="bool"/>
        <p>Return True if both <code>NestingDoll</code> objects have the same number of nested dolls and False otherwise.</p>

        <FunctionSignature name="__repr__" :params="[['self', 'NestingDoll']]" type="str"/>
        <p>Return a string representing the structure of the <code>NestingDoll</code>, using nested parentheses for each outer doll and <code>8</code> (the number eight) for the innermost doll.</p>
        <p>For example, a doll with three levels of nesting (including itself) would be <code>"((8))"</code>.</p>
      </ClassDefinition>
    </template>
  </Assignment>
</template>


<script>
import Assignment from "@/components/BaseAssignment.vue"
import ClassDefinition from "@/components/AssignmentClassDefinition.vue"
import FunctionSignature from "@/components/AssignmentFunctionSignature.vue"


export default {
  components: {
    Assignment,
    ClassDefinition,
    FunctionSignature
  },
  data:
    function () {
      return {
        name: "psetc",
        title: "Problem Set XII: Recursion",
        files: ["psetc.py", "pctests.py"]
      };
    }
}
</script>
