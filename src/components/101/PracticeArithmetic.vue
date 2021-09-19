<template>
  <Assignment :name="name" :title="title" :files="files">
    <template v-slot:description>
      <p>In this assignment, requesting a number involves calling the <code>input</code> function to prompt the user for a number; <strong>assume the user will always enter a valid number, as defined by each problem</strong>. Because the <code>input</code> function always returns strings, these values will need to be converted to integers prior to arithmetic evaluation. At the end of each problem, use the <code>print</code> function to display the result <strong>as an integer</strong>.</p>
      <p>Importantly, to help the auto-grader distinguish between prompts and printed results, be sure that every prompt string ends with a space, as in <samp>"Choose a number: "</samp>.</p>
      <p>The following table lists all built-in functions necessary for this assignment.</p>
      <table>
        <thead>
          <tr>
            <th>Function</th>
            <th>Description</th>
            <th>Example</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>input</code></td>
            <td>request value</td>
            <td><code>input("Name: ")</code></td>
          </tr>
          <tr>
            <td><code>print</code></td>
            <td>display value</td>
            <td><code>print("Hello!")</code></td>
          </tr>
          <tr>
            <td><code>int</code></td>
            <td>convert to integer</td>
            <td><code>int("10")</code> &rArr; <samp>10</samp></td>
          </tr>
          <tr>
            <td><code>min</code></td>
            <td>get smaller of two values</td>
            <td><code>min(1, 2)</code> &rArr; <samp>1</samp></td>
          </tr>
          <tr>
            <td><code>max</code></td>
            <td>get larger of two values</td>
            <td><code>max(1, 2)</code> &rArr; <samp>2</samp></td>
          </tr>
        </tbody>
      </table>
      <br/>
      <p>Each problem must be solved using <strong>only arithmetic operations and the permitted built-in functions</strong>. Do not use loops, string indexing, or any other operations not discussed in lecture.</p>
      <p>The math tricks used for these problems were written by <a target="_blank" href="https://www.math.hmc.edu/~benjamin/">Arthur Benjamin</a> of Harvey Mudd College. For each problem, any valid input will always produce the same answer.</p>
    </template>

    <template v-slot:implementation>
      <p>Each problem below starts with its function's <strong>header</strong>, which incidates the parameters and return type of the function, both of which will be discussed later. For this assignment, as each function's header is already provided for you in the starter file, begin each problem by simply removing the keyword <code>pass</code> and writing your solution. (The <code>pass</code> serves as a placeholder and is only initially necessary because Python does not allow a function definition to be empty.)</p>
      <FunctionSignature name="problem_1"/>
      <p>Request a number from 1 to 20. Double it, add 10, divide by 2, and then subtract the original number.</p>

      <FunctionSignature name="problem_2"/>
      <p>Request any two numbers, storing each in a variable. Add those numbers and store this sum in a third variable. Add the second input number and the previous sum and store this new sum in a fourth variable. Continue this process of adding the most recent two variables until you have 10 variables total, including the initial two. Now add up the 10 variables and divide by the number in the 7th variable.</p>

      <FunctionSignature name="problem_3"/>
      <p>Request one four-digit number, such that each digit is different. Without requesting another number, create a new number with the first and last digits of the previous number swapped. Subtract the smaller number from the larger and add together the digits of the resulting number, then add this new number's two digits together (if the sum is only one digit, zero can be added).</p>

      <FunctionSignature name="problem_4"/>
      <p>Request a number from 1 to 50 that is not divisible by 7 and then divide it by 7. Now add up the first six digits after the decimal point.</p>
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
        name: "pset1",
        title: "Problem Set I: Arithmetic Operations",
        files: ["pset1.py"]
      };
    }
}
</script>


<style scoped>
div.flex-container {
  background-color: whitesmoke;
  border: 1px solid lightgray;
  display: flex;
  flex-wrap: wrap;
  font-family: monospace;
  font-size: 1.1em;
  margin-bottom: 0.5em;
  padding: 0.5em 0.5em 0.5em 1em;
}
table {
  text-align: center;
}
</style>
