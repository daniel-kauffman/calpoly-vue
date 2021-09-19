<template>
  <div>
    <h1>Activities &amp; Evaluation</h1>
    <hr/>

    <h2>Course Activities</h2>
    <p>All programming work must be submitted on one of the department's Computer Systems Lab (CSL) servers. Instructions for how to connect and work on these servers is available in the SSH Guide. Assignments must meet all submission requirements, which includes correct style and may include a valid test suite, to receive any credit.</p>
    <p>Submissions are usually due by <strong>9PM Pacific</strong> on the due date, unless otherwise noted at the top of the assignment specification.</p>

    <div v-if="course === 101 || course === 202">
      <h4>Problem Sets</h4>
      <p>Problem sets (or "p-sets") serve as the entry point to practice the concepts discussed during lecture. Each problem set will require you to implement several functions that are united by a conceptual theme but do not necessarily depend on one another to run.</p>
      <p>You are encouraged to work with a partner on problem sets, as many of the problems offer a significant logical challenge. However, it is not recommended to use a "divide and conquer" approach (whereby one student does half the problems and the other student does the other half), as this method will deny you practice with the problems that you did not complete. In addition, working with more than one partner is discouraged (though not prohibited), as it can make each student less active in the learning process.</p>
      <p>Although problem sets are worth few points relative to other activities, they serve as the best review for quizzes, which draw heavily from their content.</p>
      <p><strong>Late problem sets will not be accepted</strong>.</p>
    </div>

<!--
    <div v-if="course === 480">
      <h4>Group Discussions</h4>
      <p>You will be given short reading material (e.g. news articles) or activities throughout the term to be discussed within a peer group. Each student is expected to contribute to the discussion, demonstrating thoughtfulness of the material. One student will be selected to moderate the discussion. Moderators should help keep the discussion on topic, as well as ensure that everyone has a chance to participate and that no one dominates the discussion.</p>
      <p>Discussions should be about 4 minutes in length <strong>per person</strong>. For example, a 5-person group should conduct an approximately 20-minute discussion. At least one participant must record the discussion for submission, providing a link (not an attachment) to the video. Once you begin recording, each person must state their full name before the discussion begins. <strong>Everyone</strong> must be use a camera, though it need not be high quality (a phone camera should suffice). Furthermore, the recording should show the speaker while they are speaking (i.e. do not just send a video of the person recording while others speak unseen). Be sure to CC all group members when submitting the discussion link to the instructor so everyone knows it was submitted.</p>
      <p>Because this term is virtual, when trying to schedule a time that works for all members, keep in mind that some people live in different time zones or have full-time jobs or other commitments. You may want to use a scheduling app (e.g. <a href="https://doodle.com/create">Doodle</a>) to avoid excessive emails. Please give all group members at least 48 hours to respond, and do not conduct the discussion without a group member present if they previously seemed committed to attending. Extensions may be awarded in situations involving scheduling miscommunication between group members.</p>
    </div>
-->

    <h4>Projects</h4>
    <p style="color: red;">Important: Collaboration is strictly prohibited for this activity. Students have failed this course for not abiding by this rule. For more information, see the collaboration policy.</p>
    <p>Projects are of greater length and complexity than problem sets and must be completed <strong>individually</strong>. Projects will require you to connect various individual components into a cohesive whole with a clear application goal. You are strongly encouraged to begin a project as soon as it is assigned, as they often take much longer to complete than initially estimated. Procrastinate at your peril.</p>
    <p>Projects may be submitted up to 2 days late with a 30% point deduction.</p>
    <p>Each student will be given one 2-day extension without penalty; any extensions requested beyond this first one will require documentation from a medical provider or other relevant source and will only be granted at the discretion of the instructor. You do not need to contact the instructor to use your free extension, as it will be allocated automatically.</p>

    <div v-if="course === 101 || course === 202">
      <h4>Quizzes</h4>
      <p>There will be a few programming-based quizzes throughout the term. You will have 48 hours to complete each quiz. These quizzes must be completed <strong>solely by you</strong>; however, you are permitted to use external reference material, including online tutorials, past assignments you have written and programming aides such as Python Tutor. You are not permitted to receive personal assistance on the quiz in any form - including but not limited to tutoring or posting questions to forums - but you may ask the instructor for clarification on quiz content.</p>
<!--
      <h4>Quizzes</h4>
      <p>Starting around the third week of instruction, there will be weekly paper-based timed quizzes administered during the lecture hour. You will not be permitted to use notes or other resources during a quiz. Questions on the quiz will be based on problems from the problem sets.</p>
      <p>Your two lowest quiz scores will be dropped.</p>
-->
    </div>

    <div v-if="course === 480">
      <h4>Quizzes</h4>
      <p>There will be 5 quizzes administered throughout the term. These quizzes must be completed <strong>solely by you</strong>; however, you are permitted to use external reference material, including course resources and online references. You are not permitted to receive personal assistance on the quiz in any form - including but not limited to tutoring or posting questions to forums - but you may ask the instructor for clarification on quiz content.</p>
      <p>Details about how the quizzes will be administered will be announced soon.</p>
    </div>

    <div v-if="course === 101 || course === 202">
      <h4>Final Exam</h4>
      <p style="color: red;">The final exam is the only component of this course for which you may be required to attend at a specific time (to be announced).</p>
      <p>There will be one cumulative final exam at the end of the term. The exam will cover concepts discussed during lecture and techniques from assigned work. Details about how the exam will be administered will be given later in the term.</p>
      <p>Because the department does not want to encourage students to "practice" the exam for a subsequent attempt of the course, <strong>if your cumulative score in the course before the final exam is so low that earning 100% on it would not enable you to pass, you will not be eligible to take it.</strong></p>
