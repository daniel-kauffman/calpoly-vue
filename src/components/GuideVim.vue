<template>
  <div class="container-fluid">
    <h1 class="text-center">Vim Guide</h1>
    <hr/>

    <p>Vim is a terminal-based text editor, which means that it allows you to write text documents inside the terminal window. It is primarily used for coding (though you could use it to write plain text documents as well). In particular, it is usually used to code on a remote machine (server), which we will be doing regularly.</p>

    <p>While Vim is not the only terminal-based editor, we will use it for the following reasons:</p>
    <ul>
      <li>It is available on any Linux machine (sometimes as the pared-down version Vi)</li>
      <li>Unlike with Nano, you will often be able to code faster in Vim than in an IDE</li>
      <li>Unlike Emacs, Vim is simple enough to not be overwhelming for an intro course</li>
      <li>While it has a notoriously steep learning curve, the benefits of having invested the time to learn it will be evident before the course ends</li>
    </ul>

    <h2>Configuration</h2>
    <p>You should first add a configuration file to make Vim a little easier to use. This file includes features like syntax highlighting (displaying certain keywords in different colors to increase readability) and converting tabs to spaces.</p>
    <p>To get the config file, go to your home directory (enter <code>cd</code> with no argument) and run the command:</p>
    <pre>
    wget http://users.csc.calpoly.edu/~dkauffma/.vimrc</pre>

    <p>While you are free to make changes to this configuration, do not change <code>set expandtab</code> as it will help mitigate the spacing issues that cause a <code>TabError</code> in Python.</p>

    <p>You may also want to change the default Vim color scheme. Sites such as <a target="_blank" href="http://vimcolors.com/">vimcolors.com</a> provide links to the .vim files containing a color scheme. These files should be saved into <code>.vim/colors/</code> within your home directory.</p>

    <h2>Creating &amp; Opening Files</h2>
    <p>In a terminal, Vim may be started using <code>vim newbie.py</code> to open (or create) a file named newbie.py. Additionally, you can just type <code>vim</code> to start an untitled file which may later be given a name using the command <code>:w newbie.py</code> within Vim.</p>

    <h4>Swap Files</h4>
    <p>When a file is open for editing, Vim creates a temporary swap file to hold changes that have not yet been saved. If you exit the terminal without properly saving and closing Vim, or if you lose your server connection, Vim will retain this swap file in case it contains changes that you want to keep. When you open the file with Vim again, you will be prompted with a few options regarding the unsaved changes.</p>
    <pre>
    [O]pen Read-Only, (E)dit anyway, (R)ecover, (D)elete it, (Q)uit, (A)bort:</pre>
    <p>To recover these unsaved changes, enter <code>R</code> and you will be returned to your document. At this point, you should save the changes from the swap file before you continue editing.</p>
    <p>If you close and open the document again, you will see the same swap file warning message as before. The simplest solution is to enter <code>D</code> this second time to delete the swap file (which, if you saved previously, you will no longer need). If this option is not present, you may also delete the swap file at the command line, which is a hidden file usually ending with a .swp or similar extension (such as .newbie.py.swp).</p>

    <h4>Suspending Vim</h4>
    <p>It will often be necessary to run the program you are editing with the <code>python3</code> command. Instead of exiting Vim, you can simply suspend (or minimize) it using <code>CTRL+z</code> and, when you are ready to enable Vim again, bring it back to the "foreground" with the <code>fg</code> command. The main advantage of this approach is that your Vim session will remain intact, including all files you have open (see Editing Multiple Files below).</p>

    <h2>Common Commands</h2>
    <p>The following collection of frequently-used commands is split into different sections to help you learn Vim in stages. It is recommended that you only begin practicing commands from a subsequent section when you feel comfortable with those in the previous section.</p>
    <p>Although not specified below, any command that begins with a colon must be completed with the <code>Enter</code> key.</p>
    <p>For additional practice, enter <code>vimtutor</code> in a terminal and complete the relevant sections.</p>

    <h4>Highlighting</h4>
    <p>Vim has a simple and effective find feature that allows you to quickly cycle through the matches from a search. When matches are found, Vim highlights them as a visual cue. Sometimes (especially for Vim novices) words are searched by accident and this highlighting is not desired. To remove highlighting, enter the "no highlight" command <code>:noh</code>.</p>

    <h4>Modes</h4>
    <p>Vim has a few different modes that alter its behavior. When you first open a file, you are in <strong>command</strong> mode, through which you can use any of the commands listed in this section. To use Vim like a typical text editor, you must enter <strong>insert</strong> mode. Finally, to select portions of text, you must do so in <strong>visual</strong> mode.</p>
    <div class="d-inline-flex flex-wrap">
      <CommandTable :commands="{'ESC': 'command mode',
                                'i': 'insert before cursor',
                                'a': 'insert after cursor'}">
        Command &amp; Insert Modes
      </CommandTable>
      <CommandTable :commands="{'v': 'select characters with line wrap',
                                'CTRL+v': 'select characters without line wrap',
                                'SHIFT+v': 'select lines'}">
        Visual Modes
      </CommandTable>
    </div>

    <h4>Critical Commands</h4>
    <p>The commands for saving, exiting, and correcting mistakes are the most important to learn.</p>
    <div class="d-inline-flex flex-wrap">
      <CommandTable :commands="{':+w': 'save',
                                ':+wq': 'save and quit',
                                'SHIFT+z+z': 'save and quit'}">
        Saving &amp; Exiting
      </CommandTable>
      <CommandTable :commands="{':+q!': 'force quit',
                                'SHIFT+z+q': 'force quit'}">
        Exiting without Saving
      </CommandTable>
      <CommandTable :commands="{'u': 'undo',
                                'CTRL+r': 'redo'}">
        Undo &amp; Redo
      </CommandTable>
    </div>

    <h4>Navigation</h4>
    <p>Efficiently moving around a document is one of Vim's primary advantages. There are several methods for navigating documents in Vim, including the arrow keys. However, even while initially learning Vim, try not to use the arrow keys for navigation. Although they provide that function, doing so is much slower than using the keys below. Since speed is one of the primary reasons to use Vim, you will more quickly reap its benefits if you force yourself to use the home row for movement.</p>
    <div class="d-inline-flex flex-wrap">
      <CommandTable :commands="{'h': 'move left',
                                'j': 'move down',
                                'k': 'move up',
                                'l': 'move right'}">
        Single-Character Movement
      </CommandTable>
      <CommandTable :commands="{'CTRL+u': 'scroll up',
                                'CTRL+d': 'scroll down',
                                'g+g': 'move to file top',
                                '<NUM>+g+g': 'move to line <NUM>',
                                'SHIFT+g': 'move to file bottom'}">
        Vertical Movement
      </CommandTable>
      <CommandTable :commands="{'0': 'move to line start',
                                '$': 'move to line end', 
                                'w': 'move to next word start',
                                'b': 'move to previous word start',
                                'e': 'move to current word end',
                                'f+<CHAR>': 'move to next <CHAR>',
                                'SHIFT+f+<CHAR>': 'move to previous <CHAR>'}">
        Horizontal Movement
      </CommandTable>
    </div>

    <h4>Clipboard</h4>
    <p>The clipboard stores text that was previously cut or copied to it. Text may be cut by deleting it, which saves it to the clipboard. Text may also be added to the clipboard in a non-destructive manner by copying it. In both cases, the contents of the clipboard can be reproduced by pasting it.</p>
    <div class="d-inline-flex flex-wrap">
      <CommandTable :commands="{'d': 'cut (delete) selection',
                                'dd': 'cut (delete) line',
                                'y': 'copy (yank) selection',
                                'p': 'paste clipboard contents'}">
        Cut, Copy &amp; Paste
      </CommandTable>
    </div>

    <h4>Editing Multiple Files</h4>
    <p>Your productivity will increase significantly as you use Vim for multiple files simultaneously. Each Vim window can be split vertically or horizontally (though a vertical split tends to be more practical). Additional Vim windows can also be created as tabs like in a web browser. Since these split and tabbed windows exist in the same Vim session, characters can be copied from one file and pasted into another easily. In all cases, opening a file will create that file if it doesn't already exist.</p>
    <div class="d-inline-flex flex-wrap">
      <CommandTable :commands="{':+vs <FILE>': 'vertically split window and open <FILE>',
                                ':+s <FILE>': 'horizontally split window and open <FILE>',
                                'CTRL+w+w': 'switch between window panes'}">
        Splitting Windows
      </CommandTable>
      <CommandTable :commands="{':+tabe <FILE>': 'create new tab and open <FILE>',
                                'g+t': 'go to next tab',
                                'g+SHIFT+t': 'go to previous tab'}">
        Adding Windows
      </CommandTable>
    </div>
  </div>
</template>


<script>
import CommandTable from "./GuideVimCommandTable"


export default {
  components: {
    CommandTable
  }
}
</script>
