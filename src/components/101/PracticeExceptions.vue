<template>
  <Assignment :name="name" :title="title" :files="files">
    <template v-slot:description>
      <p>When an illegal operation occurs in your Python program, it raises an exception. Examples of commonly raised exceptions include a <code>NameError</code> for using an undefined variable, an <code>IndexError</code> for going outside the bounds of a sequence or a <code>TypeError</code> when a value of the wrong type is used for an operation. To prevent your program from simply crashing with a stack trace, you can instead cause it to handle the exception more gracefully with a <code>try-except</code> block.</p>
      <pre>
    try:
        x = 1 / int(input())
        print(x)
    except (ValueError, ZeroDivisionError):
        pass
</pre>
      <p>In the above example, if a user enters a zero or non-number, the program would raise a <code>ValueError</code> or <code>ZeroDivisionError</code> without proper error handling. However, since the casting operation occurs in a <code>try</code> block and has a corresponding <code>except</code> block (which, in this case, contains only the <code>pass</code> placeholder and thus does nothing) for these two error types, the program will not raise an exception.</p>

      <p>In addition to handling exceptions, Python allows you to cause exceptions to occur that might not have otherwised happened with the <code>raise</code> statement, which takes an exception name and will force that exception to be raised when that line is executed.</p>
      <pre>
    if len(n) == 0:
        raise ValueError</pre>
      <h4>Testing</h4>
      <p>Test cases for functions that raise an exception should have the following structure.</p>
      <pre>
    try:
        f(0)  # suppose TypeError should be raised when argument is 0
        assert False
    except TypeError:
        assert True</pre>
      <p>Functions that simply catch exceptions may be tested normally.</p>
    </template>

    <template v-slot:implementation>
      <p>Each of the functions below must be implemented with at least one pair of <code>try-except</code> blocks, using a specific exception type (and which may not include general exceptions such as <code>Exception</code>). For a list of built-in exceptions, see the <a target="_blank" href="https://docs.python.org/3/library/exceptions.html">documentation</a>.</p>
      <p>This assignment has strict limitations on language features to force an emphasis on try-except blocks. Do not use conditional branching (<code>if</code> statements), relational or Boolean operators, or any built-in functions <strong>except</strong> type-casting functions (e.g. <code>int</code>, <code>float</code>, <code>str</code>). For any iteration, use a <code>while</code> loop with condition <code>True</code>. Additionally, while you will have <code>assert</code> statements for your tests, do not use them in your definitions.</p>

      <FunctionSignature name="try_open" :params="[['primary', 'str'], ['secondary', 'str']]" type="Optional[List[str]]"/>
      <p>Attempt to open a file for reading using the string in the variable <code>primary</code>. If the file does not exist, attempt the same process using the string in the variable <code>secondary</code>. Return the list of strings retrieved from reading the lines of the available file. If both files do not exist, return <code>None</code>. As this function requires the <code>open</code> built-in function, do not include test cases for it in your tests file.</p>

      <FunctionSignature name="reverse" :params="[['ints', 'List[int]']]" type="List[int]"/>
      <p>Return the reversal of the given list of integers.</p>

      <FunctionSignature name="count_zeros" :params="[['ints', 'List[int]']]" type="int"/>
      <p>Return a count of the number of zeros in the given list of integers.</p>

      <FunctionSignature name="try_sqrt" :params="[['x', 'int']]" type="Optional[float]"/>
      <p>Return the square root of <code>x</code> if it is non-negative; otherwise, return <code>None</code>.</p>

      <FunctionSignature name="is_int" :params="[['x', 'Union[int, float]']]" type="bool"/>
      <p>Return <code>True</code> if <code>x</code> is of type <code>int</code> and <code>False</code> if it is of type <code>float</code> (even if its decimal component is zero, as in 1.0).</p>

      <FunctionSignature name="get_sequence_type" :params="[['sequence', 'Union[str, List[str], Tuple[str]]']]" type="str"/>
      <p>Return a string of either <code>"str"</code>, <code>"list"</code> or <code>"tuple"</code>, depending on the type of <code>sequence</code>.</p>

      <FunctionSignature name="are_same_type" :params="[['x', 'Optional[str]'], ['y', 'Optional[str]']]" type="bool"/>
      <p>Return <code>True</code> if the two arguments are of the same type (both <code>str</code> or both <code>NoneType</code>) and <code>False</code> otherwise.</p>
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
        title: "Problem Set VII: Exceptions",
        files: ["pset7.py", "p7tests.py"]
      };
    }
}
</script>
