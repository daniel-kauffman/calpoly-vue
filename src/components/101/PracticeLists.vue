<template>
  <Assignment :name="name" :title="title" :files="files">
    <template v-slot:description>
      <p>Python lists provide an easy means to contain a collection of values. These lists are <b>mutable</b>, allowing them to be changed (both size and contents) after creation. In addition, unlike arrays in some other languages, lists may be <b>heterogeneous</b>, containing values of different types (though doing so is usually not recommended).</p>

      <h4>List Operations</h4>
      <p>The following table demonstrates some common list operations. For each example, let <code>ints = [1, 2, 1]</code>. Note that <code>append</code> is faster than <code>insert</code> (for reasons to be discussed in a data structures course) and should be prioritized for use when possible.</p>
      <table>
        <thead>
          <tr>
            <th></th>
            <th></th>
            <th colspan="2">Example</th>
          </tr>
          <tr>
            <th>Operation</th>
            <th>Description</th>
            <th>Expression</th>
            <th>State of <code>ints</code></th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>+</code></td>
            <td>concatenate lists</td>
            <td><code>ints + ints -&gt; [1, 2, 1, 1, 2, 1]</code></td>
            <td>unchanged</td>
          </tr>
          <tr>
            <td><code>append</code></td>
            <td>add value to end of list</td>
            <td><code>ints.append(2)</code></td>
            <td><code>[1, 2, 1, 2]</code></td>
          </tr>
          <tr>
            <td><code>remove</code></td>
            <td>remove first instance of value from list<br/><code>ValueError</code> if absent</td>
            <td><code>ints.remove(1)</code></td>
            <td><code>[2, 1]</code></td>
          </tr>
          <tr>
            <td><code>insert</code></td>
            <td>add value <code>x</code> at index <code>i</code></td>
            <td><code>ints.insert(0, 2)</code></td>
            <td><code>[2, 1, 2, 1]</code></td>
          </tr>
          <tr>
            <td><code>pop</code></td>
            <td>remove and return value at index<br/>default is last index</td>
            <td><code>ints.pop(0) -&gt; 1</code><br/><code>ints.pop() -&gt; 1</code></td>
            <td><code>[2, 1]</code><br/><code>[1, 2]</code></td>
          </tr>
          <tr>
            <td><code>index</code></td>
            <td>return index of argument<br/><code>ValueError</code> if absent</td>
            <td><code>ints.index(1) -&gt; 0</code></td>
            <td>unchanged</td>
          </tr>
          <tr>
            <td><code>count</code></td>
            <td>return number of occurrences of value</td>
            <td><code>ints.count(1) -&gt; 2</code></td>
            <td>unchanged</td>
          </tr>
        </tbody>
      </table>
      <br/>

      <h4>Tuples</h4>
      <p>Like lists, Python tuples provide a means to store a sequence of values (also of any type). However, unlike lists (but like strings), tuples are <strong>immutable</strong>, meaning that their contents or size cannot be changed after creation. Using immutable sequence types can result in programs that are less bug-prone since you do not need to be concerned with how the sequence might get changed elsewhere in the program. Tuples also require less memory to manage (for reasons discussed in a systems programming course) and are thus more memory efficient.</p>
      <p>To create a tuple, use parentheses instead of brackets: <code>ints = (1, 2, 3)</code></p>

      <h4>List Comprehensions</h4>
      <p>List comprehensions offer a means of creating simple or complex lists with relatively few lines of code. This feature does have some limitations, and may not be used for any list that requires referencing itself (such as removing duplicates).</p>

      <p>List comprehensions often have the structure shown below (colored words represent placeholders).</p>
      <pre>values = [<span style="color: red;">value</span> for <span style="color: green;">variable</span> in <span style="color: blue;">sequence</span> if <span style="color: orange;">condition</span>]</pre>
      <p>The <span style="color: green;">variable</span> and <span style="color: blue;">sequence</span> values function just like those in a <code>for</code> statement. On each iteration of the <code>for</code> loop, <span style="color: red;">value</span> is added to the new list being created unless <span style="color: orange;">condition</span> is <code>False</code> on that iteration. The <span style="color: red;">value</span> may be any expression, including literals, arithmetic expressions, function calls, if-expressions, or even other list comprehensions. The <span style="color: orange;">condition</span> is optional, and may be omitted when <span style="color: red;">value</span> is to be added on every iteration.</p>

      <p>Without using a list comprehension, the example above would look like the following:</p>
      <pre>