<!--  
      <p>The exam will be proctored in a remote manner to be announced.</p>
      <p>Your computer will need an internal or external webcam connected to it for this process (an external device, like a phone, will not suffice). <strong>Students who do not have a camera connected to their computer will not be permitted to take the exam.</strong></p>
-->
    </div>

<!--
    <div v-if="course === 480">
      <h4>Final Presentation</h4>
      <p>Each student will give a short presentation over Zoom on an applied AI-related topic of their choice. The theme of these presentations will be centered around the ethical considerations of the technology presented. Topics should not be too general (e.g. "Deep Learning") nor too specific; if in doubt, ask the instructor. Details about the required structure of the presentation will be provided at a later date.</p>

      <p>Each student will give a short presentation over Zoom on an AI-related topic of their choice. The theme of these presentations will be centered around the ethical considerations of the technology presented. The topic should not be too general (e.g. "Computer Vision", "NLP"), nor should it be so specific that it requires an enormous amount of background information to be understood; <strong>if unsure, ask the instructor.</strong></p>

      <p>The introductory portion of the presentation should be objective, providing the audience with as much information about the topic as possible in the time allotted. The remaining time must be used to argue why the technology does or does not provide a net good to society; that is, whether or not its most promising aspects outweigh the potential for exploitation. Do not hedge; take a side and argue for it.</p>

      <p>The entire class is invited to attend every presentation, but attendance as an audience member will be <strong>optional</strong> (yes, that's right, optional; no, you do not need to confirm whether attendance is optional, it is). You will be able to decide when to schedule the presentation within a window of time (to be announced). As an audience member, your mic must remain off throughout each presentation unless you are asking a question at the end of it.</p>

      <p>An 8-minute time limit will be loosely enforced. You may lose points if you greatly exceed this limit and were unable to adequately present your topic in the time you were allotted, but going over by two or three minutes will not be penalized. After your presentation, a short period for questions will be permitted.</p>

      <p>You are <strong>highly</strong> encouraged to practice your presentation in advance (e.g. in front of a mirror, your quarantine buddy, your favorite stuffed animal). If you are not a frequent public speaker, practice is the best method to build confidence and improve your delivery.</p>

      <h5>Slides</h5>
      <p>All presentations must use slides displayed with Zoom's screen share feature. You will submit these slides in <strong>PDF</strong> format to the instructor over email. You are encouraged to use graphics to make your slides both more easily understood and interesting. Very short videos (not over about one minute in total) are permitted, so long as the reason for their use is evident; in other words, the video was able to communicate in a short time what would have been difficult to convey using text and images.</p>
      <p>The slides are due by the end of the day <strong>before</strong> your presentation (to allow for instructor review). Only minor changes (e.g. language errors) may be made after submitting but before presenting the slides. The instructor will be following the presentation with the submitted slides and any significant changes will result in a deduction.</p>
      <p>You must include your first and last name on the title slide, as well as cite all references used for your research on the final slide.</p>

      <h5>Format</h5>
      <ol>
        <li>Introduction (~1.5 minutes)</li>
        <ul>
          <li>Title slide <strong>must</strong> include first and last name of presenter.</li>
          <li>What is your topic? Why did you choose it?</li>
          <li>Convince the audience why they should offer their attention. Explain the topic at a high level; go into details later.</li>
        </ul>
        <li>Informative (~3 minutes)</li>
        <ul>
          <li>What problem does this technology seek to solve?</li>
          <li>What do we need to know about the topic's domain?</li>
          <li>What methods existed beforehand? Why is this method better than others in some cases? When is this method not better than others (if ever)?</li>
          <li>Prioritize graphical illustrations over algorithmic text when possible.</li>
          <li>Avoid multiple slides of algorithmic text. Distill the essence of any algorithms into as few lines of pseudo-code as possible.</li>
          <li>Only use easily understood pseudo-code; do not use code from a real programming language (not even Python).</li>
        </ul>
        <li>Argumentative (~3 minutes)</li>
        <ul>
          <li>How can this technology be used to help society? Cite researched examples.</li>
          <li>What are the potentials for exploitation? Has it already happened? If so, cite examples.</li>
          <li>Do you believe society will be better off with this technology? Provide a detailed explanation of your reasoning.</li>
        </ul>
        <li>Conclusion (~0.5 minutes)</li>
        <ul>
          <li>What did we just listen to?</li>
          <li>Act like the audience wasn't paying attention and needs to get caught up in half a minute.</li>
          <li>Final slide <strong>must</strong> cite all references; do not use a "Questions?"-like final slide.</li>
        </ul>
        <li>Questions (2 minutes)</li>
        <ul>
          <li>The question period does not count toward the 8-minute limit.</li>
        </ul>
      </ol>
    </div>
-->

    <hr/>
    <h2>Student Evaluation</h2>
    <p>Course activities will have the following contributions toward your final grade. Although the activity totals will remain constant, the number of some activities (and thus the weight of each one) is subject to change.</p>

    <ActivityTable/>

    <h4>Grade Requirements</h4>
    <p>Final grades will be awarded according to the following scores, which will not be rounded up.</p>
    <GradeTable/>
  </div>
</template>


<script>
import ActivityTable from "./CourseEvaluationActivityTable"
import GradeTable from "./CourseEvaluationGradeTable"


export default {
  components: {
    ActivityTable,
    GradeTable
  },
  props: {
    course: Number
  }
}
</script>
