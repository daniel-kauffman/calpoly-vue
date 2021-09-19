<template>
  <Assignment :name="name" :title="title" :files="files" :rubric="rubric">
    <template v-slot:description>
      <p>Supervised Learning (a subset of Machine Learning) is primarily concerned with the process of approximating a function that maps some input <code>x</code> to an appropriate output <code>y</code>. These functions are usually "learned" by constructing some sort of model built iteratively over many observations of known x-to-y mappings, known as a training set. In the simplest case, once the model is "trained" on this set, its accuracy can be evaluated on a testing set, which is composed of other known x-to-y mappings that were not seen during training. In doing so, a data scientist can have some degree of confidence that the model generalizes well to inputs that have yet to be encountered by the model.</p>
      <p>While there are many forms of learning models (including Naive Bayes, Decision Trees, and Support Vector Machines, to name a few), the most sophisticated of these come in the form of artificial neural networks (often called "neural nets" or just "networks"). These networks are <em>very loosely</em> based on how the human brain functions, and their recent success is largely tied to how well they can scale and be adapted to suit a problem (in addition to the accessibility of very large data sets and massively parallel computing via GPUs). Put another way, neural networks represent one of the most versatile means to approximate a function.</p>

      <h4>Layered Model</h4>
      <p>The architecture of a neural network is composed of a sequence of <em>layers</em>, with each layer composed of a number of <em>neurons</em> (also known as units). Neurons each contain exactly one bias value, which is used in generating a value to send to the next layer. The neurons in one layer are connected to the neurons in another layer by weights, which may be thought of as edges between two vertices. In a <em>Feedforward Network</em>, these edges are directed toward the output layer only; because neurons within the same layer are not connected, these networks represent directed <a target="_blank" href="https://en.wikipedia.org/wiki/Multipartite_graph">Multipartite Graphs</a>.</p>
      <img src="https://1.cms.s81c.com/sites/default/files/2021-01-06/ICLH_Diagram_Batch_01_03-DeepNeuralNetwork-WHITEBG.png"
         style="display: block; margin-left: auto; margin-right: auto; width: 30%;"/>
      <figcaption style="font-size: 0.8em;">https://www.ibm.com/cloud/learn/neural-networks</figcaption>

      <br/>
      <p>The minimum number of layers in a network is two: an input layer and an output layer. However, these simple networks rarely generalize to meaningful mappings, and therefore additional layers are added in between to increase the sophistication of the network. Because the inputs and outputs of these layers are not directly observed, they are known as <em>hidden layers</em>, and any network that uses one or more hidden layers is said to be a deep neural network (and hence engages in "deep learning").</p>

      <h4>Network Training</h4>
      <p>The goal of training a neural network is to find suitable values for the weights and biases (mentioned above). An optimal assignment of these values would allow any never-before-seen input to map to its expected output, providing a highly accurate approximation of the target function.</p>
      <p>At the start of the training process, the weights are often initialized to small random values; because the biases are added to the output instead of multiplied, they may be initialized to zero. On each iteration of a forward propagation, a training sample is sent through the network, layer by layer, up until and including the output layer. The output is then compared to the expected output (which is known during supervised training), and the <em>loss</em> is computed using a loss function (e.g. squared error).</p>
      <p>At each layer, the output of each neuron to be sent to the next layer is computed as</p>
      <pre>a = &sigma;(wx+b)</pre>
      <p>where the input vector <code>x</code> is multiplied by the neuron's incoming weights <code>w</code> and then added to the bias <code>b</code>. The result is then passed to the activation function <code>&sigma;</code>, which is typically the <a target="_blank" href="https://en.wikipedia.org/wiki/Rectifier_(neural_networks)">ReLU</a> function for hidden layers and the <a target="_blank" href="https://en.wikipedia.org/wiki/Sigmoid_function">sigmoid</a> function for the output layer.</p>
      <p>On each iteration of training, forward propagation processes multiple training samples - but usually not <em>all</em> training samples, as that would take too long with the typically large training sets used. Instead, small random subsets of the training set called mini-batches are used for that iteration; on the next iteration, a new random mini-batch is created. The use of mini-batching allows for many iterations of the training process while still making it likely that every training sample is used at least once.</p>
      <p>Once all mini-batch training samples have been forward propagated, the losses are aggregated (usually averaged) to a <em>cost</em>, which serves as a measure of how well the network did during that iteration of training. The cost is then used to determine how to update the output layer's weights and biases. These updates are in turn used to update the previous layer's weights and biases, which continues up until but not including the input layer (which has no weights or biases). This process is known as backpropagation, and is central to training the network.</p>

      <h4>Backpropagation</h4>
      <p>Once the cost is known, the next step is to determine by how much the weights and biases need to be adjusted in order for the cost to be reduced on subsequent iterations. Doing so requires knowing the <em>gradient</em> (essentially a slope in multidimensional space) of certain values, which will point to their direction of steepest descent with respect to the cost and thus provide faster learning. This technique is known as gradient descent - or stochastic gradient descent (SGD) when mini-batching is used.</p>
      <p>Consider that the output of a network during forward propagation may be thought of as a composite of activation functions (where <code>x</code> is the input vector, <code>y</code> is the output vector, <code>W</code> is a weight matrix and <code>b</code> is a bias vector).</p>
      <pre>y = &sigma;<sub>2</sub>(W<sub>2</sub>&sigma;<sub>1</sub>(W<sub>1</sub>&sigma;<sub>0</sub>(W<sub>0</sub>x+b<sub>0</sub>)+b<sub>1</sub>)+b<sub>2</sub>)</pre>
      <p>Thus, to get the gradients, the <a target="_blank" href="https://en.wikipedia.org/wiki/Chain_rule">Chain Rule</a> from calculus may be used. Gradients are computed starting at the final (output layer) and working toward the input layer, with <code>da</code> initialized to the derivative of the loss function. Although the following formulas should be used, understanding why they work is not necessary to complete this assignment.</p>
      <pre>
