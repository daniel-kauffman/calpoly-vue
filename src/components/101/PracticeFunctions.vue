<template>
  <Assignment :name="name" :title="title" :files="files">
    <template v-slot:description>
      <p>Functions are one of the most import building blocks of a program, which:</p>
      <ul>
        <li>Provide an easy means of reusing segments of code</li>
        <li>Allow the programmer to encapsulate parts of long programs</li>
        <li>Simplify testing and debugging by allowing the programmer to focus on one area</li>
      </ul>

      <h4>Function Calls</h4>
      <p>A function can be <strong>called</strong> by referencing its name along with a parenthesized list of arguments (if any). Functions can be called any number of times; however, calls must occur after the function's definition (or associated <code>import</code> statement, as described in the testing section).</p>
      <p>The following code shows 3 calls for a function <code>add_one</code>, which is a very simple function that simply evaluates to its argument plus one.</p>
      <pre>
      add_one(0)   # evaluates to 1
      add_one(1)   # evaluates to 2
      add_one(99)  # evaluates to 100</pre>
      <p>Typically, the result of a function call will be stored in a variable.</p>
      <pre>
      number = add_one(9)                    # number contains 10</pre>
      <p>Since a function call is itself a value (the value that it returns), it can also be used as an argument to another function call.</p>
      <pre>
      number = add_one(add_one(1))           # number contains 3
      number = add_one(add_one(add_one(1)))  # number contains 4</pre>

      <h4>Function Definitions</h4>
      <p>In Python, functions are <strong>defined</strong> using the <code>def</code> keyword. A function is only ever defined <strong>once</strong> for a program.</p>
      <p>Function definitions are composed of a header and a body. The header includes the name of the function and its parameters, which are the variable names to use for the arguments that will be passed in when the function is called. The body makes up all the lines of code that will run when the function is called; it must be indented and may be composed of one or more lines.</p>
      <pre>
      def add_one(x):   # header
          return x + 1  # body</pre>
      <p>The body will almost always contain one or more <code>return</code> statements, which determine the value of a function call. A function will immediately stop when it reaches a <code>return</code> statement. (Multiple <code>return</code> statements only make sense in the context of conditional execution, as described in a later assignment.) A Python function call that completes without encountering a <code>return</code> statement will evaluate to <code>None</code> by default.</p>

      <h4>Type Annotations</h4>
      <p>As of Python 3.5, function headers may also include parameter and return type annotations to make it clear what data types are input and output by the function. If the <code>add_one</code> function was meant to receive an integer argument and return an integer result, its type-annotated header would be the following:</p>
      <pre>
      def add_one(x: int) -&gt; int:</pre>
      <p>Python is a <a target="_blank" href="https://en.wikipedia.org/wiki/Type_system#Dynamic_type_checking_and_runtime_type_information">dynamically-typed</a> language, meaning that data types used in the program are not known to be correct until the program is already running (in contrast to a <a target="_blank" href="https://en.wikipedia.org/wiki/Type_system#Static_type_checking">statically-typed</a> language). The benefit of dynamic typing is less code and more flexibility, at the cost of less error checking by a compiler and the potential for more bugs.</p>
      <p>To aid your learning and help you detect bugs early, all functions headers in this and future assignments must have correct type annotations. With some exceptions, variables will not require type annotations.</p>
      <p>The following is a list of the type annotations for the types discussed thus far.</p>
      <ul>
        <li><code>bool</code></li>
        <li><code>int</code></li>
        <li><code>float</code></li>
        <li><code>str</code></li>
        <li><code>None</code></li>
      </ul>

      <h4>Testing</h4>
      <p>You are required to write tests for every function implemented. Tests must be written using <code>assert</code> statements, which are composed of the reserved word <code>assert</code> followed by some expression. When this expression evaluates to <code>True</code>, the program continues to the next line; otherwise, an <code>AssertionError</code> is raised and the program terminates.</p>
      <p>In the following example, several lines are executed until one of the expressions following <code>assert</code> evaluates to <code>False</code>, causing an <code>AssertionError</code> that terminates the program. The <code>==</code> operator checks for the equality of its operands.</p>
      <pre>
      assert True
      assert not False
      assert 1 == 1
      assert add_one(1) == 2
      assert add_one(2) == 4  # AssertionError raised
      assert add_one(3) == 4  # line not reached</pre>
      <p>In the preceding case, the cause of the test failure was a bad test; in other words, the expected value should have been <code>3</code> instead of <code>4</code>. However, the usual cause of a test failure is a bug in the function definition, which may have remained unknown to the developer without a comprehensive test suite.</p>
      <p>Tests are typically written in a separate file (known in Python as a module). To access function definitions from another module, they must be imported into the test module. Thus, if the <code>add_one</code> function is defined in a <code>defs.py</code>, it can be imported and used as in the following example.</p>
      <pre>
      import defs                  # do not include ".py" extension of file name

      assert defs.add_one(1) == 2  # each call must be preceded by module name (e.g. "defs.")
      assert defs.add_one(2) == 3
      assert defs.add_one(3) == 4</pre>
      <p>A test module can be run just like any other Python module. If the above file was named <code>tests.py</code>, it could be run with the following command:</p>
      <pre>
      python3 tests.py</pre>
      <p>If an <code>AssertionError</code> is displayed, it means one of the tests failed; otherwise, all executed tests passed.</p>

      <p>As a software engineer, it is <strong>strongly</strong> recommended that, when possible, you practice test-driven development (TDD). This practice entails writing tests <strong>before</strong> writing the function definitions for those tests. In doing so, you will have a better understanding as to what the functions take as input and produce as output, which makes writing the function definition easier.</p>
    </template>

    <template v-slot:implementation>
      <FunctionSignature name="print_hello" :params="[['name', 'str']]"/>
      <p>Given a string <code>name</code>, display the message <samp>"Hello " + name</samp>. This function should not have a return statement but will still require test cases.</p>

      <FunctionSignature name="get_numbers" type="int"/>
      <p>Prompt the user twice for an integer and return the sum of these numbers. This function must <strong>not</strong> have a test case. (Consider why a test case would be difficult to use.) Instead, you should test this function using the Python interpreter.</p>
      <pre>
      python3
      &gt;&gt;&gt; import pset2
      &gt;&gt;&gt; pset2.get_numbers()</pre>

      <FunctionSignature name="exp" :params="[['x', 'int'], ['y', 'int']]" type="int"/>
      <p>Return <code>x<sup>y</sup></code>, without using the assignment <code>=</code> operator. (This restriction demonstrates that you can return expressions and do not need to first assign values to variables before returning them.)</p>

      <FunctionSignature name="sum_to" :params="[['n', 'int']]" type="float"/>
      <p>Return the sum of all integers from <code>1</code> to <code>n</code>, using the closed form of the <a target="_blank" href="https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF">infinite series of natural numbers</a>.</p>

      <FunctionSignature name="get_hypotenuse" :params="[['a', 'int'], ['b', 'int']]" type="float"/>
      <p>Given two arguments corresponding to the lengths of the sides adjacent to the right angle of a triangle, return the hypotenuse of the triangle using the <a target="_blank" href="https://en.wikipedia.org/wiki/Pythagorean_theorem">Pythagorean theorem</a>. To perform the square root operation, you may take a value to its ½ power.</p>

      <FunctionSignature name="get_distance" :params="[['x1', 'int'], ['y1', 'int'], ['x2', 'int'], ['y2', 'int']]" type="float"/>
      <p>Return the <a target="_blank" href="https://en.wikipedia.org/wiki/Euclidean_distance#Two_dimensions">Euclidean distance</a> between points <code>(x<sub>1</sub>, y<sub>1</sub>)</code> and <code>(x<sub>2</sub>, y<sub>2</sub>)</code>. Do not rewrite the Pythagorean Theorem; instead, this function <strong>must</strong> make a call to <code>get_hypotenuse</code>.</p>

      <FunctionSignature name="get_perimeter" :params="[['x1', 'int'], ['y1', 'int'], ['x2', 'int'], ['y2', 'int'], ['x3', 'int'], ['y3', 'int']]" type="float"/>
      <p>Return the perimeter of a triangle with points at <code>(x<sub>1</sub>, y<sub>1</sub>)</code>, <code>(x<sub>2</sub>, y<sub>2</sub>)</code> and <code>(x<sub>3</sub>, y<sub>3</sub>)</code>. Do not rewrite the distance formula; instead, this function <strong>must</strong> make calls to <code>get_distance</code>.</p>

      <FunctionSignature name="round_to_hundredths" :params="[['x', 'float']]" type="float"/>
      <p>Return the result of rounding the given number to the hundredths place. This function must not use any built-in functions, including <code>int</code> or <code>round</code>. Assume that the given number is non-negative.</p>
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
        title: "Problem Set II: Functions & Testing",
        files: ["pset2.py", "p2tests.py"]
      };
    }
}
</script>
