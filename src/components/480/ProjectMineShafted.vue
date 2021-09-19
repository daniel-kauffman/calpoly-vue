<template>
  <Assignment :name="name" :title="title" :files="files" :rubric="rubric">
    <template v-slot:description>
      <p>Minesweeper is a single-player game consisting of a MxN board of spaces that each either conceal a mine or a clue about possible adjacent mines. The player must uncover the unknown contents of these spaces by selecting them one at a time, using the revealed clues to determine which spaces are safe to explore. The game is won if the player is able to explore every space except the ones with mines.</p>

      <p>An example of a 4x3 game instance both in progress and solved are shown below. An instance is considered solved if all spaces but those containing mines have been explored.</p>
      <div class="flex-container board-set">
        <table class="board">
          <tr><td>0</td><td>1</td><td></td></tr>
          <tr><td>0</td><td>2</td><td></td></tr>
          <tr><td>0</td><td>2</td><td></td></tr>
          <tr><td>0</td><td>1</td><td></td></tr>
          <th colspan=3>A. In Progress</th>
        </table>
        <table class="board">
          <tr><td>0</td><td>1</td><td>1</td></tr>
          <tr><td>0</td><td>2</td><td></td></tr>
          <tr><td>0</td><td>2</td><td></td></tr>
          <tr><td>0</td><td>1</td><td>1</td></tr>
          <th colspan=3>B. Solved</th>
        </table>
      </div>
      <p>The above game instance only has one solution; that is, from Diagram A, there are no other places the mines could be that would satisfy the contraints provided by the clues.</p>

      <h4>CSP Formulation</h4>
      <p>When a search problem is formulated as a constraint satisfaction problem (CSP), the states in the search space are represented as a collection of variables, each with their own domain. When all variables in a state are assigned a value, the state is <strong>complete</strong>. When variables with assignments in a state are only assigned values in their domains, the state is <strong>consistent</strong>. A state that is both complete and consistent is a solution to the CSP.</p>
      <p>In Minesweeper, it may initially seem natural to represent the state space using unexplored spaces as variables, each with a domain of <code>{MINE, NO_MINE}</code>. However, this formulation quickly becomes problematic because there is no simple means to associate clues to collections of spaces. For example, in Diagram A above, it would be difficult to infer that indices 2 and 11 (the top and bottom of the right-most column) are safe if all we know about each unexplored space is that it may or may not contain a mine.</p>

      <p>Instead of unexplored spaces, the clues themselves should be the variables, and each such variable's domain represents all the possible mine placements around that clue. The following boards represent all the possible mine placements with respect to only the clue <code>2</code> at index 4. When taking all clues into account, only Assignment #3 is possible.</p>
      <div class="flex-container board-set">
        <table class="board">
          <tr><td>0</td><td>1</td><td>&#x1f4a5;</td></tr>
          <tr><td>0</td><td>2</td><td>&#x1f4a5;</td></tr>
          <tr><td>0</td><td>2</td><td></td></tr>
          <tr><td>0</td><td>1</td><td></td></tr>
          <th colspan=3>Assignment #1</th>
        </table>
        <table class="board">
          <tr><td>0</td><td>1</td><td>&#x1f4a5;</td></tr>
          <tr><td>0</td><td>2</td><td></td></tr>
          <tr><td>0</td><td>2</td><td>&#x1f4a5;</td></tr>
          <tr><td>0</td><td>1</td><td></td></tr>
          <th colspan=3>Assignment #2</th>
        </table>
        <table class="board">
          <tr><td>0</td><td>1</td><td></td></tr>
          <tr><td>0</td><td>2</td><td>&#x1f4a5;</td></tr>
          <tr><td>0</td><td>2</td><td>&#x1f4a5;</td></tr>
          <tr><td>0</td><td>1</td><td></td></tr>
          <th colspan=3>Assignment #3</th>
        </table>
      </div>

      <p>Thus, to set up the CSP, all possible mine placements with respect to each clue should be generated, which serve as that clue's domain. These domains will then be reduced during the propagation step (see below) to determine which spaces are safe.</p>

      <h4>Constraint Propagation</h4>
      <p>In a CSP, a pair of variables that share a binary constraint (that is, some limitation placed on both variables together), is known as an <strong>arc</strong>. If all binary constraints are satisfied in a state (an assignment of variables), that state is said to be <strong>arc consistent</strong>. It is possible to represent any CSP in terms of only binary constraints, and doing so can make writing the propagation algorithm easier. (The conversion to binary constraints can sometimes be cumbersome, as in the case of the 9x9 puzzle Sudoku, in which the cells in every row, for example, have 9-ary constraints.)</p>
      <p>For this problem, any two clues that share at least one unexplored space form an arc. Diagram A has the following arcs, where each number refers to the index of a clue.</p>
      <pre>(1, 4) (4, 1) (1, 7) (7, 1) (4, 7) (7, 4) (4, 10) (10, 4) (7, 10) (10, 7)</pre>
      <p>Notice that the ordering of each arc matters - <code>(1, 4)</code> is distinct from <code>(4, 1)</code> - which will be important for the propagation algorithm.</p>
      <p>By establishing the arcs between variables, their domains may be reduced (known as constraint propagation) by determing which values in each of the pair's domain conflict with one another. For example, in arc <code>(4, 1)</code>, since the clue at index 1 allows for only one adjacent mine, Assignment #1 above (taken from the domain of the clue at index 4) is not possible.</p>

      <p>Constraint propagation may be performed over a set of arcs using the <a target="_blank" href="https://en.wikipedia.org/wiki/AC-3_algorithm">AC-3 algorithm</a>. This process uses a set that contains every arc in the state space. As each arc is removed from the set, the domain of one variable (say, the left-sided one in the arc) is made arc consistent with the other variable by eliminating any values in the left-sided variable's domain that are impossible in the other. If no values are removed from the variable's domain, the algorithm moves on to the next arc; otherwise, all arcs containing the left-sided variable <strong>on the right side</strong> are added to the set. For example, since making <code>(4, 1)</code> arc consistent resulted in a domain reduction, then <code>(7, 4)</code> would need to be re-added. This step is necessary since reductions to the variable's domains might allow reductions of other variable's domains with which it shares a binary constraint, which would only be found if these arcs were brought back into the set. The algorithm continues until the set is empty, at which point all variables have been made arc consistent. However, if at any point a variable's domain is reduced to nothing, then there exists no solution from the state at which constraint propagation was run.</p>
       <p>Unlike some CSPs, in Minesweeper, trial and error is not an option, as uncovering a mine ends the game (an example of an environment that is <strong>not safely explorable</strong>). Thus, all boards used for this assignment will be solvable using inference via constraint propagation without any guessing.</p>

      <h4>Exploring Safely</h4>
      <p>A Minesweeper solver must alternate between domain reduction (via AC-3) and inferring which spaces are safe in these reduced domains. Again using Diagram A above, the clues adjacent to an unexplored space have the following domains. In this notation, each integer represents a board index, with a positive integer representing a mine at that index and a negative integer representing that index as safe. Integers within parentheses represent one possible assignment in the domain.</p>
      <p>When comparing two domains for a contradiction, only compare the indices they have in common. For example, when comparing the domains of Clues 1 and 4, ignore the <code>8</code>. Doing so shows that <code>(2, 5, -8)</code> is not possible because <code>(2, 5)</code> is not in Clue 1's domain.</p>
      <table>
        <tr><th>Clue Index</th><th>Clue Value<br />(Mine Count)</th><th>Domain</th></tr>
        <tr>
          <td>1</td>
          <td>1</td>
          <td><code>(2, -5)</code> <code>(-2, 5)</code></td>
        </tr>
        <tr>
          <td>4</td>
          <td>2</td>
          <td><code>(2, 5, -8)</code> <code>(2, -5, 8)</code> <code>(-2, 5, 8)</code></td>
        </tr>
        <tr>
          <td>7</td>
          <td>2</td>
          <td><code>(5, 8, -11)</code> <code>(5, -8, 11)</code> <code>(-5, 8, 11)</code></td>
        </tr>
        <tr>
          <td>10</td>
          <td>1</td>
          <td><code>(8, -11)</code> <code>(-8, 11)</code></td>
        </tr>
      </table>
      <br />

      <p>To start a domain reduction simulation, let's remove <code>(2, 5, -8)</code> since <code>2</code> and <code>5</code> cannot both contain a mine; <code>(-5, 8, 11)</code> can be removed for a similar reason. The updated domains are shown below. Note that AC-3 has not completed at this point, as more reductions can still be made.</p>
      <table>
        <tr><th>Clue Index</th><th>Clue Value<br />(Mine Count)</th><th>Domain</th><th>Note</th></tr>
        <tr>
          <td>1</td>
          <td>1</td>
          <td><code>(2, -5)</code> <code>(-2, 5)</code></td>
          <td></td>
        </tr>
        <tr>
          <td>4</td>
          <td>2</td>
          <td><code>(2, -5, 8)</code> <code>(-2, 5, 8)</code></td>
          <td><code>8</code> must contain a mine</td>
        </tr>
        <tr>
          <td>7</td>
          <td>2</td>
          <td><code>(5, 8, -11)</code> <code>(5, -8, 11)</code></td>
          <td><code>5</code> must contain a mine</td>
        </tr>
        <tr>
          <td>10</td>
          <td>1</td>
          <td><code>(8, -11)</code> <code>(-8, 11)</code></td>
          <td></td>
        </tr>
      </table>
      <br />

      <p>Since we now know that <code>5</code> and <code>8</code> contain mines, we can reduce the domains of Clues 1 and 10. Further reductions would then be made to Clues 4 and 7 (not shown).</p>
      <table>
        <tr><th>Clue Index</th><th>Clue Value<br />(Mine Count)</th><th>Domain</th><th>Note</th></tr>
        <tr>
          <td>1</td>
          <td>1</td>
          <td><code>(-2, 5)</code></td>
          <td><code>2</code> is safe</td>
        </tr>
        <tr>
          <td>4</td>
          <td>2</td>
          <td><code>(2, -5, 8)</code> <code>(-2, 5, 8)</code></td>
          <td></td>
        </tr>
        <tr>
          <td>7</td>
          <td>2</td>
          <td><code>(5, 8, -11)</code> <code>(5, -8, 11)</code></td>
          <td></td>
        </tr>
        <tr>
          <td>10</td>
          <td>1</td>
          <td><code>(8, -11)</code></td>
          <td><code>11</code> is safe</td>
        </tr>
      </table>
      <br />

      <p>Once the AC-3 algorithm has completed, the domains of one or more variables will have been sufficiently reduced so that a guaranteed-safe selection is possible (again, these problems assume that the board is solvable by pure logic). Recall that a variable's domain represents all possible assignments to that variable. Thus, if there exists an index in any domain that is always safe (i.e. every possible assignment in a domain has no mine at an index), that index must be safe. In this example, both indices <code>2</code> and <code>11</code> are always mine-free in at least one domain; thus, both of these spaces are safely explorable and either may be selected for the next move.</p>
    </template>

    <template v-slot:implementation>
      <p><b>Allowed Modules:</b> <code>itertools</code> (for combinations and permutations)</p>

      <p>For this assignment, Minesweeper boards will be represented as 2D lists of integers, in which each inner list represents one row of the board; within each row, a non-negative integer indicates the number of mines adjacent to the space at that position and <code>-1</code> represents a mine. The top-left index will always have a clue of <code>0</code>, indicating that its surrounding spaces are safe to explore - every search should start here. A sample 4x3 board is shown below.</p>
      <pre>
