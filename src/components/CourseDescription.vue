<template>
  <div>
    <h1>Course Description</h1>
    <hr/>

    <p v-if="course === 101">Welcome to the Fundamentals of Computer Science! This course offers an exciting and challenging foray into writing instructions for computers using the Python programming language.</p>

    <p v-if="course === 202">Welcome to Data Structures! This course offers an introduction to efficiently creating and accessing information, as well as how to analyze the performance of these operations.</p>

    <p v-if="course === 101 || course === 202">Because this course serves as the starting point for all Computer Science majors, the following assumptions will be made:</p>

    <div v-if="course === 480">
      <p>Welcome to the Introduction to Artificial Intelligence! This course offers an exciting and challenging foray into writing goal-oriented programs that must function under some degree of uncertainty, often using implicit data structures.</p>
      <p>Because this course relies on some specific background knowledge, the following assumptions will be made:</p>
    </div>

    <ul>
      <div v-if="course === 101">
        <li><strong>You have no programming or command-line experience.</strong> This course, while very challenging, is for absolute beginners. Occasionally, references to the Java language will be made because many students have taken a programming course in high school, which is usually taught in Java. These references are meant to compare how Python differs to help these students make the transition and may be ignored by students that do not have this background.</li>
        <li><strong>You are a Computer Science major.</strong> This course is required by several majors, including EE and Statistics, as well as some concentrations in Business and Graphic Communications. It is also required by Computer Science majors, who require a high level of rigor in their coursework to prepare them for future courses in the department. Because all students must receive the same assignments, you will be treated as a Computer Science major, even if you are not one.</li>
      </div>

      <div v-if="course === 202">
        <li><strong>You know or are willing to learn Python.</strong> Our introductory course (CPE 101) is taught with the Python language, and thus all students are expected to know the basics of Python for this course. All assignments will need to be completed exclusively in Python, however, very few (if any) standard library modules will be necessary. If you are new to Python, there are countless free resources available, and becoming proficient in the language will be a great addition to your resume.</li>
        <li><strong>You are a Computer Science major.</strong> While this course serves as an elective for several majors, it is also required by Computer Science majors, who demand a high level of rigor in their coursework to prepare them for future courses in the department. Because all students must receive the same assignments, you will be treated as a Computer Science major, even if you are not one.</li>
      </div>

      <div v-if="course === 480">
        <li><strong>You understand the concepts discussed in an introductory data structures course.</strong> Throughout the course, we will be using queues, trees, and graphs to represent the states of our agent's environment, as well as topics like hashing and sorting for particular purposes. You should have a solid understanding of elementary data structures and the algorithms used to operate on them. If you feel rusty on these concepts, start reviewing at the beginning of the course as it will be difficult to catch up later.</li>
        <li><strong>You know or are willing to learn Python.</strong> The Python language has become perhaps the most-used language in modern AI-related fields. All assignments will need to be completed exclusively in Python, however, only a few modules will be necessary to do so (see each spec for which modules are permitted). If you are new to Python, there are countless free resources available, and becoming proficient in the language will be a great addition to your resume.</li>
      </div>

      <li><strong>You are motivated to learn and will be proactive about getting the information you need to succeed.</strong> Learning to program, like all challenging pursuits, requires a lot of initiative on the part of the learner. Your instructor's job is to present the material in a clear, structured, and hopefully interesting manner; it is your job to get started on assignments early, study regularly, and ask questions when something is not understood. When you request assistance, your instructor will not provide you solutions but rather give you guidance on what to consider or how next to proceed.</li>
    </ul>

    <h2>Course Topics</h2>
    <p>Throughout the term, you will be introduced, among others, to the following topics.</p>

    <ul v-if="course === 101">
      <li>Atomic Data Types: Integers, Floats, Booleans, Strings</li>
      <li>Variables and Scope</li>
      <li>Function Calls and Definitions</li>
      <li>Arithmetic, Relational, and Boolean Expressions</li>
      <li>Conditional Branching: If Statements</li>
      <li>Conditional and Sequential Iteration: While and For Loops</li>
      <li>Sequential Compound Data Types: Lists and Tuples</li>
      <li>Error Handling</li>
      <li>Object-Oriented Basics</li>
      <li>Simple Sorting and Searching Algorithms</li>
    </ul>

    <ul v-if="course === 202">
      <li>Linked Lists</li>
      <li>Stacks &amp; Queues</li>
      <li>Recursion &amp; Recursive Sorting</li>
      <li>Unit Testing</li>
      <li>Binary Search Trees</li>
      <li>Heaps</li>
      <li>Hash Tables</li>
      <li>Algorithm Analysis &amp; Big-O Notation</li>
      <li>Basic Graph Theory</li>
    </ul>

    <ul v-if="course === 480">
      <li>The Agent Model</li>
      <li>Informed Search Methods</li>
      <li>Local Search Methods</li>
      <li>Genetic Algorithms</li>
      <li>Constraint Propagation</li>
      <li>Monte Carlo Tree Search</li>
      <li>Overview of Supervised/Unsupervised Learning</li>
      <li>Applied Reinforcement Learning</li>
      <li>Feedforward Neural Networks</li>
    </ul>
  </div>
</template>


<script>
export default {
  props: {
    course: Number
  }
}
</script>
