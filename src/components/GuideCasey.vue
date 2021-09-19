<template>
  <div>
    <h1>Casey Submission System</h1>
    <hr/>

    <p>Casey is a system that provides automated validation and grading of submitted code to increase evaluation transparency and help students achieve higher scores. The system has multiple components and options, as described in this document.</p>

    <h2>Usage</h2>
    <p>To submit work to Casey, your instructor should have provided you with a list of files that you are required to write. With these files in your current directory, the format of the submission command (with <code>&lt;...&gt;</code> indicating placeholders) is as follows:</p>
    <pre>
    /home/&lt;instructor&gt;/casey &lt;course_number&gt; &lt;assignment&gt;</pre>

    <p>For example, to submit CPE 101's Moonlander project to Daniel Kauffman:</p>
    <pre>
    /home/dkauffma/casey 101 moonlander</pre>

    <p>This command will verify the existence of all required files (as documented in your project specification) and submit these files if they satisfy the necessary style and test suite requirements.</p>

    <p>To see a summary of all submitted work and associated scores to date for a course, run the Casey command without an assignment name.</p>
    <pre>
    /home/dkauffma/casey 101</pre>

    <h4>Submission</h4>
    <p>If all style and test requirements are met, the student's work will be submitted. Casey will retain a student's <strong>highest-scoring</strong> (not necessarily most recent) submission for an assignment. While not required, it is recommended each student use proper version control (e.g. with Git) to maintain a history of program changes to be able to revert to a previous version as needed.</p>
    <p>If the files were submitted for grading, you will see a message similar to the following:</p>
    <pre>
    ------------------------------
     Submission Status | <span style="color:green;">SUCCESS</span> |
    ------------------------------</pre>

    <p>However, if the files were not submitted due to not meeting requirements, a message similar to the following will be displayed:</p>
    <pre>
    ------------------------------
     Submission Status | <span style="color:red;">FAILURE</span> |
    ------------------------------</pre>
    <p>Above this failure message, the details of all unmet requirements will also be displayed.</p>

    <h2>Components</h2>
    <p>Casey has three primary components: style parsing, test validation, and grading. Style parsing verifies that the student's project implementation satisfies the rules set by the instructor. Test validation ensures that the student's test cases run, meet the minimum required number for each function, and provide complete coverage of project code. Grading assesses the student's project against the instructor's test cases; grading is only performed if style and test validation are successful.</p>

    <h4>Style Parser</h4>
    <p>Your instructor may set requirements for the formatting of submitted code, which may include spacing rules, line limits, prohibition of globals, etc. Casey's style parser reads through code before it is submitted to ensure that it adheres to the style rules. Any style violations detected are displayed, along with the line numbers on which they occur.</p>

    <h4>Test Validation</h4>
    <p>Casey ensures that the following is true about <strong>student-submitted</strong> test suites:</p>
    <ul>
      <li>The test suite runs and all test cases pass.</li>
      <li>The minimum number of test cases per function are included.</li>
      <li>The test suite provides complete code coverage of the program.</li>
    </ul>

    <p>The student's test suite must include the minimum number of <strong>non-duplicate</strong> test cases per function. If this number is not met for one or more functions, Casey will display a message for each function with an insufficient number of tests. Importantly, Casey is not able to check for duplicate test cases.</p>

    <p>Code coverage requires that every line of the program be executed at least once by the test suite. Casey displays any lines within a function not covered by the test suite.</p>

    <p>In contrast, branch coverage requires that every branch of the program be executed at least once by the test suite.</p>
    <p>The following example illustrates the difference between code and branch coverage.</p>
    <pre>
    1. def f(x):
    2.     if x &gt; 0:
    3.         y = 10
    4.     return x * y</pre>
    <pre>
    assert f(10) == 100  # provides complete code coverage</pre>

    <p>The test case provides complete code coverage of the function - every line of the function definition is executed. However, a test case for which execution jumps from line 2 to 4 (any non-positive value of <var>x</var>) would reveal the <code>NameError</code> raised as a result of <var>y</var> not yet being defined before being used in the <code>return</code> statement. Thus, both code and branch coverage serve as necessary initial steps for any comprehensive test suite.</p>

    <p>When a test suite does not exhibit complete code coverage, a message like the following will be displayed.</p>
    <pre>
    Lines Not Tested:
      10, 20-&gt;25, 30-&gt;exit</pre>
    <p>A number by itself indicates a line not reached by any test cases for that function. When two numbers are connected by an arrow, it means that no test case traverses the branch from the first line number to the second line number; if the second such number is the word <code>exit</code>, no test case goes from the first line number to the end of the function.</p>

    <h4>Grader</h4>
    <p>If both style and tests pass, submissions are graded using the instructor's test cases, which are hidden from students. Grades are presented in a tabular format, with each row representing a function or component required by the project specification. The <code>pass</code> column refers to the percentage of tests passed for that component. If there is a number in brackets at the end of a row, it indicates the weight of that component toward the total (for example, <code>[2.0]</code> means the component is worth twice as much as an unweighted component). The total score on the assignment is displayed at the very bottom.</p>

    <p>If work is submitted late but within the provided late window, the score will reflect any penalty the instructor uses to calculate the score.</p>
  </div>
</template>
