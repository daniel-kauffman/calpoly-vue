<template>
  <Assignment :name="name" :title="title" :files="files">
    <template v-slot:description>
      <p>Boolean values can be either <code>True</code> or <code>False</code> and constitute one of the fundamental data types of many programming languages. These values are often used for the conditions of branches or loops.</p>

      <h4>Boolean Operators</h4>
      <p>Python has 3 operators that take Boolean (True or False) values as operands: <code>not</code>|<code>and</code>|<code>or</code>. Boolean operations are evaluated after both arithmetic and relational operations.</p>
      <p>The <code>not</code> operator takes one operand and negates it.</p>
      <pre>
p = True
not p      # evaluates to False
not not p  # evaluates to True</pre>
      <p>The <code>and</code> operator takes two operands and evaluates to <code>True</code> only if both operands are <code>True</code>.</p>
      <pre>
p = True
q = True
p and q      # evaluates to True
not p and q  # evaluates to False</pre>
      <p>The <code>or</code> operator also takes two operands and evaluates to <code>True</code> if either (or both) operands are <code>True</code>.</p>
      <pre>
p = True
q = True
p or q          # evaluates to True
not p or q      # evaluates to True
not p or not q  # evaluates to False</pre>
      <p>With regard to operator precedence, the unary <code>not</code> operator is evaluated first, followed by <code>and</code> and finally <code>or</code> (as a mnemonic, remember that these two binary operators evaluate in alphabetic order).</p>

      <h4>Membership Operator</h4>
      <p>Python provides the <code>in</code> operator to check whether one value is within another; the second value must be a sequence (iterable) type, such as a string or list. The expression evaluates to <code>True</code> if the first operand is contained with the second and <code>False</code> otherwise.</p>
      <pre>
"A" in "ABC" -&gt; True
"D" in "ABC" -&gt; False</pre>
      <p>Note that the membership operator is separate from the use of <code>in</code> within a <code>for</code> loop statement.</p>

      <h4>Conditional Branching</h4>
      <p>Conditional branches are one means by which you can control the flow of execution of your program. Specifically, they allow your program to make "either/or" decisions, executing a block of code based on a provided Boolean expression. Only one branch may be taken each time the branching structure is executed.</p>
      <p>Conditional statements are created using the keywords <code>if</code>, <code>elif</code>, and <code>else</code>. Each conditional statement must start with an <code>if</code> branch and can be followed by any number of <code>elif</code> branches. A final <code>else</code> branch may be added at the end as a default case.</p>
      <pre>
if x &gt; 0:
    print("x &gt; 0")
elif x &lt; 0:
    print("x &lt; 0")
else:
    print("x == 0")</pre>

      <h4>If-Expression</h4>
      <p>An if-expression (also called a ternary operation) concisely allows an expression to equal one of two possible values based on a condition.</p>
      <pre>
s = "ABC" if x &gt; 0 else "XYZ"</pre>
      <p>In this example, the variable <code>s</code> will contain <code>"ABC"</code> when <code>x</code> is positive and <code>"XYZ"</code> otherwise. Note that the variable assignment is not part of the if-expression but is often used with one. In general, if-expressions evaluate to the value before the <code>if</code> when the condition is true and the value after the <code>else</code> when the condition is false.</p>
      <p>The if-expression above is equivalent to the following code.</p>
      <pre>
if x &gt; 0:
    s = "ABC"
