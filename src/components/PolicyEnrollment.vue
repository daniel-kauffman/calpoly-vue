<template>
  <div>
    <h1>Enrollment Policy</h1>
    <hr/>
    <p v-if="course === 101 || course === 202">This course is required by several majors in order to progress and is heavily impacted. Thus, enrollment can be very competitive.</p>
    <p v-if="course === 480">This course is a popular elective for computer science majors and has limited offerings. Thus, enrollment can be very competitive.</p>
    <h2>Before Start of Term</h2>
    <p>Enrollment may be initially permitted only for CSSE or other select majors during the first round of registration, opening up to other majors during subsequent rounds. If you are unable to enroll but believe that you should be able to do so, contact the CSSE department office.</p>
    <p style="color: red;">Please do not contact me for a permission number, as I do not have access to them until after the term begins.</p>
    <h2>After Start of Term</h2>
    <p>As per university rules, students will be automatically enrolled in order from the waitlist if space becomes available in the first 4 days of the term. During this time, instructors have no control over the enrollment process and do not have access to permission numbers.</p>
    <p>After this 4-day window, instructors can provide permission numbers for any remaining seats in a course section at their discretion. These numbers will be allocated by the following priorities.</p>
    <ol>
      <li>CSSE and CPE majors</li>
      <li>Other majors who require the course</li>
      <li>CSC minors</li>
      <li>Other majors who may use the course toward their degree</li>
      <li>Other majors who wish to take the course for employment or interest</li>
    </ol>
    <p>These priorities may be overidden for students with special circumstances. Students, including CSSE majors, who failed the course in their most recent term will usually be given lowest priority.</p>
  </div>
</template>


<script>
export default {
  props: {
    course: Number
  }
}
</script>
