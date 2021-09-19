<template>
  <Assignment :name="name" :title="title" :files="files">
    <template v-slot:description>
      <p>Regular expressions are patterns used with strings to determine whether some or all of the string matches the pattern. They are very useful in parsing out information from a large collection of text when it is known that the information conforms to a particular structure (for example, HTML).</p>

      <p>In this assignment, you will write regular expressions that will be used to determine whether some text conforms to a particular pattern. All regular expressions should be made from Python raw strings, which can be made by placing an <code>r</code> immediately before the opening quote, as in <code>r"..."</code>. Note that no knowledge of the <code>re</code> module will be necessary; only the construction of regular expressions will be required.</p>

      <p>The following tables highlight the primary components of regular expressions; additional components will not be necessary for this assignment. Use of <code>...</code> represents any character(s) and is not an actual part of a regular expression. The examples demonstrate how <code>re.search</code> would be called with a regular expression and a string to search (in that order), as well as the string that the function would return; however, in your implementation, you need only return the regular expression in each function.</p>

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
      <p style="color: red;">Important: While you may help one another in understanding how various regular expression components are used with your own examples, please do not share any parts of the solutions to each problem.</p>
      <p>A <code>search</code> function is provided in <code>p8tests.py</code>, which you must use to test the functions below for accuracy. See the test file for some examples. No use of the <code>re</code> module beyond this provided function will be necessary.</p>

      <p>Note that a long string may span multiple lines using parentheses and concatentation:</p>
      <pre>
pattern = (r"..."
           + r"...")</pre>

      <FunctionSignature name="parse_term" type="str"/>
      <p>Return a regular expression to match a valid quarter system term, which is one of Fall/Winter/Spring/Summer, followed by a space and a year, which may be in the format <code>YYYY</code> or <code>'YY</code>, as in <code>Fall '20</code>.</p>

      <FunctionSignature name="parse_time" type="str"/>
      <p>Return a regular expression to match a valid time, which may be formatted as <code>HH:MM</code> or <code>HH:MM:SS</code> and may optionally have AM/PM at the end (for 12-hour time), as in <code>12:01:59PM</code>.</p>

      <FunctionSignature name="parse_date" type="str"/>
      <p>Return a regular expression to match a valid date, which may be formatted using <code>/</code> notation as <code>DD/MM/YYYY</code>, though <code>-</code> may be used instead of <code>/</code>, and the year may be expressed with only the final two digits. A date may also be expressed in long form, as in <code>January 1, 2020</code>, where the year (and the comma that precedes it) is optional.</p>

      <FunctionSignature name="parse_name" type="str"/>
      <p>Return a regular expression to match a valid name, which must contain at least two capitalized words. A middle name may be provided and can either be in full or abbreviated with <code>.</code>, as in <code>Samuel L. Jackson</code>. The first name may also be abbreviated, as in <code>B. D. Wong</code>, and the last name may contain a hyphen, as in <code>Alexandria Ocasio-Cortez</code>. The name may optionally end in a <a target="_blank" href="https://en.wikipedia.org/wiki/Roman_numerals">Roman numeral</a>, as in <code>John Paul II</code>, going no higher than <code>VIII</code>.</p>

      <FunctionSignature name="parse_math" type="str"/>
      <p>Return a regular expression to match a valid binary arithmetic operation, which must include two operands and one binary operator, as in <code>12 + 34.5</code>. The operands may be numbers (integers or floats) or variables (which are alphanumeric and may include underscores), as in <code>a_b // -z0</code>. Spaces may or may not be included between operands and operators.</p>
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
        name: "pset8",
        title: "Problem Set VIII: Regular Expressions",
        files: ["pset8.py", "p8tests.py"]
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
