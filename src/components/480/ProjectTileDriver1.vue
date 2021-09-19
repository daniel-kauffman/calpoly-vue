<template>
  <Assignment :name="name" :title="title" :files="files" :rubric="rubric">
    <template v-slot:description>

      <p>Sliding Tile Puzzles (or N-Puzzles) are single-user games that require one to move tiles around a grid until the tiles are in a particular order. Since the tiles cannot be lifted, their movement is made possible by having one tile missing from the grid. Each move thus involves moving a tile adjacent to this empty space.</p>
      <div class="flex-container tile-container">
        <table class="tiles">
          <tr><td>3</td><td>7</td><td>1</td></tr>
          <tr><td>4</td><td></td><td>2</td></tr>
          <tr><td>6</td><td>8</td><td>5</td></tr>
          <th colspan=3>Empty Tile in Center</th>
        </table>
        <table class="tiles">
          <tr><td>3</td><td>7</td><td>1</td></tr>
          <tr><td>4</td><td>2</td><td></td></tr>
          <tr><td>6</td><td>8</td><td>5</td></tr>
          <th colspan=3>Tile 2 Slides Left</th>
        </table>
        <table class="tiles">
          <tr><td>3</td><td>7</td><td>1</td></tr>
          <tr><td>4</td><td>2</td><td>5</td></tr>
          <tr><td>6</td><td>8</td><td></td></tr>
          <th colspan=3>Tile 5 Slides Up</th>
        </table>
      </div>
      <p>As simple as this puzzle appears, it turns out that finding an optimal (shortest-path) solution - from an arbitrary mixed tile state to the final solved state - becomes extremely difficult as the value of N, the number of tiles, increases. In fact, this problem is classified as NP-hard, which means it is at least as difficult as other known computation problems that cannot be solved in polynomial (n<sup>x</sup>) time. For this reason, this project will only focus on small values of N.</p>

      <h4>Path Encoding and A* Search</h4>
      <p>While each state of a sliding tile puzzle can be represented as a sequence of integers (see implementation below), this value does not provide any information about how the user arrived there. Furthermore, a puzzle solver should display to the user the sequence of moves required to get from the initial state to the final state. We will represent such a sequence of moves as a string, where each character in the string is a single move.</p>

      <p>To represent tile movement, we will use the same navigation keys as in Vim, specifically:</p>
      <ul>
        <li><code>"H"</code>: Left</li>
        <li><code>"J"</code>: Down</li>
        <li><code>"K"</code>: Up</li>
        <li><code>"L"</code>: Right</li>
      </ul>

      <p>In the following sequence of diagrams, a 2x2 puzzle is solved with the path of moves that is generated under each state.</p>

      <div class="flex-container tile-container">
        <table class="tiles">
          <tr><td></td><td>2</td></tr>
          <tr><td>3</td><td>1</td></tr>
          <th colspan=2>""</th>
        </table>
        <table class="tiles">
          <tr><td>2</td><td></td></tr>
          <tr><td>3</td><td>1</td></tr>
          <th colspan=2>"H"</th>
        </table>
        <table class="tiles">
          <tr><td>2</td><td>1</td></tr>
          <tr><td>3</td><td></td></tr>
          <th colspan=2>"HK"</th>
        </table>
        <table class="tiles">
          <tr><td>2</td><td>1</td></tr>
          <tr><td></td><td>3</td></tr>
          <th colspan=2>"HKL"</th>
        </table>
        <table class="tiles">
          <tr><td></td><td>1</td></tr>
          <tr><td>2</td><td>3</td></tr>
          <th colspan=2>"HKLJ"</th>
        </table>
      </div>

      <p>The path "HKLJ" is an optimal (shortest possible) path from the initial state to the final state. There are, of course, infinite non-optimal paths, such as "HLHLHLHLHLHKLJ" where the first move is repeatedly undone by going backward. Note that finding the optimal path using brute force is impractical; if the optimal path for a 4x4 puzzle is 20 moves long and there are an average of two valid, non-opposing moves that can be made on each turn, that would require up to 2<sup>20</sup> (over one million) paths to check!</p>

      <p>Thus, to efficiently find an optimal path, you will implement the A* algorithm, a famous search technique in the field of artificial intelligence. The algorithm works by evaluating the cost of each path using the following sum:</p>

      <p>Path Cost = Length of Current Path + Estimated Distance to Final State</p>

      <p>For example, the cost of the path "HKL" in the fourth diagram above is the sum of its length, 3, and the Manhattan distance to the final state, 1, for a path cost of 4.</p>

      <p>The algorithm begins by finding all frontier puzzle states available from the initial state. On each iteration of a loop, the frontier state with the lowest cost is explored, which requires generating all possible new puzzle states from it. Once these new states are created, the state that created them is removed from the list of frontier states. This process of exploring lowest-cost states and generating new states continues until the lowest-cost state has a distance of zero, indicating that it is the final state and an optimal path was found.</p>

      <h4>Search Heuristics</h4>
      <p>In order for A* Search to be optimal, all heuristics used must be admissible and consistent when combined. Thus, it is important that the heuristics do not count any of the same moves when computing their estimated distances.</p>
      <p><strong>Note that the following heuristics methods are already implemented for you in the starter file.</strong> The descriptions below serve as an example of the potential complexities in computing the heuristic for an informed search.</p>

      <h6>Manhattan Distance</h6>
      <p>Unlike Euclidean distance, which measures the distance between two points as a straight line, Manhattan distance does so by counting the number of tiles that must be traversed between two tiles in a grid. This approach is similar to how one thinks about distance when driving in a grid-like city or moving between squares on a game board. Importantly, when calculating Manhattan distance you cannot traverse diagonally.</p>
      <div class="flex-container tile-container">
        <table>
          <tr>
            <td style="background-color: lime"></td>
            <td></td><td></td><td></td><td></td>
            <td></td><td></td><td></td><td></td>
          </tr>
          <tr>
            <td></td><td></td><td></td>
            <td style="background-color: blue"></td>
            <td></td><td></td><td></td><td></td><td></td>
          </tr>
          <tr>
            <td></td><td></td><td></td><td></td>
            <td></td><td></td><td></td><td></td>
            <td style="background-color: red"></td>
          </tr>
        </table>
      </div>
      <br />
      <p>In the grid above, the green and blue squares have a distance of 4, the blue and red squares have a distance of 6, and the green and red squares have a distance of 10.</p>
      <p>Manhattan distance can be used to determine how far a particular state of a puzzle is from its final solved state. To do so, sum up the Manhattan distance of each tile (not including the blank tile) from its current position to its final position.</p>
      <div class="flex-container tile-container">
        <table class="tiles">
          <tr><td>3</td><td>7</td><td>1</td></tr>
          <tr><td>4</td><td></td><td>2</td></tr>
          <tr><td>6</td><td>8</td><td>5</td></tr>
          <th colspan=3>Random Puzzle State</th>
        </table>
        <table class="tiles">
          <tr><td></td><td>1</td><td>2</td></tr>
          <tr><td>3</td><td>4</td><td>5</td></tr>
          <tr><td>6</td><td>7</td><td>8</td></tr>
          <th colspan=3>Final Puzzle State</th>
        </table>
      </div>
      <p>In the example above, the Manhattan distance is 8 (verify this result yourself).</p>

      <h6>Linear Conflicts</h6>
      <p>The Manhattan distance used as a heuristic for solving sliding tile puzzles can be augmented by observing when two or more tiles are in linear conflict. For two tiles to be in linear conflict, they must be in their correct row or column but be in incorrect order. Since one tile will need to move out of the row or column (to get out of the other tile's way) and then move back again, each linear conflict adds 2 to the total estimated distance.</p>
      <div class="flex-container tile-container">
        <table>
          <tr><td>*</td><td>7</td><td>*</td></tr>
          <tr><td>*</td><td>4</td><td>*</td></tr>
          <tr><td>*</td><td>1</td><td>*</td></tr>
          <th colspan=3>1, 4, and 7 are<br>in linear conflict</th>
        </table>
        <table>
          <tr><td>7</td><td>*</td><td>*</td></tr>
          <tr><td>*</td><td>4</td><td>*</td></tr>
          <tr><td>*</td><td>*</td><td>1</td></tr>
          <th colspan=3>1 and 7 can exit goal<br>column to go around 4</th>
        </table>
        <table>
          <tr><td>*</td><td>*</td><td>1</td></tr>
          <tr><td>*</td><td>4</td><td>*</td></tr>
          <tr><td>7</td><td>*</td><td>*</td></tr>
          <th colspan=3>1 and 7 must eventually<br>re-enter goal column</th>
        </table>
      </div>
      <p>A conflicting tile only needs to move out of the way of other tiles once. Furthermore, only the <b>minimum</b> number of tiles that must move in a row or column should be counted as conflicts to ensure that conflicts are not overcounted. This heuristic may be calculated as follows:</p>
      <ol>
        <li>Find the tiles that are in conflict for each row or column.</li>
        <li>For each row or column with conflicts:</li>
        <ol type="a">
          <li>Find the tile that has the highest number of conflicts relative to the other tiles. Remove this tile from consideration and increment the number of conflicts found.</li>
          <li>Repeat the step above until the remaining tiles under consideration have no conflicts with one another.</li>
        </ol>
      </ol>
    </template>

    <template v-slot:implementation>
      <p><b>Allowed Modules:</b> queue</p>
      <p>Tiles will be represented as a tuple of integers, with each integer a single tile in the puzzle in row-major order. The blank tile will be represented with the integer 0.</p>

      <p>For example, the left-most puzzle in the first diagram above would be represented as:</p>
      <pre>(3, 7, 1, 4, 0, 2, 6, 8, 5)</pre>
      <p>Tiles may only be moved in a given direction if the blank tile is there. For example, a tile may only be moved up if the blank tile is above it.</p>

      <p>Use the <code>get</code> static method in the provided <code>Heuristic</code> class to compute the combined Manhattan distance and linear conflicts heuristic for a given set of tiles.</p>
      <pre>
Heuristic.get((0, 1, 2, 3)) -&gt; 0
Heuristic.get((3, 2, 1, 0)) -&gt; 6</pre>

      <h4>Required Functions</h4>
      <p>You only need to implement the function(s) below, which will serve as the interface for the submission system's test driver. However, your program should demonstrate good decomposition with additional functions or classes.</p>

      <AssignmentFunctionSignature name="solve_puzzle" :params="[['tiles', 'Tuple[int, ...]']]" type="str" />
      <p>Find a path containing the optimal number of moves to the solution and return it as a string. A state is considered a solution if its Manhattan distance to an ordered tuple of integers equals zero.</p>
      <p>Any state added to the frontier should represent a move that is both <b>valid</b> (a tile can move in that direction) and <b>non-opposing</b> (does not undo the previous move). There is at least one and at most three valid, non-opposing moves that can be made from an arbitrary state (except the first move, which may have up to four).</p>
      <p>Your puzzle states representations (whether they be objects, dictionaries, etc.) should, in addition to the tiles, contain at least the path string used to get to the state and its estimated distance to the goal. For efficiency, the heuristic should only be computed once per state. To be under the time limit, you may need to use a priority queue (see <a href="https://docs.python.org/3/library/queue.html?highlight=queue%20priorityqueue#queue.PriorityQueue">queue.PriorityQueue</a>) for the frontier states; if inserting objects into the queue, you will need to implement a <code><a target="_blank" href="https://docs.python.org/3/reference/datamodel.html#object.__lt__">__lt__</a></code> method for its class so that the objects may be compared for prioritiy.</p>

      <h4>Sample Puzzles</h4>
      <p>The following 3x3 puzzles have an optimal solution of 30 moves and may be useful for testing.</p>
      <pre>
(0, 3, 6, 5, 4, 7, 2, 1, 8)
(6, 7, 8, 3, 0, 5, 1, 2, 4)
(8, 2, 0, 5, 4, 3, 7, 1, 6)</pre>
    </template>
  </Assignment>
</template>


<script>
export default {
  data:
    function () {
      return {
        name: "tiledriver1",
        title: "Project I: Tile Driver",
        files: ["tiledriver.py"],
        rubric: {
          "Solve Any 2x2 Puzzle": 5,
          "Optimally Solve Any 2x2 Puzzle": 20,
          "Solve 20-Length 3x3 Puzzles": 10,
          "Optimally Solve 20-Length 3x3 Puzzles": 20,
          "Solve 30-Length 3x3 Puzzles": 15,
          "Optimally Solve 30-Length 3x3 Puzzles": 30
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
