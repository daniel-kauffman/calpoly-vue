<template>
  <Assignment :name="name" :title="title" :files="files">
    <template v-slot:description>
      <p>In Python, <code>for</code> loops offer a convenient means to iterate over a sequence of values, guaranteeing that each value in the sequence will be iterated on exactly once. While the types of sequences used are typically strings or lists, the <code>range</code> function is often used to provide a simple sequence of integers over which the <code>for</code> loop can iterate.</p>

      <p><code>for</code> loops are constructed using the keywords <code>for</code> and <code>in</code> with a variable to initialize and sequence to iterate over. All code that is to be repeated must be indented to be included in the body of the loop.</p>
      <pre>
      for &lt;variable&gt; in &lt;sequence&gt;:
          # for loop body</pre>

      <h4>ASCII Character Set</h4>
      <p>ASCII characters are represented in a machine as a single byte, which is a sequence of 8 bits. Each bit (or "binary digit") has a value of either 0 or 1. Thus, since each bit can hold one of two values and there are 8 such values in a byte, the number of possible values a byte can store is 2<sup>8</sup> or 256. As the English language comprises far fewer symbols than 256 (including numbers and punctuation), it is possible to store each character in English in a byte.</p>
      <table>
        <tr><td>Bit</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td></tr>
        <tr><td>Position</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr>
      </table>
      <br/>

      <p>The bits displayed above represent the number 65, which, in ASCII, is the character "A". This number can be found by adding all 2<sup>p</sup>, where <code>p</code> refers to any position in the byte for which the value is one. In the above example, 2<sup>0</sup> + 2<sup>6</sup> which equals 1 + 64 or 65.</p>
      <p>In Python, a character's ASCII number can be obtained using the <code>ord</code> function, which takes a one-character string and returns an integer. The reverse process, obtaining a character from a valid ASCII number, is provided by the <code>chr</code> function.</p>
      <pre>
      ord("A") -&gt; 65</pre>
      <pre>
      chr(65) -&gt; "A"</pre>
    </template>

    <template v-slot:implementation>
      <p>All of the following functions must be implemented with a <code>for</code> loop. Do not use lists, tuples, or slicing.</p>
      <p>For any problem requiring ASCII encodings, <span style="color: red;">do not consult an ASCII table for the encodings</span>; use the <code>ord</code> function instead. Use of literal ASCII codes (such as <code>65</code>) in a solution detracts from its readability and may result in receiving no credit for that problem.</p>

      <h4>Rangeless Functions</h4>
      <p>Implement the following functions without the <code>range</code> function.</p>

      <FunctionSignature name="reverse_string" :params="[['chars', 'str']]" type="str"/>
      <p>Return the reverse of the given string.</p>

      <FunctionSignature name="translate_string" :params="[['chars', 'str'], ['old', 'str'], ['new', 'str']]" type="str"/>
      <p>Return a string where each occurrence of character <code>old</code> is replaced with character <code>new</code> and all other characters are left unchanged. Assume that <code>old</code> and <code>new</code> are single-character strings. Do not use any built-in string functions with similar behavior, such as <code>str.replace</code>.</p>
      <p>Example: <code>translate_string("I LOVE 101", "O", "I") -&gt; "I LIVE 101"</code></p>

      <FunctionSignature name="rotate_chars" :params="[['chars', 'str'], ['n_pos', 'int']]" type="str"/>
      <p>Return the rotation of the given characters, such that each character is replaced by the character that follows <code>n_pos</code> positions in the alphabet, wrapping around to the beginning of the alphabet when reaching the end. For example, if <code>n_pos</code> is 13, "a" becomes "n", "b" becomes "o", "N" becomes "A", etc. Non-alphabetic characters should be left unchanged. Moreover, the rotation is only within the characters of the same case, such that a lowercase letter always rotates to a lower case letter and likewise for uppercase letters.</p>

      <FunctionSignature name="encode_ascii" :params="[['chars', 'str']]" type="str"/>
      <p>Return a string containing the encodings of every character in the given string. Each character encoding should be represented as three digit characters; if the actual encoding is shorter than three digits (such as <code>65</code> for <code>A</code>), pad the encoding with zeros to make it three digits (as in <code>"065"</code>).</p>
      <p>Example: <code>encode_ascii("ABC") -&gt; "065066067"</code></p>
      <p>Use of Python f-strings is recommended. Values can be zero-padded by including a <code>0</code> before the width option. If a variable named <code>code</code> contained an integer ASCII code, the f-string would look like <code>f"{code:03}"</code>.</p>

      <FunctionSignature name="parse_word" :params="[['words', 'str'], ['position', 'int']]" type="str"/>
      <p>Given a string of space-separated words, return a string containing only the word at the specified position, with the first word in the string at position zero. If there are not enough words to support the given position, return an empty string.</p>
      <p>Example: <code>parse_word("COMPUTER SCIENCE", 0) -&gt; "COMPUTER"</code></p>
      <p>Example: <code>parse_word("COMPUTER SCIENCE", 1) -&gt; "SCIENCE"</code></p>
      <p>You may use the string function <code>count</code> to determine how many words are in the string.</p>
      <pre>