dz<sub>n</sub> = da<sub>n</sub> &#8857; g'<sub>n</sub>(z<sub>n</sub>)
dW<sub>n</sub> = dz<sub>n</sub> &sdot; a<sup>T</sup><sub>n-1</sub>
db<sub>n</sub> = dz<sub>n</sub>
da<sub>n-1</sub> = W<sup>T</sup><sub>n</sub> &sdot; dz<sub>n</sub></pre>
      <p>In the above, <code>n</code> denotes a value at the current layer and <code>n - 1</code> the layer that comes before it. The &sdot; operator refers to matrix multiplication whereas the &#8857; operator refers to elementwise multiplication (or Hadamard product). Variables prefixed with a <code>d</code> refer to the gradient (derivative) of those values (e.g. <code>dz<sub>n</sub></code> refers to the gradient vector of <code>z<sub>n</sub></code>).</p>

      <h4>Updating Parameters</h4>
      <p>Once backpropagation has been performed on every sample that was forward propagated in a mini-batch, the weights and biases may be updated. Recall that it is these updates that ultimately train the network. Fortunately, unlike backpropagation, updating the network's parameters is more straightforward. In this step, a <em>learning rate</em> is used, which typically starts high at the beginning of the training process and decreases over time to keep the network from diverging. For each layer, update each weight and bias value by subtracting it from the negated product of the gradient and the learning rate.</p>
      <pre>w<sub>p</sub><sub>q</sub> = w<sub>p</sub><sub>q</sub> - &alpha;&#9661;</pre>
      <p>In the above, let <code>&alpha;</code> be the learning rate, <code>&#9661;</code> be the gradient, and <code>p</code> and <code>q</code> be the position of a single weight in the weight matrix to be updated. Each bias vector would be updated in a similar way.</p>
    </template>

    <template v-slot:implementation>
      <p><strong>Allowed Modules:</strong> math, itertools, random</p>

      <p style="color: red;">You may optionally work in pairs for this assignment. However, the collaboration policy still applies; do not share code outside your pair. You may quit a pair after working together if you like, but you should then complete the assignment individually (i.e. do not join a new pair). Include both names of your pair at the top of your submission - even if you stopped working together - so that your submissions do not get flagged for collaboration.</p>

      <p>The following free resources may help you in completing this assignment:</p>
      <ul>
        <li>Text: <a target="_blank" href="http://neuralnetworksanddeeplearning.com/">neuralnetworksanddeeplearning.com</a></li>
        <li>Videos: <a target="_blank" href="https://www.youtube.com/playlist?list=PLPaWThlrpebULGM5bbaCX6M7bRuzcM8rd">www.youtube.com/playlist?list=PLPaWThlrpebULGM5bbaCX6M7bRuzcM8rd</a> (suggested list - not all videos required)</li>
      </ul>

      <p>In this assignment, you will train a network to learn how to perform simple arithmetic operations. For example, given the operation <code>x + y</code>, the network must be able to accept two operands as input and output their sum. However, to help the network form more complex associations with these operands, they will be represented in 8-bit binary - specifically, as a tuple of <code>0</code>s and <code>1</code>s; for inputs of multiple operands, the tuples will be concatenated into a single tuple. You may assume inputs and outputs will always be non-negative integers (i.e. standard division will not be used) and that all outputs will be small enough to represent with 8 bits.</p>

      <p>To illustrate, suppose the operation to be learned is multiplication (<code>x * y</code>) and we have the following sample:</p>
      <pre>
