<template>
  <div>
    <h1>Style Requirements</h1>
    <hr />

    <h2>Automatically Verified</h2>
    <p>All submissions must pass the automated style check to receive any credit.</p>

    <h4>Language Features</h4>

    <div v-if="course === 101 || course === 202">
      <p>Only use Python language features or algorithms discussed in lecture and permitted for the assignment.</p>
      <p>The following language features will never be allowed. Note that this list is not exhaustive.</p>
      <ul>
        <li>Slicing</li>
        <li>Dictionaries and sets</li>
        <li>Lambda expressions</li>
      </ul>
      <p>In addition, Python lists will not be permitted for many assignments. This restriction exists to require the use of other data structures.</p>
    </div>
    <p v-else>Only use Python modules permitted on the spec for each assignment. As this course emphasizes learning algorithms and not Python itself, very few modules will be made available for assignments.</p>

    <h4>Header</h4>
    <p>All submitted files must include a heading at the very top with the following format (which you may copy to your files):</p>
    <pre>
# Name: 
# Course: 
# Instructor: 
# Assignment: 
# Term: 
    </pre>
    <p>Example:</p>
    <pre>
# Name: Edward Wong Hau Pepelu Tivruski IV
# Course: CPE 101
# Instructor: Daniel Kauffman
# Assignment: Moonlander
# Term: Fall 2071
    </pre>

    <h4>File and Function Names</h4>
    <p>The following items must have names that match those stated in a specification:</p>
      <ul>
        <li>File names</li>
        <li>Function and class names</li>
      </ul>
    <p>Do not name variables, functions, or classes after already existing built-in functions.</p>

    <h4>Line Length</h4>
    <p>All lines of code must be under 80 characters. If a line is too long, it may span across multiple lines using parentheses or the escape <code>\</code> character.</p>

    <h4>Function Length</h4>
    <p>Function definitions must contain no more statements than 30 statements. (A statement, unlike an expression, typically has no value, and includes variable assignment, <code>return</code>, <code>if</code>, <code>while</code>/<code>for</code>, and <code>try</code>/<code>except</code>.) Functions exceeding the limit must be decomposed into 2 or more smaller functions.</p>
    <p>Do not use semi-colons <code>;</code> to put multiple statements on a single line.</p>

    <h4>Spacing</h4>
    <p>Spaces must be placed after commas and around operators. At least two empty lines must exist between function or class definitions.</p>

    <h4>Indentation</h4>
    <p>Use 4 spaces for indentation. Do not use tabs; your editor should have a way to convert tabs to spaces so that you can continue using the tab key for convenience. In addition, use indentation for all code blocks, including functions, conditional statements, and loops, even when Python does not require it.</p>

    <h4>Global Code</h4>
    <p>Any code that is not within a function definition is global and not permitted. If a value is required by multiple functions, it should be passed in as an argument. Class static variables similarly should not be used.</p>

    <h4>Importing Modules</h4>
    <p>Only use regular <code>import</code> statements to import a module, as in <code>import math</code>. To avoid <a target="_blank" href="https://en.wikipedia.org/wiki/Name_collision">name collision</a>, do not use the <code>from ... import ...</code> syntax (except for the <code>typing</code> module).</p>
    <p>All import statements must be at the top of each file, just below the header.</p>

    <h4>Type Annotations</h4>
    <p>All function headers must have complete type annotations for each parameter, as well as a return type. Variables do not need to be annotated. Type annotations are a relatively new Python feature that make code more clear. (Note that Python is a dynamically typed language and does not perform static type checking on its own; you may use <a target="_blank" href="http://mypy-lang.org/">MyPy</a> for this purpose.)</p>
    <p>Primitive types can be annotated without importing a module. These types are:</p>
    <pre>bool, int, float, str, None</pre>
    <p>More complex types require importing the <code>typing</code> module. This is the only module that should be imported using the <code>from ... import ...</code> notation, as in:</p>
    <pre>from typing import List, Tuple</pre>
    <p>The following annotations are permitted:</p>
    <pre>Callable, Dict, FrozenSet, Iterator, List, Match, Optional, Tuple, Set, Union</pre>
    <p>For a helpful guide to Python type annotations, see the MyPy cheat sheet: <a target="_blank" href="https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html">https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html</a>.</p>

    <h4>Boolean Brevity</h4>
    <p>Do not compare Boolean expressions to True or False.</p>
    <ul>
      <li style="color: red;">Bad style:</li>
      <pre>  if is_valid == True:</pre>
      <li style="color: green;">Good style:</li>
      <pre>  if is_valid:</pre>
    </ul>
    <ul>
      <li style="color: red;">Bad style:</li>
      <pre>  if is_valid == False:</pre>
      <li style="color: green;">Good style:</li>
      <pre>  if not is_valid:</pre>
    </ul>
    <p>Do not write conditional branches that simply return True and False if they can be condensed into a single line.</p>
    <ul>
      <li style="color: red;">Bad style:</li>
      <pre>
  if is_valid:
      return True
  else:
      return False</pre>
      <li style="color: green;">Good style:</li>
      <pre>  return is_valid</pre>
    </ul>

    <h4>Error Handling</h4>
    <p>All <code>except</code> blocks must specify the error(s) being handled, which must derive from the <code>Exception</code> class. Catch-all <code>except</code> blocks are not permitted. Do not use parentheses after the name of the error being raised.</p>

    <h4>Instance Variables</h4>
    <p>All instance variables must be initialized in a constructor (but may be updated in other methods).</p>

    <h4>Returned Types</h4>
    <p>Functions should consistently return one data type. For example, if a function can return a float, it should always do so. NoneType is excluded from this restriction; thus, it's acceptable for a function to sometimes return, say, a string and at other times None.</p>

    <hr />
    <h2>Verify Manually</h2>

    <h4>Variable Initialization</h4>
    <p>Use null-like values (e.g. <code>0</code>, <code>""</code>, <code>[]</code>, <code>None</code>) to initialize a variable if its desired value is not yet known. Do not use strange placeholder values like <code>" "</code> or <code>9999</code>.</p>

    <h4>Variable and Added Function Names</h4>
    <p>Use descriptive names for variables and any functions added outside those required by the specification. Single-letter variable names are usually bad, whereas <code>moon_gravity</code> is easy to understand. In loops, it is acceptable to use <code>i</code>, <code>j</code>, <code>k</code> for index variables.</p>
    <p>When decomposing a function (e.g. <code>blur</code>), give the helper function(s) meaningful names that describe what they do, not which function they derive from (in other words, do not name it <code>blur_helper</code> or <code>blur_2</code>).</p>

    <h4>I/O Operations</h4>
    <p>Only perform input and output (I/O) operations, such as <code>input</code> and <code>print</code>, in main or in functions specifically designed to do I/O. Logical functions (those that calculate) should not do any I/O. Using <code>print</code> in logical functions for debugging is encouraged but should be removed prior to submission.</p>

    <h4>Magic Numbers</h4>
    <p>A number that is used on its own rather than being assigned to a variable is considered magic; in other words, its meaning is made more difficult to infer because it has no name. Instead, store the number in a well-named variable, even if that variable is only used once. The commonly used integers -1, 0, 1, 2 are exempt from this rule.</p>

    <h4>Side Effects and Mutation</h4>
    <p>Side effects, especially mutation of arguments, should be minimized as much as is feasible unless it significantly impacts performance. Unless the structure is very large, function arguments should be copied locally before being modified, after which the function should return the modified copy.</p>

    <h4>Repeated Code</h4>
    <p>Do not write multiple lines of similar code that can be condensed into a few lines within a loop. If a block of code is necessary in multiple places, it should be made into a function that is called multiple times.</p>

    <hr />
    <h2>Additionally...</h2>
    <p>Never try to excuse bad style by saying, "But it works!"</p>
  </div>
</template>


<style scoped>
h4 {
  margin-left: 1em;
}
li, p {
  margin-left: 1.5em;
}
pre {
  margin-left: 1.8em;
}
</style>


<script>
export default {
  props: {
    course: Number
  }
}
</script>
