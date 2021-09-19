<template>
  <Assignment :name="name" :title="title" :files="files">
    <template v-slot:description>
      <p>What is recursion? Recursion is defined by the definition of recursion. While somewhat unsatisfying, this definition illustrates the basic idea: a recursive function definition is one that calls the function it defines.</p>
      <p>A concept this abstract is best understood with an example (test cases in <span style="color: green;">green</span>):</p>

      <pre>
      def sum_to(n: int) -&gt; int:<span style="color: red;">
          if n == 0:
              return 0</span>
          <span style="color: blue;">return n + sum_to(n - 1)</span>
      <span style="color: green;">
      sum_to(0)       # returns 0
      sum_to(3)       # returns 6
      sum_to(10)      # returns 55</span></pre>

      <p>Although this function definition is only 4 lines, there is a deep and fascinating process embedded in this code. The argument <code>n</code> is an integer up to which all integers starting from 1 must be added. However, what if this number is zero? What should the function return in this case? Zero seems most appropriate, so the first two lines of the function body (highlighted in <span style="color: red;">red</span>) check for this condition; this branch is called the <strong>base case</strong>.</p>
      <p>The final line of the function is the most dense but notice that there are no new language features. Here, the given integer is added to the result of a recursive call, which itself is passed <code>n - 1</code>. This line (highlighted in <span style="color: blue;">blue</span>) is the <strong>recursive case</strong>. Importantly, each recursive call must receive its arguments in such a way that eventually one recursive call will result in the base case being true.</p>
      <p>To further illustrate the process, the following lines go through the recursive steps, starting with the top-most function call in <span style="color: red;">red</span>. Since the base case is not used until the last recursive call, it is de-emphasized in <span style="color: gray;">gray</span>. It is perhaps easiest to trace the recursion from the bottom, starting with the function call in <span style="color: purple;">purple</span>. In this case, the argument is zero and the base condition is true, resulting in zero. Since the <span style="color: purple;">purple</span> call returned <code>0</code>, the <span style="color: blue;">blue</span> recursive call will return <code>1 + 0</code> which simply equals <code>1</code>. This process continues back to the top-most function call returning <code>6</code>.</p>

      <pre><span style="color: red;">
      sum_to(3)</span><span style="color: gray;">
          if 3 == 0:
              return 0</span>
          return 3 + <span style="color: green;">sum_to(2)</span>    # return 3 + <span style="color: green;">3</span>
      <span style="color: green;">
      sum_to(2)</span><span style="color: gray;">
          if 2 == 0:
              return 0</span>
          return 2 + <span style="color: blue;">sum_to(1)</span>    # return 2 + <span style="color: blue;">1</span>
      <span style="color: blue;">
      sum_to(1)</span><span style="color: gray;">
          if 1 == 0:
              return 0</span>
          return 1 + <span style="color: purple;">sum_to(0)</span>    # return 1 + <span style="color: purple;">0</span>
      <span style="color: purple;">
      sum_to(0)</span>
          if 0 == 0:
              return 0            # return 0<span style="color: gray;">
          return 0 + sum_to(-1)</span></pre>

      <p>Notice that the base case does not make a recursive call. What would happen had there been no base case? Each recursive call would continue to make a subsequent call to reverse indefinitely; this bug is referred to as <strong>infinite recursion</strong>. Like an infinite loop, infinite recursion stems from a lack of sufficient checks to halt the endless repetition of code execution. Unlike an infinite loop, however, there is a limit to the number of recursive calls a computer can make and thus the program will usually halt without requiring user intervention.</p>
    </template>

    <template v-slot:implementation>
      <p>All functions must use recursion; do not use any iteration (<code>while</code> or <code>for</code> loops). Do not use any Python lists.</p>

      <FunctionSignature name="mul" :params="[['x', 'int'], ['y', 'int']]" type="int"/>
      <p>Return the product of <code>x</code> and <code>y</code> without using the multiplication operator.</p>
      <pre>mul(-2, -3) -&gt; 6</pre>

      <FunctionSignature name="exp" :params="[['x', 'int'], ['y', 'int']]" type="int"/>
      <p>Return <code>x<sup>y</sup></code> without using the multiplication or exponentiation operators, instead making calls to the <code>mul</code> function. Assume <code>y</code> is non-negative.</p>
      <p>If you receive a <code>RecursionError</code> even for relatively small numbers, consider how <code>mul</code> is called in this function: which argument, <code>x</code> or <code>y</code>, determines how many recursive calls <code>mul</code> will make, and how can changing how <code>mul</code> is called reduce the number of those recursive calls?</p>
      <pre>exp(-2, 3) -&gt; -8</pre>

      <FunctionSignature name="fac" :params="[['n', 'int']]" type="int"/>
      <p>Return <code>n!</code> without using the multiplication operator, instead making calls to the <code>mul</code> function. Assume <code>n</code> is non-negative. This function should be able to handle arguments as high as 20 within one second.</p>
      <p>As with <code>exp</code>, if you receive a <code>RecursionError</code> even for relatively small numbers, consider changing how <code>mul</code> is called to reduce the number of recursive calls it makes.</p>
      <pre>fac(5) -&gt; 120</pre>

      <FunctionSignature name="fibonacci" :params="[['n', 'int'], ['a', 'int'], ['b', 'int']]" type="int"/>
      <p>Return an integer representing the Fibonacci Sequence at the given <code>n</code>th position. Each integer in this sequence is the sum of the previous two integers (except for the first two integers, 0 and 1, which are base values not derived from adding other integers). Assume <code>n</code> is positive.</p>
      <p>Use the a and b parameters to keep track of the previous two values in the sequence. These two values should always start as 0 and 1, respectively. This function should be able to handle arguments as high as 90 within one second. Do not use more than one recursive call in the same recursive case, as doing so will be very inefficient.</p>
      <pre>fibonacci(8, 0, 1) -&gt; 13</pre>

      <FunctionSignature name="make_substring" :params="[['chars', 'str'], ['start', 'int'], ['stop', 'int'], ['step', 'int']]" type="str"/>
      <p>Return a substring of the given string that begins at the start index (inclusive) and ends at the stop index (exclusive), increasing step characters each iteration. Assume start and stop are non-negative and step is positive.</p>
      <pre>make_substring("COMPUTER", 0, 10, 3) -&gt; "CPE"</pre>

      <FunctionSignature name="is_palindrome" :params="[['chars', 'str']]" type="bool"/>
      <p>Return True if the given string is a palindrome and False otherwise. A palindrome is a symmetric sequence of characters, reading the same forward and backward. Use make_substring to modify the string for each recursive call.</p>
      <pre>
