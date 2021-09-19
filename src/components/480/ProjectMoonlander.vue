<template>
  <Assignment :name="name" :title="title" :files="files" :rubric="rubric">
    <template v-slot:description>
      <figure>
        <img src="@/assets/480/img/lunar-module.jpeg" style="width: 12em;"/>
        <figcaption>Eagle in lunar orbit<br/>photographed from Columbia</figcaption>
      </figure>

      <p><em>This project is based off "Moonlander", assigned in Cal Poly's CPE 101.</em></p>
      <p>You are tasked with training an agent in a simulation to land the Lunar Module (LM) from the Apollo space program on the moon. The simulation starts when the retro-rockets cut off, using a predetermined amount of fuel and altitude (with an initial velocity of zero meters per second). With the thrusters off and the LM in free-fall, lunar gravity is causing the LM to accelerate toward the surface. The agent must control the rate of descent using the thrusters of the LM by selecting a rate of fuel flow each second. A fuel rate of 0% means free-fall, 50% maintains the current velocity, and 100% means maximum thrust. To make things interesting (and to reflect reality) the LM has a limited amount of fuel. If your agent runs out of fuel before touching down, it has lost control of the LM, which then free-falls to the surface. The goal is to land the LM on the surface with a velocity greater than <code>-1</code> meters per second, using the least amount of fuel possible. Note that a negative velocity indicates movement toward the moon, while a positive velocity indicates movement away from it.</p>
      <p>While this simulation is inspired from the moon landing, you may simulate landing on other celestial bodies as well. One of the simulator initialization values is the <a target="_blank" href="https://en.wikipedia.org/wiki/G-force">g-force</a> applied to the module. The following table provides the g-force at (or near) the surface of various objects.</p>
      <table>
        <tr><th>Object</th><th>G-force</th></tr>
        <tr><td>Pluto</td><td>0.063</td></tr>
        <tr><td>Moon</td><td>0.1657</td></tr>
        <tr><td>Mars</td><td>0.378</td></tr>
        <tr><td>Venus</td><td>0.905</td></tr>
        <tr><td>Earth</td><td>1.0</td></tr>
        <tr><td>Jupiter</td><td>2.528</td></tr>
      </table><br/>

      <h4>Q-Learning</h4>
      <p>Reinforcement learning is an iterative process using a system of rewards to develop a policy that dictates what action to apply in any given state. That is, it approximates a function <code>&pi;(S) -&gt; A</code> that maps states to (ideally optimal) actions to apply in those states. Each state in the environment has a (usually unknown) utility value that is approximated throughout the learning process, so that ultimately actions can be chosen that lead to states with higher utilities. The utility of a state is based on predefined rewards received in that state and the potential rewards of successor states.</p>
      <p>As with problems discussed previously, learning environments use a transition model <code>T(S, A) -&gt; S'</code> that maps a state-action pair to a successor state. However, many environments exist in which this model is not known prior to the learning process. A well-established approach to <a target="_blank" href="https://en.wikipedia.org/wiki/Model-free_(reinforcement_learning)">model-free</a> reinforcement learning is <a target="_blank" href="https://en.wikipedia.org/wiki/Q-learning">Q-learning</a>, which observes transitions from exploring the environment to approximate a function <code>Q(S, A) -&gt; U</code> that maps state-action pairs to the estimated utility of that successor state. With this Q-function, the policy function &pi; would be equivalent to <code>&pi;(S) = argmax<sub>A</sub> Q(S, A)</code>, which means return the action <code>A</code> that results in the highest utility returned from <code>Q(S, A)</code>.</p>
      <p>While a more precise approximation of the Q-function would use a sophisticated model like a neural network, for small environments a Q-table (matrix) indexed by state (row-wise) and action (column-wise) to a utility entry can be sufficient and is much faster to train and easier to implement.</p>
      <p>During the training phase, table updates are performed using the following formula,</p>
      <pre>
