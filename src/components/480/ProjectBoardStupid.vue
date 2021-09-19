<template>
  <Assignment :name="name" :title="title" :files="files" :rubric="rubric">
    <template v-slot:description>
      <p>In some search problems, including many games, one or more agents may be attempting to thwart your ambitions. Adversarial search algorithms provide a way to increase the likelihood of reaching a desired state (a winning condition) while other agents try to prevent you from reaching this goal. In the simplest case, this competition is between two players, traditionally labeled <code>MAX</code> and <code>MIN</code>, who select moves that respectively maximize or minimize an estimated utility value. These utility values guide each player through the game tree toward a favorable goal.</p>
      <p>When experimenting with adversarial search methods, Tic-Tac-Toe is a popular choice due to the simplicity of its rules. The state space can also easily be expanded by increasing the size and number of the boards. Even with four 4x4 boards - known as 3D Tic-Tac-Toe (or Qubic) - the game tree becomes far too large for an exhaustive search. See this <a target="_blank" href="http://users.csc.calpoly.edu/~dkauffma/480/3dtictactoe.pdf">document</a> for a visual representation of all the 3D Tic-Tac-Toe winning conditions. Whereas classic Tic-Tac-Toe has 8 winning conditions, the 3D version has 76 winning conditions (verify this number for yourself to ensure you understand the rules).</p>

      <h4>The Multi-Armed Bandit Problem</h4>
      <p>Suppose you are at a casino (i.e. you don't value your free time) and you decide to play the slot machines (i.e. you <i>really</i> don't value your free time). These slot machines (or "one-armed bandits") may have different payout rates, which can only be determined by observation. As you begin experimenting by playing different machines, you find that some machines initially appear to pay out more often than others, but the number of experiments has been too small to be conclusive. After <code>N</code> plays, which machine should you play next?</p>
      <p>This problem demonstrates the <strong>exploration</strong> versus <strong>exploitation</strong> tradeoff. By continuing to play machines that have thus far paid well, you are exploiting them; however, another machine could have a higher payout rate if your observations are insufficient, requiring you to occasionally explore other machines to see if those options become better.</p>
      <p>When selecting the next machine to play, the exploration versus exploitation tradeoff can be balanced using the calculation for an Upper Confidence Bound (UCB).</p>
      <img style="position: relative; left: 5em;" src="@/assets/480/img/ucb.png" width=20% height=20%>
      <p>In this equation, <code>W</code> refers to the number of wins from the machine under consideration, <code>N</code> is the number of times that machine was played, and <code>T</code> represents the total number of plays on all machines. The variable <code>C</code> is used as an <strong>exploration bias</strong> parameter to help control the frequency of exploration (<code>&radic;2</code> serves as a typical baseline). The UCB is then calculated for each machine, with the highest-valued machine selected for the next experiment.</p>

      <h4>Monte Carlo Tree Search</h4>
      <p>In almost all games, it is impractical to do an exhaustive search of the game tree. Some approaches to finding good moves in large trees involve engineering game features for use in a state evaluation function. While effective if the features closely reflect likely outcomes, evaluation functions are specific to the game for which they are developed and ill-suited for many complex games such as Go.</p>
      <p><a target="_blank" href="https://en.wikipedia.org/wiki/Monte_Carlo_tree_search">Monte Carlo Tree Search</a> is a method that uses sampling to estimate the quality of a move by exploring many paths through the move and tallying the number that result in victory. The algorithm works by performing a large number of tree traversals, each known as a playout. During these playouts, a frontier is maintained (see below).</p>
      <p>On each iteration of the search, the following actions are performed.</p>
      <ul>
        <li><strong>Selection:</strong> Starting from the root of the game tree (which represents the current state of the game), traverse down the tree by selecting the child state at each level with the highest UCB. (States yet to be traversed may be assigned the value <code>C</code> or something similar.) Note that, at each level, <code>T</code> is equivalent to the <code>N</code> of the parent; that is, the total number of attempts of a level is equal to the number of attempts through the parent of the level. Continue until a frontier or terminal state is reached (whichever comes first).</li>
        <li>If a state is selected that is non-terminal and on the frontier:</li>
        <ul>
          <li><strong>Expansion:</strong> Add one of its children at random to the frontier and traverse to it. Remove its parent from the frontier. It is recommended to maintain an explored set for former-frontier states so that their win ratios can still be accessed and updated. Only one state should be added to the frontier on each iteration of the search.</li>
          <li><strong>Simulation:</strong> Perform a random walk toward a terminal state.</li>
        </ul>
        <li><strong>Backpropagation:</strong> Once at a terminal state, determine the outcome of the game with respect to the current player: win, loss, or tie. Each outcome should have a different value, as determined through experimentation. Return this value back up through the tree to the root, updating each state's win ratio appropriately along the way.</li>
      </ul>
    </template>

    <template v-slot:implementation>
      <p><strong>Allowed Modules:</strong> math, random</p>

      <p>For this assignment, a 3D board will be represented as a 4-tuple of 2D boards, with each 2D board represented as a tuple of integers, using <code>0</code> for an empty space and <code>1</code> and <code>-1</code> for <code>MAX</code> and <code>MIN</code>, respectively. Each 2D board has <code>16</code> spaces, for a total of <code>64</code> spaces per game state. The initial state is shown below.</p>
      <pre>