"BOOLEAN".count("O") -&gt; 2</pre>

      <h4>Range Functions</h4>
      <p>Implement the following functions using the <code>range</code> function.</p>

      <FunctionSignature name="swap_chars" :params="[['chars', 'str']]" type="str"/>
      <p>Return a string in which each pair of adjacent characters in the given string have switched positions. If the number of characters in the string is odd, leave the position of the final character unchanged.</p>
      <p>Example: <code>swap_chars("AaBbCcD") -&gt; "aAbBcCD"</code></p>

      <FunctionSignature name="is_palindrome" :params="[['word', 'str']]" type="bool"/>
      <p>Return True if the given string is a palindrome and False otherwise. A palindrome is a symmetric sequence of characters, reading the same forward and backward (e.g. <code>"racecar"</code> or <code>"tacocat"</code>).</p>

      <FunctionSignature name="decode_ascii" :params="[['chars', 'str']]" type="str"/>
      <p>Given a string of three-digit ASCII encodings (as returned by <code>encode_ascii</code>), return a string of the original characters.</p>
      <p>Example: <code>decode_ascii("065066067") -&gt; "ABC"</code></p>

      <FunctionSignature name="make_substring" :params="[['chars', 'str'], ['start', 'int'], ['stop', 'int'], ['step', 'int']]" type="str"/>
      <p>Return a substring of the given string that begins at the start index (inclusive) and ends at the stop index (exclusive), increasing step characters each iteration. Assume start and stop are non-negative and step is positive.</p>
      <p>Example: <code>make_substring("COMPUTER", 0, 10, 3) -&gt; "CPE"</code></p>

      <FunctionSignature name="longest_substring" :params="[['s1', 'str'], ['s2', 'str']]" type="str"/>
      <p>Return the longest substring that exists in both the given strings. A substring only exists in both given strings if its characters occur with the same adjacency and order. If no common substring exists, return an empty string. This definition must make calls to <code>make_substring</code> (using a <code>step</code> value of <code>1</code>).</p>
      <p>A naive solution would be to generate every possible substring of <code>s1</code> and <code>s2</code> and track the longest matching substring; however, this approach would be very inefficient. Instead, generate every possible substring of either <code>s1</code> or <code>s2</code> and determine whether it exists in the other string.</p>

      <FunctionSignature name="transpose_string" :params="[['chars', 'str'], ['width', 'int']]" type="str"/>
      <p>Return a transposition of <code>chars</code>, using <code>width</code> as the initial number of characters per row. Transposing a two-dimensional grid means converting its rows to columns and its columns to rows. Since strings are one-dimensional, the result will be a string with its characters shifted around.</p>
      <p>As an example, suppose the given string is <code>"ABCDEFGHI"</code> and the width is <code>3</code>. The one-dimensional string could be thought of as a two-dimensional grid (matrix) like the following:</p>
      <pre>
ABC
DEF
GHI</pre>
      <p>Its two-dimensional transposition would then be:</p>
      <pre>
ADG
BEH
CFI</pre>
      <p>Thus, the result of the transposition as returned by this function would be <code>"ADGBEHCFI"</code>.</p>
      <p>Do not assume that the length of the string is <code>width<sup>2</sup></code>; however, you may assume that the length is divisible by the <code>width</code>.</p>
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
        name: "pset5",
        title: "Problem Set V: Sequential Iteration",
        files: ["pset5.py", "p5tests.py"]
      };
    }
}
</script>