[[ 0,  1,  1],
 [ 0,  2, -1],
 [ 0,  2, -1],
 [ 0,  1,  1]]</pre>

      <p>See the <code>mineshafted.py</code> starter file (linked above) for the initial structure of this program, including the provided <code>BoardManager</code> class, which provides an interface to select spaces to explore and receive clues about the number of mines surrounding that space.</p>
      <p>Sample boards may be generated manually or using an external source such as <a target="_blank" href="https://minesweeper.online">World of Minesweeper</a> (select "No guessing mode" but note that this site is not perfect at generating such boards).</p>

      <FunctionSignature name="sweep_mines" :params="[['bm', 'BoardManager']]" type="List[List[int]]"/>
      <p>Given a BoardManager (bm) instance, return a solved board (represented as a 2D list) by repeatedly calling <code>bm.move(index)</code> until all safe indices have been explored. If at any time a move is attempted on a non-safe index, the BoardManager will raise an error; this error signifies the end of the game and cannot be caught.</p>

      <pre>
board = [[0, 1, 1], [0, 2, -1], [0, 2, -1], [0, 1, 1]]
bm = BoardManager(board)
sweep_mines(bm) -&gt; [[0, 1, 1], [0, 2, -1], [0, 2, -1], [0, 1, 1]]</pre>

      <p>Note that the <code>BoardManager</code> hides the contents of the board; to recreate it, this function will need to explore safe spaces until the locations of all mines can be inferred.</p>
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
        name: "mineshafted",
        title: "Project IV: Mine Shafted",
        files: ["mineshafted.py"],
        rubric: {
          "Sweeps 1 Mine": 10,
          "Sweeps 2 Mines": 15,
          "Sweeps 3 Mines": 20,
          "Sweeps 4 Mines": 25,
          "Sweeps 5+ Mines": 30
        }
      };
    }
}
</script>


<style scoped>
table.board {
  border-collapse: collapse;
  margin-left: 1em;
  margin-right: 1em;
}
.flex-container.board-set {
  display: flex;
  justify-content: center;
}
table.board td {
  border: 1px solid gray;
  height: 4em;
  width: 4em;
}
table.board td:empty {
  background-color: lightgray;
}
th, td {
  text-align: center;
}
</style>