((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
 (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
 (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
 (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))</pre>
      <p>In addition, some spaces may be set to <code>None</code> before the game begins. These spaces should be considered barriers that no player may select for a move. This feature allows for the reduction of the search space, which can simplify the creation of tests.</p>
      <p>See the starter file for the <code>GameState</code> class, which provides a representation of game states, including the current player, the actions available at that state, and the utility of the state, as well as a means to traverse the game tree.</p>

      <FunctionSignature name="find_best_move" :params="[['state', 'GameState']]"/>
      <p>Search the game tree for the optimal move for the current player, storing the index of the move in the given GameState object's <code>selected</code> attribute. The move must be an integer indicating an index in the 3D board - ranging from <code>0</code> to <code>63</code> - with <code>0</code> as the index of the top-left space of the top board and <code>63</code> as the index of the bottom-right space of the bottom board.</p>
      <p>This function must perform a Monte Carlo Tree Search to select a move, calling additional functions as necessary. During the search, whenever a better move is found, the <code>selected</code> attribute should be immediately updated for retrieval by the instructor's game driver. Be sure to update <code>selected</code> with the move that has the highest <strong>win ratio</strong>, not highest UCB.</p>
      <p>Each call to this function will be given a set number of seconds to run; when the time limit is reached, the index stored in <code>selected</code> will be used. Note that this function will only be evaluated on finding the best move for isolated boards; in other words, it will <strong>not</strong> be run multiple times in succession on the same board until a player wins.</p>

      <h4>Extra Credit Tournament</h4>
      <p>You may earn extra credit through a class 3D Tic-Tac-Toe tournament that will be conducted in a round-robin format (each agent plays against every other agent), with the top students receiving an amount based on their ranking (ties will grant each such student the highest number of points for that block). An empty table will be passed in for the player as a dictionary on the first turn to memoize the win ratio statistics that it finds at each game state and its contents will be maintained and provided for each subsequent call of <code>find_best_move</code> for that player throughout a game.</p>
      <p>Every functioning program will be automatically entered into the tournament. There will be no <code>None</code> barrier spaces in the tournament.</p>
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
        name: "boardstupid",
        title: "Project V: Board Stupid",
        files: ["boardstupid.py"],
        rubric: {
          "Finds Optimal Move Among 8 Spaces": 20,
          "Finds Optimal Move Among 14 Spaces": 30,
          "Finds Optimal Move Among 22 Spaces": 50
        }
      };
    }
}
</script>


<style scoped>
tr:first-child {
  text-align: center;
}
</style>
