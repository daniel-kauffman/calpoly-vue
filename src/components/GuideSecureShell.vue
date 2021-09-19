<template>
  <div>
    <h1>Secure Shell Guide</h1>
    <hr/>

    <p>A secure shell (SSH) client allows one to connect to another computer that has made itself available to such connections. These computers, usually called servers, are almost always located remotely; in other words, the server is in a different location from the user connecting to it. The servers used for this class are located in the Computer Systems Lab (CSL), a 24-hour student lab located in 14-235 (the north end of the computer science building).</p>

    <p>There are 3 commands worth knowing when wishing to interact with a server:</p>
    <table>
      <thead>
        <tr>
          <th>Command</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>ssh</td>
          <td>log into a server to execute commands</td>
        </tr>
        <tr>
          <td>scp</td>
          <td>copy a file to or from a server</td>
        </tr>
        <tr>
          <td>sftp</td>
          <td>establish a persistent connection for the purpose of copying multiple files</td>
        </tr>
      </tbody>
    </table>

    <br />
    <h2>Connecting to a Server</h2>

    <p><span style="color: red;">Note that the following process now requires first connecting to Cal Poly's VPN. For instructions, see:</span> <a href="https://tech.calpoly.edu/services/vpn">https://tech.calpoly.edu/services/vpn</a></p>
    <p>To connect to one of the CSL servers, use the following command (replacing <strong>username</strong> with your Cal Poly username):</p>
    <pre>
    ssh <strong>username</strong>@unix1.csc.calpoly.edu</pre>

    <p>This command will connect you to the CSL machine named <code>unix1</code>. Sometimes, a server may be busy or down and you will want to try a different one. The following machine names are alternatives that will have all your CSL server-saved files (even those saved on a different machine):</p>
    <pre>
    unix1, unix2, unix3, unix4</pre>

    <h2>Copying Files</h2>
    <p>If you are saving files locally (on your computer's storage instead of a server) and you want to copy a file to the server, use the secure copy command <code>scp</code>. To copy a file from your current local directory to your home directory on the server:</p>
    <pre>
    scp project.py <strong>username</strong>@unix1.csc.calpoly.edu:~</pre>

    <p>To copy a file from your home directory on the server to your current local directory (don't forget the final . to indicate your current local directory as the destination):</p>
    <pre>
    scp <strong>username</strong>@unix1.csc.calpoly.edu:~/project.py .</pre>

    <p>In addition to the scp command, the sftp command also allows files to be transferred between a local and remote machine. However, this command provides a persistent connection that only needs to be entered once per session and allows multiple files to be uploaded or downloaded.</p>

    <p>To begin a Secure File Transfer Protocol (SFTP) session:</p>
    <pre>
    sftp <strong>username</strong>@unix1.csc.calpoly.edu</pre>

    <p>Once connected, you may use the commands <code>ls</code> and <code>cd</code> to view and navigate to the desired directory on the server. In addition, you may use <code>lls</code> (local <code>ls</code>) and <code>lcd</code> (local <code>cd</code>) to view and navigate locally during the session.</p>

    <p>To download or upload files in a SFTP session, use the following commands:</p>
    <table>
      <thead>
        <tr>
          <th>SFTP Command</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>get FILE</td>
          <td>download <code>FILE</code> to the current local directory</td>
        </tr>
        <tr>
          <td>put FILE</td>
          <td>upload <code>FILE</code> to the current remote directory</td>
        </tr>
        <tr>
          <td>lls</td>
          <td>view contents of current local directory</td>
        </tr>
        <tr>
          <td>lcd DIR</td>
          <td>change current local directory to <code>DIR</code></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>


<style scoped>
td:first-child {
  font-family: monospace;
  font-size: 1.1em;
  text-align: center;
}
</style>
