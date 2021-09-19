<template>
  <Assignment :name="name" :title="title" :files="files">
    <template v-slot:description>
      <p>Like branching, conditional iterative statements - or <code>while</code> loops - are another means to control the flow of execution in your program. These statements use a Boolean expression to test whether another repetition of a block of code should be performed. If this test condition is always true, the loop will never terminate (a so-called infinite loop). Thus, it is important to include code in the body of the loop that allows values used in the condition to change so that it eventually becomes false.</p>
      <p><code>while</code> loops are constructed using the keyword <code>while</code> followed by a Boolean expression. All code that is to be repeated must be indented to be included in the body of the loop.</p>
      <pre>
      while ________:
          # while loop body</pre>
      <p>When first working with <code>while</code> loops, it may be helpful to follow these steps:</p>
      <ol>
        <li>Initialize a variable to be used in the loop's condition</li>
        <li>Create a valid continuing condition using the variable</li>
        <li>Modify the variable in the loop's body to eventually make the condition false</li>
      </ol>
    </template>

    <template v-slot:implementation>
      <p>All of the following functions must be implemented with a <code>while</code> loop. Do not use the built-in <code>range</code> function.</p>

      <FunctionSignature name="all_input" type="str"/>
      <p>Repeatedly prompt the user for input until no characters are entered for a particular iteration. Return the concatenation of all characters entered. Strings can be concatenated using the <code>+</code> operator. You may want to use the built-in <code>len</code> function in the condition of the <code>while</code> loop. Since this definition uses the <code>input</code> function, do <b>not</b> write <code>assert</code> statements for it in your test suite; use the Python interpreter to test it instead.</p>

      <FunctionSignature name="mul" :params="[['x', 'int'], ['y', 'int']]" type="int"/>
      <p>Return the product of <code>x</code> multiplied by <code>y</code> without using the multiplication operator. Assume both operands are non-negative.</p>

      <FunctionSignature name="exp" :params="[['x', 'int'], ['y', 'int']]" type="int"/>
      <p>Return <code>x<sup>y</sup></code> without using the multiplication or exponentiation operators. This function must make calls to the <code>mul</code> function. Assume both operands are non-negative.</p>

      <FunctionSignature name="div" :params="[['x', 'int'], ['y', 'int']]" type="int"/>
      <p>Return the integer quotient of <code>x</code> divided by <code>y</code> without using the division or modulo (including your <code>mod</code> function) operators. Assume <code>x</code> is non-negative and <code>y</code> is positive.</p>

      <FunctionSignature name="mod" :params="[['x', 'int'], ['y', 'int']]" type="int"/>
      <p>Return the integer remainder of <code>x</code> divided by <code>y</code> without using the division (including your <code>div</code> function) or modulo operators. Assume <code>x</code> is non-negative and <code>y</code> is positive.</p>

      <FunctionSignature name="gcd" :params="[['x', 'int'], ['y', 'int']]" type="int"/>
      <p>Return the <a target="_blank" href="https://en.wikipedia.org/wiki/Greatest_common_divisor">greatest common divisor</a> of the two given positive numbers.</p>

      <FunctionSignature name="is_prime" :params="[['x', 'int']]" type="bool"/>
      <p>Return <code>True</code> if the given positive number is <a target="_blank" href="https://en.wikipedia.org/wiki/Prime_number">prime</a> and <code>False</code> otherwise.</p>

      <FunctionSignature name="sum_ints" :params="[['start', 'int'], ['stop', 'int'], ['step', 'int']]" type="int"/>
      <p>Return the sum of integers beginning at <code>start</code> (inclusive), ending at <code>stop</code> (exclusive), incrementing by <code>step</code> each iteration. Assume <code>start</code> and <code>stop</code> are non-negative and <code>step</code> is positive. If <code>stop</code> is not greater than <code>start</code>, the sum must be zero.</p>
      <p>For example, start, stop and step values of 2, 11 and 3, respectively, would add up to <code>2 + 5 + 8 = 15</code> (note that 11 is not included in the sum since the stop value is exclusive).</p>

      <FunctionSignature name="sum_mul_table" :params="[['max_int', 'int']]" type="int"/>
      <p>Return the sum of all values in the multiplication table from 1 to <code>max_int</code>.</p>
      <p>For example, if <code>max_int</code> is 5, then the multiplication table (with sum 225) would be as shown below.</p>
      <pre>
          1  2  3  4  5
          2  4  6  8 10
          3  6  9 12 15
          4  8 12 16 20
          5 10 15 20 25</pre>
      <p> This function must make calls to <code>sum_ints</code> and must be implemented with only one <code>while</code> loop (not including the loop used in the <code>sum_ints</code> function).</p>

      <FunctionSignature name="rotate_string" :params="[['chars', 'str'], ['n_rot', 'int']]" type="str"/>
      <p>Perform <code>n_rot</code> rotations of the given string, in which each rotation involves moving the final character to the initial position.</p>
      <p>Example: <code>rotate_str("computer", 5) -&gt; "putercom"</code></p>

      <FunctionSignature name="weave_strings" :params="[['s1', 'str'], ['s2', 'str']]" type="str"/>
      <p>Return a string in which the first and second characters are the first characters in <code>s1</code> and <code>s2</code>, the third and fourth characters are the second characters in <code>s1</code> and <code>s2</code>, and so on. If one string is longer than the other, its remaining characters should be added to the end.</p>
      <p>Example: <code>weave_strings("cmue", "optr") -&gt; "computer"</code><br/>
         Example: <code>weave_strings("sine", "cec") -&gt; "science"</code></p>

      <FunctionSignature name="to_pig_latin" :params="[['word', 'str']]" type="str"/>
      <p>Return the translation of the given word to Pig Latin, which has the following rules:</p>
        <ol>
          <li>If the word begins with a vowel, simply return the word appended by "YAY".</li>
          <li>If the word begins with a consonant, move ALL of the word's initial consonants to the end of the word and append it with "AY".</li>
        </ol>
      <p>For this problem, Y is not considered a vowel. Assume all characters are uppercase.</p>
      <p>Example: <code>to_pig_latin("INTEGER") -&gt; "INTEGERYAY"</code><br/>
         Example: <code>to_pig_latin("FLOAT") -&gt; "OATFLAY"</code></p>

      <FunctionSignature name="greatest_factor" :params="[['x', 'int']]" type="int"/>
      <p>Return the largest single-digit (1 through 9) <a target="_blank" href="https://en.wikipedia.org/wiki/Divisor">factor</a> of the given positive number.</p>
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
        name: "pset4",
        title: "Problem Set IV: Conditional Iteration",
        files: ["pset4.py", "p4tests.py"]
      };
    }
}
</script>
