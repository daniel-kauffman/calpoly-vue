<template>
  <div>
    <h1>Getting Started</h1>
    <hr/>

    <p>This tutorial will help you learn the most basic terminal commands and Python language features. Students who are already familiar with these concepts may want to skim this document before continuing to the first assignment; all others are highly encouraged to complete this tutorial.</p>
    <p>Once you begin the assignments, your instructor will assume that you know how to do the operations below, so be sure to ask questions about this tutorial as needed.</p>

    <h2>The Linux Operating System</h2>
    <p>The servers you will use for this course run the Linux operating system. Unlike Microsoft Windows and Apple OSX, Linux was not designed with the average consumer in mind. Instead, it was created to offer all the capabilities of a commercial operating system (OS) at the impossibly low price of free, making it a very accessible platform for hobbyists and students.</p>

    <p>Because the Linux project did not have the financial resources of a private company, progress in aspects viewed as lower priority, such as user experience and design, did not come about until relatively recently. Today, there are many high-quality graphical desktop environments available for Linux, such as Gnome, that make learning the OS easier. However, the command line interface (CLI) still offers the most efficient means to send commands to the OS and will thus be an important component of this course.</p>

    <p>To use the department servers, a full installation of a Linux OS is not necessary. To gain access to a command-line environment, follow the appropriate steps for your native operating system. Once open, you may want to pin the terminal application to a menu or make a desktop shortcut.</p>

    <h4>Apple OSX</h4>
    <ul>
      <li>Search for <code>Terminal</code></li>
    </ul>

    <h4>Microsoft Windows 10</h4>
    <ul>
      <li>Hold <code>Windows Key</code> and press <code>r</code> for the Run prompt</li>
      <li>Type <code>cmd</code> and press <code>Enter</code></li>
      <li>Right click on the window bar to access the command prompt's properties and set the buffer size to the maximum value (this serves as your scroll history, which you will want to be as long as possible)</li>
    </ul>

    <p>Once you've opened your command-line interface (the terminal), connect to one of the CSL servers, as detailed in the SSH Guide. You will need to enter your Cal Poly username and password (the same as used for your Portal). When typing your password, it will appear as if nothing is happening; however, the characters are being entered.</p>

    <p>After logging into the server, create a new directory called <code>tutorial</code> using the <code>mkdir</code> (make directory) command:</p>
    <pre>mkdir tutorial</pre>

    <p>To see this new directory, along with any other files at your present location, use the <code>ls</code> (list) command:</p>
    <pre>ls</pre>

    <p>Next, enter the newly created directory using the <code>cd</code> (change directory) command:</p>
    <pre>cd tutorial</pre>

    <p>To open a file for editing (used for the next part of this tutorial), you can use the <code>vim</code> command:</p>
    <pre>vim newbie.py</pre>

    <p>In the Vim editor, you are initially in Command Mode. Press <code>i</code> to enter Insert Mode so that you can type characters. When you are done, press <code>ESC</code> to exit Insert Mode. You can save and quit Vim by entering the write-quit command <code>:wq</code> followed by <code>Enter</code>. For more Vim commands, see the Vim Editor Guide.</p>

    <p>Two other very useful commands are the <code>mv</code> (move) and <code>cp</code> (copy) commands, which work like cut and copy, respectively. If you need to rename a file, simply "move" the file to the new name.</p>
    <pre>cp newbie.py copy.py</pre>
    <pre>ls</pre>
    <pre>mv copy.py newbie.py </pre>
    <pre>ls</pre>

    <p>Notice that, after <code>copy.py</code> was renamed to <code>newbie.py</code>, only that file remains. This is because renaming a file to one that already exists will overwrite that file.</p>

    <p>If you'd like to reuse a command that you have recently entered, you can use the arrow keys to scroll backward or forward through your command history. Use the up arrow now to retrieve the <code>cp</code> command previously entered and press <code>Enter</code>.</p>

    <p>In addition, to write commands more quickly, you can use tab completion to auto-complete the names of files. Since <code>copy.py</code> has returned (from re-entering the <code>cp</code> command above), rename it again by typing <code>mv c&lt;TAB&gt; n&lt;TAB&gt;</code>, where each <code>&lt;TAB&gt;</code> refers to pressing the <code>Tab</code> key. When the file name is ambiguous (like when two files begin with the same letter), type more letters of the desired file name until no other file has those starting characters before using tab completion.</p>

    <p>When commands begin to get very long but need editing, you can hold <code>CTRL</code> and press either <code>a</code> or <code>e</code> to jump to the beginning or end of the line, respectively. To delete a command before running it, jump to the end of the line, hold <code>CTRL</code> and press <code>u</code>.</p>

    <h2>The Python Language</h2>
    <p>Python is an interpreted programming language that emphasizes code readability as well as ease with which to quickly implement programs that might otherwise be more cumbersome to write in older compiled languages, such as C and Java. Python code can either be run in the Python interpreter (to see how small segments of code work) or by running a source code file (to save programs that can be run multiple times).</p>

    <h4>The Python Interpreter</h4>
    <p>At the command line, type <code>python3</code> (with nothing afterward) to start the Python interpreter. You will see a prompt that looks like <code>&gt;&gt;&gt;</code> indicating that the interpreter is ready to accept Python commands. After typing a command, press the Enter/Return key to cause Python to execute that command. To exit the interpreter, hold <code>CTRL</code> and press <code>d</code> (think <code>d</code> for "done").</p>

    <p>Try entering the following into the interpreter:</p>
    <pre>
    &gt;&gt;&gt; 1 + 2
    &gt;&gt;&gt; 1 / 2
    &gt;&gt;&gt; 1.0 / 2.0
    &gt;&gt;&gt; not True
    &gt;&gt;&gt; "This is a string!"
    &gt;&gt;&gt; # And this is a comment!
    &gt;&gt;&gt; [1, 2, 3, 4, 5]
    &gt;&gt;&gt; x = 1
    &gt;&gt;&gt; x
    &gt;&gt;&gt; assert 1 == 1
    &gt;&gt;&gt; assert 1 == 2</pre>

    <p>Note that when you exit the interpreter, all your code disappears. The interprer is only meant for exploring the language and cannot be used to save work; be sure to save all coursework to a file, as described in the next section.</p>

    <h4>Source Code Files</h4>
    <p>Using the Python Interpreter allows you to quickly test out components of the language to see what the resulting output would be. However, for programs that are meant to be run more than once, it is not practical to type them out every time they are to be run. As with nearly all programming languages, Python code can be written to a file once and executed multiple times.</p>

    <p>Python files are run using the <code>python3</code> command with the file name afterward, as in:</p>
    <pre>python3 newbie.py</pre>

    <p>If you have not already done so, create a new file called <code>newbie.py</code>. You may use a graphical text editor, such as PyCharm, or a terminal-based editor, such as Vim. However, do not use a formatted text editor such as Microsoft Word, as doing so adds invisible formatting characters to the file which may not be interpretable by Python.</p>

    <p>In this file, do the following:</p>
    <ol>

      <li>Create four variables called <code>myint</code>, <code>myfloat</code>, <code>mystr</code> and <code>mybool</code>, each on a separate line, by assigning each variable a value of the appropriate type (based on the variable's name). Variables can be assigned values using the assignment operator <code>=</code> whereby the variable name is on the left and the value is on the right, as in:
<pre>

mystr = "Hello!"</pre>
      </li>

      <li>After each variable has been assigned, print the variables (in any order with each on a separate line) by using the print function, as in:
<pre>

print(myint)</pre>
      </li>

      <li>Repeat steps 1 and 2 again on new lines below the existing ones and be sure to assign different values to each of the existing variables before printing them.</li><br/>

      <li>Next, print the first five lines that you were asked to enter into the Python Interpreter above (again, each on a separate line).</li><br/>

      <li>Add the following two lines:
<pre>

name = input("What is your name? ")
print("Your name is", name)</pre>
      </li>

      <li>Add two more examples similar to the above, except change the question and response to something else (the response should be relevant to the question).</li>
    </ol>

    <h2>Submission</h2>
    <p>This tutorial is not graded and thus no submission is required. If you are unsure whether you successfully completed this tutorial, you may show your work to your instructor.</p>
  </div>
</template>