values = []
for <span style="color: green;">variable</span> in <span style="color: blue;">sequence</span>:
    if <span style="color: orange;">condition</span>:
        values.append(<span style="color: red;">value</span>)</pre>

      <h4>Sequence Type Annotations</h4>
      <p>Using Python's type annotation syntax, lists can be specified as <code>List[Type]</code>, where <code>Type</code> refers to a data type, such as <code>int</code> or <code>float</code>. Multidimensional sequences require nesting these annotations; for example, a 2D list of integers would be <code>List[List[int]]</code>.</p>

      <p>To gain access to the above annotations in your program, include the following line before your function definitions:</p>
      <pre>from typing import List, Tuple</pre>
      <p>Note that <code>typing</code> is the only module for which you may use the <code>from</code> import notation in this course.</p>

      <h4>Polynomial Arithmetic</h4>
      <p>You will implement two functions that perform basic arithmetic on polynomials, such that each polynomial will be represented as a list. The values in the list will represent the coefficients of the terms whereas the indices will represent the exponents for the terms.</p>
      <p>Thus, the polynomial 2x<sup>2</sup> + 3x + 5 will be represented by the following list:</p>
      <pre>
      poly = []
      poly.append(5)
      poly.append(3)
      poly.append(2)</pre>
      <p>This list can also be created directly as follows:</p>
      <pre>
      poly = [5, 3, 2]</pre>
      <p>Notice that the term with exponent 0 is first in the list while the term with exponent 2 is last; thus, the terms in the list are in reverse order of how they are typically written in mathematics so that an element's index represents that term's exponent. You may think this mapping of a polynomial to a list is a bit odd. In fact, attributing meaning to indices of a list (and not just the values within the list) is an important skill that allows a list to be used as more than just a substitution for a bunch of variables.</p>
    </template>

    <template v-slot:implementation>
      <p>For problems that require iteration, you may use either a <code>while</code> or <code>for</code> loop. Note that most of these problems cannot be solved with list comprehensions.</p>

      <FunctionSignature name="poly_add" :params="[['poly1', 'List[int]'], ['poly2', 'List[int]']]" type="List[int]"/>
      <p>Return a list representing the sum of the given polynomials, which have the same degree (list length). This function must return a new list; do not modify the contents of the input lists.</p>

      <FunctionSignature name="poly_mul" :params="[['poly1', 'List[int]'], ['poly2', 'List[int]']]" type="List[int]"/>
      <p>Return a list representing the product of the given polynomials, which have the same degree (list length). This function must return a new list; do not modify the contents of the input lists.</p>
      <p>Polynomial multiplication is not a simple multiplication of values at the same index; instead, think of the distributive law (of which the FOIL method is a simple case). The polynomial resulting from a multiplication will, in general, be of degree greater than the arguments.</p>

      <FunctionSignature name="get_mode" :params="[['ints', 'List[int]']]" type="int"/>
      <p>Return the most common integer in the given list. If two integers are equally common, return the one that occurs left-most in the list.</p>
      <pre>get_mode([1, 2, 3, 1, 2, 3, 1]) -&gt; 1</pre>

      <FunctionSignature name="index_of_smallest" :params="[['ints', 'List[int]']]" type="int"/>
      <p>Return the index of the smallest integer in the given list. If the list is empty, return -1. If there is more than one smallest integer, return the index of the first occurrence of it (from left to right).</p>
      <pre>index_of_smallest([5, 4, 3, 2, 1]) -&gt; 4</pre>

      <FunctionSignature name="has_duplicates" :params="[['ints', 'List[int]']]" type="bool"/>
      <p>Return <code>True</code> if the given list has duplicate <strong>non-zero</strong> integers and <code>False</code> otherwise.</p>
      <pre>