(1 - &alpha;) * Q(s, a) + &alpha;(R(s) + &gamma; * max<sub>a'</sub>{Q(s', a')})</pre>
      <p>where <code>&alpha;</code> is the learning rate and <code>&gamma;</code> is the discount factor, both determined using experimentation (<code>&alpha;</code> often starts high and decreases throughout the learning process). <code>R</code> is the reward function, which is specific to the problem. Note that since every call to the <code>Q</code> function is simply a table look up, this formula demonstrates <a target="_blank" href="https://en.wikipedia.org/wiki/Memoization">memoization</a> rather than recursion.</p>

      <h4>Reward Function</h4>
      <p>Every reinforcement learning process involves a reward function, which specifies the immediate value of being in a particular state. These functions may be very simple or contain a complex sequence of conditions, depending on the environment. In the context of the LM, a reward function would need, at a minimum, to detect when a terminal state is reached (i.e. when the altitude is zero) and provide a value based on the LM's velocity so that softer landings are more highly rewarded. In addition, the LM should be encouraged to move toward a terminal state (mainly so it does not try to hover in place until fuel runs out), which can be done in various ways that may include using the altitude, fuel, as well as imposing a small penalty for being in a non-terminal state. Devising an appropriate reward function is one of the many challenges of implementing a reinforcement learning-based agent.</p>

      <h4>&epsilon;-Greedy Selection</h4>
      <p>During the training phase of reinforcement learning, actions must be selected to produce successor states. It would seem natural to select actions greedily by choosing the action in a given state that, according to the Q-function, results in the successor state with the highest utility. This greedy approach is <strong>exploitive</strong> of the knowledge built thus far, but since the utilities during training are still changing, it is possible that higher-utility action sequences exist. A simple way to encourage <strong>exploration</strong> is to allow a small &epsilon; chance of choosing an action at random instead of the current best one. This chance may start higher at the beginning of training and gradually decrease over time, which has the effect of encouraging a lot of exploration early on and reinforcing known strong action sequences near the end.</p>
    </template>

    <template v-slot:implementation>
      <p><strong>Allowed Modules:</strong> random</p>
      <p>The provided starter file contains the <code>ModuleState</code> class to represent states in the simulation. These objects are initialized with a starting fuel, altitude, velocity (which is always zero for the first state), the g-force applied to the module, and a transition function. Successor <code>ModuleState</code> objects are generated by calling the <code>use_fuel</code> method, which takes a fuel rate as its argument and uses the transition function to calculate the module's acceleration, which in turn impacts the altitude and velocity of the successor state. The transition function can be any callable that accepts two floats: the acceleration due to gravity (in m/s<sup>2</sup>) and the fuel rate selected. While a reasonable transition function is provided in the file, you may use any (unrealistic) function with this signature for your tests (e.g. a function that just returns a constant value).</p>
      <p>At each state, the module can use one of its available fuel rates to move to a successor state by passing the rate to <code>use_fuel</code>. For example, a module with <code>5</code> available rates would have the following action set and corresponding amounts of thrust.</p>
      <table>
        <tr><th>Action</th><th>Fuel Rate</th></tr>
        <tr><td>0</td><td>0%</td></tr>
        <tr><td>1</td><td>25%</td></tr>
        <tr><td>2</td><td>50%</td></tr>
        <tr><td>3</td><td>75%</td></tr>
        <tr><td>4</td><td>100%</td></tr>
      </table>
      <br/>
      <p>Note that larger action sets offer more control (higher sensitivity to differences in rate changes), but require larger Q-tables and thus more training time.</p>

      <FunctionSignature name="learn_q" :params="[['state', 'ModuleState']]" type="Callable[[ModuleState, int], float]"/>
      <p>Return a Q-function that maps a state-action pair to a utility value. This function must be a callable with the signature shown. When this Q-function is used by an agent to make a policy, the lander must always reach its target surface with an impact velocity greater than <code>-1</code>. Assume that the g-force and transition function provided to the given <code>ModuleState</code> object will be the same one used to test the Q-function generated (but make no such assumption about the other initial values). For both the training and testing phases, assume that the starting altitude is never above <code>100</code> meters.</p>
      <p>The function returned may be a <a target="_blank" href="https://en.wikipedia.org/wiki/Closure_(computer_programming)">closure</a> as in the following example:</p>
      <pre>q = lambda s, a: table.get((s, a))</pre>
      <p>This example assumes a variable named <code>table</code> exists and its value has a <code>get</code> method. Your implementation may be different so long as it returns a function object with the signature <code>(ModuleState, int) -&gt; float</code>. For simplicity, it is recommended that this function use a table lookup (i.e. a dictionary) to map state-action pairs to utilities. Care must be taken to appropriately discretize the state representations (which may include the module's current fuel, altitude, and velocity) so that the table does not become too large.</p>

      <p>The action set may be changed from the default of <code>(0, 1, 2, 3, 4)</code> by calling the <code>set_actions</code> method of the <code>ModuleState</code> class. Doing so is optional, but must only be done once before the training process begins.</p>
      <pre>state.set_actions(8)  # sets the action set to be (0, 1, 2, 3, 4, 5, 6, 7), with 7 as 100% thrust</pre>
      <p>Changing the action set can be useful for implementations that seem to benefit from more or less granularity in the decision-making process.</p>
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
        name: "moonlander",
        title: "Project VI: Moonlander II - Crash & Learn",
        files: ["moonlander.py"],
        rubric: {
          "Starts at Altitude 10m": 10,
          "Starts at Altitude 25m": 15,
          "Starts at Altitude 50m": 20,
          "Starts at Altitude 75m": 25,
          "Starts at Altitude 100m": 30
        }
      };
    }
}
</script>


<style scoped>
figure {
  color: gray;
  float: right;
  font-size: 0.9em;
  margin: 0.5em;
}
table {
  margin-left: 2em;
  text-align: center;
}
</style>
