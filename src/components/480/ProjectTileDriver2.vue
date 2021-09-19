<template>
  <Assignment :name="name" :title="title" :files="files" :rubric="rubric">
    <template v-slot:description>
      <p>This specification assumes the completion of Tile Driver: Part I.</p>
      <p>Whereas the previous project involved solving puzzles, this project requires creating them. Searching for puzzles of maximum difficulty - that is, puzzles with the longest optimal path for their size - represents a very different challenge.</p>
      <p>One strategy would be to start from a solved puzzle and move toward puzzle states with longer optimal paths; another would be to start from randomly generated puzzles, which would first need to be verified to be solvable. In either case, the length of the optimal path for any state in the search can often only be known by solving that puzzle, which is an expensive operation. To expedite the search, only select states should be solved, guiding the search through unsolved states using heuristics.</p>
      <h4>Puzzle Solvability</h4>
      <p>Some local search algorithms rely on creating many random states to cover more of the state space. Therefore, when searching for complex shuffled states, it becomes necessary to verify that a state generated randomly is solvable before using it as a starting point to search for more complex states.</p>
      <p>Any move made from a solvable puzzle state is guaranteed to be solvable; conversely, any move made from an unsolvable puzzle state is likewise unsolvable. If the solved puzzle state is used to search for shuffled puzzle states, any resulting state will always be solvable.</p>
      <p>The solvability of a puzzle state can be determined by counting the number of inversions in a one-dimensional list of integers representing the tiles. Inversions are defined by the number of occurrences of a pair of integers in incorrect order. For sliding tile puzzles, the blank tile is not counted toward the number of inversions.</p>
      <p>For example, the following sequence has 10 inversions:</p>
      <pre>(3, 7, 1, 4, 0, 2, 6, 8, 5)</pre>
      <p>Given the width of the puzzle and the number of inversions, the solvability of any configuration of tiles can be found using the following approach.</p>

      <ul>
        <li>If the width of the puzzle is an odd number:</li>
        <ul>
          <li>The puzzle is solvable only if the number of inversions in the puzzle is an even number</li>
        </ul>
        <li>If the width of the puzzle is an even number:</li>
        <ul>
          <li>If the blank tile is in an even row (zero-indexed):</li>
          <ul>
            <li>The puzzle is solvable only if the number of inversions in the puzzle is an even number</li>
          </ul>
          <li>If the blank tile is in an odd-numbered row (zero-indexed):</li>
          <ul>
            <li>The puzzle is solvable only if the number of inversions in the puzzle is an odd number</li>
          </ul>
        </ul>
      </ul>
      <p>The logic for determining puzzle solvability is provided for you in the starter file.</p>
    </template>

    <template v-slot:implementation>
      <p><b>Allowed Modules:</b> random</p>
      <p>Design a local search algorithm for use in the required functions below. This algorithm should be based off elements from one or more of the following methods:</p>
      <ul>
        <li><a target="_blank" href="https://en.wikipedia.org/wiki/Hill_climbing">Hill Climbing</a>, which includes random restarts</li>
        <li><a target="_blank" href="https://en.wikipedia.org/wiki/Simulated_annealing">Simulated Annealing</a>, which allows worse successors to be explored</li>
        <li><a target="_blank" href="https://en.wikipedia.org/wiki/Beam_search">Beam Search</a>, which uses multiple current states</li>
      </ul>

      <p>Creativity in your design is encouraged and you may deviate from these traditional algorithms so long as the resulting method constitutes a local search; in other words, the number of active states throughout the search should remain constant. Methods that rely only on random chance and do not use search logic will not receive credit, even if successful.</p>
      <p>The same algorithm need not be used for both search functions. Furthermore, consider the differences in search space topography between <code>conflict_tiles</code> and <code>shuffle_tiles</code>. Does one have smoother slopes? What about the frequency and range of plateaus? Not all local search methods discussed will perform equally well on both problems.</p>

      <h4>Required Functions</h4>
      <AssignmentFunctionSignature name="conflict_tiles" :params="[['width', 'int'], ['min_lc', 'int']]" type="Tuple[int, ...]" />
      <p>Create a solvable shuffled puzzle of the given width with a minimum number of linear conflicts (ignoring Manhattan distance). Return a suitable puzzle <strong>as soon as it is found</strong> to satisfy the time constraint. Because the path cost of each state is irrelevant, no call to <code>tiledriver.solve_puzzle</code> will be necessary.</p>
      <p>Use <code>tiledriver.Heuristic._get_linear_conflicts</code> from <code>tiledriver.py</code> to compute the number of linear conflicts in a state. Note that the maximum number of conflicts for a puzzle of width 3 or greater is <code>2 * ((width - 1)<sup>2</sup> + (width - 2))</code>.</p>

      <p>Based on the puzzle width, your implementation will be required to produce puzzles with the following number of linear conflicts:</p>
      <ul>
        <li>3x3: 10 conflicts</li>
        <li>4x4: 14 conflicts</li>
        <li>5x5: 18 conflicts</li>
      </ul>

      <AssignmentFunctionSignature name="shuffle_tiles" :params="[['width', 'int'], ['min_len', 'int'], ['solve_puzzle', 'Callable[[Tuple[int, ...]], str]']]" type="Tuple[int, ...]" />
      <p>Create a solvable shuffled puzzle of the given width with an optimal solution length equal to or greater than the given minimum length. Return a suitable puzzle <strong>as soon as it is found</strong> to satisfy the time constraint. Because solving the puzzle for every state in the search would be too expensive, you must search many states between solving them; determining a good frequency with which to solve states is part of the challenge.</p>
      <p>The <code>solve_puzzle</code> argument is a callable that solves a puzzle and returns an optimal path. This callable will be provided by the instructor's test suite (primarily for students who were unable to complete the first part of the project). For those who have successfully implemented <code>tiledriver.solve_puzzle</code>, simply pass a reference to that function to <code>shuffle_tiles</code> when testing locally: <code>shuffle_tiles(2, 6, tiledriver.solve_puzzle)</code>.</p>
      <p>Based on the puzzle width, your implementation will be required to produce puzzles with the following optimal path lengths:</p>
      <ul>
        <li>2x2: 6 moves</li>
        <li>3x3: 29 moves</li>
      </ul>
    </template>
  </Assignment>
</template>


<script>
export default {
  data:
    function () {
      return {
        name: "tiledriver2",
        title: "Project II: Tile Driver II",
        files: ["shuffle.py", "tiledriver.py"],
        rubric: {
          "Creates 10-Conflict 3x3 Puzzles": 10,
          "Creates 14-Conflict 4x4 Puzzles": 15,
          "Creates 18-Conflict 5x5 Puzzles": 25,
          "Creates 6-Length 2x2 Puzzles": 15,
          "Creates 29-Length 3x3 Puzzles": 35
        }
      };
    }
}
</script>


<style scoped>
.flex-container.tile-container {
  display: flex;
  justify-content: center;
}
table {
  border-collapse: collapse;
  margin-left: 1em;
  margin-right: 1em;
}
td {
  border: 1px solid gray;
  height: 4em;
  width: 4em;
  text-align: center;
}
table.tiles td:empty {
  background-color: gray;
}
th {
  text-align: center;
}
</style>