has_duplicates([1, 0, 2, 0, 3]) -&gt; False
has_duplicates([1, 2, 3, 2, 4]) -&gt; True</pre>

      <FunctionSignature name="products" :params="[['int_lists', 'List[List[int]]']]" type="List[int]"/>
      <p>Return a list of integers such that each integer is the product of all integers from the corresponding inner list of the input list. If an inner list is empty, its corresponding integer is zero.</p>
      <pre>products([[1, 2, 3], [4, 5], [-10], []]) -&gt; [6, 20, -10, 0]</pre>

      <FunctionSignature name="fibonacci" :params="[['n', 'int']]" type="List[int]"/>
      <p>Return a list that represents the Fibonacci Sequence up to the given number of places. Each integer in the sequence is the sum of the previous two integers (except for the first two integers, 0 and 1, which are base values not derived from adding other integers).</p>
      <pre>fibonacci(10) -&gt; [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]</pre>

      <FunctionSignature name="geo_mean" :params="[['floats', 'List[float]']]" type="float"/>
      <p>Return the <a target="_blank" href="https://en.wikipedia.org/wiki/Geometric_mean">geometric mean</a> of the given list of real numbers, defined as the product of all <code>N</code> numbers taken to the <code>N</code>th root.</p>

      <FunctionSignature name="harmonic_mean" :params="[['floats', 'List[float]']]" type="float"/>
      <p>Return the <a target="_blank" href="https://en.wikipedia.org/wiki/Harmonic_mean">harmonic mean</a> of the given list of real numbers, defined as the reciprocal of the sum of reciprocals of the numbers, multiplied by the number of numbers. Filter out any non-positive numbers from the given list before calculating the harmonic mean.</p>

      <FunctionSignature name="nest_lists" :params="[['n', 'int']]" type="List"/>
      <p>Return a nesting of lists, in which the innermost list is empty and the number of nested lists equals the given positive integer argument.</p>
      <pre>
nest_lists(1) -&gt; []
nest_lists(2) -&gt; [[]]
nest_lists(3) -&gt; [[[]]]</pre>
      <p>Since the dimension of the list varies, use only <code>List</code> (without brackets) as the return type. (This is generally a bad annotation, but there are few options for a type in which the dimensionality varies.) You may need to set the type annotation of your list variable inside the function definition to <code>List</code> as well, as in <code>lists: List = []</code>.</p>

      <FunctionSignature name="reciprocate" :params="[['ints', 'List[int]']]" type="List[float]"/>
      <p>Return a list of the reciprocals of the integers in the given list, ignoring any zeros. This function must be defined using a single <code>return</code> statement that returns a list comprehension (in other words, do not assign the list to a variable and then return the variable). The list comprehension can span multiple lines, if needed.</p>
      <pre>
reciprocate([0, 1, 2, 4, 5]) -&gt; [1, 0.5, 0.25, 0.2]</pre>

      <FunctionSignature name="solve_bool_exp" :params="[['bool_exp', 'List[str]'], ['bools', 'Tuple[bool, bool]']]" type="bool"/>
      <p>Evaluate the given Boolean expression (represented as a list of strings) and return its true or false value. The Boolean expression is contained in <code>bool_exp</code> and has the following format, always with exactly two Boolean variables around one binary Boolean operator. There may optionally be a <code>"not"</code> string occurring before either Boolean variable.</p>
      <ol>
        <li>Optional: <code>"not"</code></li>
        <li>Boolean Variable (e.g. <code>"P"</code>)</li>
        <li>Boolean Operator: <code>"and"</code>|<code>"or"</code></li>
        <li>Optional: <code>"not"</code></li>
        <li>Boolean Variable (e.g. <code>"Q"</code>)</li>
      </ol>
      <p>The given tuple <code>bools</code> contains two Boolean literals (either of which may be <code>True</code> or <code>False</code>) and each corresponds to the value of one of the Boolean variables in the expression (the first Boolean literal corresponds to the first Boolean variable and similarly for the second).</p>
      <pre>solve_bool_exp(["not", "X", "or" , "Y"], (True, False)) -&gt; False</pre>
      <p>The above example may be interpreted as follows:</p>
      <ul>
        <li><code>X</code> is <code>True</code></li>
        <li><code>Y</code> is <code>False</code></li>
        <li><code>not X or Y</code> is <code>False</code> (the return value of the function)</li>
      </ul>
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
        name: "pset6",
        title: "Problem Set VI: Lists",
        files: ["pset6.py", "p6tests.py"]
      };
    }
}
</script>


<style scoped>
td:first-child, td:nth-child(2) {
  text-align: center;
}
th:nth-child(2), td:nth-child(2) {
  border-right: 1px solid lightgray;
}
</style>
