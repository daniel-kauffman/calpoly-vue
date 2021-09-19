<template>
  <div>
    <div class="flex-container">
      <div style="width: 16em; margin-right: 0.5em;">
        <img src="@/assets/img/profile.jpeg" style="width: 100%;"/>
        <button @click="displayAbout = !displayAbout">About Instructor</button>
        <InstructorAbout v-if="displayAbout"/>
      </div>

      <div style="width: 40em;">
        <div id="title">
          <h3>{{ name }}</h3>
          <h6>Department of Computer Science</h6>
        </div>

        <InstructorRow title="E-mail Address">
          <div style="border: 1px solid lightgray;">{{ username }}</div>
          <div style="background-color: whitesmoke; border: 1px solid lightgray;">@{{ domain }}</div>
        </InstructorRow>

        <InstructorRow title="Zoom Meeting ID">
          <div style="border: 1px solid lightgray;">775</div>
          <div style="background-color: whitesmoke; border: 1px solid lightgray;">654</div>
          <div style="border: 1px solid lightgray;">3394</div>
        </InstructorRow>

        <InstructorRow title="Office Location">
          <a target="_blank" href="https://maps.calpoly.edu"
             style="border: 1px solid lightgray;">
            Building 14
          </a>
          <a target="_blank"
             href="https://afd.calpoly.edu/facilities/campus-maps/building-floor-plans/docs/building%20014-0_frank%20e%20pilling%20building.pdf"
             style="background-color: whitesmoke; border: 1px solid lightgray;">
            Room 245
          </a>
        </InstructorRow>

        <InstructorRow title="Tutoring Hours">
          <InstructorHours/>
        </InstructorRow>
      </div>
    </div>
  </div>
</template>


<script>
import InstructorAbout from "./InstructorAbout.vue"
import InstructorHours from "./InstructorHours.vue"
import InstructorRow from "./InstructorRow.vue"


export default {
  components: {
    InstructorAbout,
    InstructorHours,
    InstructorRow
  },
  props: {
    course: Number
  },
  data:
    function () {
      return {
        name: "Daniel Kauffman",
        username: "dkauffma",
        domain: "calpoly.edu",
        displayAbout: false
      };
    },
  computed: {
    updates:
      function () {
        return this.$parent.updates[this.course];
        // return Object.keys(updates).reduce((x, y) => x > y ? x : y);
      }
  }
}
</script>


<style scoped>
button {
  background-color: var(--calpoly-green);
  border: 0px;
  margin-top: 0.2em;
  color: white;
  width: 100%;
}
div#title {
  background-color: var(--calpoly-green);
  border-color: var(--calpoly-gold);
  border-style: double;
  border-width: 6px;
  color: white;
  font-size: 2em;
  margin-bottom: 0.5em;
  padding: 0.5em;
  text-align: center;
}
div.flex-container {
  display: flex;
  flex-direction: row;
  margin-bottom: 0.5em;
}
div.update {
  display: flex;
  background-color: whitesmoke;
  border: 1px solid lightgray;
  flex-direction: row;
  font-size: 0.8em;
}
div.notes {
  display: block;
  font-size: 0.6em;
  border: 1px solid lightgray;
  border-top: none;
  padding: 0.5em 0.5em 0.5em 1em;
}
</style>