Operand<sub>1</sub>: 2 -&gt; 00000010
Operand<sub>2</sub>: 3 -&gt; 00000011
 <sub> </sub>Result: 6 -&gt; 00000110</pre>
      <p>In this example, the inputs and the expected outputs would look like:</p>
      <pre>
INPUT
LAYER
------
0 -&gt; |          |
0 -&gt; |          |
0 -&gt; |          |
0 -&gt; |          |
0 -&gt; |          |        | -&gt; 0
0 -&gt; |          |        | -&gt; 0
1 -&gt; |          |        | -&gt; 0
0 -&gt; |  HIDDEN  | OUTPUT | -&gt; 0
0 -&gt; | LAYER(S) | LAYER  | -&gt; 0
0 -&gt; |          |        | -&gt; 1
0 -&gt; |          |        | -&gt; 1
0 -&gt; |          |        | -&gt; 0
0 -&gt; |          |
0 -&gt; |          |
1 -&gt; |          |
1 -&gt; |          |
</pre>
      <p>In practice, the network will not be so accurate as to get exactly a <code>0</code> or <code>1</code> from its output layer (which uses the sigmoid activation function). Rather, these values will be somewhere between <code>0.0</code> and <code>1.0</code>; the farther an output is from <code>0.5</code> in either direction, the more confident the network is in that decision. Regardless of its confidence, each output value will be rounded to whichever integer is closer during network evaluation (e.g. a <code>0.49</code> will be rounded to <code>0</code>).</p>



      <p>See the starter file for the following provided components.</p>
      <div style="margin-left: 2em;">
      <h6>Classes</h6>
      <ul>
        <li><code>Math</code> provides a collection of static methods for mathematical operations</li>
        <li><code>Layer</code> serves as the foundation for the network's representation</li>
      </ul>
      <h6>Functions</h6>
      <ul>
        <li><code>create_samples</code> generates a mapping of input-output pairs to be used in training and testing</li>
        <li><code>main</code> contains a simple test driver</li>
      </ul>
      </div>

      <FunctionSignature name="train_network" :params="[['samples', 'Dict[Tuple[int, ...], Tuple[int, ...]]'], ['i_size', 'int'], ['o_size', 'int']]" type="List[Layer]"/>
      <p>Given a training set (with labels) and the sizes of the input and output layers, create and train a network by iteratively propagating inputs (forward) and their losses (backward) to update its weights and biases. Return the resulting trained network, represented as an ordered list of <code>Layer</code> objects (with the output layer as the last one in the list).</p>
      <p></p>
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
        name: "knowop",
        title: "Project VII: Know Op",
        files: ["knowop.py"],
        rubric: {
          "Constant Function [Single Argument]": 10,
          "Linear Function [Single Argument]": 10,
                  "Complement [Single Argument]": 10,
              "Bitwise Shift [Single Argument]": 10,
                  "Bitwise OR [Double Argument]": 20,
              "Bitwise AND [Double Argument]": 20,
          "Bitwise Left Shift [Double Argument]": 20
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