is_palindrome("tacocat") -&gt; True
is_palindrome("palindrome") -&gt; False</pre>

      <FunctionSignature name="swap_chars" :params="[['chars', 'str']]" type="str"/>
      <p>Return a string in which each pair of adjacent characters in the given string have switched positions. If the number of characters in the string is odd, leave the position of the final character unchanged. Use make_substring to modify the string on each recursive call.</p>
      <pre>swap_chars("AaBbCcD") -&gt; "aAbBcCD"</pre>

      <FunctionSignature name="length" :params="[['head', 'Optional[Node]']]" type="int"/>
      <p>Return the number of nodes in the given linked list.</p>
      <pre>length(ListNode(1, ListNode(2, ListNode(3, None)))) -&gt; 3</pre>

      <FunctionSignature name="find_max" :params="[['head', 'Optional[Node]']]" type="int"/>
      <p>Return the highest integer in the given linked list. Assume the linked list is not empty.</p>
      <pre>find_max(ListNode(2, ListNode(3, ListNode(4, ListNode(1, None))))) -&gt; 4</pre>

      <FunctionSignature name="reverse" :params="[['head', 'Optional[Node]'], ['acc', 'Optional[Node]']]" type="Optional[Node]"/>
      <p>Return the reverse of the given linked list.</p>
      <p>Use the accumulator to build the reversed list as an argument to the recusive calls, instead of building the reversed list after each recursive call returns.</p>
      <pre>reverse(Node(1, Node(2, Node(3, None))), None) -&gt; Node(3, Node(2, Node(1, None)))</pre>

      <ClassDefinition name="NestingDoll">
        <FunctionSignature name="__init__" :params="[['self', 'NestingDoll'], ['count', 'int']]"/>
        <p>Representation of a nesting (Matryoshka) doll, with <code>count</code> specifying how many dolls are to be created. Each <code>NestingDoll</code> should have exactly one attribute, <code>inner</code>, which is either a <code>NestingDoll</code> or, if it is the innermost doll, <code>None</code>. Do not add an attribute for the <code>count</code> parameter.</p>
        <pre>
doll = NestingDoll(3)
doll.inner.inner.inner == None -&gt; True</pre>

        <FunctionSignature name="__eq__" :params="[['self', 'NestingDoll'], ['other', 'NestingDoll']]" type="bool"/>
        <p>Return True if both <code>NestingDoll</code> objects have the same number of nested dolls and False otherwise.</p>
        <p>When comparing an object to <code>None</code> inside its own <code>__eq__</code> method, use the <code>is</code>/<code>is not</code> operators instead of <code>==</code>/<code>!=</code>, as in <code>if self.inner is None:</code>.</p>
        <pre>
NestingDoll(1) == NestingDoll(1) -&gt; True
NestingDoll(1) == NestingDoll(2) -&gt; False</pre>

        <FunctionSignature name="__repr__" :params="[['self', 'NestingDoll']]" type="str"/>
        <p>Return a string representing the structure of the <code>NestingDoll</code>, using nested parentheses for each outer doll and <code>8</code> (the number eight) for the innermost doll.</p>
        <pre>str(NestingDoll(3)) -&gt; "((8))"</pre>
      </ClassDefinition>
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
        name: "pset3",
        title: "Problem Set III: Recursion",
        files: ["pset3.py", "p3tests.py"]
      };
    }
}
</script>
