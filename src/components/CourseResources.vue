<template>
  <div>
    <h1>Course Resources</h1>
    <hr/>

    <div v-if="course === 101 || course === 202">
      <h2>Free Tutoring</h2>
      <ul>
        <li>
          <a target="_blank" href="http://tutoring.csc.calpoly.edu/">CSSE Department Tutoring</a>
        </li>
        <li>
          <a target="_blank" href="https://asc.calpoly.edu/study-session">Cal Poly Study Sessions</a>
        </li>
      </ul>
    </div>

    <h2>Course Forum</h2>
    <p>Students may post questions and assist their peers on the course Discord server (to be announced).</p>

    <h2>Zoom Hours</h2>
    <p>This course is asynchronous, meaning that there is no required time that you must be engaged with the class on any given day. There is, however, time allocated for one-on-one tutoring with the instructor. During this time, students will be admitted to the Zoom meeting room individually and in the order they arrived; if you find yourself waiting for a long time, it is because there are many students that day. Generally (when possible), Zoom hours will be extended until all students waiting have been seen at least once. Be sure to make your Zoom chat visible for status updates occasionally sent to all attendees in the waiting room.</p>

    <h2>Course Videos</h2>
    <p>Instead of synchronous lectures, course videos will be available on the instructor's <a target="_blank" href="https://www.youtube.com/channel/UCQx0QD7DUF7bhkS0gtIcimA">YouTube Channel</a>.</p>

    <div v-if="course === 480">
      <h2>AI Slides</h2>
      <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRJ-_RwetapXQ7O42-hjAxXq0j09-JzSaGsNgLA5pzP22ZZkSZbBVkGPlTRgd_C75uuvkbFf1hTGLqi/embed?start=false&loop=false&delayms=60000"
                frameborder="0"
                width="480"
                height="299"
                allowfullscreen="true"
                mozallowfullscreen="true"
                webkitallowfullscreen="true">
      </iframe>
    </div>
    <p>These slides may be downloaded <a target="_blank" href="https://docs.google.com/presentation/d/1-JbzbcVsv6uwzSf5V7efypFGr1Tl6ITbbmJDUAJyuaY/edit?usp=sharing">here</a>.</p>

    <h2>Python Slides</h2>
    <p>These slides are from the instructor's most recent offering of CPE 101 and may be useful for Python review.</p>
    <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vT7Q_2InaxfoD_QMWj-ITq4nfVbvzeIiBKQ41pj4_XkLZZ92syvdDm8jyyqSOlVP5xoSZqOJwVbaq86/embed?start=false&loop=false&delayms=60000"
            frameborder="0"
            width="480"
            height="299"
            allowfullscreen="true"
            mozallowfullscreen="true"
            webkitallowfullscreen="true">
    </iframe>
    <br/><br/>

    <h2>Python Tutor</h2>
    <p>All students are strongly encouraged to use <a target="_blank" href="http://www.pythontutor.com/visualize.html#mode=edit">Python Tutor</a>, a web-based learning tool that allows you to step through your program's execution and visualize some aspects of its state.</p>

    <h2>Algorithm Visualizations</h2>
    <p>The site <a target="_blank" href="https://visualgo.net/en">VisuAlgo</a> provides interactive animations for many introductory algorithms.</p>
  </div>
</template>


<script>
export default {
  props: {
    course: Number
  }
}
</script>
