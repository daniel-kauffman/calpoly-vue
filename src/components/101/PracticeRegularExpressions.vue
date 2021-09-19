<template>
  <Assignment :name="name" :title="title" :files="files">
    <template v-slot:description>
      <p>Regular expressions are patterns used with strings to determine whether some or all of the string matches the pattern. They are very useful in parsing out information from a large collection of text when it is known that the information conforms to a particular structure (for example, HTML).</p>
      <p>In this assignment, you will use the <code>search</code> function of the <code>re</code> module to find which sections of a string conform to certain criteria using patterns that you create. This function is called as <code>re.search(pattern, text)</code> where <code>pattern</code> contains a regular expression and <code>text</code> is any string. All patterns should use Python raw strings, which can be made by placing an <code>r</code> immediately before the opening quote, as in <code>r"..."</code>.</p>
      <p>The following tables highlight the primary components of regular expressions; additional components will not be necessary for this assignment. Use of <code>...</code> represents any character(s) and is not an actual part of a regular expression.</p>

      <table>
        <thead>
          <tr>
            <th>Component</th>
            <th>Description</th>
            <th>Example</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>.</code></td>
            <td>any character</td>
            <td><code>re.search(r".", "!") -&gt; "!"</code></td>
          </tr>
          <tr>
            <td><code>[...]</code></td>
            <td>any one of <code>...</code></td>
            <td><code>re.search(r"[a-z]", "123abc") -&gt; "a"</code></td>
          </tr>
          <tr>
            <td><code>[^...]</code></td>
            <td>not any one of <code>...</code></td>
            <td><code>re.search(r"[^a-z]", "abcXYZ") -&gt; "X"</code></td>
          </tr>
          <tr>
            <td><code>P|Q</code></td>
            <td>either pattern <code>P</code> or pattern <code>Q</code></td>
            <td><code>re.search(r"ABC|xyz", "abcxyz") -&gt; "xyz"</code></td>
          </tr>
          <tr>
            <td><code>(...)</code></td>
            <td>override precedence</td>
            <td><code>re.search(r"(abc){2}", "abcabc") -&gt; "abcabc"</code></td>
          </tr>
          <tr>
            <td><code>...*</code></td>
            <td>0 or more <code>...</code></td>
            <td><code>re.search(r"az*", "a") -&gt; "a"</code></td>
          </tr>
          <tr>
            <td><code>...+</code></td>
            <td>1 or more <code>...</code></td>
            <td><code>re.search(r"a+", "aabaaaa") -&gt; "aa"</code></td>
          </tr>
          <tr>
            <td><code>...?</code></td>
            <td>0 or 1 <code>...</code></td>
            <td><code>re.search(r"ab?", "a") -&gt; "a"</code></td>
          </tr>
          <tr>
            <td><code>...{m}</code></td>
            <td><code>...</code> occurs <code>m</code> times</td>
            <td><code>re.search(r"a{2}", "aaaa") -&gt; "aa"</code></td>
          </tr>
        </tbody>
      </table>
    </template>

    <template v-slot:implementation>
      <p>For each problem, use <code>re.search</code> to find the relevant section of the text matching the pattern. To obtain the actual string that was matched from the text, simply call the <code>m.group()</code> method, where <code>m</code> is the <code>Match</code> object returned by <code>re.search</code>.</p>

      <FunctionSignature name="parse_term" :params="[['text', 'str']]" type="str"/>
      <p>Return the substring containing a valid quarter system term, which is one of Fall/Winter/Spring/Summer, followed by a space and a year, which may be in the format <code>YYYY</code> or <code>'YY</code>, as in <code>Fall '20</code>.</p>

      <FunctionSignature name="parse_time" :params="[['text', 'str']]" type="str"/>
      <p>Return the substring containing a valid time, which may be formatted as <code>HH:MM</code> or <code>HH:MM:SS</code> and may optionally have AM/PM at the end (for 12-hour time), as in <code>12:01:59PM</code>.</p>

      <FunctionSignature name="parse_name" :params="[['text', 'str']]" type="str"/>
      <p>Return the substring containing a valid name, which must contain at least two capitalized words. A middle name may be provided and can either be in full or abbreviated with <code>.</code>, as in <code>Samuel L. Jackson</code>. The first name may also be abbreviated, as in <code>B. D. Wong</code>, and the last name may contain a hyphen, as in <code>Alexandria Ocasio-Cortez</code>. The name may optionally end in a <a target="_blank" href="https://en.wikipedia.org/wiki/Roman_numerals">Roman numeral</a>, as in <code>John Paul II</code>, going no higher than <code>VIII</code>.</p>

      <FunctionSignature name="parse_math" :params="[['text', 'str']]" type="str"/>
      <p>Return the substring containing a valid binary arithmetic operation, which must include two operands and one binary operator, as in <code>12 + 34.5</code>. The operands may be numbers (integers or floats) or variables (which are alphanumeric and may include underscores), as in <code>a_b // z0</code>. Spaces may or may not be included between operands and operators.</p>
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
        name: "psetb",
        title: "Problem Set XI: Regular Expressions",
        files: ["psetb.py", "pbtests.py"]
      };
    }
}
</script>


<style scoped>
table {
  margin-bottom: 1em;
}
tr td:first-child {
  text-align: center;
}
</style>