else:
    s = "XYZ"</pre>
      <p>Although if-expressions can nest in one another (for three or more outcomes), doing so is generally considered poor style as it reduces readability.</p>

      <h4>Functions with Optional Return Types</h4>
      <p>In Python, functions do not need to specify a return type. Thus, it is possible for the function to return different data types from different calls to that function. For example, a function used to calculate the area of a triangle could sometimes return an integer and sometimes return a float. This approach, however, is almost always bad practice, as it can become difficult to anticipate what type of value will result from a function call. The exception to this rule is the value <code>None</code>, which can sometimes make sense to return when no other value makes sense (such as when the operation would be mathematically undefined).</p>

      <p>Using Python's type annotation syntax, a type can be specified to be either something or <code>None</code> using the <code>Optional[Type]</code> annotation. For example, if a function sometimes returns a string and sometimes returns <code>None</code>, use <code>Optional[str]</code> for the return type.</p>
      <p>To gain access to the <code>Optional</code> annotation in your program, include the following line before your function definitions:</p>
      <pre>from typing import Optional</pre>
      <p>Note that <code>typing</code> is the only module for which you may use the <code>from</code> import notation in this course.</p>
    </template>

    <template v-slot:implementation>
      <h4>Branchless Functions</h4>
      <p>Implement the following functions <b>without</b> the use of any <code>if</code> statements or if-expressions.</p>

      <FunctionSignature name="is_positive" :params="[['x', 'int']]" type="bool"/>
      <p>Return <code>True</code> if the given argument is positive (zero exclusive) and <code>False</code> otherwise.</p>

      <FunctionSignature name="both_positive" :params="[['x', 'int'], ['y', 'int']]" type="bool"/>
      <p>Return <code>True</code> if both given arguments are positive and <code>False</code> otherwise. This function must call the <code>is_positive</code> function instead of reproducing its logic.</p>

      <FunctionSignature name="is_triangle" :params="[['a', 'int'], ['b', 'int'], ['c', 'int']]" type="bool"/>
      <p>Return <code>True</code> if the given line lengths are able to construct a triangle and <code>False</code> otherwise. Three lines may construct a triangle if, for all pairs of lines, their sum is greater than the length of the third line. Assume all lengths are positive.</p>

      <FunctionSignature name="is_isosceles_triangle" :params="[['a', 'int'], ['b', 'int'], ['c', 'int']]" type="bool"/>
      <p>Return <code>True</code> if the given line lengths are able to construct an isosceles triangle and <code>False</code> otherwise. An isosceles triangle is defined as a triangle having at least two sides of the same length. This function must call the <code>is_triangle</code> function to determine whether the given line lengths can form a triangle. Assume all lengths are positive.</p>

      <FunctionSignature name="is_rotation" :params="[['rotated', 'str'], ['word', 'str']]" type="bool"/>
      <p>Return <code>True</code> if <code>rotated</code> is a rotation of <code>word</code> and <code>False</code> otherwise. A string is rotated by moving its last character to the front of the string (or vice versa); this step may be performed multiple times and still be considered a rotation. Any other scrambling of the characters is not a rotation.</p>
      <p>Example: <code>is_rotation("putercom", "computer") -&gt; True</code><br/>
         Example: <code>is_rotation("computre", "computer") -&gt; False</code></p>
      <p>Hint: use Python string concatenation to join strings together (e.g. <code>"A" + "B" -&gt; "AB"</code>).</p>

      <h4>Branching Functions</h4>
      <p>Implement the following functions using <code>if</code>|<code>elif</code>|<code>else</code> statements or if-expressions (when only two outcomes are possible).</p>

      <FunctionSignature name="max_of_two" :params="[['x', 'int'], ['y', 'int']]" type="int"/>
      <p>Using an if-expression, return the largest of two given numbers, using at most two branches. If both numbers are equal, return either one. Do <b>not</b> call the built-in <code>max</code> function.</p>

      <FunctionSignature name="max_of_three" :params="[['x', 'int'], ['y', 'int'], ['z', 'int']]" type="int"/>
      <p>Return the largest of three given numbers, using at most three branches. If two or more numbers tie for largest, return any one of them. Do <b>not</b> call <code>max</code> or <code>max_of_two</code>.</p>

      <FunctionSignature name="mix_colors" :params="[['a', 'str'], ['b', 'str']]" type="str"/>
      <p>Return a string that contains the name of a color resulting from "mixing" the two given strings, each of which contains the name of a primary color (red, yellow, or blue). If both strings contain the same color, simply return that color. If two different colors are present, mix them using the following rules:</p>
      <pre>
      "red"    + "yellow" &rArr; "orange"
      "yellow" + "blue"   &rArr; "green"
      "blue"   + "red"    &rArr; "purple"</pre>

      <FunctionSignature name="find_discriminant" :params="[['a', 'int'], ['b', 'int'], ['c', 'int']]" type="float?"/>
      <p>Return the result of calculating the discriminant as part of the <a target="_blank" href="https://en.wikipedia.org/wiki/Quadratic_formula">quadratic formula</a>. (The discriminant is the portion of the formula inside the square root operation, not including the square root operation.) Return <code>None</code> if the discriminant is negative.</p>

      <FunctionSignature name="solve_poly" :params="[['a', 'int'], ['b', 'int'], ['c', 'int']]" type="float?"/>
      <p>Return the result of calculating the quadratic formula for only the <code>+</code> value of the <code>±</code> operation. Return <code>None</code> if the discriminant is negative. This function must call <code>find_discriminant</code> instead of reproducing its logic.</p>
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
        name: "pset3",
        title: "Problem Set III: Booleans & Branching",
        files: ["pset3.py", "p3tests.py"]
      };
    }
}
</script>
