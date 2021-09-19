<template>
  <Assignment :name="name" :title="title" :files="files" :rubric="rubric">
    <template v-slot:description>
      <p>In this project, you will write a program that itself writes programs. These programs will be run using a simple interpreter to write integers to a memory - represented as a fixed-length array - using a minimalist language that supports the commands listed below. This language derives from <a target="_blank" href="https://en.wikipedia.org/wiki/Brainfuck">Brainfuck</a> (BF), an esoteric programming language designed by Urban Müller.</p>
      <table>
        <tr><td><strong>Command</strong></td><td><strong>Description</strong></td></tr>
        <tr><td>&gt;</td><td>Increment memory pointer</td></tr>
        <tr><td>&lt;</td><td>Decrement memory pointer</td></tr>
        <tr><td>+</td><td>Increment integer at current memory location</td></tr>
        <tr><td>-</td><td>Decrement integer at current memory location</td></tr>
        <tr><td>[</td><td>If cell at memory pointer is zero, jump to corresponding <code>]</code> command<br />Otherwise, move to next command</td></tr>
        <tr><td>]</td><td>If cell at memory pointer is non-zero, jump to corresponding <code>[</code> command<br />Otherwise move to next command</td></tr>
      </table>
      <br />

      <p>Thus, the programs generated will be sequences of these commands and, when interpreted, must write values to an empty memory that exactly matches a provided target array. To create these programs, you will implement a genetic algorithm, a local search method loosely based off of biological evolution for finding sequences of values that meet given criteria.</p>
      <p>For a demonstration of the language, see this <a target="_blank" href="https://fatiherikli.github.io/brainfuck-visualizer/">Brainfuck Visualizer</a>.</p>

      <h4>Genetic Algorithms</h4>
      <p>Local search algorithms often employ a strategy of creating many candidate solutions to a problem and exploring the states around the best ones. While this approach can be effective for simple problems, global optima may not be found unless the number of states being explored is intractably high. Genetic algorithms (or GAs) improve on these algorithms by using more sophisticated methods for selecting individual states and using their components to create more diverse populations in subsequent generations.</p>

      <h6>Fitness Functions</h6>
      <p>An objective (or evaluation) function is necessary to assess the quality of each individual in a generation; in GA parlance, this method is referred to as a fitness function. Unlike the other components of a GA, the implementation of a fitness function is specific to the problem domain and often represents its most costly operation.</p>
      <p>For this project, a natural fitness evaluation would compare the contents of the array modified by an individual program against a target array that the program is supposed to produce. This comparison can be made by calculating the sum of the absolute difference between the two arrays. Additional metrics may also be used, such as attributing higher scores to smaller programs to promote brevity; however, while such additions may be used to break ties, accuracy should be the primary basis for evaluation.</p>

      <h6>Selection</h6>
      <p>Once all of the individuals in a generation have been scored, the next generation can be constructed. To do so, individuals from the current generation must be selected (typically in pairs) for the crossover stage. Prior to selection, the entire generation's fitness scores are usually normalized to probabilities (if lower fitness scores indicate better individuals, simply subtract each score from the sum of all scores). Afterward, individuals may be randomly sampled from the population and their corresponding weights accumulated until this sum exceeds a randomized threshold, at which point that individual is selected.</p>
      <p>In addition to this approach, it can also be beneficial to only consider for selection individuals that fall within a certain top percentile. However, it is important not to remove too many individuals from consideration or else the population will converge too quickly.</p>

      <h6>Crossover and Mutation</h6>
      <p>Once two individuals have been selected, the crossover method specifies at which point the individuals will be divided and recombined to create new individuals. Typically, two-point crossover is used in which both individuals are divided at the same point and two successor individuals result from swapping either of the two segments. Other forms of crossover exist, including three-point and uniform crossover, the latter of which swaps individual elements of the sequents instead of segments as a whole.</p>
      <p>In addition, GAs often provide a chance for the resulting successor individuals to undergo mutation, whereby one or more of their elements are randomly changed. This step can help prevent individuals from converging by promoting diversity; however, if used too frequently, the benefits of crossover are lost and the search becomes a random walk. Mutation may include different probabilities for adding, deleting, or modifying parts of an individual.</p>
    </template>

    <template v-slot:implementation>
      <p><strong>Allowed Modules:</strong> <code>random</code></p>
      <p>Your GA implementation should not deviate too far from methods discussed in lecture. You may need to experiment with different parameters to find a balance that works in a timely manner. These parameters include (not exhaustively):</p>
      <ul>
        <li>Size of the starting population</li>
        <li>Lower and upper bounds on program lengths</li>
        <li>Percentile kept for the next generation</li>
        <li>Mutation rates</li>
      </ul>
      <p>The <code>biogimmickry.py</code> file (linked above) provides a <code>FitnessEvaluator</code> class that performs scoring for a program, with a score of zero indicating that the program, when interpreted, populates a memory array that exactly matches an array that was used to instantiate the <code>FitnessEvaluator</code>. It is this score that must be used for the selection process, as well as determining whether the search is complete.</p>
      <p>The <code>FitnessEvaluator</code> class should not be modified. It is instantiated once prior to a search and is accessed using <code>FitnessEvaluator.evaluate(program)</code> to receive a score for a <code>program</code> string. For an example of how to instantiate it, see the <code>main</code> function in the file.</p>

      <h4>Required Functions</h4>
      <p>In the following instructions, "program" refers to a BF program, and "loop" refers to loops in BF programs (not Python loops). The "target array" is what the BF interpreter's memory must match when a solution program is run.</p>
      <p>Assume all target arrays have an <strong>absolute sum</strong> no greater than <code>20</code> (e.g. <code>(2, -4, 6, -8)</code>).</p>

      <FunctionSignature name="create_program" :params="[['fe', 'FitnessEvaluator'], ['max_len', 'int']]" type="str" />
      <p>Return a program string no longer than <code>max_len</code> that, when interpreted, populates a memory array that exactly matches a target array.</p>

      <p>The <code>max_len</code> argument forces programs to use loops by limiting their length. If <code>max_len</code> is zero, it may be disregarded; in other words, a loop will not be necessary to match the target array. In this case, you may choose an appropriate upper bound for program lengths, keeping in mind that longer programs take more time to evaluate. However, if <code>max_len</code> is positive, the length of the program returned by this function must not exceed this value. Use this distinction to first ensure your algorithm correctly generates programs without loops before adding the logic to match arrays iteratively.</p>
      <p>For non-loop programs, the target array will never exceed a length of <code>8</code>; for programs requiring a loop, the target array length will always be <code>2</code>, with one element set to zero (to be used as a loop counter) and the absolute value of the other element greater than <code>max_len</code>. For example, a target array might be <code>(0, 20)</code> with a <code>max_len</code> of <code>18</code>. Thus, because the length of the program must be less than the absolute sum of the array, a proper use of the loop (with a counter) must be found by the genetic algorithm to match the target array.</p>
      <p>Note that the minimum length of any program containing a loop should be <code>12</code>, as a loop in a shorter program would not be necessary or meaningful. For example, a minimum-length loop-containing program might look like <code>"+++[&gt;++++&lt;-]"</code>. Programs without loops may be of any length.</p>

      <p>When implementing this function, you may want to follow these steps:</p>
      <ol>
        <li>
          Initialize a population of random programs
          <ul>
            <li>Population size should be as large as possible (usually over <code>500</code>) without significantly slowing down each generation</li>
            <li>Programs should never be greater in length than <code>max_len</code> (if non-zero)</li>
            <li>Do not create programs with more than one loop; that way lies madness</li>
          </ul>
        </li>
        <li>
          Score all programs using <code>FitnessEvaluator.evaluate(program)</code>
          <ul>
            <li>Stop if a program has a fitness score of zero</li>
          </ul>
        </li>
        <li>
          Select two programs in the top <code>N</code> percentile weighted by score using <code><a target="_blank" href="https://docs.python.org/3/library/random.html#random.choices">random.choices</a></code> (or some other weighting method)
          <ol type="a">
            <li>
              Use crossover to create two new programs, ensuring both do not exceed <code>max_len</code> (if non-zero)<br />If a loop exists, avoid breaking it by ensuring the crossover point is:
              <ul>
                <li>To the left of both programs' <code>[</code> command</li>
                <li>To the right of both programs' <code>]</code> command</li>
                <li>Between both programs' <code>[</code> and <code>]</code> commands</li>
              </ul>
            </li>
            <li>
              Randomly mutate zero or more elements in each of the new programs
              <ul>
                <li>Mutation may be any of addition, deletion, or editing of commands, each with separate probabilities</li>
                <li>Ensure that mutation maintains one loop in the program and does not cause it to exceed <code>max_len</code></li>
              </ul>
            </li>
            <li>Add the new programs to the next generation</li>
          </ol>
        </li>
        <li>Repeat Step 3 until the next generation is the size of the previous generation</li>
        <li>Go to Step 2 using the next generation UNLESS it has converged, in which case go to Step 1</li>
      </ol>
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
        name: "biogimmickry",
        title: "Project III: Biogimmickry",
        files: ["biogimmickry.py"],
        rubric: {
          "Matches 1 Length Array": 15,
          "Matches 2-4 Length Non-Negative Array": 20,
          "Matches 5-8 Length Array": 30,
          "Iteratively Matches 2 Length Array": 35
        }
      };
    }
}
</script>


<style scoped>
td:first-child {
  text-align: center;
}
</style>
